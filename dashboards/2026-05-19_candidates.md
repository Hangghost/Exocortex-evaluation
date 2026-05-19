# Axiom Evaluation Review — 2026-05-19

- axiom: **a09**
- window: 30 天
- total candidates: 97

對每個 candidate 勾選 **一個** 選項。多選或全空會被 parser 拒絕。

## a09

### Candidate 1
- session: `03288b23-cf7f-449d-a14b-b2f31325314e`
- timestamp: 2026-05-17T21:55:34.142Z
- command: `git checkout -b content/2026-05-18 main && git add -A && git status --short | head -25`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/03288b23-cf7f-449d-a14b-b2f31325314e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 2
- session: `03288b23-cf7f-449d-a14b-b2f31325314e`
- timestamp: 2026-05-17T23:26:48.216Z
- command: `git checkout -b content/2026-05-18 main && git add -A && git commit -m "content: 2026-05-18 stale-bridge trilogy补建 + routing-guard edge case aggregation" && echo "---log---" && git log --oneline -3 && echo "---back to main per step 4.3---" && git checkout main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/03288b23-cf7f-449d-a14b-b2f31325314e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 3
- session: `0e3ce94f-5ed2-4d39-874e-d8fc356b72f3`
- timestamp: 2026-04-29T17:18:44.034Z
- command: `git checkout main && git merge --squash content/2026-04-29 && git commit -m "content: 2026-04-29 daily snapshot" && git branch -D content/2026-04-29 && git checkout -b content/2026-04-30 && echo "---" && git log --oneline -5`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/0e3ce94f-5ed2-4d39-874e-d8fc356b72f3.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 4
- session: `1822eb6d-8b86-4ffe-b2a8-8571aebbf61b`
- timestamp: 2026-05-01T04:05:01.151Z
- command: `git checkout main && git checkout -b feature/add-state-audit && echo "---" && git status --short && echo "---" && git branch --show-current`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/1822eb6d-8b86-4ffe-b2a8-8571aebbf61b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 5
- session: `195eec1d-6749-4bc0-985c-d7d0a2c21de5`
- timestamp: 2026-04-28T20:55:22.609Z
- command: `git checkout -b content/2026-04-29 && git stash pop`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/195eec1d-6749-4bc0-985c-d7d0a2c21de5.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 6
- session: `20b603bb-85be-4952-9f70-e5f5e5f84204`
- timestamp: 2026-05-05T09:58:35.363Z
- command: `cd /Users/dj_workstation/Documents/Projects/Exocortex-personal

echo "=== 1. switch main + 建 content/2026-05-05 ==="
git switch main
git status --short
git checkout -b content/2026-05-05 main
git status --short

echo ""
echo "=== 2. commit .gitignore on content/2026-05-05 ==="
git add .gitignore
git commit -m "$(cat <<'EOF'
gitignore: add .claude/scheduled_tasks.lock (cron skill runtime state)

Cron skill (CronCreate/CronDelete) writes runtime state here; not meant for
commit. Mirrors the existing .claude/settings.local.json ignore pattern.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git log --oneline -3

echo ""
echo "=== 3. 確認 dirty 已清乾淨 ==="
git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/20b603bb-85be-4952-9f70-e5f5e5f84204.jsonl`

- [ ] approve — 送 LLM judge
- [x] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 7
- session: `20b603bb-85be-4952-9f70-e5f5e5f84204`
- timestamp: 2026-05-05T10:02:49.754Z
- command: `cd /Users/dj_workstation/Documents/Projects/Exocortex-personal

echo "=== 當前分支 ==="
git branch --show-current

echo ""
echo "=== working tree 狀態 ==="
git status --short

echo ""
echo "=== 本地分支列表 ==="
git branch

echo ""
echo "=== local vs origin sync ==="
git fetch --all --quiet
echo "main:                    local=$(git rev-parse --short main)  origin=$(git rev-parse --short origin/main)"
echo "project/yoga-cs-agent:   local=$(git rev-parse --short project/yoga-cs-agent)  origin=$(git rev-parse --short origin/project/yoga-cs-agent)"
echo "content/2026-05-05:      $(git rev-parse --verify --short origin/content/2026-05-05 2>/dev/null || echo '✓ 已從 origin 刪除')"

echo ""
echo "=== main 最近 5 commit ==="
git log main --oneline -5

echo ""
echo "=== 今日 (2026-05-05) 在 main 的 commits ==="
git log main --oneline --since="2026-05-05 00:00" --until="2026-05-06 00:00" 2>&1

echo ""
echo "=== state_audit 最終結果 ==="
uv run python -c "
from infra.periodic_jobs.state_audit import audit
report = audit()
if not report.findings:
    print('✓ 0 findings — clean state')
else:
    print(f'{len(report.findings)} findings:')
    for f in report.findings:
        print(f'  - {f.kind}: {getattr(f, \"detail\", {})}')
