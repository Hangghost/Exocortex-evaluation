# Axiom Evaluation Review — 2026-05-26

- axiom: **a09**
- window: 7 天
- total candidates: 24

對每個 candidate 勾選 **一個** 選項。多選或全空會被 parser 拒絕。

## a09

### Candidate 1
- session: `00d134e5-8fb8-465f-929f-b26b6862d925`
- timestamp: 2026-05-25T02:58:00.678Z
- command: `git checkout -b content/2026-05-25 main 2>&1 | tail -5 && echo "---STATUS---" && git status --short && echo "---COMMIT---" && git commit -m "logs: add qheart-ap 2026-05-25 update — QES-124 recap + Jira backfill" 2>&1 | tail -10`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/00d134e5-8fb8-465f-929f-b26b6862d925.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 2
- session: `061424ca-a6c7-4551-81cd-ef1ba4903ec7`
- timestamp: 2026-05-22T01:42:33.291Z
- command: `git checkout -b feature/add-eod-recovery-flow main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/061424ca-a6c7-4551-81cd-ef1ba4903ec7.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 3
- session: `0ad8e8ab-7e1a-424d-8930-b27d1f268f9f`
- timestamp: 2026-05-20T17:48:10.649Z
- command: `git checkout -b feature/migrate-cron-to-launchd main 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/0ad8e8ab-7e1a-424d-8930-b27d1f268f9f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 4
- session: `1b441183-d6ad-4a3a-bf78-b31e7ff606d3`
- timestamp: 2026-05-20T16:20:08.549Z
- command: `git checkout -b content/2026-05-21 main && git add infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/2026-05-21_state_audit.md inbox/captured/heptabase/article/2026-05-20.md inbox/captured/heptabase/github/2026-05-20.md inbox/captured/heptabase/threads/2026-05-20.md inbox/captured/heptabase/youtube/2026-05-20.md && git commit -m "content: 2026-05-21 daily snapshot" 2>&1 | tail -20`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/1b441183-d6ad-4a3a-bf78-b31e7ff606d3.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 5
- session: `1ce05e1c-4f96-46b7-a41e-fbfdd0844d06`
- timestamp: 2026-05-20T03:44:31.916Z
- command: `echo "=== Setup throwaway branch with helper removed ==="
git checkout -b temp/helper-missing-test main
git mv infra/tools/project_smart_gather/scan.py infra/tools/project_smart_gather/scan.py.bak
git commit -m "test: temp remove helper for negative case"
echo ""
echo "=== Verify helper absent on this branch ==="
ls infra/tools/project_smart_gather/ 2>&1
echo ""
echo "=== Test fallback chain (per spec) ==="
echo "Primary: git show main:..."
git show main:infra/tools/project_smart_gather/scan.py | python3 - --project qheart-ap --limit 1 > /tmp/neg-helper.json 2>&1
PRIMARY_RC=$?
if [ $PRIMARY_RC -eq 0 ]; then
  echo "  Primary succeeded (main ref still has helper from main checkout's perspective)"
  echo "  → For full hard-abort test, need to also break main ref. Simulating by changing primary to point at this branch HEAD:"
  echo ""
  echo "Test against THIS branch's ref (helper removed):"
  git show HEAD:infra/tools/project_smart_gather/scan.py 2>&1 | head -3
  echo ""
  echo "→ git show HEAD:helper fails (helper removed). This simulates 'main ref helper missing' scenario"
fi
echo ""
echo "=== Cleanup ==="
git checkout main
git branch -D temp/helper-missing-test
ls infra/tools/project_smart_gather/scan.py
echo "✓ helper restored on main"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/1ce05e1c-4f96-46b7-a41e-fbfdd0844d06.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 6
- session: `1ce05e1c-4f96-46b7-a41e-fbfdd0844d06`
- timestamp: 2026-05-20T04:00:41.368Z
- command: `echo "=== Step 3 branch type ==="
echo "WORKTREE_BRANCH=main, IS_BG=true, IN_WORKTREE=false → fg-mode-like (main checkout)"
echo ""
echo "=== Step 4 路由: main + 純 content-shaped → content/2026-05-20 ==="
echo ""
echo "=== Step 4.1 build content branch from main ==="
git branch --list content/2026-05-20
git checkout -b content/2026-05-20 main 2>&1
git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/1ce05e1c-4f96-46b7-a41e-fbfdd0844d06.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 7
- session: `1ec67a51-7e36-4118-a908-fd26e3a41212`
- timestamp: 2026-05-22T03:23:44.301Z
- command: `git add contexts/work_logs/2026-05-22_exocortex-dev_update.md && git checkout -b content/2026-05-22 main 2>&1`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/1ec67a51-7e36-4118-a908-fd26e3a41212.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 8
- session: `1ec67a51-7e36-4118-a908-fd26e3a41212`
- timestamp: 2026-05-22T03:24:27.486Z
- command: `git checkout -b content/2026-05-22 main 2>&1 && git add contexts/work_logs/2026-05-22_exocortex-dev_update.md && git commit -m "logs: add exocortex-dev 2026-05-22 update — 19 archives + macOS 26.x cron TCC incident + acceptance fixture P0 finding" 2>&1 | tail -5`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/1ec67a51-7e36-4118-a908-fd26e3a41212.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 9
- session: `2f28ad74-5b4e-4d7f-9bf5-2b27278a249a`
- timestamp: 2026-05-21T03:50:17.206Z
- command: `git checkout -b content/2026-05-21 main && git add contexts/blog/2026-05-16_blog-claude-code-bg-session.md inbox/captured/post_staging/2026-05-16_blog-claude-code-bg-session.json library/character_joey_chibi/ && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/2f28ad74-5b4e-4d7f-9bf5-2b27278a249a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 10
- session: `4c722e1a-1f8e-48ef-868a-2d90a037a00f`
- timestamp: 2026-05-20T02:19:29.022Z
- command: `git checkout -b project/27001-support main && mkdir -p projects/27001-support/context && echo "---" && git branch --show-current && ls projects/27001-support/`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4c722e1a-1f8e-48ef-868a-2d90a037a00f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 11
- session: `4c722e1a-1f8e-48ef-868a-2d90a037a00f`
- timestamp: 2026-05-20T03:22:29.551Z
- command: `git checkout -b content/2026-05-20 main && git add contexts/work_logs/2026-05-20_27001-support_jira-cli-markdown-quirks.md && git commit -m "logs: add work log on Jira CLI markdown 渲染怪癖

