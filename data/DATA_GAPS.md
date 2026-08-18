# Data Gaps — 已知不可用的掃描批次

本檔記錄 `data/` 內**存在但不可作為證據使用**的批次。任何跨期比較、趨勢圖、
compliance 統計 SHALL 先排除此處列出的批次。

> 為什麼需要這份檔案：`*_candidates.json` 的 `total_candidates: 0` 有兩種完全
> 不同的含義——「掃了，該窗口沒有 candidate」與「根本沒掃到」。JSON 本身無法
> 區分兩者（axiom `v02`）。這份檔案就是那個缺失的訊號。

---

## 2026-06-07 repo 搬遷造成的路徑失效（8 批）

**受影響批次**（皆 `total_candidates: 0`，皆 axiom `a09`）：

| batch | 可重建性 |
|---|---|
| 2026-06-14 | ❌ transcript 已過 retention |
| 2026-06-21 | ❌ transcript 已過 retention |
| 2026-06-28 | ❌ transcript 已過 retention |
| 2026-07-05 | ❌ transcript 已過 retention |
| 2026-07-12 | ❌ transcript 已過 retention |
| 2026-07-19 | ❌ 窗口 07-12~07-19，僅末日倖存，其餘已過 retention |
| 2026-07-26 | ⏳ 窗口 07-19~07-26，**約 2026-08-25 前後全數過期** |
| 2026-08-02 | ⏳ 窗口 07-26~08-02，**約 2026-09-01 前後全數過期** |

> ⏳ **retention 是滾動的，「以後再補」等於「不補」**：Claude Code 預設 30 天清理本地
> transcript（兩機皆無 `cleanupPeriodDays` 覆寫；Mac mini `.last-cleanup` 於
> 2026-08-17 23:03 執行）。2026-08-18 實測 retention 底線＝2026-07-19：Mac mini
> 26 個 Exocortex 相關 project 目錄共 1449 個 jsonl，無一早於該日；MacBook 21 個
> 目錄底線更晚（2026-07-27），亦無法補足。因此上表兩個 ⏳ 批次若不在數週內處理即
> 永久消失——`add-historical-window-rescan` 那條 ticket 完成時，很可能已無資料可重掃。
> 這正是 2026-08-18 放棄重掃決策的補強理由，而非反對理由。

> 🔍 **其他來源已排除**：`~/.claude/history.jsonl` 不受 30 天清理限制（可回溯至
> 2025-12-18，盲區窗口內有 2521 筆 Exocortex-personal 記錄），但它儲存的是**使用者
> 輸入的 prompt**，非 assistant 執行的 bash tool call；其中僅 128 筆為 `!` 前綴的真實
> 指令。以此推論 a09（agent 開分支是否顯式帶 base）會取到嚴重偏斜的樣本，故不可用。
> Claude Code transcript 為本機檔案、不同步至帳號層；claude.ai 對話history 為另一套
> 儲存且不含 Claude Code 的 bash tool call。

**成因**：Exocortex-personal repo 於 2026-06-07 由 `~/Documents/Projects/` 搬到
`~/Code/`，Claude Code 的 transcript project slug 隨之由
`-Users-dj-workstation-Documents-Projects-Exocortex-personal` 變為
`-Users-dj-workstation-Code-Exocortex-personal`。掃描器當時的 `--exocortex-root`
預設值仍指向舊路徑，於是連續八週掃到空目錄、回報 0 candidate、無任何錯誤訊號。

**該缺陷已修**：`tools/scan_axiom_usage.py` 的 `--exocortex-root` 已改為
`required=True` 無預設，並在環境缺失時拋 `TranscriptEnvironmentError` 且
**不寫輸出檔**——讓 `data/` 內最新檔案的陳舊本身成為故障訊號。2026-08-03 起的
批次另有 `scanned_dirs` 欄位標示量測範圍，可據此區分兩代 calibration。

**2026-08-18 決策（Joey 拍板）：放棄重掃，接受為永久資料缺口。**
理由：五批已無 transcript 可重建；剩三批的邊際價值低於為此新增一次性工具的
維護成本。歷史窗口重掃能力改由
`[repo:exocortex-evaluation][ticket:add-historical-window-rescan]` 正式處理
（登記在 Exocortex `inbox/todos.md` 跨 repo handoff 節）。

**Stage 2 處置**：這 8 批**不會**產出 `*_human_review.json`，因此會持續被
`state_audit` 的 `axiom_eval_review_backlog` 計為 pending。這是刻意的——
現行 pipeline 沒有「盲區、不可審」這個終態，唯一的結案方式是產出
human_review.json，而那等同於宣稱審過了一個從未被掃描的窗口。**寧可讓計數
持續偏高，也不要用假的結案換取乾淨的儀表板**（axiom `v01`：聚合綠燈只驗證
「有沒有」，不驗證「對不對」）。
