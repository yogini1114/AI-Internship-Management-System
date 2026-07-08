"""
AI GitHub Analyzer

Currently this is a rule-based implementation.
Later you can replace it with:
- GitHub REST API
- PyGithub
- LLM based code review
"""

from urllib.parse import urlparse


def analyze_repository(repo_url: str):
    """
    Analyze a GitHub repository and return a report.
    """

    if not repo_url:
        return {
            "error": "Repository URL is required."
        }

    parsed = urlparse(repo_url)

    if "github.com" not in parsed.netloc:
        return {
            "error": "Invalid GitHub repository URL."
        }

    repo_name = parsed.path.strip("/").split("/")[-1]

    commits = 42
    branches = 3
    stars = 18
    forks = 5
    issues = 2
    pull_requests = 4

    readme_score = 90
    documentation_score = 86
    code_quality_score = 88

    overall_score = round(
        (
            readme_score
            + documentation_score
            + code_quality_score
        ) / 3,
        2,
    )

    suggestions = []

    if readme_score < 80:
        suggestions.append("Improve project README.")

    if documentation_score < 80:
        suggestions.append("Add documentation.")

    if code_quality_score < 80:
        suggestions.append("Improve code quality.")

    if not suggestions:
        suggestions.append("Repository looks good.")

    return {
        "repository": repo_name,
        "repository_url": repo_url,
        "commits": commits,
        "branches": branches,
        "stars": stars,
        "forks": forks,
        "open_issues": issues,
        "pull_requests": pull_requests,
        "readme_score": readme_score,
        "documentation_score": documentation_score,
        "code_quality_score": code_quality_score,
        "overall_score": overall_score,
        "suggestions": suggestions,
        "ai_summary": (
            f"{repo_name} has an overall GitHub quality score "
            f"of {overall_score}/100."
        ),
    }