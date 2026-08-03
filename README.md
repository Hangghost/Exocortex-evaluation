# exocortex-evaluation

Exocortex self-evolution loop 第四階段（Evaluation）的觀測資料倉。

與 [Exocortex-personal](https://github.com/Hangghost/exocortex-personal) 分離，**reflector 物理隔絕看不到本 repo 任何內容**。

## 為什麼存在

Exocortex 已有 Capture / Promote / Inject 三階段：
- Observer (daily) → raw signals
- Reflector (weekly) → axioms / SKILL / SOUL.md
- Session inject → CORE.md + axioms

第四階段 Evaluation 從未存在：規則注入後沒有任何機制驗證「axiom 真的改變了 agent 行為嗎？在哪裡作用？多久觸發一次？」。本 repo 補這層。

詳見 Exocortex `openspec/specs/axiom-evaluation-pipeline/spec.md`（架構契約由 Exocortex 主 spec 規範；本 repo 內部 schema 自治）。

## Reflector blind 三層保護約束

| Layer | 保護內容 |
|---|---|
| 1. 物理 repo 隔絕 | 本 repo 不在 Exocortex-personal repo 內，不是 submodule / subtree / 內含目錄 |
| 2. Reflector scan whitelist | Exocortex reflector 的 `KNOWLEDGE_BASE.md` § 2 source path whitelist SHALL NOT 包含本 repo 任何路徑 |
| 3. Exocortex 內檔案 cite ban | 任何 reflector 可讀檔案（`rules/`、`contexts/`、`inbox/`、`memory/`）SHALL NOT 引用本 repo 路徑作為 evaluation 結論的 cite source。例外：`memory/reference_evaluation_repo.md`、`infra/periodic_jobs/SCHEDULE.md` 可記錄 path string，但不含結論 |

**為什麼三層而非一層**：信任根基不應在「reflector 程式碼不漏 ignore logic」。物理隔絕讓「可能誤掃」這個 surface 都消失。

## 目錄結構

```
axioms/        每條 axiom 一份 evaluation card（<id>.md）
digests/       週月整理（依需求新增）
tools/         觀測 script
  transcript_source.py     共用：transcript 目錄枚舉 + fail-loud 契約
  scan_axiom_usage.py      Stage 1：per-axiom compliance（純 grep candidate）
  scan_axiom_reads.py      Stage 1：全 axiom read-frequency（無需 per-axiom 設定）
  render_review_dashboard  Stage 2 a：candidates.json → markdown checklist
  parse_human_review.py    Stage 2 b：reviewed markdown → human_review.json
  llm_judge.py             Stage 3：human_review.json → axiom card（human-triggered）
data/          各次 scan 的 raw + reviewed snapshot
  <date>_candidates.json
  <date>_human_review.json
  <date>_read_frequency.json
dashboards/    HTML / markdown 報表
  <date>_candidates.md
  <date>_axiom_status.html
```

**`data/` 產出採人工入版控**：scanner **不執行任何 git 操作**。讓週跑的排程角色動 git 會在排程期間引入 repo 狀態競爭，而產出頻率是週級、人工 commit 成本可忽略。定期把 `data/` 新產出納入版控即可。

## 3-Stage Pipeline

```
Stage 1 (auto, cron, free)
  tools/scan_axiom_usage.py
    └─ output: data/<date>_candidates.json

         ↓ (檔案接力)

Stage 2 (human, MANDATORY gate)
  edit dashboards/<date>_candidates.md
    └─ tools/parse_human_review.py
       └─ output: data/<date>_human_review.json

         ↓ (Stage 3 預檢此檔存在,否則 abort)

Stage 3 (human-triggered, LLM)
  tools/llm_judge.py
    └─ output: axioms/<id>.md (evaluation card updated)
```

**Stage 2 是強制 gate**：Stage 3 不存在 human_review.json 直接 abort，cron 永遠不會 auto-burn token。

## 兩種指標並列（compliance vs read-frequency）

Stage 1 有兩支 scanner，量的是不同的東西，**不互相取代**：

| | `scan_axiom_usage.py`（compliance） | `scan_axiom_reads.py`（read-frequency） |
|---|---|---|
| 問題 | 行為有沒有符合這條規則？ | 這條規則有沒有進到 agent 眼前？ |
| 覆蓋 | 需 per-axiom grep pattern，僅 command-shaped axiom 可行 | 全部 axiom，零 per-axiom 設定 |
| 因果宣稱 | 有（且因此易被汙染） | 無（只報 presence） |
| Human gate | Stage 2 必經（下游接 Stage 3 LLM） | 不適用（零 LLM，產出直接可讀） |

**為什麼需要第二種**：a09 首輪 compliance 是 88.7%，但 2026-08-02 量測顯示該 axiom 在 926 個 session 中被讀取 **0 次**——那個 compliance 其實來自 `/ctx:arch` 命令散文裡明寫的 `git checkout -b <name> main`，與 axiom 本體無因果關係。compliance 單獨看會把「別處的 enforcement」記在 axiom 頭上。

兩者交叉判讀：

- read-freq 高 + compliance 高 → 規則可能真的在起作用
- read-freq 為 0 + compliance 高 → 效果來自別處，axiom 本體是**退役候選**
- read-freq 為 0 + 無其他來源 → 死重量

**排序依賴**：read-frequency 在 Exocortex 的 injection 層修好之前恆為接近 0（axiom index 進 `rules/CORE.md` 必讀清單之前，agent 幾乎不會主動去讀）。2026-08-02 基準：6/928 session（0.6%）、53 條中 46 條零讀取。

## Fail-loud 契約

兩支 scanner 在**環境缺失**（transcript 根目錄不存在、`--exocortex-root` 指錯、找不到 axiom registry）時 SHALL 以非零 exit code 結束、**且不寫出產出檔**。

「環境壞了」與「掃描成功但確實沒有結果」不可共用同一個沉默空值回傳。2026-06-07 主 repo 從 `~/Documents` 搬到 `~/Code` 後，舊版 scanner 印一行 warn 就 `exit 0` 並照常寫空 JSON，導致連續 8 週靜默失效無人察覺。

此契約也是外部監控得以成立的前提：因為失敗時不寫檔，「`data/` 最新產出檔過舊」就等價於「沒跑或跑失敗」，Exocortex 端的 `state_audit` 只需 stat 檔案 mtime 即可判斷死活，**不需要讀取檔案內容**（讀 candidate 計數會洩漏評估結論，違反 reflector blind 第三層）。

`--exocortex-root` **為必填、無 default**：硬編碼的路徑 default 是排程層樣板置換管不到的環境假設，正是上述失效的根因。plist 透過 `__REPO_ROOT__` 顯式傳入。

## Transcript 掃描範圍

兩支 scanner 共用 `tools/transcript_source.py` 的目錄枚舉：主 checkout 的 encoded 目錄 **加上全部 `.claude/worktrees/*`** 各自的目錄。

background session 一律在 worktree 內執行，其 transcript 落在獨立的 encoded 目錄。舊版只解析主 checkout 單一目錄，2026-08-02 實測漏掉 295/926（**32%**）的 session——此盲區自始存在，與 repo 搬遷無關。產出檔的 `scanned_dirs` 欄位記錄實際掃描範圍，使新舊口徑的歷史資料可辨識（早於 2026-08 的產出無此欄位，數值系統性偏低，不可與新資料直接比較）。

## Axiom card schema

詳見 `axioms/_schema.md`（本 repo 自治；schema 演化不需要 Exocortex spec migration）。

## 跨機 setup

```bash
# 1. Clone
cd ~/Code
git clone git@github.com:Hangghost/exocortex-evaluation.git

# 2. 建本地 venv（即使 tools 純標準庫也需要）
# 理由：macOS TCC 會擋 /usr/bin/python3 從 launchd user-context 讀使用者目錄，
# user-owned venv binary 不受此限。詳見 Exocortex 2026-05-26 incident 紀錄。
cd ~/Code/exocortex-evaluation
python3 -m venv .venv

# 3. 在 Exocortex repo 註冊 LaunchAgent（plist 內 Python path 指向本 repo .venv）
# 見 Exocortex infra/periodic_jobs/launch_agents/be.keepthinking.axiom_eval_scan.plist
# install.sh 會自動處理；新機器跑一次即可
```

## 已知 limitation

Self-fulfilling bias 仍存在——rule 注入會改變 agent 行為，grep 看到更多 follow 不能 prove rule works。**Repo 隔絕只解決「evaluation 結論不形成新 feedback loop」，不消除「行為被 rule 改變」這個事實**。長期可擴展到跨 repo external corpus 對照，目前 scope 內不處理。
