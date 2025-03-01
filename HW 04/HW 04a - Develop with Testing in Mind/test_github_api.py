import unittest
import github_api  # Make sure this imports the correct function from your github_api.py

class TestGitHubAPI(unittest.TestCase):

    def test_get_repositories_success(self):
        # Test that GitHub API retrieves real repositories for a known user.
        user = "cvitanza"  
        result = github_api.get_repos_and_commits(user)  # Ensure you're calling the correct function

        self.assertIsInstance(result, list)  # Since it's a list of tuples, check if it's a list
        self.assertGreater(len(result), 0)

    def test_get_commit_count_success(self):
        # Test commit count retrieval from an actual repository.
        user = "cvitanza"  
        result = github_api.get_repos_and_commits(user)  # Ensure you're calling the correct function

        first_repo, commit_count = result[0]  # Access the first repo and commit count tuple
        self.assertIsNotNone(first_repo)  # Ensure there's at least one repo
        self.assertGreaterEqual(commit_count, 0)  # Commit count should be >= 0

    def test_invalid_user(self):
        # Test that an invalid user returns an error.
        user = "thisuserdoesnotexist123456"  # Invalid GitHub user
        result = github_api.get_repos_and_commits(user)  # Call the correct function

        self.assertEqual(result, f"Error: Unable to fetch repositories for user '{user}'.")

if __name__ == "__main__":
    unittest.main()
