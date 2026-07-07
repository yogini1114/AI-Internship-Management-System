import os
import json
import requests

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def analyze_repository(repo_url: str) -> dict:
    """
    Analyze a GitHub repository using GitHub API + Groq LLM.
    """

    repo_path = repo_url.replace(
        "https://github.com/",
        ""
    ).strip("/")

    headers = {}

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    repo_api = f"https://api.github.com/repos/{repo_path}"

    response = requests.get(
        repo_api,
        headers=headers
    )

    if response.status_code != 200:
        return {
            "error": "Repository not found."
        }

    repo = response.json()

    prompt = f"""
You are a Senior Software Engineer.

Analyze the following GitHub repository.

Repository Name: {repo.get("full_name")}
Description: {repo.get("description")}
Primary Language: {repo.get("language")}
Stars: {repo.get("stargazers_count")}
Forks: {repo.get("forks_count")}
Open Issues: {repo.get("open_issues_count")}
Default Branch: {repo.get("default_branch")}

Evaluate:

1. Documentation
2. Repository Structure
3. Code Quality
4. Maintainability
5. Git Practices

Return ONLY valid JSON.

{{
    "overall_score": 8,
    "documentation_score": 8,
    "code_quality_score": 7,
    "git_practices_score": 9,

    "strengths": [
        "...",
        "..."
    ],

    "weaknesses": [
        "...",
        "..."
    ],

    "suggestions": [
        "...",
        "...",
        "..."
    ]
}}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    result = completion.choices[0].message.content.strip()

    # Remove markdown if model returns ```json
    if result.startswith("```json"):
        result = (
            result.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    elif result.startswith("```"):
        result = (
            result.replace("```", "")
            .strip()
        )

    # Convert string to JSON
    try:
        result = json.loads(result)

    except Exception:
        result = {
            "raw_response": result
        }

    return {

        "repo_url": repo_url,

        "repo_name": repo.get("full_name"),

        "language": repo.get("language"),

        "stars": repo.get("stargazers_count"),

        "forks": repo.get("forks_count"),

        "watchers": repo.get("watchers_count"),

        "open_issues": repo.get("open_issues_count"),

        "default_branch": repo.get("default_branch"),

        "analysis": result
    }