" 2>&1 | head -10`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/20b603bb-85be-4952-9f70-e5f5e5f84204.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 8
- session: `247f6191-ba3a-4494-9c0a-876b99725f84`
- timestamp: 2026-05-04T05:18:36.931Z
- command: `git checkout main && git checkout -b project/qt-ai-enablement`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/247f6191-ba3a-4494-9c0a-876b99725f84.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 9
- session: `27273989-e1a1-49e6-8288-f3e637f6aa1e`
- timestamp: 2026-04-29T04:57:04.233Z
- command: `cd /Users/dj_workstation/Documents/Projects/qtm-action-potential && git checkout -b feature/dev-workflow-commands && openspec new change dev-workflow-commands`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/27273989-e1a1-49e6-8288-f3e637f6aa1e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 10
- session: `2940ff84-b7c8-495c-993c-c44be119b969`
- timestamp: 2026-05-01T19:45:50.556Z
- command: `git checkout -b feature/add-system-state-coordination`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/2940ff84-b7c8-495c-993c-c44be119b969.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 11
- session: `2b8f5011-0432-47bb-9041-e6b363bf099c`
- timestamp: 2026-05-12T19:34:08.193Z
- command: `git checkout -b content/2026-05-13 main && git add infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/heptabase/article/2026-05-12.md inbox/captured/heptabase/threads/2026-05-12.md && git commit -m "content: overnight cron writes (heptabase 2026-05-12 + observations)" && git checkout main && git merge --squash content/2026-05-13 && git commit -m "content: 2026-05-13 daily snapshot" && git branch -D content/2026-05-13 && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/2b8f5011-0432-47bb-9041-e6b363bf099c.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 12
- session: `336a1ede-d7c0-4b70-9958-f724ac658c8c`
- timestamp: 2026-05-02T10:23:01.570Z
- command: `git checkout -b feature/add-reports-publishing 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/336a1ede-d7c0-4b70-9958-f724ac658c8c.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 13
- session: `336a1ede-d7c0-4b70-9958-f724ac658c8c`
- timestamp: 2026-05-02T10:27:06.620Z
- command: `git branch -D feature/add-reports-publishing && git checkout -b feature/add-reports-publishing && git status`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/336a1ede-d7c0-4b70-9958-f724ac658c8c.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 14
- session: `37afc943-2234-408d-9263-f9918fd7242d`
- timestamp: 2026-05-08T03:30:57.684Z
- command: `git checkout main && git checkout -b feature/add-project-worktree-flow main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/37afc943-2234-408d-9263-f9918fd7242d.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 15
- session: `396d9e6f-6483-4264-a10a-6d0df4a0d648`
- timestamp: 2026-04-28T20:57:43.967Z
- command: `git checkout -b project/yoga-cs-agent main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/396d9e6f-6483-4264-a10a-6d0df4a0d648.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 16
- session: `3d51fd37-3859-4727-b594-1bdac3bb5843`
- timestamp: 2026-05-07T02:18:21.629Z
- command: `git checkout -b feature/add-project-update-milestone-hint main && git rev-parse --abbrev-ref HEAD && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/3d51fd37-3859-4727-b594-1bdac3bb5843.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 17
- session: `409f999f-a95a-4f23-acfe-a3da247899b8`
- timestamp: 2026-05-01T02:00:04.644Z
- command: `git checkout -b feature/add-threads-polish-skill main 2>&1 && echo "---" && git status --short && echo "---" && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/409f999f-a95a-4f23-acfe-a3da247899b8.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 18
- session: `409f999f-a95a-4f23-acfe-a3da247899b8`
- timestamp: 2026-05-01T02:07:57.501Z
- command: `git checkout -b content/2026-05-01 && git add inbox/ideas.md && git commit -m "ideas: add observer Date validation extension to work_logs/surveys" && echo "---" && git log -1 --oneline && echo "---" && git branch --show-current`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/409f999f-a95a-4f23-acfe-a3da247899b8.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 19
- session: `41615cbf-c16c-41cf-8d17-786918e68594`
- timestamp: 2026-05-09T23:34:35.775Z
- command: `git checkout -b feature/ctx-onboard-inbox-reconciliation main && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/41615cbf-c16c-41cf-8d17-786918e68594.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 20
- session: `4503f597-9870-4fdf-90be-fae47703174f`
- timestamp: 2026-05-10T00:25:20.385Z
- command: `git checkout -b feature/tune-cc-hooks-capture main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4503f597-9870-4fdf-90be-fae47703174f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 21
- session: `4580de44-8110-4874-91c8-8f437ba0c43a`
- timestamp: 2026-05-12T01:33:43.692Z
- command: `git checkout -b content/2026-05-12 main 2>&1 && echo "---" && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4580de44-8110-4874-91c8-8f437ba0c43a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 22
- session: `4b2817b6-66eb-42ec-b91d-ff6c0fae28ee`
- timestamp: 2026-04-26T01:59:06.816Z
- command: `git checkout -b content/2026-04-26`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4b2817b6-66eb-42ec-b91d-ff6c0fae28ee.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 23
- session: `4c22d469-0827-46bf-96f8-960944989a15`
- timestamp: 2026-05-06T02:29:45.254Z
- command: `git checkout -b content/2026-05-06 main && git add memory/OBSERVATIONS.md infra/state/system_state.json inbox/captured/2026-05-05_state_audit.md && git commit -m "content: 2026-05-06 daily snapshot (overnight cron)"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4c22d469-0827-46bf-96f8-960944989a15.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 24
- session: `4c22d469-0827-46bf-96f8-960944989a15`
- timestamp: 2026-05-06T02:34:20.240Z
- command: `git checkout -b feature/onboard-command main && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4c22d469-0827-46bf-96f8-960944989a15.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 25
- session: `4c64fee0-6241-4dec-9fbd-8f5bce74b70c`
- timestamp: 2026-05-11T02:02:43.186Z
- command: `git checkout -b content/2026-05-11 main && git add contexts/work_logs/2026-05-10_qheart-ap_update2.md && git commit -m "logs: add work log for qheart-ap update (2026-05-10)" && git checkout main && echo "---" && git log --oneline -3 content/2026-05-11`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4c64fee0-6241-4dec-9fbd-8f5bce74b70c.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 26
- session: `4d322105-5cef-4686-b7e5-fd8bfc3a77fb`
- timestamp: 2026-05-18T07:21:49.866Z
- command: `git checkout -b project/career-growth-3y main && \
git branch --show-current && \
mkdir -p projects/career-growth-3y/context && \
git mv contexts/survey_sessions/2026-05-17_career-strategy-3y-300m-survey.html projects/career-growth-3y/context/ && \
git mv contexts/survey_sessions/2026-05-17_career-strategy-3y-300m-survey.md projects/career-growth-3y/context/ && \
echo "---" && \
git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4d322105-5cef-4686-b7e5-fd8bfc3a77fb.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 27
- session: `4eee95f6-5635-421f-ae37-85a325b1200b`
- timestamp: 2026-05-10T08:31:28.687Z
- command: `git checkout -b feature/route-project-update-to-project-branch main && \
echo "---" && git branch --show-current && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4eee95f6-5635-421f-ae37-85a325b1200b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 28
- session: `540cbbb7-94ff-499c-a145-f57afcf1417e`
- timestamp: 2026-05-09T12:08:05.373Z
- command: `git checkout -b content/2026-05-09 main && git add memory/OBSERVATIONS.md && git commit -m "mem: update observations - 2026-05-09 cc-hooks-capture architecture pivot + meta findings"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/540cbbb7-94ff-499c-a145-f57afcf1417e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 29
- session: `540cbbb7-94ff-499c-a145-f57afcf1417e`
- timestamp: 2026-05-09T13:36:08.724Z
- command: `git checkout -b feature/fix-stale-running-role main && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/540cbbb7-94ff-499c-a145-f57afcf1417e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 30
- session: `540cbbb7-94ff-499c-a145-f57afcf1417e`
- timestamp: 2026-05-09T13:59:26.448Z
- command: `git checkout main && git checkout -b content/2026-05-09 main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/540cbbb7-94ff-499c-a145-f57afcf1417e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 31
- session: `5437c7dc-a78d-4fd8-a0bf-5ee2d761bcc4`
- timestamp: 2026-04-26T08:05:36.450Z
- command: `git checkout main && git checkout -b project/gcp-ace-cert`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/5437c7dc-a78d-4fd8-a0bf-5ee2d761bcc4.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 32
- session: `6804494e-9426-4b24-aa49-88ad4ca3df59`
- timestamp: 2026-04-28T02:30:51.866Z
- command: `git checkout main && git checkout -b content/2026-04-28`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/6804494e-9426-4b24-aa49-88ad4ca3df59.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 33
- session: `6c7d9604-2eb7-4687-892a-216bf1dadd17`
- timestamp: 2026-05-04T01:41:37.263Z
- command: `git checkout main && git checkout -b content/2026-05-04 && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/6c7d9604-2eb7-4687-892a-216bf1dadd17.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 34
- session: `6c7d9604-2eb7-4687-892a-216bf1dadd17`
- timestamp: 2026-05-04T01:41:45.621Z
- command: `git stash push -u -m "ctx-eod-route-to-today" && git checkout main && git checkout -b content/2026-05-04 && git stash pop && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/6c7d9604-2eb7-4687-892a-216bf1dadd17.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 35
- session: `6c7d9604-2eb7-4687-892a-216bf1dadd17`
- timestamp: 2026-05-04T01:44:48.633Z
- command: `git branch -D content/2026-05-03 && git checkout -b content/2026-05-04 && git stash pop && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/6c7d9604-2eb7-4687-892a-216bf1dadd17.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 36
- session: `6c7d9604-2eb7-4687-892a-216bf1dadd17`
- timestamp: 2026-05-04T09:29:15.333Z
- command: `git checkout -b feature/add-conversation-capture && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/6c7d9604-2eb7-4687-892a-216bf1dadd17.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 37
- session: `74522efc-bf53-4057-9daf-5241dc71c055`
- timestamp: 2026-04-21T11:56:19.413Z
- command: `git checkout -b work/2026-04-21-wwpf-screening origin/work/2026-04-21-wwpf-screening`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/74522efc-bf53-4057-9daf-5241dc71c055.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 38
- session: `74522efc-bf53-4057-9daf-5241dc71c055`
- timestamp: 2026-04-21T11:57:26.077Z
- command: `git stash && git checkout -b work/2026-04-21-wwpf-screening origin/work/2026-04-21-wwpf-screening`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/74522efc-bf53-4057-9daf-5241dc71c055.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 39
- session: `7d9243d3-c141-46b8-b8d0-ae49a1a71b6a`
- timestamp: 2026-05-01T08:36:27.911Z
- command: `git checkout -b feature/fix-feature-branch-arch-routing && git status`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/7d9243d3-c141-46b8-b8d0-ae49a1a71b6a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 40
- session: `80c8fb96-03c0-4db9-969f-3ffb07fd023b`
- timestamp: 2026-05-06T08:43:28.605Z
- command: `git checkout main 2>&1 | tail -3 && git checkout -b feature/heptabase-ingest-pipeline 2>&1 | tail -3 && git stash pop 2>&1 | tail -10 && echo "---status---" && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/80c8fb96-03c0-4db9-969f-3ffb07fd023b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 41
- session: `84023922-ed19-40c8-bbc2-a8c6a5e3444b`
- timestamp: 2026-05-04T17:36:16.044Z
- command: `today=$(date +%Y-%m-%d)
echo "today: $today"
if git rev-parse --verify content/$today >/dev/null 2>&1; then
  echo "content/$today exists, checking out"
  git checkout content/$today
else
  echo "content/$today does not exist, creating from main"
  git checkout -b content/$today main
