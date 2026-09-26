# Axiom Evaluation Review — 2026-09-20

- axiom: **a09**
- window: 7 天
- total candidates: 12

對每個 candidate 勾選 **一個** 選項。多選或全空會被 parser 拒絕。

## a09

### Candidate 1
- session: `16b17d91-0bcf-4859-bb88-98985a41221e`
- timestamp: 2026-09-17T02:29:58.651Z
- command: `git checkout -b content/2026-09-17 origin/content/2026-09-17 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/16b17d91-0bcf-4859-bb88-98985a41221e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 2
- session: `347669dd-aa20-4602-9a8c-5b8cebdc4f55`
- timestamp: 2026-09-17T22:55:40.613Z
- command: `git checkout -b content/2026-09-18 origin/content/2026-09-18 2>&1 | tail -5; echo "=== 分支與 dirty 狀態 ==="; git branch --show-current; git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/347669dd-aa20-4602-9a8c-5b8cebdc4f55.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 3
- session: `347669dd-aa20-4602-9a8c-5b8cebdc4f55`
- timestamp: 2026-09-17T22:56:05.312Z
- command: `git checkout -b content/2026-09-18 main 2>&1 | tail -3; echo "=== 分支 ==="; git branch --show-current; echo "=== upstream（應為空，避免裸 push 風險）==="; git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>&1 | head -2; echo "=== dirty ==="; git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/347669dd-aa20-4602-9a8c-5b8cebdc4f55.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 4
- session: `3add17a1-c396-419e-9216-94c6a729d3cd`
- timestamp: 2026-09-15T08:26:10.904Z
- command: `git branch --list feature/fix-validate-roadmap-hash-rule-inverted
git branch feature/fix-validate-roadmap-hash-rule-inverted origin/feature/fix-validate-roadmap-hash-rule-inverted
git log main..feature/fix-validate-roadmap-hash-rule-inverted --oneline`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/3add17a1-c396-419e-9216-94c6a729d3cd.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 5
- session: `3add17a1-c396-419e-9216-94c6a729d3cd`
- timestamp: 2026-09-15T08:28:00.455Z
- command: `git status --short | head -3
echo "---branch check---"
git branch --list feature/fix-board-test-completed-project-skip
git fetch -q origin feature/fix-board-test-completed-project-skip 2>&1 | tail -2
git branch feature/fix-board-test-completed-project-skip origin/feature/fix-board-test-completed-project-skip 2>&1
echo "---Step 1: status---"
git log main..feature/fix-board-test-completed-project-skip --oneline
git diff main...feature/fix-board-test-completed-project-skip --name-only`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/3add17a1-c396-419e-9216-94c6a729d3cd.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 6
- session: `5b2e32f0-d5c6-403c-88c8-176d157451eb`
- timestamp: 2026-09-19T14:32:44.025Z
- command: `set -e
git branch content/2026-09-19 origin/content/2026-09-19
TMP_WT="/Users/dj_workstation/Code/Exocortex-personal/.claude/worktrees/tmp-content-2026-09-19"
git worktree add "$TMP_WT" content/2026-09-19
mv inbox/captured/2026-09-19_state_audit.md "$TMP_WT/inbox/captured/2026-09-19_state_audit.md"
git -C "$TMP_WT" add inbox/captured/2026-09-19_state_audit.md
git -C "$TMP_WT" commit -q -m "content: add 2026-09-19 state_audit snapshot（18:30 cron）"
git -C "$TMP_WT" log --oneline -1
git -C "$TMP_WT" status --short
git worktree remove "$TMP_WT"
echo "--- main checkout ---"
git branch --show-current; git status --porcelain; git rev-list --left-right --count content/2026-09-19...origin/content/2026-09-19`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/5b2e32f0-d5c6-403c-88c8-176d157451eb.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 7
- session: `a1265d7b-e480-41a0-835a-d65ce85dfb3c`
- timestamp: 2026-09-16T01:26:31.755Z
- command: `cd /Users/dj_workstation/Code/Exocortex-personal
if git rev-parse --verify content/2026-09-15 >/dev/null 2>&1; then
  git checkout content/2026-09-15
else
  git checkout -b content/2026-09-15 main
