# GitHub Activity CLI

A command-line tool to fetch and display recent activity of a GitHub user. This tool leverages the GitHub API to provide insights into a user’s latest actions, including pushes, issues, and stars, directly in the terminal.

## Features

- Fetch recent GitHub activity for any user
- Display activities like:
  - Commits pushed
  - Issues opened/closed
  - Stars given
- Handles errors for invalid usernames or API issues

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/github-activity-cli.git
   cd github-activity-cli
   ```
2. **Make the script executable**:
   ```bash
   chmod +x github_activity.py
   ```

## Usage

Run the CLI by providing a GitHub username as an argument:

```bash
python github_activity.py <username>
```

**Example**:
```bash
python github_activity.py kamranahmedse
```

**Output**:
```
Pushed 3 commits to kamranahmedse/developer-roadmap
Opened an issue in kamranahmedse/developer-roadmap
Starred kamranahmedse/developer-roadmap
```

## Error Handling

- **Invalid Username**: Returns a "User not found" message.
- **API Issues**: Handles non-200 HTTP statuses with clear error messages.

---

Enjoy tracking GitHub activity directly from your terminal!
