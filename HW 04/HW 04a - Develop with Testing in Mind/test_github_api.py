import unittest
from unittest.mock import patch
import github_api

class MockResponse:
    # Mock class to simulate requests.get response
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class TestGitHubAPI(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_valid_user(self, mock_get):
        # Test with a valid user having repositories.
        mock_get.side_effect = [
            MockResponse([{"name": "Repo1"}, {"name": "Repo2"}], 200),
            MockResponse([{"commit": "abc123"}] * 5, 200),  # 5 commits in Repo1
            MockResponse([{"commit": "xyz456"}] * 8, 200)   # 8 commits in Repo2
        ]

        # Expected result: List of tuples with repo name and commit count
        expected = [("Repo1", 5), ("Repo2", 8)]
        self.assertEqual(github_api.get_repos_and_commits("validuser"), expected)

    @patch("github_api.requests.get")
    def test_invalid_user(self, mock_get):
        # Test with an invalid GitHub username.
        mock_get.return_value = MockResponse({"message": "Not Found"}, 404)
        self.assertEqual(github_api.get_repos_and_commits("invaliduser"), "Error: Unable to fetch repositories for user 'invaliduser'.")

if __name__ == "__main__":
    unittest.main()
