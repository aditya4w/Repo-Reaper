from config import GITHUB_PAT
import requests
from datetime import datetime, timezone

def line():
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_PAT}",
    "X-GitHub-Api-Version": "2022-11-28"
}

url = "https://api.github.com/user/repos"
parameters = {"affiliation": "owner", "per_page": 100, "page": 1}

masterList = []
while True:
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if not data:
        break

    else:
        masterList.extend(data)
        parameters["page"] +=1 

line()
print(f"Repos count: {len(masterList)}")

junkBin = []

for repo in masterList:
    name = repo["name"]
    url = repo["html_url"]
    stars = repo["stargazers_count"]
    forks = repo["forks_count"]
    last_push = repo["pushed_at"]

    last_push_date = datetime.fromisoformat(last_push.replace("Z", "+00.00"))
    current_time = datetime.now(timezone.utc)

    days_inactive = (current_time - last_push_date).days

    if days_inactive > 365 and stars == 0 and forks == 0:
        junkBin.append({"name": name, "url": url})


if len(junkBin) > 0:
    line()
    print("===== JUNK REPOS =====")
    for repo in junkBin:
        print(f"{repo['name']}: {repo['url']}")
        line()

else:
    line()
    print("No junk repo found. You're all set!")
    line()
