# Git Practical Activities
**Student:** Coder-sus | **University:** UTS

---

## Lecture 1 - Git Fundamentals

### Activity 1 - Create and Initialize a Repository
Initialised a local Git repo and linked it to a remote repository on GitHub.

```bash
mkdir git-practical-activities && cd git-practical-activities
git init
git remote add origin https://github.com/Coder-sus/git-practical-activities.git
git remote -v
```

![Remote verified](screenshots/L1_A1_remote_verified.png)

---

### Activity 2 - Clone and Associate a Repository
Cloned the remote repo locally and made the first commit.

```bash
git clone https://github.com/Coder-sus/git-practical-activities.git
echo "Hello GitHub" > README.md
git add README.md
git commit -m "Initial commit"
git push -u origin main
```

![Commit history](screenshots/L1_A2_commit_history.png)

---

### Activity 3 - Branching and Merging
Created two feature branches independently and merged both back into main.

```bash
git checkout -b feature-1
echo "<h2>Feature 1</h2>" > feature1.html
git add feature1.html
git commit -m "feature-1: Added feature1.html"
git push origin feature-1
git checkout main
git merge feature-1
git push origin main
```

![Branch network](screenshots/L1_A3_branch_network.png)
![Files present](screenshots/L1_A3_ls_output.png)

---

### Activity 4 - Amend, Revert, Reset and Fetch by Hash
Used amend to fix a commit message, revert to undo a commit safely, reset to go back to a previous state, and checkout to inspect an old commit.

```bash
# Amend the last commit message
git commit --amend -m "Updated index.html with description"
git push origin main --force

# Revert a specific commit by hash
git revert d802eb8 --no-edit
git push origin main

# Hard reset to a previous commit
git reset --hard 5678efg
git push origin main --force

# Inspect a specific commit then return to main
git checkout cdef456
git checkout main
```

![Revert log](screenshots/L1_A4_revert_log.png)

---

### Activity 5 - Rebase and Resolve Conflicts
Created two branches editing the same file to deliberately cause a conflict, then rebased and resolved it manually.

```bash
git checkout branch-a
git rebase main
# resolve conflict in the file, then:
git add activities/lecture4/index.html
git rebase --continue
git push origin branch-a --force
```

![Conflict markers](screenshots/L1_A5_conflict_markers.png)
![Rebase complete](screenshots/L1_A5_rebase_complete.png)

---

## Lecture 2 - GitHub Actions Workflow

### Activity 1 - Setup Workflow
Created a workflow file that triggers automatically on every push to main.

![Workflow listed](screenshots/L2_A1_workflow_listed.png)

---

### Activity 2 - Update HTML Step
On each push, the workflow detects the GitHub actor and appends a timestamped line to `index.html`. GitHub Pages was enabled to serve the file live.

![Pages enabled](screenshots/L2_A2_pages_enabled.png)

---

### Activity 3 - Update README Step
The workflow appends the actor name, timestamp and short commit hash to `README.md` as a log entry after each push.

![README log](screenshots/L2_A3_readme_log.png)

---

### Activity 4 - Commit Changes Step and Permissions
The workflow commits the updated files and pushes them back to the repo using the GitHub token. Read and write permissions were enabled in repository settings.

![Permissions](screenshots/L2_A4_permissions.png)

---

### Activity 5 - Test the Workflow
Triggered the workflow with a push and confirmed all 4 steps completed successfully. Verified the live GitHub Pages site showed the updated content.

![Workflow success](screenshots/L2_A5_workflow_success.png)
![Pages live](screenshots/L2_A5_pages_live.png)

---

## Lecture 3 - Custom Docker Action

### Activity 3 - Project Structure
The repo follows a specific structure with the Dockerfile at the root and all scripts inside `.github/scripts/`.