fi
echo "---"
git branch --show-current`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/84023922-ed19-40c8-bbc2-a8c6a5e3444b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 42
- session: `84023922-ed19-40c8-bbc2-a8c6a5e3444b`
- timestamp: 2026-05-04T17:39:29.102Z
- command: `git checkout main && git branch -D content/2026-05-05 && git checkout -b content/2026-05-05 main && echo "---" && echo "new content/2026-05-05 head:" && git rev-parse HEAD && echo "main head:" && git rev-parse main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/84023922-ed19-40c8-bbc2-a8c6a5e3444b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 43
- session: `84023922-ed19-40c8-bbc2-a8c6a5e3444b`
- timestamp: 2026-05-04T17:56:09.054Z
- command: `git status --short && echo "---" && git checkout -b feature/fix-eod-step-ordering main && echo "---" && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/84023922-ed19-40c8-bbc2-a8c6a5e3444b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 44
- session: `85a4f091-1f5e-4580-805f-925e5c13d3db`
- timestamp: 2026-05-14T11:39:29.535Z
- command: `git checkout -b content/2026-05-14 main && git status --short && echo "---" && git push origin main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/85a4f091-1f5e-4580-805f-925e5c13d3db.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 45
- session: `85a4f091-1f5e-4580-805f-925e5c13d3db`
- timestamp: 2026-05-14T11:39:39.157Z
- command: `git checkout -b content/2026-05-14 main && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/85a4f091-1f5e-4580-805f-925e5c13d3db.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 46
- session: `86476cce-b66b-4ed2-9a78-160ecb48f88f`
- timestamp: 2026-05-13T18:05:41.651Z
- command: `git checkout -b content/2026-05-14 main && git add infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/heptabase/threads/2026-05-13.md && git commit -m "content: nightly observer + heptabase capture 2026-05-14" && git log --oneline -3`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/86476cce-b66b-4ed2-9a78-160ecb48f88f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 47
- session: `8bcffd6a-6113-4fb2-b4eb-2719d9819537`
- timestamp: 2026-05-13T21:28:58.396Z
- command: `git branch project/exocortex-gtm main && echo "BRANCH_CREATED"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/8bcffd6a-6113-4fb2-b4eb-2719d9819537.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 48
- session: `8f53653a-2ddd-4024-a515-711c232b65fb`
- timestamp: 2026-05-03T02:14:55.900Z
- command: `git checkout -b content/2026-05-03 main && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/8f53653a-2ddd-4024-a515-711c232b65fb.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 49
- session: `9677ec10-891b-4df7-b50d-5a07ef0524d8`
- timestamp: 2026-05-01T11:16:43.574Z
- command: `current=$(git branch --show-current); today=$(date +%Y-%m-%d); echo "current=$current today=$today"; if [ "$current" != "content/$today" ]; then if git rev-parse --verify content/$today >/dev/null 2>&1; then git checkout content/$today; else git checkout -b content/$today main; fi; fi; git branch --show-current`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/9677ec10-891b-4df7-b50d-5a07ef0524d8.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 50
- session: `9d0520b6-0641-4571-9272-4f74085cc65d`
- timestamp: 2026-04-28T06:36:35.051Z
- command: `git checkout main && git branch -D feature/axioms-a05-t07-t10 && git checkout -b feature/axioms-a05-t07-t10 && git cherry-pick d87550d`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/9d0520b6-0641-4571-9272-4f74085cc65d.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 51
- session: `a31b1914-ad6c-49e6-8762-7d29b89d44bd`
- timestamp: 2026-04-22T04:11:06.213Z
- command: `git checkout -b content/2026-04-22 && git add contexts/survey_sessions/2026-04-22_ai-customer-service-vendors-survey.md contexts/survey_sessions/evolver-insight.html contexts/survey_sessions/evolver-insight.md && git commit -m "docs: add AI 客服 vendors survey，移除 evolver-insight 重複稿"`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/a31b1914-ad6c-49e6-8762-7d29b89d44bd.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 52
- session: `a4efdf52-c56f-4352-960e-5224e2de9eaa`
- timestamp: 2026-05-01T21:22:42.891Z
- command: `git checkout -b feature/changelog-0.10-0.11`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/a4efdf52-c56f-4352-960e-5224e2de9eaa.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 53
- session: `ac059835-169d-43b3-9e2c-930891b6985f`
- timestamp: 2026-05-08T05:17:50.499Z
- command: `git branch project/wwpf-qd main && echo "BRANCH_CREATED" && git worktree add ~/Documents/Projects/Exocortex-worktrees/wwpf-qd project/wwpf-qd 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ac059835-169d-43b3-9e2c-930891b6985f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 54
- session: `b080c6f1-ba98-457a-a47d-9764d639cead`
- timestamp: 2026-05-13T18:05:41.651Z
- command: `git checkout -b content/2026-05-14 main && git add infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/heptabase/threads/2026-05-13.md && git commit -m "content: nightly observer + heptabase capture 2026-05-14" && git log --oneline -3`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b080c6f1-ba98-457a-a47d-9764d639cead.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 55
- session: `b080c6f1-ba98-457a-a47d-9764d639cead`
- timestamp: 2026-05-13T18:56:51.497Z
- command: `git checkout main && git checkout -b feature/add-personal-skills-layer main && git cherry-pick c055429 && git log --oneline -3`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b080c6f1-ba98-457a-a47d-9764d639cead.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 56
- session: `b080c6f1-ba98-457a-a47d-9764d639cead`
- timestamp: 2026-05-13T21:25:45.577Z
- command: `ssh macbook 'cd ~/Documents/Procjects/Exocortex-personal && git checkout -b feature/add-personal-skills-layer origin/feature/add-personal-skills-layer 2>&1 | tail -5 && git log --oneline -3'`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b080c6f1-ba98-457a-a47d-9764d639cead.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 57
- session: `b080c6f1-ba98-457a-a47d-9764d639cead`
- timestamp: 2026-05-13T21:51:36.459Z
- command: `git checkout -b feature/migrate-skills-to-personal main && git merge --ff-only worktree-migrate-skills && git worktree remove .claude/worktrees/migrate-skills && git branch -d worktree-migrate-skills && git log --oneline -3`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b080c6f1-ba98-457a-a47d-9764d639cead.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 58
- session: `b6b7ca85-4b96-414c-9a3d-293f85c35e8b`
- timestamp: 2026-05-13T11:39:13.881Z
- command: `cd ~/Documents/Projects/Exocortex-personal && git checkout -b content/2026-05-13 main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b6b7ca85-4b96-414c-9a3d-293f85c35e8b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 59
- session: `b7df301e-9d33-45c8-9f5d-df36b6fc2b39`
- timestamp: 2026-04-23T20:41:26.552Z
- command: `git checkout -b content/2026-04-24`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b7df301e-9d33-45c8-9f5d-df36b6fc2b39.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 60
- session: `b818b1c8-09e0-4c5b-a577-b00d0cb3f277`
- timestamp: 2026-04-29T20:01:13.695Z
- command: `git checkout main && git branch --list "project/agent-security-hacker" && echo "---" && git checkout -b project/agent-security-hacker && git branch --show-current && echo "---" && mkdir -p projects/agent-security-hacker/context && ls projects/agent-security-hacker/`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b818b1c8-09e0-4c5b-a577-b00d0cb3f277.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 61
- session: `b818b1c8-09e0-4c5b-a577-b00d0cb3f277`
- timestamp: 2026-04-29T21:52:20.944Z
- command: `git checkout main && git checkout -b feature/evomap-gene-capsule-alignment && echo "---POPPING---" && git stash pop stash@{0} && echo "---STATUS---" && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b818b1c8-09e0-4c5b-a577-b00d0cb3f277.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 62
- session: `ba23d339-ffa4-4b90-bfbf-50bc559eddfe`
- timestamp: 2026-05-06T20:25:00.702Z
- command: `git checkout -b content/2026-05-07 main && git add memory/OBSERVATIONS.md infra/state/system_state.json inbox/captured/2026-05-06_state_audit.md && git commit -m "mem: overnight observations + 2026-05-06 audit snapshot"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ba23d339-ffa4-4b90-bfbf-50bc559eddfe.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 63
- session: `ba23d339-ffa4-4b90-bfbf-50bc559eddfe`
- timestamp: 2026-05-06T21:08:39.096Z
- command: `git checkout main && git checkout -b feature/add-role-failure-watch main && echo "---status---" && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ba23d339-ffa4-4b90-bfbf-50bc559eddfe.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 64
- session: `bcc4de2a-a541-433e-802c-a5b12bb7c33d`
- timestamp: 2026-05-15T05:12:59.688Z
- command: `git branch project/resume-refresh main && git worktree add .claude/worktrees/resume-refresh project/resume-refresh 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/bcc4de2a-a541-433e-802c-a5b12bb7c33d.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 65
- session: `bcc4de2a-a541-433e-802c-a5b12bb7c33d`
- timestamp: 2026-05-15T08:04:14.677Z
- command: `git branch project/freelance-job-hunt-2026q2 main && git worktree add ../freelance-job-hunt-2026q2 project/freelance-job-hunt-2026q2 2>&1 | tail -3 && cd ../freelance-job-hunt-2026q2 && pwd && mkdir -p projects/freelance-job-hunt-2026q2/context`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/bcc4de2a-a541-433e-802c-a5b12bb7c33d.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 66
- session: `beae7e34-d1e7-4708-8583-0ca13a0630c1`
- timestamp: 2026-05-09T10:13:59.510Z
- command: `git checkout -b feature/add-cc-hooks-capture main && git status --short && echo "---" && ls openspec/changes/add-cc-hooks-capture/`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/beae7e34-d1e7-4708-8583-0ca13a0630c1.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 67
- session: `bf9a3c59-f42c-4e8d-bb96-a5faf84915e4`
- timestamp: 2026-05-11T08:46:28.690Z
- command: `git checkout -b content/2026-05-11 main && git add contexts/work_logs/2026-05-11_qt-ai-enablement_qes-114-multi-app-foundation-task1-to-5.md && git commit -m "logs: add work log for QES-114 multi-app foundation task1-5" && git checkout main && git log -1 content/2026-05-11 --oneline`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/bf9a3c59-f42c-4e8d-bb96-a5faf84915e4.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 68
- session: `bf9a3c59-f42c-4e8d-bb96-a5faf84915e4`
- timestamp: 2026-05-11T09:49:22.017Z
- command: `git checkout -b feature/add-inbox-digest-pipeline main && git branch --show-current && echo "---" && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/bf9a3c59-f42c-4e8d-bb96-a5faf84915e4.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 69
- session: `c5f9f6eb-e42a-4d28-ab00-0a880b88fb72`
- timestamp: 2026-05-04T19:07:45.959Z
- command: `git checkout -b feature/guard-arch-feature-branch-from-main && git status`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/c5f9f6eb-e42a-4d28-ab00-0a880b88fb72.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 70
- session: `c5f9f6eb-e42a-4d28-ab00-0a880b88fb72`
- timestamp: 2026-05-04T19:16:36.638Z
- command: `git commit -m "$(cat <<'EOF'
feat(ctx:arch): add Step 1.5 branch guard before opening feature/* branch

Guard 在 /opsx:propose 完成、git checkout -b feature/<name> 之前介入：
- HEAD detached / 在 feature/* → abort（前者引導 checkout main，後者引導收尾上一個 feature）
- HEAD 在 main 但 behind origin/main → 自動 git pull --ff-only origin main
- HEAD 在 project/<x> 或 content/<date> → 列出 ahead/behind 並詢問是否切 main
純討論流程不會走到此步，guard 不觸發。

新增 capability spec: ctx-arch-command（互斥檢查 / explore+propose 委派 /
branch guard 6 scenarios / Step 2 提示 / 不直接改 rules）。

Refs: 2026-05-02 開 feature/add-reports-publishing 時 HEAD 在
project/yoga-cs-agent，feature 分支落後 main 並繼承 5 個非預期 commits。

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/c5f9f6eb-e42a-4d28-ab00-0a880b88fb72.jsonl`

- [ ] approve — 送 LLM judge
- [x] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 71
- session: `c5f9f6eb-e42a-4d28-ab00-0a880b88fb72`
- timestamp: 2026-05-05T03:37:43.412Z
- command: `git checkout -b feature/fix-state-audit-read-from-main main && git status --short && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/c5f9f6eb-e42a-4d28-ab00-0a880b88fb72.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 72
- session: `c5f9f6eb-e42a-4d28-ab00-0a880b88fb72`
- timestamp: 2026-05-05T05:36:51.206Z
- command: `git checkout -b feature/enforce-explicit-branch-base main && git status --short && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/c5f9f6eb-e42a-4d28-ab00-0a880b88fb72.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 73
- session: `c5f9f6eb-e42a-4d28-ab00-0a880b88fb72`
- timestamp: 2026-05-05T06:05:22.316Z
- command: `git commit -m "$(cat <<'EOF'
feat(branch-flow): enforce explicit branch base via axiom a09 + ctx command sweep

新增 axiom `rules/axioms/a09_explicit_branch_base.md`：「開分支 SHALL 使用
一行式 git checkout -b <name> <base>，base 須顯式寫成 main」。codify
跨 ctx 命令的 fork-point 紀律。

實作要點：
- arch.md (3 處)：raw `git checkout -b feature/<name>` → 加 `main` base，
  並補 axiom cross-reference 註腳
- content.md / experiment.md / project.md (4 處)：兩步式 `git checkout main;
  git checkout -b X` → 一行式（含 `&&` 變體），idiom 一致
- eod.md：已是 gold standard 一行式，不動
- project-branch-flow spec：新增 requirement「開分支 SHALL 顯式指定 base」
  + 6 scenarios（4 種分支 + normalize 規則 + hint message 例外）

defense-in-depth 模型：
- layer A（semantic）：guard-arch 的 Step 1.5 prompt-level 決策樹（HEAD
  detached / nested / non-main 詢問 / pull behind 等 5 個 edge cases）
- layer B（syntactic）：本 change 的一行式顯式 base，保證 fork 點正確

Refs: 2026-05-02 feature/add-reports-publishing 從 project/yoga-cs-agent
開出（5 個非預期 commits）/ 2026-05-05 content/2026-05-05 從 stale main
fork。subsume 關係已逆轉成 complementary（layer A 先 merge）。

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/c5f9f6eb-e42a-4d28-ab00-0a880b88fb72.jsonl`

