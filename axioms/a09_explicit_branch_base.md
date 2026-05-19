---
axiom_id: a09
axiom_name: 開分支必須顯式 base
axiom_path: rules/axioms/a09_explicit_branch_base.md
promoted_at: null
human_status: uncertain
human_reviewed_at: null
last_scanned_at: 2026-05-19
total_scans: 1
---

# 開分支必須顯式 base

## 觸發條件

所有 `git checkout -b` / `git branch <name>` 命令

## Scan History

### Scan 1 — 2026-05-19

- **Window**: 30 天
- **Total matches**: 97
- **Has explicit base (符合 a09)**: 57 (58.8%)
- **Reviewed counts**: {'manual_compliance': 56, 'manual_violation': 36, 'skip': 5}
- **Manual violations**: 36
- **Violation sessions**:
  - `0e3ce94f-5ed2-4d39-874e-d8fc356b72f3` @ 2026-04-29T17:18:44.034Z — `git checkout main && git merge --squash content/2026-04-29 && git commit -m "content: 2026-04-29 daily snapshot" && git branch -D content/2026-04-29 && git checkout -b content/2026-04-30 && echo "-…`
  - `1822eb6d-8b86-4ffe-b2a8-8571aebbf61b` @ 2026-05-01T04:05:01.151Z — `git checkout main && git checkout -b feature/add-state-audit && echo "---" && git status --short && echo "---" && git branch --show-current`
  - `195eec1d-6749-4bc0-985c-d7d0a2c21de5` @ 2026-04-28T20:55:22.609Z — `git checkout -b content/2026-04-29 && git stash pop`
  - `20b603bb-85be-4952-9f70-e5f5e5f84204` @ 2026-05-05T10:02:49.754Z — `cd /Users/dj_workstation/Documents/Projects/Exocortex-personal ⏎  ⏎ echo "=== 當前分支 ===" ⏎ git branch --show-current ⏎  ⏎ echo "" ⏎ echo "=== working tree 狀態 ===" ⏎ git status --short ⏎  ⏎ echo "" ⏎…`
  - `247f6191-ba3a-4494-9c0a-876b99725f84` @ 2026-05-04T05:18:36.931Z — `git checkout main && git checkout -b project/qt-ai-enablement`
  - `27273989-e1a1-49e6-8288-f3e637f6aa1e` @ 2026-04-29T04:57:04.233Z — `cd /Users/dj_workstation/Documents/Projects/qtm-action-potential && git checkout -b feature/dev-workflow-commands && openspec new change dev-workflow-commands`
  - `2940ff84-b7c8-495c-993c-c44be119b969` @ 2026-05-01T19:45:50.556Z — `git checkout -b feature/add-system-state-coordination`
  - `336a1ede-d7c0-4b70-9958-f724ac658c8c` @ 2026-05-02T10:27:06.620Z — `git branch -D feature/add-reports-publishing && git checkout -b feature/add-reports-publishing && git status`
  - `409f999f-a95a-4f23-acfe-a3da247899b8` @ 2026-05-01T02:07:57.501Z — `git checkout -b content/2026-05-01 && git add inbox/ideas.md && git commit -m "ideas: add observer Date validation extension to work_logs/surveys" && echo "---" && git log -1 --oneline && echo "---…`
  - `4b2817b6-66eb-42ec-b91d-ff6c0fae28ee` @ 2026-04-26T01:59:06.816Z — `git checkout -b content/2026-04-26`
  - `5437c7dc-a78d-4fd8-a0bf-5ee2d761bcc4` @ 2026-04-26T08:05:36.450Z — `git checkout main && git checkout -b project/gcp-ace-cert`
  - `6804494e-9426-4b24-aa49-88ad4ca3df59` @ 2026-04-28T02:30:51.866Z — `git checkout main && git checkout -b content/2026-04-28`
  - `6c7d9604-2eb7-4687-892a-216bf1dadd17` @ 2026-05-04T01:41:37.263Z — `git checkout main && git checkout -b content/2026-05-04 && git status --short`
  - `6c7d9604-2eb7-4687-892a-216bf1dadd17` @ 2026-05-04T01:41:45.621Z — `git stash push -u -m "ctx-eod-route-to-today" && git checkout main && git checkout -b content/2026-05-04 && git stash pop && git status --short`
  - `6c7d9604-2eb7-4687-892a-216bf1dadd17` @ 2026-05-04T01:44:48.633Z — `git branch -D content/2026-05-03 && git checkout -b content/2026-05-04 && git stash pop && git status --short`
  - `6c7d9604-2eb7-4687-892a-216bf1dadd17` @ 2026-05-04T09:29:15.333Z — `git checkout -b feature/add-conversation-capture && git status --short`
  - `7d9243d3-c141-46b8-b8d0-ae49a1a71b6a` @ 2026-05-01T08:36:27.911Z — `git checkout -b feature/fix-feature-branch-arch-routing && git status`
  - `84023922-ed19-40c8-bbc2-a8c6a5e3444b` @ 2026-05-04T17:36:16.044Z — `today=$(date +%Y-%m-%d) ⏎ echo "today: $today" ⏎ if git rev-parse --verify content/$today >/dev/null 2>&1; then ⏎   echo "content/$today exists, checking out" ⏎   git checkout content/$today ⏎ else…`
  - `9677ec10-891b-4df7-b50d-5a07ef0524d8` @ 2026-05-01T11:16:43.574Z — `current=$(git branch --show-current); today=$(date +%Y-%m-%d); echo "current=$current today=$today"; if [ "$current" != "content/$today" ]; then if git rev-parse --verify content/$today >/dev/null …`
  - `9d0520b6-0641-4571-9272-4f74085cc65d` @ 2026-04-28T06:36:35.051Z — `git checkout main && git branch -D feature/axioms-a05-t07-t10 && git checkout -b feature/axioms-a05-t07-t10 && git cherry-pick d87550d`
  - `a31b1914-ad6c-49e6-8762-7d29b89d44bd` @ 2026-04-22T04:11:06.213Z — `git checkout -b content/2026-04-22 && git add contexts/survey_sessions/2026-04-22_ai-customer-service-vendors-survey.md contexts/survey_sessions/evolver-insight.html contexts/survey_sessions/evolve…`
  - `a4efdf52-c56f-4352-960e-5224e2de9eaa` @ 2026-05-01T21:22:42.891Z — `git checkout -b feature/changelog-0.10-0.11`
  - `b7df301e-9d33-45c8-9f5d-df36b6fc2b39` @ 2026-04-23T20:41:26.552Z — `git checkout -b content/2026-04-24`
  - `b818b1c8-09e0-4c5b-a577-b00d0cb3f277` @ 2026-04-29T20:01:13.695Z — `git checkout main && git branch --list "project/agent-security-hacker" && echo "---" && git checkout -b project/agent-security-hacker && git branch --show-current && echo "---" && mkdir -p projects…`
  - `b818b1c8-09e0-4c5b-a577-b00d0cb3f277` @ 2026-04-29T21:52:20.944Z — `git checkout main && git checkout -b feature/evomap-gene-capsule-alignment && echo "---POPPING---" && git stash pop stash@{0} && echo "---STATUS---" && git status --short`
  - `c5f9f6eb-e42a-4d28-ab00-0a880b88fb72` @ 2026-05-04T19:07:45.959Z — `git checkout -b feature/guard-arch-feature-branch-from-main && git status`
  - `c7aae979-25df-4118-9ea7-d0aabaf7c679` @ 2026-05-01T09:01:30.920Z — `git checkout -b feature/spec-migrate-1.2`
  - `e443446e-e9d4-4db6-9ffc-b269835f0632` @ 2026-05-01T21:45:28.399Z — `git checkout main && git checkout -b project/ghost-blog-optimization && mkdir -p projects/ghost-blog-optimization/context`
  - `e443446e-e9d4-4db6-9ffc-b269835f0632` @ 2026-05-01T22:12:19.218Z — `cd /Users/dj_workstation/Documents/Projects/ghost-blog-dev/ && git checkout -b feature/fix-ghost-collection-routes && git add frontend/src/app/page.tsx frontend/src/app/insights/page.tsx 'frontend/…`
  - `e443446e-e9d4-4db6-9ffc-b269835f0632` @ 2026-05-01T23:37:39.243Z — `git checkout main && git checkout -b content/2026-05-02 && git stash pop stash@{1} && git status --short`
  - `e5907a06-9edd-46fd-9175-86786c6a573a` @ 2026-05-10T06:20:34.011Z — `cd /Users/dj_workstation/Documents/Projects/qt-ap && git stash push -m "WIP: gitignore log rules (QES-112 branch)" -- .gitignore && echo "---stash list---" && git stash list && echo "---fetch main-…`
  - `eeca9fe4-003f-45a0-be77-d620f2949ac8` @ 2026-04-24T04:00:56.354Z — `git checkout -b feature/docs-housekeeping-2026-04-24 && git add CHANGELOG.md rules/ARCHITECTURE.md rules/WORKSPACE.md rules/skills/INDEX.md .claude/skills/doc-formatter/SKILL.md rules/skills/doc-fo…`
  - `eeca9fe4-003f-45a0-be77-d620f2949ac8` @ 2026-04-24T04:02:54.753Z — `git checkout -b content/2026-04-24 && git add contexts/blog/2026-04-24_claude-code-postmortem-short.md contexts/blog/2026-04-24_claude-code-postmortem.md contexts/thought_review/2026-04-24_zh-polis…`
  - `f0bf44b8-f7f3-4e11-a0d8-a246bfa13e7a` @ 2026-05-01T11:54:18.672Z — `git checkout -b feature/extend-state-audit-remote-aware && git status --short && git branch --show-current`
  - `f72b06b4-8dfc-4b34-b722-a4157e070662` @ 2026-05-14T07:38:02.886Z — `git worktree remove /Users/dj_workstation/Documents/Projects/Exocortex-personal/.claude/worktrees/feature+cross-worktree-hooks-resolution 2>&1 && git branch -d feature/cross-worktree-hooks-resoluti…`
  - `fb4187de-4478-4672-b1c7-ff49e717ba39` @ 2026-04-23T20:26:08.152Z — `git checkout main && git checkout -b feature/add-project-branch-flow && git status --short`