記錄用 ankitpokhrel/jira-cli 更新 DATA-534 description 時觀察到的三條 plain view 渲染怪癖：
- **bold** → *bold*（單星號為 Jira 原生粗體語法）
- ~~strike~~ → -strike-（單破折號為 Jira 原生刪除線）
- URL 在 plain view 重複兩次（text + link annotation 同時 dump）

Jira Web UI 渲染正常；建議 verify 開 UI 而非 jira issue view --plain。" && echo "--- [1/2] DONE ---" && git checkout project/27001-support && git add projects/27001-support/PROJECT.md projects/27001-support/context/task-breakdown.md && git commit -m "project(27001-support): 補入 DATA-534 完整 sub-tasks + 稽核時程確認

- context/task-breakdown.md 新增 — 四項任務拆 ~35 sub-tasks，含 DATA-491/372 歷史 comments 整合（防火牆採購硬截止 6/30、CCTV 30 天備份 Ted 爬蟲現況待自查、ISMS 表單清單、程序書連結）
- PROJECT.md 反映：
  - frontmatter 加 audit_dates（5/22 內稽 / 5/29 管審 / 6/2 外稽）
  - 現況：Ted/Pierce 離職、Joey sole owner、Ruth 為唯一活躍諮詢窗口
  - 下一步：拆三段（5/22 內稽前立即 / 5/22→6/2 短期 / 外稽後中期）