- [ ] approve — 送 LLM judge
- [x] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 74
- session: `c7aae979-25df-4118-9ea7-d0aabaf7c679`
- timestamp: 2026-05-01T09:01:30.920Z
- command: `git checkout -b feature/spec-migrate-1.2`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/c7aae979-25df-4118-9ea7-d0aabaf7c679.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 75
- session: `d604463a-8314-465b-a22b-62c9a176e60d`
- timestamp: 2026-05-10T04:04:13.733Z
- command: `git checkout -b feature/prune-l0-capture-pipeline main 2>&1 && echo "---" && git status --short && echo "---" && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/d604463a-8314-465b-a22b-62c9a176e60d.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 76
- session: `d8ea5c7c-53e6-47cb-a22f-c8d76fef85af`
- timestamp: 2026-05-15T09:03:14.663Z
- command: `cat > /Users/dj_workstation/Documents/Projects/Exocortex/rules/WORKSPACE.md <<'EOF'
# WORKSPACE.md - 目錄路由速查

目標：讓 AI 每輪 session 都能快速知道"去哪裡找/放什麼"。**找任何檔案前先查這裡。**

> **設計新功能或進行架構變更前**，先讀 `rules/ARCHITECTURE.md`——了解各區塊設計意圖、邊界與資料流，再開始規劃。

## 路由規則

### 專案與程式碼
- 寫程式碼 / 跑指令碼 / 一次性專案：`infra/adhoc_jobs/<project>/`
- 工具指令碼（郵件、語義搜尋等）：`infra/tools/`
- 定時任務：`infra/periodic_jobs/`
- 系統執行狀態（system_state.json + helper）：`infra/state/`

### 知識與記錄
- 通用研究報告：`contexts/survey_sessions/`
- 思考 / 覆盤 / 方法論：`contexts/thought_review/`
- 部落格文章草稿與思考產物：`contexts/blog/`
- 工作紀錄（任務執行過程、進度、產出）：`contexts/work_logs/`
- `contexts/` 子資料夾的觀察設定 → `contexts/MANIFEST.md`
- 系統記憶（observer/reflector 產出）：`memory/`
- 快速捕獲（待辦、閱讀清單、靈感、raw notes）：`inbox/`
- **領域路由索引**（跨系統任務時查詢）：`registry/`
  - `registry/career.md` — 履歷、工作記錄、專案經歷、技術能力的資訊來源
  - `registry/dev.md` — 活躍 repo、開發筆記、issue tracking 的資訊來源
  - `registry/life.md` — 目標、學習計畫、待辦事項的資訊來源
- **專案脈絡**：`projects/`
  - `projects/INDEX.md`：所有專案一覽（被動載入）
  - `projects/<name>/PROJECT.md`：單一專案的目標、現況、下一步、決策、材料地圖——用 `/ctx:project load <name>` 載入
  - `projects/<name>/context/`：深度技術文件（按需，不自動載入）

### 個人 Library（選用）

- **個人珍藏文件索引**（文章、PDF、個人文件）：`registry/library.md` → `library/INDEX.md` → `library/<card>.md`
  - Index cards 在 repo，binary 本體放在你自己的 local 文件目錄（不入 git），AI 透過 card 的 `file_path` 定位
  - 格式規範見 `library/README.md`

### 系統與規則
- **跨 agent 共享行為協定（SSOT）**：`rules/CORE.md` — 所有 agent 每 session 必讀，包含 session 閱讀清單、記憶架構、sub-agent 路由、safety
- 系統 Skills（**作用對象在此 repo 內部**、跨 agent 可複用）：`rules/skills/`
- 核心公理（Axioms）：`rules/axioms/`
- 環境事實（設備、帳號、工具）：`rules/ENVIRONMENT.md`
- 記憶系統：`memory/` + `infra/periodic_jobs/ai_heartbeat/`

### Git Hook

換機後需重裝 pre-commit hook（防止 AGENTS.md / CLAUDE.md 與 CORE.md drift）：

