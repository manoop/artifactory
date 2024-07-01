from pyartifactory import Artifactory
from datetime import datetime

def get_artifactory_versions(base_url, repo, username, password):
    # Create an Artifactory instance
    artifactory = Artifactory(
        url=base_url,
        auth=(username, password)
    )

    # Function to fetch versions from a given repository path
    def fetch_versions(repo_path):
        artifacts = artifactory.artifacts.list(repository=repo_path)
        versions = []
        for artifact in artifacts:
            version = artifact['uri'].split('/')[-1]
            created_date = artifact['created']
            created_date = datetime.strptime(created_date, '%Y-%m-%dT%H:%M:%S.%fZ')
            versions.append((version, created_date))
        return versions

    # Fetch releases and snapshots
    releases_path = f"{repo}/releases"
    snapshots_path = f"{repo}/snapshots"

    releases = fetch_versions(releases_path)
    snapshots = fetch_versions(snapshots_path)

    # Print the versions with dates
    if releases:
        print("Release Versions:")
        for version, date in releases:
            print(f"Version: {version}, Date: {date}")

    if snapshots:
        print("\nSnapshot Versions:")
        for version, date in snapshots:
            print(f"Version: {version}, Date: {date}")

# Replace with your Artifactory URL, repository, username, and password
artifactory_url = "https://your-artifactory-domain/artifactory"
repository = "libs-release-local"  # Example repository name
user = "your-username"
pwd = "your-password"

# Get the list of versions
get_artifactory_versions(artifactory_url, repository, user, pwd)
