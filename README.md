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
| 1. 物理 repo 隔絕 | 本 repo 不在 `~/Documents/Projects/Exocortex-personal/` 內，不是 submodule / subtree / 內含目錄 |
| 2. Reflector scan whitelist | Exocortex reflector 的 `KNOWLEDGE_BASE.md` § 2 source path whitelist SHALL NOT 包含本 repo 任何路徑 |
| 3. Exocortex 內檔案 cite ban | 任何 reflector 可讀檔案（`rules/`、`contexts/`、`inbox/`、`memory/`）SHALL NOT 引用本 repo 路徑作為 evaluation 結論的 cite source。例外：`memory/reference_evaluation_repo.md`、`infra/periodic_jobs/CRONTAB.md` 可記錄 path string，但不含結論 |

**為什麼三層而非一層**：信任根基不應在「reflector 程式碼不漏 ignore logic」。物理隔絕讓「可能誤掃」這個 surface 都消失。

## 目錄結構

```
axioms/        每條 axiom 一份 evaluation card（<id>.md）
digests/       週月整理（依需求新增）
tools/         觀測 script
  scan_axiom_usage.py      Stage 1：純 grep candidate
  render_review_dashboard  Stage 2 a：candidates.json → markdown checklist
  parse_human_review.py    Stage 2 b：reviewed markdown → human_review.json
  llm_judge.py             Stage 3：human_review.json → axiom card（human-triggered）
data/          各次 scan 的 raw + reviewed snapshot
  <date>_candidates.json
  <date>_human_review.json
dashboards/    HTML / markdown 報表
  <date>_candidates.md
  <date>_axiom_status.html
```

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

## Axiom card schema

詳見 `axioms/_schema.md`（本 repo 自治；schema 演化不需要 Exocortex spec migration）。

## 跨機 setup

```bash
# 1. Clone
cd ~/Documents/Projects
git clone git@github.com:Hangghost/exocortex-evaluation.git

# 2. 在 Exocortex repo 註冊 cron（僅 schedule，script 在本 repo）
# crontab -e 新增（如 CRONTAB.md 描述）
# 0 21 * * 0  test -d ~/Documents/Projects/exocortex-evaluation && cd ~/Documents/Projects/exocortex-evaluation && python tools/scan_axiom_usage.py --axiom a09 --days 7

# 3. 確認 Python 標準庫足夠（Stage 1/2 純標準庫，Stage 3 LLM 才需 anthropic SDK，本階段 a09 試點不啟用）
python3 --version  # 3.10+
```

## 已知 limitation

Self-fulfilling bias 仍存在——rule 注入會改變 agent 行為，grep 看到更多 follow 不能 prove rule works。**Repo 隔絕只解決「evaluation 結論不形成新 feedback loop」，不消除「行為被 rule 改變」這個事實**。長期可擴展到跨 repo external corpus 對照，目前 scope 內不處理。
