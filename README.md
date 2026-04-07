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
   git clone https://github.com/aditya4w/Repo_Reaper.git
   cd Repo_Reaper

2. **Install dependencies:**
   ```bash
   pip install requests

3. **Configure authentication:**
   - Rename `config.example.py` to `config.py`.
   - Open `config.py` and replace the placeholder with your actual GitHub PAT:

   ```bash
   GITHUB_PAT = "YOUR_GITHUB_PAT_TOKEN"

## Usage

Exucute the script in your terminal:
  ```bash
  python app.py
  ```

> The script will fetch your data, run the time math, and output a clean list of URLs for any repositories ready to be deleted.
