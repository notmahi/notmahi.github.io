import json

import requests
import html


class HTMLEncodedJSONEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, str):
            return '"' + html.escape(obj) + '"'
        elif isinstance(obj, list):
            return "[" + ", ".join(self.encode(e) for e in obj) + "]"
        elif isinstance(obj, dict):
            items = (f"{json.dumps(k)}: {self.encode(v)}" for k, v in obj.items())
            return "{" + ", ".join(items) + "}"
        else:
            return super().encode(obj)


GITHUB_API_URL = "https://api.github.com/repos/{}"

if __name__ == "__main__":
    # Load the configuration file
    with open("_data/repos.json", "r") as jsonfile:
        cfg = json.load(jsonfile)
    repo_list = [repo["full_name"] for repo in cfg]
    data_dict = []
    for repo in repo_list:
        # Get the repo data
        response = requests.get(GITHUB_API_URL.format(repo))
        # Filter out only the necessary data:
        # full_name, name, description, language, stargazers_count, forks_count
        data = response.json()
        data_dict.append(
            {
                "full_name": data["full_name"],
                "name": data["name"],
                "description": data["description"],
                "language": data["language"],
                "stargazers_count": data["stargazers_count"],
                "forks_count": data["forks_count"],
                "html_url": data["html_url"],
            }
        )
    # Save the data to a file
    with open("_data/repos.json", "w") as jsonfile:
        jsonfile.write(json.dumps(data_dict, cls=HTMLEncodedJSONEncoder))
