from ai_modules.github_analyzer import analyze_repository


def get_github_analysis(repo_url: str):

    return analyze_repository(repo_url)