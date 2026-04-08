# Repo Reaper

A lightweight Python script that scans your GitHub account to identify dead, abandoned repositories.
> It filters your profile for repos that meet three strict conditions:
> - 0 Stars
> - 0 Forks
> - No code pushes in over 365 days

## Prerequisites
- Python 3.x
- A GitHub Personal Access Token (PAT) with `repo` scopes.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aditya4w/Repo-Reaper.git
   cd Repo_Reaper

2. **Install dependencies:**
   ```bash
   pip install requests

3. **Configure authentication:**
   - Rename `config.example.py` to `config.py`.
   - Open `config.py` and replace the placeholder with your actual GitHub PAT:

   ```bash
   GITHUB_PAT = "YOUR_GITHUB_PAT_TOKEN"

## How to Generate a GitHub PAT (Personal Access Token)

1. Log in to GitHub and click your profile picture in the top right corner, then select **Settings**.
2. Scroll to the bottom of the left sidebar and click **Developer settings**.
3. In the left sidebar, click **Personal access tokens**, then select **Tokens (classic)**.
4. Click **Generate new token** (top right) and select **Generate new token (classic)**.
5. In the **Note** field, name it something recognizable (e.g., "Repo Reaper").
6. Set an **Expiration** date (30 days is recommended for security).
7. Under **Select scopes**, check the box next to `repo`. This grants the script permission to read your repositories.
8. Scroll to the bottom and click **Generate token**.
9. **Copy the token immediately.** GitHub will only display it once. Paste this token into your `config.py` file. 

## Usage

Exucute the script in your terminal:
  ```bash
  python app.py
  ```

> The script will fetch your data, run the time math, and output a clean list of URLs for any repositories ready to be deleted.
