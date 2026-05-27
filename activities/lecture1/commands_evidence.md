# Lecture 1 – Git Practical Activities Evidence

## Activity 1: Create and Initialize a Repository

```bash
# Create remote repo on GitHub via UI, then locally:
mkdir git-practical-activities
cd git-practical-activities
git init
git remote add origin https://github.com/Coder-sus/git-practical-activities.git

# Verify remote connection
git remote -v
# origin  https://github.com/Coder-sus/git-practical-activities.git (fetch)
# origin  https://github.com/Coder-sus/git-practical-activities.git (push)
```

---

## Activity 2: Clone and Associate a Repository

```bash
# Clone the repo locally
git clone https://github.com/Coder-sus/git-practical-activities.git
cd git-practical-activities

# First commit
echo "Hello GitHub" > README.md
git add README.md
git commit -m "Initial commit for git-practical-activities"
git push -u origin main

# Simulate a second contributor commit
echo "Second update" >> README.md
git add README.md
git commit -m "Second commit: updated README"
git push origin main

# Pull to sync
git pull origin main
```

---

## Activity 3: Branching and Merging

```bash
# Create and merge feature-1 branch
git checkout -b feature-1
echo "<h2>Feature 1</h2>" > feature1.html
git add feature1.html
git commit -m "feature-1: Added feature1.html"
git push origin feature-1
git checkout main
git merge feature-1
git push origin main

# Create and merge feature-2 branch
git checkout -b feature-2
echo "<h2>Feature 2</h2>" > feature2.html
git add feature2.html
git commit -m "feature-2: Added feature2.html"
git push origin feature-2
git checkout main
git merge feature-2
git push origin main

# Sync and verify all files present
git fetch origin
git pull origin main
ls
# Expected: README.md  feature1.html  feature2.html  index.html
```

---

## Activity 4: Amend, Revert, Reset, and Fetch a Commit by Log ID

```bash
# Amend a commit
echo "<h1>Updated Title</h1>" > index.html
git add index.html
git commit -m "Initial commit with index.html"
echo "<p>Description added</p>" >> index.html
git add index.html
git commit --amend -m "Updated index.html with description"
git push origin main --force

# Revert a commit
git log --oneline
# abcd123 Added feature1.html
# 5678efg Updated index.html with description
git revert abcd123
git push origin main

# Reset to a previous state
git log --oneline
# 9876hij Added unnecessary file
# 5678efg Updated index.html with description
git reset --hard 5678efg
git push origin main --force

# Checkout a specific commit by hash (detached HEAD)
git log --oneline
# cdef456 Added a feature
git checkout cdef456
git checkout main   # return to main
```

---

## Activity 5: Rebase and Resolve Conflicts

```bash
# Create two branches that both modify index.html (to force a conflict)
git checkout -b branch-a
echo "<h3>Change from branch-a</h3>" >> index.html
git add index.html
git commit -m "branch-a: updated index.html"
git push origin branch-a

git checkout main
git checkout -b branch-b
echo "<p>Change from branch-b</p>" >> index.html
git add index.html
git commit -m "branch-b: updated index.html"
git push origin branch-b
git checkout main
git merge branch-b
git push origin main

# Rebase branch-a onto main (conflict will occur)
git checkout branch-a
git fetch origin main
git rebase origin/main
# Conflict markers appear in index.html:
# <<<<<<< HEAD
# <p>Change from branch-b</p>
# =======
# <h3>Change from branch-a</h3>
# >>>>>>> branch-a
# Edit the file to keep both changes, then:
git add index.html
git rebase --continue
git push origin branch-a --force

# Merge and clean up
git checkout main
git merge branch-a
git push origin main
git branch -d branch-a
git branch -d branch-b
```
