# Git Practical Activities
**Student:** Tushar Kaushik **Repo:** git-practical-activities

---

## Lecture 1 - Git Fundamentals

### Activity 1 - Create and Initialize a Repository
Created a remote repository on GitHub, initialised a local repo and linked them.

```bash
mkdir git-practical-activities && cd git-practical-activities
git init
git remote add origin https://github.com/Coder-sus/git-practical-activities.git
git remote -v
```

![Remote verified](screenshots/L1_A1_remote_verified.png)

---

### Activity 2 - Clone and Associate a Repository
Cloned the repo locally, made an initial commit and pushed to remote.

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
Created two feature branches, made changes on each and merged both into main.

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

```bash
# Amend
git commit --amend -m "Updated index.html with description"
git push origin main --force

# Revert
git revert d802eb8 --no-edit
git push origin main

# Reset
git reset --hard 5678efg
git push origin main --force

# Checkout by hash
git checkout cdef456
git checkout main
```

![Revert log](screenshots/L1_A4_revert_log.png)

---

### Activity 5 - Rebase and Resolve Conflicts
Created two branches that both modified the same file to force a conflict, then rebased and resolved it.

```bash
git checkout branch-a
git rebase main
# conflict appears -- resolve it, then:
git add activities/lecture4/index.html
git rebase --continue
git push origin branch-a --force
```

![Conflict markers](screenshots/L1_A5_conflict_markers.png)
![Rebase complete](screenshots/L1_A5_rebase_complete.png)

---

## Lecture 2 - GitHub Actions Workflow

### Activity 1 - Setup Workflow
Created `.github/workflows/main.yml` triggering on push to main.

![Workflow listed](screenshots/L2_A1_workflow_listed.png)

### Activity 2 - Update HTML Step
Workflow appends a timestamped paragraph tag to `index.html` on every push. GitHub Pages enabled.

![Pages enabled](screenshots/L2_A2_pages_enabled.png)

### Activity 3 - Update README Step
Workflow appends actor name, timestamp and commit hash to `README.md` on every push.

![README log](screenshots/L2_A3_readme_log.png)

### Activity 4 - Commit Changes Step and Permissions
Workflow commits and pushes changes back to the repo. Read and write permissions set.

![Permissions](screenshots/L2_A4_permissions.png)

### Activity 5 - Test the Workflow
Pushed a change and verified all 4 steps completed successfully.

![Workflow success](screenshots/L2_A5_workflow_success.png)
![Pages live](screenshots/L2_A5_pages_live.png)

---

## Lecture 3 - Custom Docker Action

### Activity 3 - Project Structure

```
git-practical-activities/
├── README.md
├── Dockerfile
├── data.txt
├── .github/
│   ├── actions/vowel-frequency-analyzer/
│   │   └── action.yml
│   ├── workflows/
│   │   └── ci.yml
│   └── scripts/
│       ├── frequency.py
│       ├── update_readme.sh
│       └── entrypoint.sh
```

![Repo structure](screenshots/L3_A3_repo_structure.png)

### Activity 4 - ci.yml
Workflow builds a Docker image and runs the container, passing the GitHub actor as an environment variable.

### Activity 5 - action.yml
Custom action definition using Docker, specifying the entrypoint script and file input.

### Activity 6 - frequency.py
Python script that counts vowel frequency in a text file using Counter.

```bash
python3 activities/lecture3/.github/scripts/frequency.py activities/lecture3/data.txt
# Output: Counter({'e': 20, 'a': 18, 'i': 15, 'o': 13, 'u': 11})
```

![Frequency output](screenshots/L3_A6_frequency_output.png)

### Activities 7 and 8 - update_readme.sh and entrypoint.sh
Shell scripts that run the Python analyser, then append results with username and timestamp to README.

![README updated](screenshots/L3_A78_readme_updated.png)

### Activity 9 - Dockerfile
Container built from python:3.9-slim, installs git, copies project files and runs entrypoint.sh.

![Docker run success](screenshots/L3_A9_docker_run_success.png)

---

## Lecture 4 - Full CI/CD Pipeline

### Activity 3 - todo.py
Python task management system with Task and TaskPool classes.

```bash
python3 activities/lecture4/todo.py
```

![todo output](screenshots/L4_A3_todo_output.png)

### Activity 4 - todo-test.py
Unit tests for the TaskPool class. All 3 tests pass.

```bash
python3 activities/lecture4/todo-test.py
```

![Tests pass](screenshots/L4_A4_tests_pass.png)

### Activities 5, 6 and 7 - update_index.sh, entrypoint.sh, Dockerfile
Scripts that inject task lists and test results into index.html, run via Docker container.

![Index updated](screenshots/L4_A567_index_updated.png)

### Activity 8 - ci.yml
Builds and runs the Docker container on every push to main.

### Activity 9 - tracker.yml
Triggers on PR close. If merged, labels the linked issue as done via GitHub API.

![Issue labelled](screenshots/L4_A9_issue_labelled.png)

### Activity 10 - Testing the CI/CD Pipeline

| Step | Action | Result |
|------|--------|--------|
| 1 | Created GitHub Project board | Done |
| 2 | Created issue and assigned to self | Done |
| 3 | Created branch, committed, pushed | Done |
| 4 | Created PR with Closes #1 in description | Done |
| 5 | Merged PR, triggered ci.yml | Done |
| 6 | Merged PR, triggered tracker.yml | Done |
| 7 | index.html updated with task and test data | Done |

![Project board](screenshots/L4_A10_project_board.png)
![Pull request](screenshots/L4_A10_pull_request.png)
![Workflows green](screenshots/L4_A10_workflows_green.png)
