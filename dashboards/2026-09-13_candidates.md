# Axiom Evaluation Review — 2026-09-13

- axiom: **a09**
- window: 7 天
- total candidates: 7

對每個 candidate 勾選 **一個** 選項。多選或全空會被 parser 拒絕。

## a09

### Candidate 1
- session: `26bc67ff-5e7f-4b97-a27c-e0a04df678aa`
- timestamp: 2026-09-10T18:51:46.570Z
- command: `set -e
if git rev-parse --verify content/2026-09-10 >/dev/null 2>&1; then
  git checkout content/2026-09-10
else
  git checkout -b content/2026-09-10 main
fi
echo "---"
git branch --show-current`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/26bc67ff-5e7f-4b97-a27c-e0a04df678aa.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 2
- session: `3946f07f-f4d0-4c5b-8d38-8a842bf11f85`
- timestamp: 2026-09-07T18:30:12.328Z
- command: `git checkout -b content/2026-09-08 main
git add memory/OBSERVATIONS.md memory/observations_archive/2026-W37.md
git status --short`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/3946f07f-f4d0-4c5b-8d38-8a842bf11f85.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 3
- session: `5b46aca7-15c4-4978-8e11-40b9792c6b65`
- timestamp: 2026-09-07T10:10:21.954Z
- command: `cat >> contexts/work_logs/2026-09-07_resume-refresh_update.md <<'WLEOF'

## 18:09

### 進展

**架構決策：履歷能力抽離專案容器——`add-career-asset-layer` 已 propose 並 push**

本輪起點是使用者的一句反駁：專案初衷是「建立履歷工具，讓 Exocortex 未來能順暢取得、累積資料
並改履歷」，不是只產出一批 artifact。順著這條線重新檢視，**17:28 那輪的 A／B 收尾二分是個假問題**
——兩者都在「履歷資產綁在專案容器內」這個前提下打轉，而該前提本身才是要處理的東西。

**Exocortex 的擴展機制盤點**（回答使用者「目前有這種新增工具或工作流的能力嗎」）：有，而且依形狀分四種，
全部有正式規約（`rules/ARCHITECTURE.md` §擴展點）。本專案產出四種形狀的東西，**只有方法論已對位**：

| 形狀 | 機制 | 現況 |
|---|---|---|
| 方法論（怎麼做） | `personal-skills/<name>/SKILL.md` + `manifest.yaml` | ✅ `profile-revamp`，trigger 含「改履歷」 |
| 確定性工具（跑指令） | skill `scripts/`（PEP 723）或 `infra/tools/` | ❌ render 走 pyenv 全域、不在 `pyproject.toml` |
| 工作流入口（slash command） | `.claude/commands/<ns>/` + capability spec | ❌ 無 |
| 知識庫路由（資料在哪） | `registry/<domain>.md` + `library/` card | ❌ `registry/career.md` 指 Notion |

**三個實查出的事實**（非推論）：

1. **CV yaml 零引用 STAR 檔**——`grep -c 'B1\|star_materials'` 對 `Hung-Lun_Chen_CV.yaml` 與
   `CV_full.yaml` 皆回 0。事實層與渲染層之間是人手抄寫，沒有機械連結。
2. **`registry/career.md` 指向 Notion**（stale），且 `library/INDEX.md` 對 resume/CV/履歷 三個關鍵字
   零命中——`library/README.md` 預留的 `type: resume` 從未被用。系統沒有一條路由指到真實位置。
3. **`project/resume-refresh` 領先 main 7 commits**——搬遷的硬前置（見下）。

**根因判定**：`project-context-layer` spec 明文「Materials remain in original locations——PROJECT.md
只記錄路徑指針」，本專案卻反過來把 35 份 STAR、15 份 CV yaml、Jira raw、平台文案**住進**專案目錄。
`projects/` 是走 `active → completed → archived` 狀態機的容器，而這些是**沒有終點的慢速狀態資產**。
`context/TOOLCHAIN.md` 那份「complete 後怎麼改履歷」的文件，整份都在替這個形狀錯置打補丁。

**產出：openspec change `add-career-asset-layer`（完整軌）**

- 軌別判定為**完整軌**（新增 capability requirement，非機械替換）；四份 artifact 齊備，
  `openspec validate --strict` 通過、`openspec status` 4/4。
- 新 capability：`career-asset-layer`（頂層 `career/` 的結構、形狀邊界、l0 導航、observer 不掃、
  `git mv` 保血緣）、`resume-render-skill`（PEP 723 render 腳本、版本 pin、EN／ZH 單一入口、
  patched theme 驗證、改履歷檢查清單）。
- ADDED delta：`context-registry`（registry 改指 `career/`、移除 Notion）、`architecture-map`
  （`career/` 區塊）、`profile-revamp`（Step 5 指向 `career/star/` 事實層）。
- 形狀切分：state-shaped（`star_materials/` / `rendercv/` / `jira_raw/` / 三份平台文案）搬入 `career/`；
  event-shaped（`target_jobs/`、`headhunter_agent_intro.md`、`platform_strategy.md`、2024-04 舊版 PDF、
  `context/`、`PROJECT.md`）留在專案。
- commit `1d37b8fd`（10 檔、409 行），分支 `feature/add-career-asset-layer` 已 push。

**使用者的兩個決定**（AskUserQuestion）：

- **落點為新頂層 `career/`**（而非 `library/career/` 或 `contexts/career/`）——判準是形狀語義：
  `library/` 是「index card 指向外部 binary 收藏」，35 份 markdown 一手事實放進去會扭曲該層定位；
  `contexts/` 是 event-shaped 且會被 observer 掃。
- **累積流拆成第二個 change**——訊號源（work_logs / Jira 增量 / complete retrospective）本身有分歧，
  不該拖慢搬遷落地。

**收尾方式因此解消**：A（dormant）／B（complete + 手動重建分支說明）皆已否決／部分保留。
新路徑是 `add-career-asset-layer` 落地後乾淨 complete——**改履歷不再經過這個專案**，
撞牆前提消失，B 所需的那份重建說明也不必寫。

### 經驗與觀察

- **「專案要怎麼收尾」問不出答案時，往往是容器選錯了**。17:28 那輪花了整輪查證 `completed` 專案的
  後續編輯路徑（查了 `/ctx:content` Step 4.2、`resume` Step 2、spec 無明文、兩個既有 completed 專案
  零先例、dormant 與 completed 的唯一結構差異），結論卻是「兩條路都有代價」。查證本身沒錯、事實也
  仍然成立，但**問題被框在「這個專案怎麼結束」，而真正的問題是「這些東西為什麼在專案裡」**。
  使用者一句「初衷是建立履歷工具」就換掉了框架。
- **形狀錯置的訊號是「有一份文件專門在解釋怎麼繞過系統」**。`context/TOOLCHAIN.md` §四「情境 B：
  complete 後先手動 `git checkout -b project/resume-refresh main` 重建分支」——當補丁文件出現時，
  該問的是「為什麼需要繞」而不是「繞法對不對」。
- **`registry/` 層的 stale 是靜默的**：`registry/career.md` 指 Notion 指了多久沒人知道，因為沒有任何
  機制會發現「路由指到的地方已經不是 SSOT」。與 `library_index_drift` 這類 audit finding 相比，
  registry 沒有對應的偵測器（axiom `t35` 的形態：沒有 known-positive fixture 的偵測器不存在時，
  「零結果」與「它壞了」外觀相同——這裡連偵測器都沒有）。
- **工具鏈的可攜性缺口被正確記錄卻沒被修**：`TOOLCHAIN.md` 明寫「這是最大可攜性缺口，若要修就在
  `pyproject.toml` 新增 resume group，未修的理由是體積大且只有這個專案用——**這是判斷不是遺漏**」。
  判斷本身合理，但它把選項限縮成「進主 venv 或不修」二選一，漏掉了第三個：PEP 723 inline metadata
  （`personal-skills/README.md` 明文的預設路徑）。**記錄得越清楚的取捨，越少被重新檢視。**

### 下一步

1. `add-career-asset-layer` 走 apply → archive → commit → `/ctx:merge`（已派工獨立 session）
2. 本專案 `resume --merge-main` 帶進 rename，`/ctx:project update` 改材料地圖指針
3. `/ctx:project complete resume-refresh`（含 retrospective）
4. **A′ 投後追問 AICS headcount — 09-09 觸發，距今 2 天**（與架構線平行，不互相阻擋）
WLEOF
wc -l contexts/work_logs/2026-09-07_resume-refresh_update.md`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/5b46aca7-15c4-4978-8e11-40b9792c6b65.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 4
- session: `66ac2345-374b-4a93-b7bb-809233b4adac`
- timestamp: 2026-09-08T18:56:04.682Z
- command: `git checkout -b content/2026-09-09 origin/content/2026-09-09 2>&1 | tail -4`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/66ac2345-374b-4a93-b7bb-809233b4adac.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 5
- session: `a30b1fca-77a2-44c4-a812-2f4b85792d6f`
- timestamp: 2026-09-07T01:21:10.916Z
- command: `git checkout -b content/2026-09-07 main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/a30b1fca-77a2-44c4-a812-2f4b85792d6f.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 6
- session: `e1dd6cf9-f4d9-4ebc-baaf-89f108c3ef3e`
- timestamp: 2026-09-12T13:14:02.801Z
- command: `git branch content/2026-09-12 main`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal/e1dd6cf9-f4d9-4ebc-baaf-89f108c3ef3e.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

### Candidate 7
- session: `bd04b8b4-44ab-4a67-98f1-9607e540ff53`
- timestamp: 2026-09-10T18:03:13.538Z
- command: `git branch content/2026-09-11 main && git branch --list content/2026-09-11`
- has_explicit_base: **True** (✓ has explicit base)
- source: `/Users/dj_workstation/.claude/projects/-Users-dj-workstation-Code-Exocortex-personal--claude-worktrees-exocortex-app/bd04b8b4-44ab-4a67-98f1-9607e540ff53.jsonl`

- [ ] approve — 送 LLM judge
- [ ] skip — false positive
- [ ] manual_violation — 人標 confirmed violation,跳過 LLM
- [ ] manual_compliance — 人標 follow,跳過 LLM

