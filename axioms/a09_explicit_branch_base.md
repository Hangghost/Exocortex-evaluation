---
axiom_id: a09
axiom_name: 開分支必須顯式 base
axiom_path: rules/axioms/a09_explicit_branch_base.md
promoted_at: 2026-05-05
applies_from: 2026-05-05
human_status: uncertain
human_reviewed_at: null
last_scanned_at: 2026-05-19
total_scans: 1
---

# 開分支必須顯式 base

## 觸發條件

所有 `git checkout -b` / `git branch <name>` 命令(scanner 掃 transcript JSONL 內 Bash tool_use payload)。

## Scan History

### Scan 1 — 2026-05-19

- **Window**: 30 天(applies_from=2026-05-05,實際 effective cutoff = 2026-05-05)
- **Total matches**: 53
- **Has explicit base (符合 a09 一行式)**: 47 (88.7%)
- **Manual violations** (真正違反): 0
- **Skipped (scanner false positives)**: 6
  - 4 條 heredoc / `cat > .md <<EOF` 寫文件時引用到範例命令字串
  - 1 條 `git worktree remove ... && git branch 2>&1 | grep` — scanner 把 `2` 當 branch name
  - 1 條多行診斷 script,scanner 在 `git branch\n\necho` 處誤抓 `echo` 當 branch name
- **Manual compliance**: 47
  - 46 條 一行式 `git checkout -b <name> <base>`(canonical idiom)
  - 1 條 兩步式 `git checkout main && ... && git checkout -b <name>`(per a09 doc 🟡 effective safe)

## Human Notes

**Scan 1 結論(2026-05-19)**

- a09 promote 自 2026-05-05 以來,**0 條真實違反**;47 條 follow(46 canonical + 1 yellow-zone two-step)。
- Pipeline 機械驗證通了:Stage 1 grep / Stage 2 dashboard parse / Stage 3 card 寫入 / negative test abort 全部 pass。
- Scanner 已知限制(non-blocking for fixture):
  - heredoc / `cat >` 寫文件時,body 內的範例命令字串會被 regex 抓到 → 用 prefill skip rule 處理,可接受
  - `git branch 2>&1 | grep ...` 因 `2` 是 word char 被 regex 抓 → 已加 DIGIT_NAME_RE skip rule
  - 多行 script `git branch\n` 後 `echo`,regex 把 `echo` 當 branch name → 已加 SHELL_BUILTIN_AFTER_BRANCH skip rule
  - 推廣到 a07/t10 前可考慮:scanner 改成「先 split 出獨立命令(分號/`&&`/`||`/換行 split),再對各 segment 跑 regex」,從根本上避免跨命令 match

**Self-fulfilling bias caveat(per spec)**

Repo 隔絕只解決「evaluation 結論不形成新 feedback loop」,不消除「agent 因 rule 注入改變行為」。47 條 follow 包含 fixture 跑期間 Claude(本 session)主動套用 a09 的 commits,需在 long-term 評估時切多 window 比較。

**human_status proposal**

依據 0 真實違反 + 47 follow + 1 effective-safe 兩步式,**建議 `working`**;但首輪 fixture 樣本量(53 over 14 days)偏小,等下次 cron 自動 scan 累積更多資料後再 promote 自 `uncertain` → `working`。Joey 可選:

- (A) 現在直接設 `working`,接受 fixture 樣本判定
- (B) 留 `uncertain`,等 4 週後(下次 monthly review 時)累積 200+ candidates 再 promote