fi
echo "---"
git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/a1265d7b-e480-41a0-835a-d65ce85dfb3c.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 8
- session: `beb2cc92-5ce8-4e02-9400-fff8a69c9e81`
- timestamp: 2026-09-16T21:05:37.221Z
- command: `git branch -D content/2026-09-17 && git branch content/2026-09-17 origin/main && git log --oneline -1 content/2026-09-17`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/beb2cc92-5ce8-4e02-9400-fff8a69c9e81.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 9
- session: `beb2cc92-5ce8-4e02-9400-fff8a69c9e81`
- timestamp: 2026-09-16T21:10:48.985Z
- command: `git branch content/2026-09-17 origin/main && git log --oneline -1 content/2026-09-17`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/beb2cc92-5ce8-4e02-9400-fff8a69c9e81.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 10
- session: `87781aea-ddcd-4706-a9fd-ebefb660edcd`
- timestamp: 2026-09-16T22:25:23.201Z
- command: `git checkout -b feature/quiet-state-audit-detector-noise origin/main 2>&1 && git log --oneline -1 && git rev-list origin/main..HEAD | wc -l && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal--claude-worktrees-2026-09-17-audit-cleanup-b2/87781aea-ddcd-4706-a9fd-ebefb660edcd.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 11
- session: `648b6e1d-7142-4e0f-92b9-1cbcabfe163a`
- timestamp: 2026-09-17T07:34:50.689Z
- command: `set -e; D=/Users/dj_workstation/.claude/jobs/648b6e1d/tmp/mt; rm -rf "$D"; mkdir -p "$D"; cd "$D"; git init -q -b main .; git config user.email t@e; git config user.name t
printf 'a\n' > f.txt; printf 'v1\n' > rule.md; git add -A; git commit -qm seed
git branch content
# origin-side peer content diverges
git checkout -q -b peer content; printf 'peer\n' > peer.md; git add -A; git commit -qm peer
# main advances (origin/main), touching rule.md
git checkout -q main; printf 'v2-main\n' > rule.md; git add -A; git commit -qm mainadv
# content (local) edits rule.md too (add/add style conflict)
git checkout -q content; printf 'v2-content\n' > rule.md; git add -A; git commit -qm contentedit
git checkout -q main
before=$(git for-each-ref --format='%(refname) %(objectname)' | sort | md5); objs_before=$(git count-objects -v | grep '^count')
# step 1: simulate sync (content + peer)
out1=$(git merge-tree --write-tree --name-only content peer); rc1=$?; echo "sync rc=$rc1"; T1=$(echo "$out1" | head -1); echo "T1=$T1"
# merge base between main and hypothetical merge(content,peer)
git merge-base --all main content peer
MB=$(git merge-base main content peer)
set +e
out2=$(git merge-tree --write-tree --name-only --merge-base="$MB" "$T1" main); rc2=$?
echo "base-merge rc=$rc2"; echo "$out2"
after=$(git for-each-ref --format='%(refname) %(objectname)' | sort | md5)
echo "refs same: $([ "$before" = "$after" ] && echo yes || echo no)"; git status --porcelain | wc -l; git count-objects -v | grep '^count'; echo "$objs_before"
git fsck --unreachable --no-reflogs 2>/dev/null | awk '{print $2}' | sort | uniq -c`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal--claude-worktrees-2026-09-17-p13-recover/648b6e1d-7142-4e0f-92b9-1cbcabfe163a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 12
- session: `728fd03b-7863-48d6-b31c-871b06f3c56e`
- timestamp: 2026-09-13T16:36:47.307Z
- command: `echo "=== 1) 建立 content/2026-09-14（base: origin/main，依 4.0b guard）==="
git branch content/2026-09-14 origin/main && echo "  ✓ 分支已建立"
git branch --list content/2026-09-14
echo
echo "=== 2) 開臨時 worktree（絕對路徑，錨定 main_checkout）==="
git worktree add /Users/dj_workstation/Code/Exocortex-personal/.claude/worktrees/tmp-content-2026-09-14 content/2026-09-14 2>&1 | tail -3
echo
echo "=== 3) 疊上 content-shaped 檔案 ==="
cp /Users/dj_workstation/Code/Exocortex-personal/.claude/worktrees/ghost-blog-optimization/contexts/work_logs/2026-09-14_ghost-blog-optimization_ghost-preview-route-mission.md /Users/dj_workstation/Code/Exocortex-personal/.claude/worktrees/tmp-content-2026-09-14/contexts/work_logs/ && echo "  ✓ 已複製"
ls -la /Users/dj_workstation/Code/Exocortex-personal/.claude/worktrees/tmp-content-2026-09-14/contexts/work_logs/2026-09-14_ghost-blog-optimization_ghost-preview-route-mission.md`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal--claude-worktrees-ghost-blog-optimization/728fd03b-7863-48d6-b31c-871b06f3c56e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