DATA-534 描述已同步擴展為 8-section 完整版（Jira 端已 push 兩輪）。" && echo "--- [2/2] DONE ---" && git log --oneline -5`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/4c722e1a-1f8e-48ef-868a-2d90a037a00f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 12
- session: `533c5d14-3307-452f-afea-3a3b153b82b1`
- timestamp: 2026-05-23T00:08:33.559Z
- command: `git checkout -b content/2026-05-23 main && git add inbox/digest_escalations.md inbox/ideas.md infra/state/digest_history.jsonl infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/2026-05-22_state_audit.md library/cal-diy.md && git commit -m "content: overnight cron residue + cal-diy library card"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/533c5d14-3307-452f-afea-3a3b153b82b1.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 13
- session: `5c7a0779-8553-49ca-85c3-59e91f650efd`
- timestamp: 2026-05-20T05:57:34.872Z
- command: `cd /Users/dj_workstation/Documents/Projects/qt-ap && git branch chore/codex-cleanup-worktree-gitignore && git reset --hard origin/main && echo "--- main HEAD now ---" && git log --oneline -2 && echo "--- chore branch ---" && git log chore/codex-cleanup-worktree-gitignore --oneline -2 && echo "--- push chore branch ---" && git push -u origin chore/codex-cleanup-worktree-gitignore 2>&1 | tail -10`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/5c7a0779-8553-49ca-85c3-59e91f650efd.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 14
- session: `731f8d31-c067-44df-813b-a461a27428a8`
- timestamp: 2026-05-23T07:28:41.642Z
- command: `git checkout -b feature/spec-cleanup-batch-2026-05-23 main && git branch --show-current && git log --oneline -2`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/731f8d31-c067-44df-813b-a461a27428a8.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 15
- session: `9776b5d4-6ed3-4322-8a15-ece27e132ab1`
- timestamp: 2026-05-23T22:48:09.484Z
- command: `git checkout -b content/2026-05-24 main && git add inbox/todos.md && git commit -m "inbox: todos 結 2 條 done + 加 2 條 skill candidate

結 done：
- install.sh conditional-install plist .venv guard（spec-cleanup-batch-2026-05-23 / 47dea16）
- extract-ctx-onboard-to-harness 實作（archive merge a939295 / CHANGELOG 0.25.0）

加 skill candidate（2026-05-24 onboard 提出）：
- ctx-command-harness-extraction（rules/skills/，建議等 /ctx:eod harness 化 n=2 後寫）
- scheduled-job-stuck-diagnostic-playbook（personal-skills/，源於 2026-05-20 cron TCC incident）"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/9776b5d4-6ed3-4322-8a15-ece27e132ab1.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 16
- session: `9776b5d4-6ed3-4322-8a15-ece27e132ab1`
- timestamp: 2026-05-23T22:48:36.538Z
- command: `git rev-list --left-right --count main...origin/main && git checkout -b feature/add-escalation-pattern-review-pipeline main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/9776b5d4-6ed3-4322-8a15-ece27e132ab1.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 17
- session: `a8339b4d-af95-46b1-a625-323324c0a5a7`
- timestamp: 2026-05-23T00:08:33.559Z
- command: `git checkout -b content/2026-05-23 main && git add inbox/digest_escalations.md inbox/ideas.md infra/state/digest_history.jsonl infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/2026-05-22_state_audit.md library/cal-diy.md && git commit -m "content: overnight cron residue + cal-diy library card"`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/a8339b4d-af95-46b1-a625-323324c0a5a7.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 18
- session: `b6af179a-36bf-4dc7-945e-74e6322a1df4`
- timestamp: 2026-05-20T01:21:21.607Z
- command: `git stash push -m "ctx-onboard-rotate-content-branch" && git checkout main && git branch -d content/2026-05-19 && git checkout -b content/2026-05-20 && git stash pop && git status --short`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/b6af179a-36bf-4dc7-945e-74e6322a1df4.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 19
- session: `ba123f36-3c64-4dbf-acc5-29fb7c9b63a1`
- timestamp: 2026-05-19T01:49:39.212Z
- command: `git commit -m "$(cat <<'EOF'
feat(axiom-evaluation): add reflector-blind 3-stage pipeline (a09 pilot)

Adds Stage 4 of the Reflector self-evolution loop — retrospective
observation of promoted axioms. Pipeline lives in a separate private repo
(`exocortex-evaluation`, ~/Documents/Projects/) so its conclusions cannot
become reflector input and form a self-reinforcing feedback loop.

Three-layer reflector blind:
  1. Physical repo separation (eval repo not inside Exocortex-personal)
  2. Reflector source whitelist excludes eval repo path
  3. Files inside Exocortex SHALL NOT cite eval repo as evaluation source
     (exception: this commit's CRONTAB entry / reports manifest entry /
     memory/reference_evaluation_repo.md — path strings only, no verdicts)

3-stage pipeline (per spec):
  Stage 1 — auto cron, free  scan_axiom_usage.py: pure grep over CC
                              transcript JSONLs, writes candidates.json
  Stage 2 — mandatory human   render_review_dashboard.py + edit md +
                              parse_human_review.py: produces human_review.json
  Stage 3 — human-triggered   llm_judge.py: hard precondition on
                              human_review.json existence; writes axiom card

Pipeline tooling lives in exocortex-evaluation repo (3 commits there:
init / applies_from filter / human_status promotion).