```
git-practical-activities/
├── README.md
├── Dockerfile
├── data.txt
└── .github/
    ├── actions/vowel-frequency-analyzer/
    │   └── action.yml
    ├── workflows/
    │   └── ci.yml
    └── scripts/
        ├── frequency.py
        ├── update_readme.sh
        └── entrypoint.sh
```

![Repo structure](screenshots/L3_A3_repo_structure.png)

---

### Activity 4 - ci.yml
The workflow builds the Docker image from the Dockerfile and runs the container, passing the GitHub actor username as an environment variable.

---

### Activity 5 - action.yml
Defines the custom GitHub Action, specifying Docker as the runner and `entrypoint.sh` as the script to execute inside the container.

---

### Activity 6 - frequency.py
Reads `data.txt`, converts to lowercase and counts each vowel using Python's Counter. Exits with an error if the file is not found.

```bash
python3 activities/lecture3/.github/scripts/frequency.py activities/lecture3/data.txt
# Counter({'e': 20, 'a': 18, 'i': 15, 'o': 13, 'u': 11})
```

![Frequency output](screenshots/L3_A6_frequency_output.png)

---

### Activities 7 and 8 - update_readme.sh and entrypoint.sh
`entrypoint.sh` runs the Python script and captures the result. It then calls `update_readme.sh` which appends the result, username and timestamp to `README.md` and pushes the change.

![README updated](screenshots/L3_A78_readme_updated.png)

---

### Activity 9 - Dockerfile
Uses `python:3.9-slim` as the base image, installs git, copies all project files and sets `entrypoint.sh` as the container entry point.

![Docker run success](screenshots/L3_A9_docker_run_success.png)

---

## Lecture 4 - Full CI/CD Pipeline

### Activity 3 - todo.py
Implements two classes: `Task` (title, status, mark_completed) and `TaskPool` (add, filter by ToDo or Done). Prints all open and completed tasks.

```bash
python3 activities/lecture4/todo.py
```

![todo output](screenshots/L4_A3_todo_output.png)

---

### Activity 4 - todo-test.py
Three unit tests verify that tasks can be added, open tasks are returned correctly and done tasks are returned correctly. All pass.

```bash
python3 activities/lecture4/todo-test.py
```

![Tests pass](screenshots/L4_A4_tests_pass.png)

---

### Activities 5, 6 and 7 - update_index.sh, entrypoint.sh, Dockerfile
`entrypoint.sh` runs both Python scripts and pipes output to files. `update_index.sh` injects the task lists and test results into the `<pre>` tags in `index.html`. The Dockerfile packages all of this and sets the entrypoint.

![Index updated](screenshots/L4_A567_index_updated.png)

---

### Activity 8 - ci.yml
Builds the Docker image tagged `task-manager:latest` and runs the container on every push to main, passing the GitHub actor as an environment variable.

---

### Activity 9 - tracker.yml
Listens for pull request close events. If the PR was merged, it extracts the issue number from `Closes #N` in the PR description and labels that issue as done via the GitHub API.

![Issue labelled](screenshots/L4_A9_issue_labelled.png)

---

### Activity 10 - Testing the CI/CD Pipeline
Completed a full end-to-end test by creating an issue, opening a PR that references it, and merging to trigger both workflows.

| Step | Action | Result |
|------|--------|--------|
| 1 | Created GitHub Project board | Done |
| 2 | Created issue and assigned to self | Done |
| 3 | Created branch, committed and pushed | Done |
| 4 | Opened PR with Closes #1 in description | Done |
| 5 | Merged PR, ci.yml triggered | Done |
| 6 | Merged PR, tracker.yml triggered | Done |
| 7 | index.html updated with latest task and test data | Done |

![Project board](screenshots/L4_A10_project_board.png)
![Pull request](screenshots/L4_A10_pull_request.png)
![Workflows green](screenshots/L4_A10_workflows_green.png)
### Updated by Coder-sus on 2026-05-27 12:19:26 [Commit: e76fd28]
