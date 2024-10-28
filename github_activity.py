import http.client  
import os
import json
import sys


def fetch_github_activity(username):
    connection = http.client.HTTPSConnection("api.github.com")
    endpoint = f"/users/{username}/events"
    
    headers = {"User-Agent": "GitHubActivityCLI"}
    
    connection.request("GET", endpoint, headers=headers)

    res = connection.getresponse()

    if res.status != 200:
        print("Error fetching data")
        sys.exit(1)
    
    data = res.read()
    
    return json.loads(data)


def display_github_activity(username):
    data = fetch_github_activity(username)

    for event in data:
        if event['type'] == 'PushEvent':
            print(f"Pushed to {event['repo']['name']} at {event['created_at']}")
        elif event['type'] == 'CreateEvent':
            print(f"Created {event['payload']['ref_type']} {event['payload']['ref']} at {event['repo']['name']} at {event['created_at']}")
        elif event['type'] == 'IssuesEvent':
            print(f"{event['payload']['action']} issue at {event['repo']['name']} at {event['created_at']}")
        elif event['type'] == 'IssueCommentEvent':
            print(f"{event['payload']['action']} comment on issue at {event['repo']['name']} at {event['created_at']}")
        elif event['type'] == 'WatchEvent':
            print(f"Starred {event['repo']['name']} at {event['created_at']}")
        elif event['type'] == 'ForkEvent':
            print(f"Forked {event['repo']['name']} at {event['created_at']}")
        elif event['type'] == 'PullRequestEvent':
            print(f"{event['payload']['action']} pull request at {event['repo']['name']} at {event['created_at']}")
        else:
            print(f"Unknown event type: {event['type']}")
        
def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username>")
        return

    username = sys.argv[1]
    display_github_activity(username)

if __name__ == "__main__":
    main()
    
    