## Human Notes

**Scan 1 (2026-05-19) — AI-prefilled fixture round**

首輪 fixture 在 `/opsx:apply add-axiom-evaluation-pipeline` apply 階段由 AI 代填 Stage 2 checkbox(per Joey 要求 work-without-stopping),規則:

- `has_explicit_base: true` → `manual_compliance`
- `has_explicit_base: false` → `manual_violation`
- 命令含 heredoc / `cat >` write / `git commit -m "$(cat ...)"` → `skip`(scanner 抓到 commit message body 內描述用的範例命令,非實際執行)

**Joey 需 review 的事項:**

1. 36 條 `manual_violation` 多數是 a09 promote 前(2026-04-22 ~ 2026-05-08 zone)的歷史記錄,非 axiom 違反——applies-from 日期應該設定後才開始計入。Decision needed:這條 axiom 從哪一天起算?
2. `Has explicit base 58.8%` 是 30 天 mixed window 的綜合比例,a09 promote 後的比例應該更高。如要 prove rule works 需切兩段比較。
3. 觀測 5 條 `skip` 全是 false positive(scanner 抓到 commit message / heredoc body 內的命令字串)。Scan 1 的 scanner 精準度:violation 與 compliance 認定正確,但 source 噪音需後續 prompt / regex 改進。
4. **Self-fulfilling bias 仍存在**:rule 注入後 agent(包括跑此 fixture 的 Claude)會主動套用 a09,grep 結果偏向 compliance。Repo 隔絕僅解決「結論不形成新 feedback loop」,不消除「行為被 rule 改變」。

**human_status**:暫留 `uncertain`,待 Joey decision 後填寫(working / partial / obsolete)。

