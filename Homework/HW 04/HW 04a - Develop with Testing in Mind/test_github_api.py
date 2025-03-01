import unittest
from unittest.mock import patch
import requests
from github_api import get_repos_and_commits  # Update with correct import path

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_repos_and_commits(self, mock_get):
        # Mock the response for fetching repositories (with "name" key)
        mock_repos_response = mock_get.return_value
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [
            {"name": "repo1"},  # Add the "name" key here
            {"name": "repo2"}   # Add the "name" key here
        ]
        
        # Mock the response for fetching commits for each repo
        # We need to mock different responses based on the repo name
        mock_commits_response = requests.Response()
        mock_commits_response.status_code = 200
        mock_commits_response._content = b'[{"commit": {"message": "initial commit"}}]'  # Example commit data

        # Mocking the GET call for commits for each repository
        mock_get.side_effect = [
            mock_repos_response,  # First GET call: Repos list
            mock_commits_response, # Second GET call: Commits for repo1
            mock_commits_response, # Third GET call: Commits for repo2
        ]
        
        result = get_repos_and_commits('user')

        # Assertions: Check the returned repo names and commit counts
        self.assertEqual(result[0], ('repo1', 1))  # repo1 should have 1 commit
        self.assertEqual(result[1], ('repo2', 1))  # repo2 should have 1 commit
        
        # Verify that the correct API URLs were called
        mock_get.assert_any_call('https://api.github.com/users/user/repos')  # Repos list
        mock_get.assert_any_call('https://api.github.com/repos/user/repo1/commits')  # Commits for repo1
        mock_get.assert_any_call('https://api.github.com/repos/user/repo2/commits')  # Commits for repo2

if __name__ == '__main__':
    unittest.main()
