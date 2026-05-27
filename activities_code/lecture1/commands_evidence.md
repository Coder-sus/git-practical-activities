# Lecture 1 – Git Practical Activities Evidence

## Activity 1: Create and Initialize a Repository

```bash
# 1. Create remote repo on GitHub (done via UI)

# 2. Initialize local repo
mkdir git-practical-activities
cd git-practical-activities
git init
git remote add origin https://github.com/Coder-sus/git-practical-activities.git

# 3. Verify remote connection
git remote -v
# Expected output:
# origin  https://github.com/Coder-sus/git-practical-activities.git (fetch)
# origin  https://github.com/Coder-sus/git-practical-activities.git (push)
```

---

## Activity 2: Clone and Associate a Repository

```bash
# Team clone
git clone https://github.com/Coder-sus/git-practical-activities.git

# Team leader: first commit
echo "Hello GitHub" > README.md
git add README.md
git commit -m "Initial commit for git-practical-activities"
git push -u origin main

# Team members: pull after leader pushes
git pull origin main

# Each member: make a change and push
echo "Updated by Member 1" >> README.md
git add README.md
git commit -m "Member 1: updated README"
git push origin main

# Others pull again
git pull origin main
```

---

## Activity 3: Branching and Merging

```bash
# Phase 1 – Team Leader
git branch leader-feature
git checkout leader-feature
echo "<h2>Leader's Feature</h2>" > leader.html
git add leader.html
git commit -m "Leader feature: Added leader.html"
git push origin leader-feature
git checkout main
git merge leader-feature
git push origin main

# Phase 2 – Member 1
git branch member1-feature
git checkout member1-feature
echo "<h2>Team Member 1's Feature</h2>" > member1.html
git add member1.html
git commit -m "Member 1 feature: Added member1.html"
git push origin member1-feature
# Leader merges
git checkout main
git merge member1-feature
git push origin main

# Phase 2 – Member 2
git pull origin main
git branch member2-feature
git checkout member2-feature
echo "<h2>Team Member 2's Feature</h2>" > member2.html
git add member2.html
git commit -m "Member 2 feature: Added member2.html"
git push origin member2-feature
# Leader merges
git checkout main
git merge member2-feature
git push origin main

# Phase 3 – All members sync
git checkout main
git fetch origin
git pull origin main
ls
# Expected: README.md  leader.html  member1.html  member2.html
```

---

## Activity 4: Amend, Revert, Reset, and Fetch a Commit by Log ID

```bash
# Phase 1 – Team Leader: Amend a commit
echo "<h1>Updated Title</h1>" > index.html
git add index.html
git commit -m "Initial commit with index.html"
# Realise description was missing:
echo "<p>Description added</p>" >> index.html
git add index.html
git commit --amend -m "Updated index.html with description"
git push origin main --force

# Phase 2 – Member 1: Revert a commit
git log --oneline
# abcd123 Added member1.html
# 5678efg Updated index.html with description
git revert abcd123
git push origin main

# Phase 3 – Member 2: Reset a commit
git log --oneline
# 9876hij Added unnecessary file
# 5678efg Updated index.html with description
git reset --hard 5678efg
git push origin main --force

# Phase 4 – Team Leader: Fetch a commit by hash
git log --oneline
# cdef456 Added a feature
# abcd123 Added member1.html
git checkout cdef456   # enters detached HEAD state
git checkout main      # return to main
```

---

## Activity 5: Rebase and Resolve Conflicts

```bash
# Phase 1 – Leader confirms files exist: index.html, member1.html, member2.html

# Phase 2 – Member 1: modify member1.html on a branch
git checkout -b member1-feature
echo "<h3>Updated by Member 1</h3>" >> member1.html
git add member1.html
git commit -m "Member 1 feature: Updated member1.html"
git push origin member1-feature

# Phase 2 – Member 2: modify index.html on a branch
git checkout -b member2-feature
echo "<p>Details updated by Member 2</p>" >> index.html
git add index.html
git commit -m "Member 2 feature: Updated index.html"
git push origin member2-feature

# Phase 3 – Member 1: rebase onto main
git checkout member1-feature
git fetch origin main
git rebase origin/main
# If conflict markers appear:
# <<<<<<< HEAD
# <p>Details updated by Member 2</p>
# =======
# <h3>Updated by Member 1</h3>
# >>>>>>> member1-feature
# Edit file to keep both, then:
git add index.html member1.html
git rebase --continue
git push origin member1-feature --force

# Phase 3 – Member 2: rebase
git checkout member2-feature
git fetch origin main
git rebase origin/main
git add index.html
git rebase --continue
git push origin member2-feature --force

# Phase 4 – Leader finalises
git checkout main
git merge member1-feature
git merge member2-feature
git push origin main
git branch -d member1-feature
git branch -d member2-feature
```
