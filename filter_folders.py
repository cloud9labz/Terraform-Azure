import os
import csv
from github import Github

# Replace with your GitHub personal access token
token = "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"

# Replace with your GitHub repository owner and name
repo_owner = "cloud9labz"
repo_name = "repo-b"

def filter_folders(repo):
    folders = []
    for content in repo.get_contents(""):
        if content.type == "dir":
            folder_name = content.name
            if folder_name.isdigit():
                continue  # Skip numerical folders
            match = re.search(r"(\d{14})_", folder_name)
            if match:
                folders.append((folder_name, content.commit.author.date))
    return folders

def write_to_csv(folders):
    with open("filtered_folders.csv", "w", newline="") as csvfile:
        fieldnames = ["Folder Name", "Commit Time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for folder in folders:
            writer.writerow({"Folder Name": folder[0], "Commit Time": folder[1]})

if __name__ == "__main__":
    g = Github(token)
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    folders = filter_folders(repo)
    write_to_csv(folders)
