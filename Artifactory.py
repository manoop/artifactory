from pyartifactory import Artifactory
from pyartifactory.models import RepositoryType

def get_artifactory_versions(base_url, repo, username, password):
    # Create an Artifactory instance
    artifactory = Artifactory(
        url=base_url,
        auth=(username, password),
        api_version="v1"
    )

    # Function to fetch versions from a given repository
    def fetch_versions(repo_path):
        versions = []
        for item in repo_path.glob("**/*"):
            if item.is_file():
                versions.append((item.name, item.stat().ctime))
        return versions

    # Fetch releases and snapshots
    releases_path = artifactory / repo / "releases"
    snapshots_path = artifactory / repo / "snapshots"

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
