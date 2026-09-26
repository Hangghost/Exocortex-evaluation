#!/usr/bin/env python3
"""Stage 2a (visual) — render pending candidates.json batches into ONE self-contained
HTML review page.

Alternative to the markdown checklist (`render_review_dashboard.py` +
`parse_human_review.py`); both paths end in the same `data/<date>_human_review.json`.
The page is zero-dependency (file://, offline, no server) so it can be copied to any
machine; choices live in that browser's localStorage and leave via "Export JSON",
which `import_review_json.py` turns into human_review.json files.

Pending batch = `data/<date>_candidates.json` with ≥1 candidate, no
`data/<date>_human_review.json`, and not registered in `data/DATA_GAPS.md` (the same
first-column-date rule Exocortex `state_audit` uses to exclude blind-window batches).

Pure stdlib (Python 3.10).
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = "axiom-eval-review/v1"
STATUSES = [
    # (key, label, hint, keyboard)
    ("approve", "approve", "送 LLM judge", "1"),
    ("skip", "skip", "false positive", "2"),
    ("manual_violation", "manual violation", "人標 confirmed violation，跳過 LLM", "3"),
    ("manual_compliance", "manual compliance", "人標 follow，跳過 LLM", "4"),
]
_GAP_ROW_RE = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.MULTILINE)


def gap_dates(data_dir: Path) -> set[str]:
    p = data_dir / "DATA_GAPS.md"
    return set(_GAP_ROW_RE.findall(p.read_text(encoding="utf-8"))) if p.is_file() else set()


def pending_batches(data_dir: Path) -> list[dict]:
    gaps = gap_dates(data_dir)
    out = []
    for f in sorted(data_dir.glob("*_candidates.json")):
        label = f.name[: -len("_candidates.json")]
        if label in gaps or (data_dir / f"{label}_human_review.json").exists():
            continue
        payload = json.loads(f.read_text(encoding="utf-8"))
        if payload.get("candidates"):
            out.append({"label": label, **payload})
    return out


def _js(value: object) -> str:
    """JSON safe to embed in <script> (no `</script>` break-out, no U+2028 issues)."""
    s = json.dumps(value, ensure_ascii=False)
    return s.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026") \
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def render(batches: list[dict], *, generated_on: str) -> str:
    data = [
        {
            "label": b["label"],
            "axiom_id": b["axiom_id"],
            "scan_date": b["scan_date"],
            "window_days": b.get("window_days"),
            "candidates": [
                {
                    "command": c.get("command", ""),
                    "timestamp": c.get("timestamp", ""),
                    "session_id": c.get("session_id", ""),
                    "source_path": c.get("source_path", ""),
                    "has_explicit_base": bool(c.get("has_explicit_base")),
                    "potential_violation": bool(c.get("potential_violation")),
                }
                for c in b["candidates"]
            ],
        }
        for b in batches
    ]
    statuses = [{"key": k, "label": l, "hint": h, "kbd": kb} for k, l, h, kb in STATUSES]
    total = sum(len(b["candidates"]) for b in data)
    title = f"Axiom evaluation Stage 2 審閱（{len(data)} 批、{total} 個候選）"
    return (
        "<!doctype html>\n<html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{html.escape(title)}</title>\n<style>{_CSS}</style></head><body>\n"
        f"<header><h1>{html.escape(title)}</h1>"
        f"<div class=\"sub\">產生於 {html.escape(generated_on)} · 選擇存在<b>這台機器、這個瀏覽器</b>的 "
        "localStorage，換機器不會帶著走——在標記的那台按 Export。"
        "鍵盤：<kbd>1</kbd>–<kbd>4</kbd> 標記目前卡片並跳到下一個未標，<kbd>j</kbd>/<kbd>k</kbd> 上下移動。</div>"
        "<div class=\"bar\"><select id=\"fb\"></select>"
        "<select id=\"fs\"><option value=\"\">全部</option><option value=\"todo\">只看未標</option>"
        "<option value=\"done\">只看已標</option></select>"
        "<label class=\"chk\"><input type=\"checkbox\" id=\"fv\"> 只看 ⚠ potential violation</label>"
        "<button class=\"primary\" id=\"exp\">Export JSON</button></div>"
        "<div class=\"progress\"><div id=\"pbar\"></div></div><div id=\"batches\"></div></header>\n"
        "<main id=\"list\"></main>\n<script>\n"
        f"var DATA={_js(data)};\nvar STATUSES={_js(statuses)};\n"
        f"var SCHEMA={_js(SCHEMA)};\nvar GENERATED_ON={_js(generated_on)};\n"
        f"var KEY={_js('axiom_eval_review:' + generated_on)};\n{_JS}\n</script></body></html>\n"
    )


_CSS = """
:root{--bg:#f7f7f5;--card:#fff;--fg:#1d1d1f;--mut:#6b6b70;--line:#e3e3e0;--acc:#2f5bd3;
--warn:#b4461e;--warnbg:#fbe9e2;--ok:#2d7a46;--okbg:#e3f3e8;--sel:#eef2fd;--code:#f2f2ef;
--s-approve:#2f5bd3;--s-skip:#6b6b70;--s-manual_violation:#b4461e;--s-manual_compliance:#2d7a46}
@media (prefers-color-scheme: dark){:root{--bg:#161618;--card:#1f1f22;--fg:#ececef;--mut:#a0a0a8;
--line:#333338;--acc:#7f9cf0;--warn:#f08a62;--warnbg:#3a241c;--ok:#6fc98c;--okbg:#1c3324;--sel:#232a3d;
--code:#27272b;--s-approve:#7f9cf0;--s-skip:#a0a0a8;--s-manual_violation:#f08a62;--s-manual_compliance:#6fc98c}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.5 -apple-system,BlinkMacSystemFont,"PingFang TC","Noto Sans TC",sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--bg);padding:16px 16px 8px;border-bottom:1px solid var(--line)}
h1{font-size:18px;margin:0 0 4px}.sub{color:var(--mut);font-size:13px}
kbd{font:12px ui-monospace,Menlo,monospace;border:1px solid var(--line);border-radius:4px;padding:0 4px;background:var(--card)}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0 8px}
select,button{font:inherit;font-size:14px;padding:5px 10px;border:1px solid var(--line);border-radius:8px;
background:var(--card);color:var(--fg);cursor:pointer}
.chk{font-size:14px;color:var(--mut);display:flex;gap:4px;align-items:center}
button.primary{margin-left:auto;background:var(--acc);border-color:var(--acc);color:#fff}
.progress{height:6px;background:var(--line);border-radius:3px;overflow:hidden}
#pbar{height:100%;width:0;background:var(--acc);transition:width .2s}
#batches{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.pill{font-size:12px;padding:2px 8px;border-radius:999px;border:1px solid var(--line);color:var(--mut);cursor:pointer}
.pill.full{border-color:var(--ok);color:var(--ok)}
main{max-width:980px;margin:0 auto;padding:12px 16px 80px}
.card{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--line);
border-radius:10px;padding:12px 14px;margin:10px 0}
.card.focus{outline:2px solid var(--acc);outline-offset:1px}
.card.decided{opacity:.72}
.head{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:13px;color:var(--mut)}
.idx{font-weight:600;color:var(--fg)}
.chip{font-size:12px;padding:1px 8px;border-radius:999px;background:var(--code)}
.chip.warn{background:var(--warnbg);color:var(--warn)}.chip.ok{background:var(--okbg);color:var(--ok)}
pre{margin:8px 0;padding:10px;background:var(--code);border-radius:8px;white-space:pre-wrap;
word-break:break-word;font:13px/1.45 ui-monospace,Menlo,monospace}
.meta{font-size:12px;color:var(--mut);word-break:break-all}
.acts{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.acts button{flex:1 1 150px;text-align:left}
.acts button small{display:block;color:var(--mut);font-size:11px}
.acts button.on{color:#fff;border-color:transparent}
.empty{color:var(--mut);text-align:center;padding:40px}
@media (max-width:600px){button.primary{margin-left:0}}
"""

_JS = r"""
var $=function(id){return document.getElementById(id)};
var state={};
try{state=JSON.parse(localStorage.getItem(KEY)||"{}")||{}}catch(e){state={}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}
var ROWS=[];DATA.forEach(function(b){b.candidates.forEach(function(c,i){
  ROWS.push({b:b,c:c,n:i+1,key:b.label+"#"+(i+1)})})});
var focusKey=null;
function esc(s){return String(s).replace(/[&<>"]/g,function(ch){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[ch]})}
function color(k){return "var(--s-"+k+")"}
function visible(){var fb=$("fb").value,fs=$("fs").value,fv=$("fv").checked;
  return ROWS.filter(function(r){if(fb&&r.b.label!==fb)return false;
    if(fs==="todo"&&state[r.key])return false;if(fs==="done"&&!state[r.key])return false;
    if(fv&&!r.c.potential_violation)return false;return true})}
function header(){var done=ROWS.filter(function(r){return state[r.key]}).length;
  $("pbar").style.width=(ROWS.length?100*done/ROWS.length:0)+"%";
  var h=['<span class="pill" data-b="">全部 '+done+'/'+ROWS.length+'</span>'];
  DATA.forEach(function(b){var d=b.candidates.filter(function(c,i){return state[b.label+"#"+(i+1)]}).length;
    h.push('<span class="pill'+(d===b.candidates.length?' full':'')+'" data-b="'+esc(b.label)+'">'+esc(b.label)+' · '+esc(b.axiom_id)+' '+d+'/'+b.candidates.length+'</span>')});
  $("batches").innerHTML=h.join("");
  Array.prototype.forEach.call(document.querySelectorAll(".pill"),function(p){p.onclick=function(){$("fb").value=p.dataset.b;render()}})}
function render(){header();var rows=visible();
  if(!rows.length){$("list").innerHTML='<div class="empty">這個篩選條件下沒有候選。</div>';return}
  if(!rows.some(function(r){return r.key===focusKey}))focusKey=rows[0].key;
  $("list").innerHTML=rows.map(function(r){var s=state[r.key],c=r.c;
    var flag=c.potential_violation?'<span class="chip warn">⚠ potential violation</span>':'<span class="chip ok">✓ has explicit base</span>';
    var acts=STATUSES.map(function(st){var on=s===st.key;
      return '<button data-k="'+esc(r.key)+'" data-s="'+st.key+'" class="'+(on?'on':'')+'" style="'+(on?'background:'+color(st.key):'')+'">'
        +'<kbd>'+st.kbd+'</kbd> '+esc(st.label)+'<small>'+esc(st.hint)+'</small></button>'}).join("");
    return '<div class="card'+(s?' decided':'')+(r.key===focusKey?' focus':'')+'" id="c-'+esc(r.key)+'" style="border-left-color:'+(s?color(s):'var(--line)')+'">'
      +'<div class="head"><span class="idx">#'+r.n+'</span><span class="chip">'+esc(r.b.label)+' · '+esc(r.b.axiom_id)+'</span>'+flag
      +'<span>'+esc(c.timestamp)+'</span></div>'
      +'<pre>'+esc(c.command)+'</pre>'
      +'<div class="meta">session '+esc(c.session_id)+' · '+esc(c.source_path)+'</div>'
      +'<div class="acts">'+acts+'</div></div>'}).join("");
  Array.prototype.forEach.call(document.querySelectorAll(".acts button"),function(bt){
    bt.onclick=function(){choose(bt.dataset.k,bt.dataset.s)}});
  Array.prototype.forEach.call(document.querySelectorAll(".card"),function(el){
    el.onmousedown=function(){focusKey=el.id.slice(2);mark()}})}
function mark(){Array.prototype.forEach.call(document.querySelectorAll(".card"),function(el){
  el.classList.toggle("focus",el.id==="c-"+focusKey)})}
function choose(key,st){state[key]=(state[key]===st?undefined:st);if(!state[key])delete state[key];save();
  var rows=visible(),i=rows.findIndex(function(r){return r.key===key});
  var next=rows.slice(i+1).concat(rows.slice(0,i)).find(function(r){return !state[r.key]});
  if(state[key]&&next)focusKey=next.key;render();scrollToFocus()}
function scrollToFocus(){var el=$("c-"+focusKey);if(el)el.scrollIntoView({block:"center",behavior:"smooth"})}
function move(d){var rows=visible(),i=rows.findIndex(function(r){return r.key===focusKey});
  var j=Math.max(0,Math.min(rows.length-1,i+d));if(rows[j]){focusKey=rows[j].key;mark();scrollToFocus()}}
document.addEventListener("keydown",function(e){if(e.target.tagName==="SELECT"||e.metaKey||e.ctrlKey||e.altKey)return;
  var st=STATUSES.find(function(s){return s.kbd===e.key});
  if(st&&focusKey){e.preventDefault();choose(focusKey,st.key)}
  else if(e.key==="j"){move(1)}else if(e.key==="k"){move(-1)}});
function doExport(){var batches={};DATA.forEach(function(b){var dec=[];
    b.candidates.forEach(function(c,i){var s=state[b.label+"#"+(i+1)];if(s)dec.push({candidate_index:i+1,status:s})});
    batches[b.label]={axiom_id:b.axiom_id,count:b.candidates.length,decisions:dec}});
  var doc={schema:SCHEMA,generated_on:GENERATED_ON,exported_at:new Date().toISOString(),batches:batches};
  var blob=new Blob([JSON.stringify(doc,null,2)],{type:"application/json"});
  var a=document.createElement("a");a.href=URL.createObjectURL(blob);
  a.download="axiom_eval_review_"+GENERATED_ON+".json";document.body.appendChild(a);a.click();a.remove()}
$("fb").innerHTML='<option value="">全部批次</option>'+DATA.map(function(b){
  return '<option value="'+esc(b.label)+'">'+esc(b.label)+' · '+esc(b.axiom_id)+'（'+b.candidates.length+'）</option>'}).join("");
["fb","fs","fv"].forEach(function(id){$(id).addEventListener("change",render)});
$("exp").onclick=doExport;render();
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data-dir", type=Path, default=ROOT / "data")
    ap.add_argument("--out", type=Path, help="default: dashboards/review_<today>.html")
    ap.add_argument("--date", action="append", dest="dates", help="只收這些批次（可重複）；預設全部待審")
    ap.add_argument("--generated-on", default=date.today().isoformat())
    args = ap.parse_args()

    batches = pending_batches(args.data_dir)
    if args.dates:
        want = set(args.dates)
        batches = [b for b in batches if b["label"] in want]
    if not batches:
        print("沒有待審批次（皆已審、皆為空、或登記於 DATA_GAPS.md）")
        return 0
    out = args.out or ROOT / "dashboards" / f"review_{args.generated_on}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(batches, generated_on=args.generated_on), encoding="utf-8")
    # Batch count only: candidate counts are shown on the page itself, not echoed to
    # a terminal whose session may belong to the Exocortex side of the reflector wall.
    print(f"wrote {out}（{len(batches)} 批）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