```bash
cp .git-hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

### 分支命名約定

本 repo 工作分支限定三類，各有明確資料範疇與生命週期。任何 skill/command 偵測分支類型時，以 `/` 前綴判定，未知前綴詢問使用者。

| Pattern | 生命週期 | 資料範疇 | 合併策略 |
|---|---|---|---|
| `content/YYYY-MM-DD` | short-lived（一日） | `contexts/`、`memory/`、`inbox/` 等 event-shaped | `--squash`（單一 daily snapshot commit） |
| `project/<name>` | long-lived（專案 create→complete） | `projects/<name>/` state-shaped 變更 | `--no-ff`（保留 milestone DAG，分支續命） |
| `feature/<change-name>` | short-lived（一個 openspec change） | `rules/`、`.claude/`、`openspec/` 等架構層 | `--no-ff`（用 `/ctx:merge`） |

**關鍵原則**：
- `project/<name>` 從專案 `create` 建立到 `complete` 才刪，期間 milestone merge 後分支續命；不自動 rebase 或 merge main（避免 SHA 改寫破壞多機同步）
- `projects/INDEX.md` 中 `status: active|paused` 的專案 ≡ 活躍的 `project/*` 分支（SSOT）
- 混合變更（同時動到 `contexts/` + `projects/<X>/`）由 `/ctx:content` 自動拆兩個 commit 分送
- 細節見 `openspec/specs/project-branch-flow/spec.md`

### 設計工作流
- 架構變更提案、設計文件、任務清單：`openspec/changes/<change-name>/`
- 已歸檔的變更：`openspec/changes/archive/`
- 主規格（已同步的能力 spec）：`openspec/specs/<capability>/spec.md`
  - 注意：`openspec/changes/<name>/specs/` 是草稿，apply 任務之一是同步進 `openspec/specs/`
- 系統演進里程碑記錄：`CHANGELOG.md`（根目錄，以里程碑為單位分組已歸檔的 changes）
- 架構實驗記錄索引：`openspec/experiments/INDEX.md`（每次 `ctx:experiment start/promote/discard` 自動更新）
- **架構發布到 public template**（fork 用）：`ctx:publish` — 若你 fork 此 template 又另開 private 工作 repo，可用此 command 將 archive 過的 changes 發布回你 fork 的 template；發布記錄存於 `openspec/changes/archive/<name>/published.md`

### Claude Commands 位置
- **project-scoped**：`<project-root>/.claude/commands/`（需在該 repo 根目錄）
- **user-scoped**：`~/.claude/commands/`（全局可用，跨所有 repo）
- 兩者不同位置，安裝 OpenSpec 或新增 slash commands 時需確認目標範疇

### Claude Code Hooks 位置
- **Hook scripts**：`.claude/hooks/*.py`（project-scoped、git tracked、跨機透過 git 同步）
- **Hook 註冊**：`.claude/settings.json`（project-scoped）；不要寫 `~/.claude/settings.json`
- **共用 lib**：`.claude/hooks/lib/event_writer.py`——所有 hook 透過這個 lib 寫事件到 `inbox/captured/cc_events/<session_id>/`
- **完整 spec**：`openspec/specs/cc-hooks-capture/spec.md`

### 參考素材（隔離區）
- `_reference/`：非架構、待消化的參考素材，AI 不主動載入。

## Slash Commands 速查表

日常 session 最常用到的 commands，依「工作流意圖」分組。完整定義見 `.claude/commands/ctx|opsx|think/`。

### 工作流：專案 `ctx:project`
| Command | 作用 |
|---|---|
| `/ctx:project new <name>` | 建專案 + `git checkout -b project/<name>` + INDEX.md 登記 |
| `/ctx:project load <name>` | 載入目標/現況/下一步/材料地圖（提到專案名會隱式 load） |
| `/ctx:project update <name>` | Smart-Gather 聚合進度 → 產 work_log |
| `/ctx:project pause <name>` | 狀態改 paused（**分支保留**） |
| `/ctx:project resume <name>` | `git checkout project/<name>` + 狀態改 active |
| `/ctx:project complete <name>` | Retrospective + 最終 `--no-ff` milestone merge + 刪分支 |
| `/ctx:project rename <old> <new>` | 確定性重命名（目錄 + INDEX + frontmatter） |

### 工作流：內容提交 `ctx:content`
| Command | 作用 |
|---|---|
| `/ctx:content` | 偵測變更 → 依「分支類型 × 變更組合」路由矩陣決策 → 混合變更自動拆兩個 commit |
| `/ctx:content merge` | 依當前分支分歧策略：content `--squash`、project 詢問 milestone → `--no-ff` |
| `/ctx:content merge project <X> "<msg>"` | 一行語法 milestone merge（跳過詢問，從任意分支觸發） |

### 工作流：下班總整理 `ctx:eod`
| Command | 作用 |
|---|---|
| `/ctx:eod` | 下班總整理。fetch → 跑 state_audit → 自動處理 bridge-stale / push、詢問 dirty / 舊 content/* / diverged，確保 remote 維持最新、observer 20:00 看得到今日工作。與 18:30 cron silent backstop 共享 `state_audit/core.audit()`。 |

### 工作流：開機總整理 `ctx:onboard`
| Command | 作用 |
|---|---|
| `/ctx:onboard` | 開機 / 早晨 onboarding。fetch → 跑 state_audit → 詢問 dirty 委派 /ctx:content（feature 分支 abort）→ 讀昨夜 audit findings + observer 條目（🔴 axiom watch / 🟡 skill candidate hints）→ active 專案 snapshot → 一頁式 digest 與路由建議。對稱於 /ctx:eod，共用 `state_audit/core.audit()`。 |

### 工作流：架構變更 `ctx:arch` / `opsx:*` / `ctx:merge`
| Command | 作用 |
|---|---|
| `/ctx:arch` | 架構變更工作流入口（討論 → openspec proposal → 開 feature 分支） |
| `/opsx:explore` | Thinking partner 模式（釐清需求） |
| `/opsx:propose <name>` | 產 proposal + design + specs + tasks 一次齊 |
| `/opsx:apply <name>` | 依 tasks.md 逐項實作到目標檔案 |
| `/opsx:archive <name>` | 歸檔到 `openspec/changes/archive/YYYY-MM-DD-<name>/` |
| `/ctx:merge` | 合 `feature/*` 回 main（**只處理 feature**；content/project 會被擋下導向 `/ctx:content merge`） |
| `/ctx:publish` | 將已 archive 的 change 發布到 public template repo（fork 用） |

### 工作流：實驗 / 評估 / 其他
| Command | 作用 |
|---|---|
| `/ctx:experiment start/diff/promote/discard` | 以 git branch 作隔離容器的架構實驗流程 |
| `/think:eval` | 結構化評估「要不要自動化某操作、要怎麼實作」 |

### 三種 merge 策略嚴格分家

| 分支 | 合併指令 | 策略 |
|---|---|---|
| `content/YYYY-MM-DD` | `/ctx:content merge` | `--squash`，分支刪除 |
| `project/<name>` | `/ctx:content merge project <X> "..."` | `--no-ff` + milestone message，**分支續命** |
| `feature/<change-name>` | `/ctx:merge` | `--no-ff` + 文件審查 + 版號 tag |

誤用會被對應指令的 guard 擋下並導向正確指令。

## 命名規則
- 目錄和檔名：小寫 + 下劃線 (snake_case)
- 臨時一次性專案：`tmp_<name>/`

## Python 環境
- 依賴定義於根目錄 `pyproject.toml`，用 `uv sync --all-groups` 安裝
- 每個 skill 的依賴有獨立 group；新增 skill 依賴時在 `pyproject.toml` 新增 group
- 需要隔離時在 `infra/adhoc_jobs/<project>/.venv/` 建獨立環境

## 快速查詢

<!-- 隨著你的專案增長，在這裡新增活躍專案的快捷路由 -->
<!-- 格式：- `project-name` → `adhoc_jobs/project_name/` (說明) -->
EOF
echo "✓ WORKSPACE.md written ($(wc -l < /Users/dj_workstation/Documents/Projects/Exocortex/rules/WORKSPACE.md) lines)"`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/d8ea5c7c-53e6-47cb-a22f-c8d76fef85af.jsonl`

- [ ] approve — 送 LLM judge
- [x] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 77
- session: `d8ea5c7c-53e6-47cb-a22f-c8d76fef85af`
- timestamp: 2026-05-15T09:07:43.914Z
- command: `cat > /Users/dj_workstation/Documents/Projects/Exocortex/rules/ARCHITECTURE.md <<'EOF'
# ARCHITECTURE.md - 系統架構地圖

記錄各區塊的設計意圖、邊界、關係與資料流。**查閱時機**：設計新功能、架構變更前，或需要了解「為什麼這樣設計」時。

---

## 頂層架構圖

```
Exocortex/
├── rules/          ← L3 全局約束層（靜態，每 session 被動載入）
│   ├── CORE.md         session 協定 SSOT
│   ├── WORKSPACE.md    路由速查
│   ├── ARCHITECTURE.md 架構地圖（本檔）
│   ├── SOUL.md         agent 人格
│   ├── USER.md         使用者檔案
│   ├── ENVIRONMENT.md  環境事實
│   ├── COMMUNICATION.md 溝通規範
│   ├── axioms/         核心公理
│   └── skills/         可複用技術方案（AgentSkills 標準格式）
│
├── memory/         ← 系統記憶（observer/reflector 產出）
│   └── OBSERVATIONS.md append-only 歷史事件流
│
├── contexts/       ← 使用者產出的上下文（L1/L2，主動拉取）
│   ├── blog/           部落格文章草稿與主動思考產物
│   ├── work_logs/      任務執行紀錄
│   ├── survey_sessions/ 研究報告
│   └── thought_review/ 思考覆盤
│
├── library/        ← 個人 library（index cards，AI-agent native；選用）
│   ├── INDEX.md        所有珍藏文件一覽表
│   ├── README.md       card 格式規範與新增流程
│   └── <cards>/        個別 index card（摘要、標籤、file_path）
│                       binary 本體放在使用者自選的 local 文件目錄（不入 git）
│
├── registry/       ← 跨系統路由索引
│   ├── career.md       履歷、工作、技術能力
│   ├── dev.md          活躍 repo、開發筆記
│   ├── life.md         目標、學習、待辦
│   └── library.md      個人 library 路由入口
│
├── projects/       ← 專案脈絡層（progressive disclosure）
│   ├── INDEX.md        所有專案一覽索引（被動載入）
│   └── <name>/
│       ├── PROJECT.md  核心脈絡（目標、現況、下一步、決策、材料地圖）
│       └── context/    按需載入的深度技術文件（technical.md、environment.md 等）
│
├── inbox/          ← 快速捕獲區
│   ├── todos.md        待辦事項
│   ├── reading_list.md 閱讀清單
│   ├── ideas.md        靈感捕獲
│   └── captured/       外部匯入的 raw notes
│
├── openspec/       ← 架構變更設計文件（提案、設計、任務）
│   ├── changes/        進行中的變更
│   ├── specs/          已同步的能力 spec
│   └── experiments/    架構實驗索引
│
├── infra/          ← 基礎設施層
│   ├── tools/          可複用工具指令碼
│   ├── state/          系統執行狀態紀錄（system_state.json + helper）
│   ├── periodic_jobs/  自動化定時任務
│   │   ├── CRONTAB.md   排程設定參考
│   │   ├── state_audit/ 規則性狀態審計（無 LLM）
│   │   └── ai_heartbeat/  observer.py（日）、reflector.py（週）
│   └── adhoc_jobs/     一次性專案與指令碼
│
└── _reference/     ← 隔離區（非架構，AI 不主動載入）
```

---

## 各區塊設計意圖與邊界

### `rules/` — L3 全局約束層

**意圖**：儲存在每個 session 開始時被動載入的固定知識——agent 人格、環境事實、行為協定、路由規則。這層的內容是系統的「靜態配置」，不隨工作進展改變。

**邊界**：只放「跨 session 永遠成立的事實與規則」。不放進行中任務的狀態、一次性記錄、或程式碼。

**CORE.md 的特殊地位**：所有 agent 的 SSOT，定義 session 閱讀順序與跨 agent 共享行為。所有 agent（Claude Code、Cursor 等）應都參照此檔案，不各自維護 session 協定。

### `memory/` — 系統記憶層

**意圖**：儲存 observer/reflector 的產出——append-only 的歷史事件流。`OBSERVATIONS.md` 是事件、觀察、學習的唯一存儲，只增不改。與 `contexts/`（使用者產出）語意清晰分離：`memory/` = 系統產出，`contexts/` = 使用者記錄。

**邊界**：只放 observer/reflector 的輸出。不放使用者產生的記錄，不放規則或配置。

### `contexts/` — 使用者上下文層

**意圖**：儲存使用者產出的可更新紀錄——部落格文章草稿、工作記錄、研究報告、思考覆盤。需要主動查詢時拉取。

**觀察設定 SSOT**：`contexts/MANIFEST.md` 定義各子資料夾的觀察 schema（`observation_mode`、`extraction_focus`），是 observer 掃描設定與新增資料夾設計準則的單一真實來源。

**邊界**：不放規則或全局配置。不放 observer 產出（那是 `memory/`）。不主動載入——需要歷史脈絡時才讀。

### `inbox/` — 快速捕獲區

**意圖**：低門檻的碎片捕獲，先記後整理。`todos.md`（待辦）、`reading_list.md`（閱讀清單）、`ideas.md`（靈感）各有獨立格式與生命週期；`captured/` 暫存外部匯入的 raw notes。

**邊界**：暫存區，不是最終存儲。消化後分流至 `contexts/`、`projects/`、`openspec/` 等。

### `projects/` — 專案脈絡層

**意圖**：以 progressive disclosure 組織各個進行中專案的知識，讓 AI 在任意 session 中能快速回到工作狀態。採用三層結構：
- `INDEX.md`（被動載入）：所有專案的一行摘要
- `PROJECT.md`（`/ctx:project load` 時載入）：目標、現況、下一步、關鍵決策、材料地圖
- `context/`（AI 按需自行拉取）：技術細節、環境設定等深度文件

**生命週期狀態**：專案 status 有四個合法值，形成單向狀態機：
```
active ──→ paused ──→ active (resume)
  │
  └──→ completed ──→ archived
```
- `active`：進行中，observer staleness check 生效（超過 14 天未更新觸發 🟡 提醒）
- `paused`：暫停中，不觸發 staleness check；load/update 時提醒重新啟動
- `completed`：已完成，frontmatter 含 `completed_date`，不觸發 staleness check
- `archived`：歸檔，不出現在日常操作建議中

**work_log 橋樑設計**：`/ctx:project update` 和 `/ctx:project complete` 產出 work_log 到 `contexts/work_logs/`（分別命名為 `_update.md` 和 `_retrospective.md`），讓 observer 透過既有 work_logs 通道觀察到專案更新中的經驗，而不需要 observer 直接掃描 `projects/` 目錄。

**邊界**：PROJECT.md 是「地圖」，不是「搬家」——材料（work_logs、surveys、code）留在原位，PROJECT.md 只放路徑指針。`context/` 下可能含敏感資訊（帳號、endpoints），設計上不自動載入。

### `library/` — 個人 Library 層（選用）

**意圖**：AI-agent native 的個人文件索引。只在 repo 中存放 markdown index cards（摘要、標籤、原始路徑），binary 本體（PDF、影片等）由使用者放在自選的 local 文件目錄，不進入 git。AI 透過 card 的 `file_path` 欄位定位到本地檔案，查找成本只多一步（讀 card → 得到路徑）。路由入口：`registry/library.md`。

**邊界**：只放 index cards（純文字 markdown）。binary 不進 git，由使用者自行管理備份。observer 暫不掃描 library/（不在 contexts/ 下，不受 MANIFEST.md 管轄）。

### `registry/` — 跨系統路由索引

**意圖**：跨系統任務（履歷更新、開發、生活規劃）的資訊入口，指向各外部系統中的 SSOT。Agent 在執行跨系統任務前先查 registry，找到正確的資訊來源。

**邊界**：只放「去哪裡找什麼」的指針，不放內容本身。

### `infra/` — 基礎設施層

**意圖**：將「讓系統運作的程式碼」收納在一個命名空間下，不搶認知層注意力。四個子目錄各有職責：
- `state/`：系統執行狀態紀錄。`system_state.json`（git-tracked）為各 periodic role（observer / reflector / state_audit / capture / triage_*）的全域 high-water mark cache，consumer（如 opsx:archive）讀取「上次成功跑到哪」做協調決策。`lib.py` 提供 `read_system_state()` / `update_role_state()` / `write_run_log()` 三個共用 helper，皆採用 atomic write。互補的 audit log 落在 `raw_signals/<date>/<role>_run.json`（不進 git）。
- `periodic_jobs/`：自動化定時任務，依職責拆成平行子角色。排程設定參考見 `infra/periodic_jobs/CRONTAB.md`。
  - `ai_heartbeat/`：observer.py 每日執行產生觀察，reflector.py 每週合成反思。輸出流向 `memory/`。**依賴 LLM API**（如 Anthropic API）。屬 **Behavior Pipeline**（觀察使用者做了什麼）。
  - `state_audit/`：純規則性的儲存庫狀態審計角色。`core.audit()` 跑八項檢查（dirty / unmerged content/* / bridge-stale / unpushed-or-untracked-remote / branch-behind-origin / missed-observer-or-reflector-run / role-failed-run / stale-running-role），cron.py 每日 18:30 silent backstop 寫 `inbox/captured/<date>_state_audit.md` + `raw_signals/<date>/state_audit.json`。**無 LLM、無 API 依賴**——只用 Python 標準庫 + git CLI。與 `/ctx:eod`、`/ctx:onboard` 命令共享 `core.audit()`。`role-failed-run` 為通用檢查：scan `system_state.json` 中所有 `roles.*.last_status == "failed"`，已知角色走 `ROLE_RECOVERY_HINTS` 給 bespoke 修法、未知角色 fallback 到 generic hint，新增 periodic role 自動納入監控。
- `tools/`：可複用工具指令碼
- `adhoc_jobs/`：一次性專案與指令碼

**邊界**：只放「讓系統運作的程式碼」。手動研究或任務紀錄放 `contexts/`。認知產物（規則、記憶、脈絡）不放此處。`infra/state/` 是元件協調用的 metadata，不是 observation 或記憶（因此不放 `memory/`）。

### Hooks 設計原則 — Cross-worktree 可用性

`.claude/hooks/` 與 `.claude/settings.json` 屬 **infra-shaped** 元件：必須在主 worktree 與任何 `.claude/worktrees/<name>/` 下開的 session 都正確執行，不論該 worktree 的 branch 是否 check in 這些檔案。

**核心規則**：`.claude/settings.json` 內所有 `hooks.<event>[].hooks[].command` 字串 **必須使用 `$CLAUDE_PROJECT_DIR/.claude/hooks/<script>` 絕對路徑前綴**。禁止相對路徑（如 `.claude/hooks/<script>`）或硬編碼絕對路徑。

**為什麼**：Claude Code 解析 hook command 的相對路徑時以 session cwd 為基準。當 session 跑在 `.claude/worktrees/<name>/` 且該 worktree 的 branch 未 check in `.claude/hooks/`（典型情境：long-lived `project/*` branch，依設計不自動同步 main），相對路徑會失敗，capture hook 全部 missing，capture pipeline 對該 worktree 完全失能。`$CLAUDE_PROJECT_DIR` 是 Claude Code 注入到 hook context 的 env var，永遠指向主 repo root。

**內外對稱**：本原則與 `event_writer` 從 cwd 解析回主 repo root 的內部邏輯互為對稱——shell 層由 `$CLAUDE_PROJECT_DIR` 進到主 repo 的 hook 腳本，Python 層由 `event_writer` 從當前 cwd 解析回主 repo root。任何只改一邊的「修法」都會留下隱性 bug。

**Review 機械檢查**：`grep -E '"command"\s*:\s*"\.claude/' .claude/settings.json` 應為空輸出。

### `rules/skills/` — 系統 Skills

**意圖**：儲存跨 agent 可攜的可複用能力知識——工作流、最佳實踐、API 指南。採用 [AgentSkills 開放標準](https://agentskills.dev) 格式，使任何支援標準的 agent（Claude Code、Cursor、Gemini CLI、OpenCode 等）都能直接發現與載入，無需額外轉換。

**結構**：每個 skill 以子目錄形式存在，目錄名為 kebab-case，目錄內必須包含 `SKILL.md`：

```
rules/skills/
├── INDEX.md              ← 能力速查 manifest（session 啟動時被動載入）
└── <skill-name>/
    ├── SKILL.md          ← 主體（AgentSkills frontmatter + 完整指令）
    ├── references/       ← 延伸資源（按需載入）
    └── scripts/          ← 輔助腳本（按需載入）
```

**`SKILL.md` frontmatter 必填欄位**：`name`、`description`。這兩個欄位也會反映在 `INDEX.md` 表格中。

**邊界**：只放「可複用、跨任務、跨 agent 均有效」的能力。一次性工作流或 agent-specific 指令放 `.claude/skills/`（或對應 agent 的 skills 目錄），不放此處。Axioms（決策原則）維持在 `rules/axioms/`，不混入。

### `openspec/` — 架構變更工作流

**意圖**：記錄架構變更的設計過程（提案、設計決策、任務清單）。`changes/` 是進行中的變更，`specs/` 是已同步到系統的能力規格，`experiments/` 是架構探索性實驗記錄（`ctx:experiment` 工作流產出）。

**邊界**：只在 ctx:arch 工作流中產生和修改。不直接在此執行實作——實作在對應的目標檔案（`rules/`、`.claude/` 等）中進行。

### `_reference/` — 隔離區

**意圖**：存放非架構性的參考素材，AI 不主動載入。包含待消化的工具腳本與外部文件，僅供人工查閱或手動遷移。

---

## 區塊間關係

```
CORE.md (rules/)
  └─ 定義 session 閱讀順序 ──→ SOUL, USER, ENVIRONMENT, WORKSPACE, COMMUNICATION

WORKSPACE.md (rules/)
  └─ 路由速查 ──→ memory/, contexts/, registry/, projects/, inbox/, openspec/, infra/

registry/ ──→ 外部系統（issue trackers、文件平台等）

infra/periodic_jobs/ai_heartbeat/
  ├─ observer.py ──→ memory/OBSERVATIONS.md
  └─ reflector.py ──→ memory/OBSERVATIONS.md

openspec/changes/<name>/
  └─ opsx:apply 實作後 ──→ rules/, .claude/commands/, 其他目標檔案

infra/adhoc_jobs/<project>/
  └─ 產出物 ──→ contexts/work_logs/ 或 contexts/survey_sessions/

inbox/
  └─ 消化後分流 ──→ contexts/, projects/, openspec/changes/
```

---

## Skills 系統設計

### 三層架構

Skills 分三層，由外到內依序疊加：

| 層級 | 位置 | 作用域 | 維護者 |
|------|------|--------|--------|
| **系統 skills** | `rules/skills/` | 此 repo，跨 agent | Repo（人工 + Reflector 晉升） |
| **Agent 專案 skills** | `.claude/skills/`（repo 根目錄） | 此 repo，此 agent | 專案層設定 |
| **Agent 全域 skills** | `~/.claude/skills/` | 所有 repo，此 agent | 使用者全域設定 |

Agent 在 session 中應將三層合併視為完整能力圖：**系統 skills + agent 專案 skills + agent 全域 skills = 本次 session 可用能力全集**。

三層各有職責：系統 skills 追求跨 agent 可攜性；agent 專案 skills 承載此 repo 的特定工作流（如 opsx:*、ctx:*、think:*）；agent 全域 skills 承載跨 repo 通用的 agent 能力。

### 命名空間語意

`.claude/commands/` 下的 agent 專案 commands 以命名空間組織，各有清楚的語意邊界：

| 命名空間 | 定位 | 典型工具 |
|---------|------|---------|
| `ctx:` | 架構開發工具：專案脈絡、內容提交、git 工作流、架構實驗、發布 | `ctx:project`、`ctx:content`、`ctx:arch`、`ctx:merge`、`ctx:experiment`、`ctx:publish` |
| `opsx:` | OpenSpec 設計流程工具：探索、提案、實作、歸檔 | `opsx:explore`、`opsx:propose`、`opsx:apply`、`opsx:archive` |
| `think:` | 日常使用框架時的思考輔助工具：評估、判斷、覆盤 | `think:eval` |
| （無命名空間） | 跨 repo 通用工具，適合放 `~/.claude/commands/` | — |

**歸屬判斷**：新增 command 時，依據「這個工具在什麼情境下使用？」判斷命名空間。若不確定，可用 `/think:eval` 評估。

**完整日常操作速查表**：見 `rules/WORKSPACE.md` 的「Slash Commands 速查表」一節，依工作流意圖分組列出所有 commands、三種 merge 策略的分家規則。

### AgentSkills 標準格式

`SKILL.md` 使用 YAML frontmatter 宣告 metadata：

```markdown
---
name: skill-name
description: 一行描述，說明此 skill 解決什麼問題
# 可選欄位：version, author, tags, trigger_patterns 等
---

# Skill 主體內容
...
```

此格式為開放標準，主流 agent 均原生支援。對不支援的 agent，SKILL.md 仍是可讀的 markdown，降級優雅。

### Progressive Disclosure 載入機制

Agent 讀取 skills 時遵循三層按需展開，避免 context 膨脹：

```
Session 啟動
  → 讀 rules/skills/INDEX.md（metadata only，~100 tokens/skill）
      ↓ 判斷任務需要某個 skill
  → 讀 rules/skills/<name>/SKILL.md（完整指令）
      ↓ 執行時需要延伸資源
  → 讀 references/ 或 scripts/（最按需）
```

**INDEX.md 設計原則**：只列 `name` + `description`，不嵌入完整 SKILL.md 內容。每新增或刪除 skill 必須同步更新 INDEX.md。

### Reflector 晉升流

L2 Reflector 識別出 `memory/OBSERVATIONS.md` 中的高優工作流觀察時，晉升流程：

```
reflector.py 識別高優觀察
  → 在 rules/skills/<name>/ 建立子目錄
  → 寫入符合 AgentSkills 格式的 SKILL.md
  → 更新 rules/skills/INDEX.md 新增條目
  → append 晉升事件到 memory/OBSERVATIONS.md
```

晉升後的 skill 在下一個 session 即可被任何 agent 發現。

---

## 資料流圖

### Session 初始化流

```
Agent 啟動
  → 讀 CORE.md（session 協定）
  → 讀 SOUL.md, USER.md, ENVIRONMENT.md, WORKSPACE.md, COMMUNICATION.md
  → 讀 rules/skills/INDEX.md（系統 skills metadata）
  → 合併 agent 全域 skills（~/.claude/skills/）
  → 合併 agent 專案 skills（.claude/skills/）→ 完整能力圖
  → 依任務類型：讀 registry/<domain>.md
  → 依需求：拉取 memory/OBSERVATIONS.md 或 projects/INDEX.md
```

### 記憶累積流

```
每日 18:30：state_audit/cron.py（純規則，無 LLM）
  → git fetch --all
  → 八項檢查（dirty / unmerged content/today / bridge-stale / unpushed / branch-behind-origin
              / missed-observer-or-reflector / role-failed-run / stale-running-role）
  → 寫 raw_signals/<date>/state_audit.json（永遠寫，給 observer 讀）
  → 寫 inbox/captured/<date>_state_audit.md（findings 非空時）
  → 寫 raw_signals/<date>/state_audit_run.json + 更新 infra/state/system_state.json

即時：CC hooks（SessionStart / UserPromptSubmit / SessionEnd / PostToolUseFailure(Bash) / SubagentStart / SubagentStop）
  → .claude/hooks/*.py 寫 inbox/captured/cc_events/<session_id>/{session.json | <event_type>_<ts>_<uuid>.json}
  → SessionStart 寫單檔 session.json header（cwd / transcript_path / source / model 等 session 級欄位），覆寫式
  → 其餘 event hook 寫 event delta（不重抄 session 級欄位，由 bridge 從 session.json join）
  → Hook 層 stateless write-only，無網路 / 無 LLM；失敗 fallback 到 ~/.claude/logs/hooks_failed/

每日 19:00：ai_heartbeat/v1/capture.py
  → L0 triage source（單一）：cc_events_bridge（讀 inbox/captured/cc_events/ → raw_signals）
     bridge 過濾 metadata-only event_type（session_done / subagent_start），inbox 留檔等 30 天 GC
  → 三級分流 → 寫 raw_signals/<date>/cc_event_<event_type>_<id>.json
  → 各 phase 寫 raw_signals/<date>/<role>_run.json（capture / triage_stage1 / triage_stage2）+ 更新 infra/state/system_state.json

每日 20:00：ai_heartbeat/v1/observe.py
  → 讀 infra/state/system_state.json 做冪等性檢查（fallback 至 grep OBSERVATIONS.md）
  → 讀 raw_signals/<date>/state_audit.json（meta block）
  → 讀 raw_signals/<date>/*.json 中 triage="high" 的 capture signals
  → 讀取 contexts/MANIFEST.md（各子資料夾觀察設定）
  → 分析 contexts/ 近期變更（依 MANIFEST.md 的 observation_mode）
  → 用 system_state.observer.last_finished_at 當 high-water mark 掃 openspec/changes/archive/（fallback 至 -mtime -1）
  → 產生觀察條目（開頭含 [meta] 區塊）
  → append → memory/OBSERVATIONS.md
  → 寫 raw_signals/<date>/observer_run.json + 更新 infra/state/system_state.json

每週：reflector.py
  → 合成近期觀察
  → 產生反思條目
  → append → memory/OBSERVATIONS.md
  → 寫 raw_signals/<date>/reflector_run.json + 更新 infra/state/system_state.json

opsx:archive（producer-aware）
  → 讀 infra/state/system_state.json
  → 若 observer 已跑當天 → 詢問 roll(tomorrow) / stay(today + _late.json)
  → 否則 → today 命名（既有行為）

使用者主動：/ctx:eod
  → git fetch + state_audit.core.audit()（與 cron 共享）
  → 自動處理 bridge-stale + push；詢問 dirty / 舊 content/* / diverged
  → 輸出結尾報告（✅ remote 全部最新 / ⚠️ N 項待處理）

使用者主動：/ctx:onboard
  → git fetch + state_audit.core.audit()（與 /ctx:eod 對稱共享）
  → 詢問 dirty 委派 /ctx:content（feature 分支 abort）
  → 讀 inbox/captured/<yesterday>_state_audit.md
  → 讀 memory/OBSERVATIONS.md 最近條目，分流呈現
      ├─ 🔴 Axiom watch（被動高亮，reflector weekly 蒸餾）
      └─ 🟡 Skill candidate hints（[工作流/*][流程/*][方法論/*] tag 過濾）
  → 讀 projects/INDEX.md + 各 PROJECT.md「下一步」段落
  → 輸出一頁式 digest + 路由建議（不自動 commit / push / 切分支 / 呼叫 LLM）
```

### 架構變更流

```
/ctx:arch
  → /opsx:explore（釐清意圖）
  → /opsx:propose（產出 openspec/changes/<name>/）
  → git checkout -b feature/<name>
  → /opsx:apply（實作到目標檔案）
  → /ctx:merge（合併回 main，確認 ARCHITECTURE.md 是否需更新）
```

### 分支拓樸與內容流

```
content/YYYY-MM-DD ──[--squash]──→ main      (daily snapshot, 分支刪除)
                                      ↑
project/<name> ──[--no-ff milestone]──┘      (分支續命到 complete)
                                      ↑
feature/<change-name> ──[--no-ff]─────┘      (架構變更，分支刪除)
```

- `content/*` 涵蓋 `contexts/`、`memory/`、`inbox/` 等 event-shaped 變更
- `project/*` 涵蓋 `projects/<name>/` state-shaped 變更，long-lived 不自動同步 main
- `feature/*` 涵蓋 `rules/`、`.claude/`、`openspec/` 架構層變更
- 混合變更由 `/ctx:content` 自動拆分；`/ctx:content merge` 處理 content/project，`/ctx:merge` 處理 feature
- **observer 邊界保留**：observer 不掃 `projects/`；專案事件流透過 `/ctx:project update` 產出 `contexts/work_logs/` 條目，隨 `content/*` 進 main 後才被 observer 觀察到（`projects/` 區段詳述）
- 完整 spec：`openspec/specs/project-branch-flow/spec.md`

---

## 擴展點

| 擴展類型 | 放置位置 | 需要更新的文件 |
|---|---|---|
| 新增頂層目錄 | 頂層 | `rules/WORKSPACE.md`（路由）、`rules/ARCHITECTURE.md`（本檔）、`registry/<domain>.md`（若需路由入口） |
| 新增 rules/ 規則文件 | `rules/` | `rules/CORE.md`（若需加入 session 閱讀清單） |
| 新增 registry 域 | `registry/` | `rules/WORKSPACE.md`、`rules/CORE.md` |
| 新增 agent-specific skill/command | `.claude/commands/` 或 `.claude/skills/` | 對應 agent 的 skills 目錄（不需更新系統 skills INDEX） |
| 新增 `think:` 命名空間工具 | `.claude/commands/think/` | `rules/ARCHITECTURE.md`（本檔，說明用途與邊界） |
| 新增自動化腳本 | `infra/periodic_jobs/<role>/` | `infra/periodic_jobs/CRONTAB.md`（時間線總覽 + 核心任務說明 + 示例 crontab）；若新增獨立角色（非掛在既有 ai_heartbeat / state_audit 之下），同步更新 `rules/ARCHITECTURE.md` 的 infra/ 段落與資料流圖。**新角色 SHALL 接入 `infra/state/lib.py`**：執行流程包入三段論（running → ok / failed），每個階段呼叫 `update_role_state()`；完成時呼叫 `write_run_log()`。讓未來的 missed-run 偵測與 cross-role 協調可以直接適用。 |
| 新增 CC hook | `.claude/hooks/<event>.py` + `.claude/settings.json` | Hook script 用 Python stdlib（依賴 `.claude/hooks/lib/event_writer.py`），失敗不阻塞 user input；若事件需被 capture 消化則更新 `cc_events_bridge.py` 的 `_build_content()` 與 spec 的 event_type 列表。Hook 寫入 `inbox/captured/cc_events/<session_id>/`（gitignored），bridge 為 batch consumer。**兩層分離**：Hook 即時 stateless write-only，bridge cron 批次轉 raw_signals。**Schema 兩層**：session 級欄位（cwd / transcript_path / source / model）由 SessionStart hook 寫 `session.json` 單檔，event 檔只記事件特有欄位，bridge 在 join 時 fold 進 raw_signals。**`.claude/settings.json` 引用 hook command 必用 `$CLAUDE_PROJECT_DIR/.claude/hooks/<script>` 絕對路徑前綴，禁止相對路徑**——詳見「Hooks 設計原則 — Cross-worktree 可用性」段落。 |
| 新增系統 skill | `rules/skills/` | `rules/skills/INDEX.md` |
EOF
echo "✓ ARCHITECTURE.md written ($(wc -l < /Users/dj_workstation/Documents/Projects/Exocortex/rules/ARCHITECTURE.md) lines)"`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/d8ea5c7c-53e6-47cb-a22f-c8d76fef85af.jsonl`

- [ ] approve — 送 LLM judge
- [x] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 78
- session: `e443446e-e9d4-4db6-9ffc-b269835f0632`
- timestamp: 2026-05-01T21:45:28.399Z
- command: `git checkout main && git checkout -b project/ghost-blog-optimization && mkdir -p projects/ghost-blog-optimization/context`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/e443446e-e9d4-4db6-9ffc-b269835f0632.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 79
- session: `e443446e-e9d4-4db6-9ffc-b269835f0632`
- timestamp: 2026-05-01T22:12:19.218Z
- command: `cd /Users/dj_workstation/Documents/Projects/ghost-blog-dev/ && git checkout -b feature/fix-ghost-collection-routes && git add frontend/src/app/page.tsx frontend/src/app/insights/page.tsx 'frontend/src/app/post/[slug]/page.tsx' 'frontend/src/app/[slug]/page.tsx' 'frontend/src/app/insights/[slug]/page.tsx' frontend/src/components/PostPage.tsx && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/e443446e-e9d4-4db6-9ffc-b269835f0632.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 80
- session: `e443446e-e9d4-4db6-9ffc-b269835f0632`
- timestamp: 2026-05-01T23:37:39.243Z
- command: `git checkout main && git checkout -b content/2026-05-02 && git stash pop stash@{1} && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/e443446e-e9d4-4db6-9ffc-b269835f0632.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 81
- session: `e5907a06-9edd-46fd-9175-86786c6a573a`
- timestamp: 2026-05-10T06:20:34.011Z
- command: `cd /Users/dj_workstation/Documents/Projects/qt-ap && git stash push -m "WIP: gitignore log rules (QES-112 branch)" -- .gitignore && echo "---stash list---" && git stash list && echo "---fetch main---" && git fetch origin main 2>&1 | tail -5 && echo "---checkout main---" && git checkout main && echo "---branch from main---" && git checkout -b docs/api-v3.1-update && git status -sb`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/e5907a06-9edd-46fd-9175-86786c6a573a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 82
- session: `e7bd35b5-0166-48fc-aaca-4453c72c71e7`
- timestamp: 2026-05-14T17:51:30.303Z
- command: `git checkout -b content/2026-05-15 main && \
git add inbox/ideas.md inbox/todos.md infra/state/system_state.json memory/OBSERVATIONS.md \
        inbox/captured/heptabase/article/2026-05-14.md \
        inbox/captured/heptabase/threads/2026-05-14.md \
        inbox/captured/heptabase/youtube/2026-05-14.md && \
git status --short && echo "---STAGED ABOVE---"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/e7bd35b5-0166-48fc-aaca-4453c72c71e7.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 83
- session: `e7bd35b5-0166-48fc-aaca-4453c72c71e7`
- timestamp: 2026-05-14T18:09:27.584Z
- command: `git checkout -b feature/fix-onboard-step4-existence-check main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/e7bd35b5-0166-48fc-aaca-4453c72c71e7.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 84
- session: `ea92cb20-0b1a-4143-b44e-bfbf56f0ca1c`
- timestamp: 2026-05-08T01:15:21.194Z
- command: `git checkout -b content/2026-05-08 main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ea92cb20-0b1a-4143-b44e-bfbf56f0ca1c.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 85
- session: `eb00185d-305b-4920-97fd-0e39a46293de`
- timestamp: 2026-05-15T04:11:51.924Z
- command: `git checkout -b content/test-pre-guard main && echo "---post-switch---" && source infra/state/session_mode.sh && echo "IS_BG=$IS_BG IN_WORKTREE=$IN_WORKTREE WORKTREE_BRANCH=$WORKTREE_BRANCH" && echo "---triple-check---" && [ "$IS_BG" = "true" ] && [ "$IN_WORKTREE" = "false" ] && [ "$WORKTREE_BRANCH" = "main" ] && echo "ALL_THREE_MET" || echo "AT_LEAST_ONE_MISSING → pre-guard 應 skip" && echo "---pre-guard exists on this branch?---" && grep -c "bg-mode pre-guard" .claude/commands/ctx/project.md`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/eb00185d-305b-4920-97fd-0e39a46293de.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 86
- session: `eeca9fe4-003f-45a0-be77-d620f2949ac8`
- timestamp: 2026-04-24T04:00:56.354Z
- command: `git checkout -b feature/docs-housekeeping-2026-04-24 && git add CHANGELOG.md rules/ARCHITECTURE.md rules/WORKSPACE.md rules/skills/INDEX.md .claude/skills/doc-formatter/SKILL.md rules/skills/doc-formatter/ rules/skills/zh-polish/ && echo "---staged---" && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/eeca9fe4-003f-45a0-be77-d620f2949ac8.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 87
- session: `eeca9fe4-003f-45a0-be77-d620f2949ac8`
- timestamp: 2026-04-24T04:02:54.753Z
- command: `git checkout -b content/2026-04-24 && git add contexts/blog/2026-04-24_claude-code-postmortem-short.md contexts/blog/2026-04-24_claude-code-postmortem.md contexts/thought_review/2026-04-24_zh-polish-skill-eval.md contexts/work_logs/2026-04-24_exocortex-dev_daily-usage-reference.md && git commit -m "content: 2026-04-24 drop — claude-code postmortem、zh-polish eval、daily usage ref" && echo "---return to main---" && git checkout main && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/eeca9fe4-003f-45a0-be77-d620f2949ac8.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 88
- session: `f0bf44b8-f7f3-4e11-a0d8-a246bfa13e7a`
- timestamp: 2026-05-01T11:54:18.672Z
- command: `git checkout -b feature/extend-state-audit-remote-aware && git status --short && git branch --show-current`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f0bf44b8-f7f3-4e11-a0d8-a246bfa13e7a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 89
- session: `f0bf44b8-f7f3-4e11-a0d8-a246bfa13e7a`
- timestamp: 2026-05-01T13:23:38.259Z
- command: `git rev-parse --verify content/2026-05-01 2>/dev/null && git checkout content/2026-05-01 || git checkout -b content/2026-05-01 main; git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f0bf44b8-f7f3-4e11-a0d8-a246bfa13e7a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 90
- session: `f72b06b4-8dfc-4b34-b722-a4157e070662`
- timestamp: 2026-05-14T07:38:02.886Z
- command: `git worktree remove /Users/dj_workstation/Documents/Projects/Exocortex-personal/.claude/worktrees/feature+cross-worktree-hooks-resolution 2>&1 && git branch -d feature/cross-worktree-hooks-resolution 2>&1 && echo '---worktree list---' && git worktree list 2>&1 && echo '---branches---' && git branch 2>&1 | grep -E "^\*|feature/cross-worktree"`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f72b06b4-8dfc-4b34-b722-a4157e070662.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 91
- session: `f787c58f-88ea-4626-934d-5ea39fdf614b`
- timestamp: 2026-05-13T03:03:54.336Z
- command: `git checkout -b content/2026-05-13 main && git add contexts/work_logs/2026-05-13_qheart-ap_offline-build-test-infrastructure.md && git commit -m "logs: qheart-ap offline build/test 基礎建設（QES-114 Task 8 實證）" && echo "---SHA---" && git log --oneline -1 && echo "---SWITCH BACK---" && git checkout main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f787c58f-88ea-4626-934d-5ea39fdf614b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 92
- session: `f787c58f-88ea-4626-934d-5ea39fdf614b`
- timestamp: 2026-05-13T04:42:47.369Z
- command: `echo "=== cleanup stale scaffold from first openspec new ==="
ls openspec/changes/fix-smart-gather-cross-branch/ 2>/dev/null
rm -rf openspec/changes/fix-smart-gather-cross-branch/
git status --short
echo ""
echo "=== create feature branch + cherry-pick artifacts ==="
git checkout -b feature/fix-smart-gather-cross-branch main && \
git cherry-pick worktree-fix-smart-gather-cross-branch && \
echo "---" && git log --oneline -3 && \
echo "---" && git diff --stat HEAD~1 HEAD`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f787c58f-88ea-4626-934d-5ea39fdf614b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 93
- session: `f787c58f-88ea-4626-934d-5ea39fdf614b`
- timestamp: 2026-05-13T06:04:44.506Z
- command: `echo "=== preflight: SHA references ==="
OLD_MAIN=$(git rev-parse main)
OLD_TAG=$(git rev-parse v0.14.3)
echo "OLD_MAIN: $OLD_MAIN"
echo "OLD_TAG (v0.14.3): $OLD_TAG"
echo "OLD_FEATURE_TIP (e8495b8): $(git rev-parse e8495b8)"
echo "ORIGIN_MAIN: $(git rev-parse origin/main)"
echo ""
echo "=== safety net ==="
git branch backup-before-squash main
echo "backup-before-squash created at $OLD_MAIN"
echo ""
echo "=== current log to be rewritten ==="
git log origin/main..main --oneline`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f787c58f-88ea-4626-934d-5ea39fdf614b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 94
- session: `f787c58f-88ea-4626-934d-5ea39fdf614b`
- timestamp: 2026-05-13T06:05:10.636Z
- command: `echo "=== step 4-5: recreate feature, rebase onto new main ==="
# Recreate feature branch pointing at old e8495b8
git branch feature/fix-smart-gather-cross-branch e8495b8 && \
git checkout feature/fix-smart-gather-cross-branch && \
# Rebase the 5 commits (df98036..e8495b8) onto new main
# old base for feature = 3a83bc1
git rebase --onto main 3a83bc1 feature/fix-smart-gather-cross-branch 2>&1 | tail -5
echo ""
echo "feature new tip: $(git rev-parse HEAD)"
git log --oneline -6
echo ""

echo "=== step 6: --no-ff merge to main ==="
git checkout main && \
git merge --no-ff feature/fix-smart-gather-cross-branch -m "Merge feature/fix-smart-gather-cross-branch" && \
echo "main new tip: $(git rev-parse HEAD)"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f787c58f-88ea-4626-934d-5ea39fdf614b.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 95
- session: `facae6a3-97bd-4cb4-bad8-5c06c33a7216`
- timestamp: 2026-05-08T23:23:59.903Z
- command: `git checkout -b content/2026-05-09 main 2>&1 && git add infra/state/system_state.json contexts/work_logs/2026-05-08_exocortex-dev_update.md contexts/work_logs/2026-05-08_qt-ai-enablement_mr-split-pacs-v13-and-multibinary-refactor.md inbox/captured/2026-05-08_state_audit.md inbox/captured/heptabase/article/2026-05-08.md 2>&1 && git status --short 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/facae6a3-97bd-4cb4-bad8-5c06c33a7216.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

### Candidate 96
- session: `fb4187de-4478-4672-b1c7-ff49e717ba39`
- timestamp: 2026-04-23T20:26:08.152Z
- command: `git checkout main && git checkout -b feature/add-project-branch-flow && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/fb4187de-4478-4672-b1c7-ff49e717ba39.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [x] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 97
- session: `fb4187de-4478-4672-b1c7-ff49e717ba39`
- timestamp: 2026-04-23T20:28:37.076Z
- command: `git branch project/test-split main && git branch --list 'project/*' 'content/*' 'feature/*' && echo "---status---" && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/fb4187de-4478-4672-b1c7-ff49e717ba39.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [x] manual_compliance — 人標 follow,跳過 LLM

