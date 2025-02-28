# GitHub API with Testing and Continuous Integration

This project interfaces with the GitHub API to fetch a list of repositories and their respective commit counts for a given GitHub user. It includes unit tests to ensure functionality and is integrated with **Travis CI** for continuous integration.

## Features

- Fetches the list of repositories for a given GitHub user.
- Displays the repository name along with the number of commits in each repository.
- Includes unit tests for validating the functionality of the code.
- Continuous integration with **Travis CI** to ensure the code builds correctly on each commit.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests.

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```
## Running the Application
To fetch repositories and commit counts for a specific GitHub user, run the following command:

```bash
python github_api.py <username>
```
If no username is provided, it will default to the GitHub user "cvitanza".

## Running the Tests

To run the unit tests, use the following command:
```bash
python -m unittest discover
```

## Continuous Integration with Travis CI
This project is integrated with Travis CI to automatically build and test the code on every commit. You can check the build status below:
