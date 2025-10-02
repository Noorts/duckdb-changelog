#!/usr/bin/env python3
"""
Script to fetch all DuckDB release descriptions from GitHub REST API
and write them to a CHANGELOG.md file with a table of contents.
"""

import requests
import json
import sys
import time
import re
from datetime import datetime


def fetch_all_releases():
    """
    Fetch all release information from DuckDB repository using GitHub REST API with pagination.

    Returns:
        list: List of all release information including tag name, description, and published date
    """

    all_releases = []
    page = 1
    per_page = 100  # Maximum allowed by GitHub API

    while True:
        # GitHub REST API endpoint for releases with pagination
        url = f"https://api.github.com/repos/duckdb/duckdb/releases?page={page}&per_page={per_page}"

        # Headers for the request
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "duckdb-changelog-fetcher"
        }

        try:
            print(f"Fetching page {page}...")

            # Make the REST API request
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            # Parse the response
            data = response.json()

            # If no more releases, break the loop
            if not data:
                break

            # Extract release information for each release on this page
            page_releases = []
            for release_data in data:
                release_info = {
                    "tagName": release_data.get("tag_name", ""),
                    "description": release_data.get("body", ""),
                    "publishedAt": release_data.get("published_at", ""),
                    "name": release_data.get("name", ""),
                    "url": release_data.get("html_url", "")
                }
                page_releases.append(release_info)

            all_releases.extend(page_releases)
            print(f"  Found {len(page_releases)} releases on page {page}")

            # If we got fewer releases than per_page, we've reached the end
            if len(data) < per_page:
                break

            page += 1

            # Add a small delay to be respectful to the API
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching release data on page {page}: {e}")
            # If we have some releases already, return what we have
            if all_releases:
                print(f"Returning {len(all_releases)} releases fetched so far...")
                return all_releases
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response on page {page}: {e}")
            if all_releases:
                print(f"Returning {len(all_releases)} releases fetched so far...")
                return all_releases
            return None

    print(f"Successfully fetched {len(all_releases)} total releases")
    return all_releases


def convert_author_mentions(text):
    """
    Convert @author mentions in text to GitHub profile links.

    Args:
        text (str): The text containing @author mentions

    Returns:
        str: Text with @author mentions converted to GitHub profile links
    """
    if not text:
        return text

    # Pattern to match @author mentions (alphanumeric, hyphens, underscores)
    # This matches patterns like @username, @author-name, @author_name
    pattern = r'@([a-zA-Z0-9_-]+)'

    def replace_mention(match):
        username = match.group(1)
        return f'[@{username}](https://github.com/{username})'

    # Replace all @author mentions with GitHub profile links
    return re.sub(pattern, replace_mention, text)


def generate_table_of_contents(releases):
    """
    Generate a table of contents for the changelog.

    Args:
        releases (list): List of release information

    Returns:
        str: Formatted table of contents
    """
    toc = "# Table of Contents\n\n"

    for release in releases:
        tag_name = release.get("tagName", "Unknown")
        name = release.get("name", "")

        # Create simple anchor from tag name (e.g., v1.4.0 -> v140)
        anchor = tag_name.replace(".", "").replace("-", "").lower()

        # Create TOC entry
        toc_entry = f"- [{tag_name}"
        if name and name != tag_name:
            toc_entry += f" - {name}"
        toc_entry += f"](#{anchor})\n"

        toc += toc_entry

    toc += "\n---\n\n"
    return toc


def format_changelog_entry(release_info):
    """
    Format the release information into a markdown changelog entry.

    Args:
        release_info (dict): Release information from GitHub API

    Returns:
        str: Formatted markdown changelog entry
    """
    tag_name = release_info.get("tagName", "Unknown")
    description = release_info.get("description", "")
    published_at = release_info.get("publishedAt", "")
    name = release_info.get("name", "")
    url = release_info.get("url", "")

    # Parse the published date
    if published_at:
        try:
            # Parse ISO format date and format it nicely
            date_obj = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            formatted_date = date_obj.strftime("%Y-%m-%d")
        except ValueError:
            formatted_date = published_at
    else:
        formatted_date = "Unknown date"

    # Create anchor for TOC linking
    anchor = tag_name.replace(".", "").replace("-", "").lower()

    # Create the changelog entry
    changelog_entry = f"# {tag_name}"

    if name and name != tag_name:
        changelog_entry += f" - {name}"

    changelog_entry += f" <a id=\"{anchor}\"></a>\n\n"
    changelog_entry += f"*Released on {formatted_date}*\n\n"

    # Add GitHub links at the top
    if url:
        changelog_entry += f"[View on GitHub]({url})\n\n"

    if description:
        # Clean up the description (remove extra whitespace, etc.)
        description = description.strip()
        # Remove trailing whitespace from each line
        lines = description.split('\n')
        lines = [line.rstrip() for line in lines]
        description = '\n'.join(lines)

        # Convert @author mentions to GitHub profile links
        description = convert_author_mentions(description)
        changelog_entry += description
    else:
        changelog_entry += "No description available for this release."

    return changelog_entry


def write_changelog(changelog_content, filename="README.md"):
    """
    Write the changelog content to README.md, preserving the header content.

    Args:
        changelog_content (str): The changelog content to write
        filename (str): The filename to write to
    """
    try:
        # Read existing README content to preserve the header
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                existing_content = f.read()

            # Find where the changelog section starts (look for Table of Contents or old Changelog header)
            changelog_start = existing_content.find("# Table of Contents")
            if changelog_start == -1:
                # Fall back to looking for the old "## Changelog" header
                changelog_start = existing_content.find("## Changelog")
                if changelog_start != -1:
                    # Keep everything before "## Changelog" and add the new changelog content (removing the old header)
                    header_content = existing_content[:changelog_start]
                    final_content = header_content.rstrip() + "\n\n" + changelog_content
                else:
                    # If no changelog section found, append to existing content
                    final_content = existing_content.rstrip() + "\n\n" + changelog_content
            else:
                # Check if there's a "## Changelog" header before the Table of Contents
                changelog_header_pos = existing_content.find("## Changelog")
                if changelog_header_pos != -1 and changelog_header_pos < changelog_start:
                    # Keep everything before "## Changelog" and add the new changelog content (removing the old header)
                    header_content = existing_content[:changelog_header_pos]
                    final_content = header_content.rstrip() + "\n\n" + changelog_content
                else:
                    # Keep everything before "# Table of Contents" and add the new changelog content
                    header_content = existing_content[:changelog_start]
                    final_content = header_content.rstrip() + "\n\n" + changelog_content
        except FileNotFoundError:
            # If README doesn't exist, just write the changelog content
            final_content = changelog_content

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Successfully wrote changelog to {filename}")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")
        sys.exit(1)


def main():
    """Main function to orchestrate the changelog fetching and writing."""
    print("Fetching all DuckDB releases information...")

    # Fetch all releases
    releases = fetch_all_releases()

    if not releases:
        print("Failed to fetch release information")
        sys.exit(1)

    print(f"\nFound {len(releases)} total releases:")
    for i, release in enumerate(releases[:5]):  # Show first 5
        print(f"  - {release.get('tagName', 'Unknown')}")
    if len(releases) > 5:
        print(f"  ... and {len(releases) - 5} more")

    # Generate table of contents
    print("\nGenerating table of contents...")
    toc_content = generate_table_of_contents(releases)

    # Format each release entry
    print("Formatting release entries...")
    changelog_content = toc_content

    for i, release in enumerate(releases):
        if i % 10 == 0:  # Progress indicator every 10 releases
            print(f"  Processing release {i+1}/{len(releases)}: {release.get('tagName', 'Unknown')}")
        release_entry = format_changelog_entry(release)
        changelog_content += release_entry + "\n\n"

        # Add separator line between releases (except after the last one)
        if i < len(releases) - 1:
            changelog_content += "---\n\n"

    # Write to file
    print("\nWriting changelog to file...")
    write_changelog(changelog_content)

    print("Changelog generation completed successfully!")


if __name__ == "__main__":
    main()
