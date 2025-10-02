#!/usr/bin/env python3
"""
Script to check for new DuckDB releases and update the changelog if needed.
This script is designed to be run in GitHub Actions.
"""

import requests
import json
import sys
import os
import subprocess
from datetime import datetime


def get_latest_release_tag():
    """
    Get the latest release tag from GitHub API.

    Returns:
        str: The latest release tag name, or None if error
    """
    url = "https://api.github.com/repos/duckdb/duckdb/releases/latest"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "duckdb-changelog-updater"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("tag_name")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest release: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return None


def get_current_changelog_version():
    """
    Get the latest version from the current README.md file.

    Returns:
        str: The latest version tag from changelog, or None if not found
    """
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Look for the first version header after the table of contents
        lines = content.split('\n')
        for line in lines:
            if line.startswith("# v") and ("<a id=" in line or "{" in line):
                # Extract version from line like "# v1.4.0 - DuckDB 1.4.0 "Andium" <a id="v140"></a>"
                # or "# v1.4.0 - DuckDB 1.4.0 "Andium" {#v140}"
                version = line.split()[1]  # Gets "v1.4.0"
                return version

        return None
    except FileNotFoundError:
        print("README.md not found")
        return None
    except Exception as e:
        print(f"Error reading README.md: {e}")
        return None


def run_changelog_generation():
    """
    Run the changelog generation script.

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        result = subprocess.run(
            ["python", "fetch_changelog.py"],
            capture_output=True,
            text=True,
            check=True
        )
        print("Changelog generation output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running changelog generation: {e}")
        print(f"Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def commit_and_push_changes(version):
    """
    Commit and push the updated changelog.

    Args:
        version (str): The new version that was added

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Configure git user (required for GitHub Actions)
        subprocess.run(["git", "config", "user.name", "GitHub Actions"], check=True)
        subprocess.run(["git", "config", "user.email", "actions@github.com"], check=True)

        # Add the README file
        subprocess.run(["git", "add", "README.md"], check=True)

        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "diff", "--staged", "--quiet"],
            capture_output=True
        )

        if result.returncode == 0:
            print("No changes to commit")
            return True

        # Commit the changes
        commit_message = f"feat: add DuckDB {version}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push the changes
        subprocess.run(["git", "push"], check=True)

        print(f"Successfully committed and pushed changes for {version}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error with git operations: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in git operations: {e}")
        return False


def main():
    """Main function to check for new releases and update changelog if needed."""
    print("Checking for new DuckDB releases...")

    # Get the latest release from GitHub
    latest_release = get_latest_release_tag()
    if not latest_release:
        print("Failed to fetch latest release information")
        sys.exit(1)

    print(f"Latest release on GitHub: {latest_release}")

    # Get the current version from changelog
    current_version = get_current_changelog_version()
    if not current_version:
        print("Failed to read current version from changelog")
        sys.exit(1)

    print(f"Current version in changelog: {current_version}")

    # Check if we need to update
    if latest_release == current_version:
        print("No new release available. Changelog is up to date.")
        sys.exit(0)

    print(f"New release detected: {latest_release}")
    print("Regenerating changelog...")

    # Regenerate the changelog
    if not run_changelog_generation():
        print("Failed to regenerate changelog")
        sys.exit(1)

    print("Changelog regenerated successfully")

    # Commit and push the changes
    if not commit_and_push_changes(latest_release):
        print("Failed to commit and push changes")
        sys.exit(1)

    print("Successfully updated changelog with new release!")


if __name__ == "__main__":
    main()