Exocortex-side wiring (this commit):
  - CRONTAB.md: weekly Stage 1 cron entry with `test -d` prerequisite
    (silent exit when eval repo absent; not enabled yet, see todos)
  - .claude/commands/ctx/onboard.md: Step 5.5 axiom-evaluation hint
    (📊 emoji, third hint class alongside 🔴 axiom watch / 🟡 skill candidate)
  - reports/manifest.yaml: shareable entry for cross-repo dashboard
    (../exocortex-evaluation/dashboards/<date>_axiom_status.html)
  - memory/reference_evaluation_repo.md: location + reflector-blind rules
  - rules/axioms/INDEX.md: note about evaluation living externally
  - inbox/todos.md: deferred 6.3 cron enable + 11.4 silent-skip negative test

a09 pilot result:
  - 14-day window (applies_from=2026-05-05), 53 candidates
  - 47 compliance (46 canonical one-line + 1 yellow-zone two-step)
  - 0 real violations
  - 6 scanner false positives (heredoc / multiline / `git branch 2>&1`)
  - human_status: working (Joey reviewed 2026-05-19)
  - Dashboard at https://keepthinking.be/reports/2026-05-19_axiom_status.html
    (CF Access shareable tier)

Archive: openspec/changes/archive/2026-05-19-add-axiom-evaluation-pipeline/

Tasks complete 50/54. Remaining four are inherently post-merge actions:
6.3 cron enable (in todos), 11.4 silent-skip negative test (in todos),
12.1 /ctx:merge (this branch), 12.4 work_log via /ctx:content.
EOF
)" 2>&1 | tail -10 && git log --oneline | head -3`
- has_explicit_base: **False** (⚠ potential violation)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ba123f36-3c64-4dbf-acc5-29fb7c9b63a1.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 20
- session: `d2c61259-66c3-48f0-8774-5d715c75fc3a`
- timestamp: 2026-05-19T12:23:24.799Z
- command: `git checkout -b content/2026-05-19 main && git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/d2c61259-66c3-48f0-8774-5d715c75fc3a.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 21
- session: `ec2f6187-8157-4f9c-b453-49260cd4b6c5`
- timestamp: 2026-05-26T00:58:58.427Z
- command: `cd /Users/dj_workstation/Documents/Projects/Exocortex-personal
git checkout -b project/max5x-dispatch-architecture main
echo "==="
git branch --show-current
echo "==="
mkdir -p projects/max5x-dispatch-architecture/context
ls projects/max5x-dispatch-architecture/`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ec2f6187-8157-4f9c-b453-49260cd4b6c5.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 22
- session: `ec3ce568-d03c-44e1-b38f-8f52bdff81d4`
- timestamp: 2026-05-20T16:20:08.549Z
- command: `git checkout -b content/2026-05-21 main && git add infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/2026-05-21_state_audit.md inbox/captured/heptabase/article/2026-05-20.md inbox/captured/heptabase/github/2026-05-20.md inbox/captured/heptabase/threads/2026-05-20.md inbox/captured/heptabase/youtube/2026-05-20.md && git commit -m "content: 2026-05-21 daily snapshot" 2>&1 | tail -20`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/ec3ce568-d03c-44e1-b38f-8f52bdff81d4.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 23
- session: `f67ff0eb-8f6d-443f-b7fa-afeee403741d`
- timestamp: 2026-05-20T23:20:52.422Z
- command: `git checkout -b content/2026-05-21 main && git add contexts/blog/2026-05-16_claude-code-bg-session-agent-view-survey.md contexts/work_logs/2026-05-21_feature/ inbox/captured/post_staging/2026-05-16_claude-code-bg-session-agent-view-survey.json && git commit -m "content: add bg-session survey + heptabase-collect-zone review log" && echo "---SHA---" && git rev-parse HEAD && echo "---SWITCH BACK---" && git checkout main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/f67ff0eb-8f6d-443f-b7fa-afeee403741d.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 24
- session: `fb7d0a61-4d06-4879-bb68-ba506558b941`
- timestamp: 2026-05-25T23:00:04.020Z
- command: `git checkout -b content/2026-05-26 main && git add inbox/digest_escalations.md inbox/ideas.md infra/state/digest_history.jsonl infra/state/system_state.json memory/OBSERVATIONS.md inbox/captured/heptabase/article/2026-05-25.md && git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Documents-Projects-Exocortex-personal/fb7d0a61-4d06-4879-bb68-ba506558b941.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

