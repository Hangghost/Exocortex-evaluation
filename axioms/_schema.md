# Axiom Card Schema

每條 axiom 的 evaluation card（`axioms/<id>.md`）SHALL 遵循下列 schema。

本 schema 由 evaluation repo 自治，演化只走本 repo git history，不需要 Exocortex `openspec/specs/axiom-evaluation-pipeline/` 變更（per spec D-4）。

## Frontmatter

```yaml
---
axiom_id: a09                                  # 對應 Exocortex rules/axioms/<id>.md 的 id
axiom_name: 開分支必須顯式 base                # 人類可讀名稱
axiom_path: rules/axioms/a09_explicit_branch_base.md  # 相對於 Exocortex repo
promoted_at: 2026-XX-XX                        # axiom 被 Reflector promote 的日期（人填）
applies_from: 2026-XX-XX                       # 觀測起算日（scanner 過濾掉此日期前的事件;通常等於 promoted_at）
last_scanned_at: 2026-05-19                    # 最近一次 Stage 1 scan 的日期
total_scans: 1                                 # 累計 scan 次數
human_status: uncertain                        # working | partial | obsolete | uncertain
human_reviewed_at: null                        # 最近一次人 review 並更新 status 的日期
---
```

### `human_status` 取值

- `working`：rule 有觀察到 follow，違反率低於門檻
- `partial`：部分場景 follow，某些 corner case 經常違反，可改寫
- `obsolete`：N 週 zero trigger 或全違反，候選 demote
- `uncertain`：首輪試點 / 資料不足

### `applies_from` 用途

Axiom promote 前的歷史事件不該算違反(promote 前 agent 不知道規則)。Scanner 讀此欄位後,window cutoff 取較晚者 `max(today - days, applies_from)`。

通常 `applies_from` 等於 `promoted_at`;若 axiom promote 後有一段 grace period(例如先公告兩週再 enforce),`applies_from` 可比 `promoted_at` 晚。

### 不允許的欄位

下列欄位 SHALL NOT 出現在 frontmatter：
- LLM 自動生成的判斷結論（如 `llm_verdict: working`）—— 結論 must 經人 review
- Exocortex 內檔案的引用 path 作為 evidence（per reflector blind layer 3）

## Body 結構

```markdown
# {axiom_name}

## 觸發條件

axiom 適用範圍 / 場景（人類描述,不一定 mirror Exocortex axiom 本體文字）。

## Scan History

### Scan N — YYYY-MM-DD

- **Window**: <days> 天
- **Total matches**: <int>
- **Followed (含顯式 base / 符合 axiom)**: <int> (<pct>%)
- **Potential violations**: <int>
- **Violation sessions**:
  - <session_id> @ <timestamp> — `<command>`
  - ...

(append-only，新一輪 scan 不覆寫舊 scan)

## Human Notes

(人填，自由格式;典型內容:首輪試點觀察、是否需要 prompt 調整、是否考慮 demote)
```

## 範例

見 `axioms/a09_explicit_branch_base.md`（首條落地試點）。
