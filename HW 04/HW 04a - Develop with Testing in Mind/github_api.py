import requests # type: ignore

def get_repos_and_commits(username="cvitanza"):
    # Fetch a GitHub user's repositories and the number of commits in each.
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        return f"Error: Unable to fetch repositories for user '{username}'."

    repos = repos_response.json()
    repo_commit_counts = []

    for repo in repos:
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        commit_count = len(commits_response.json()) if commits_response.status_code == 200 else "Error fetching commits"
        repo_commit_counts.append((repo_name, commit_count))

    return repo_commit_counts

def print_repos_and_commits(username="cvitanza"):
    # Prints the repositories and commit counts in the required format.
    results = get_repos_and_commits(username)
    
    if isinstance(results, str):  # Error case
        print(results)
    else:
        for repo_name, commit_count in results:
            print(f"Repo: {repo_name}, Number of Commits: {commit_count}")

if __name__ == "__main__":
    user = input("Enter GitHub username (Press Enter for default cvitanza): ").strip() or "cvitanza"
    print_repos_and_commits(user)
