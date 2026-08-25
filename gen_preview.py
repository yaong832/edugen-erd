"""README.md의 Mermaid 블록을 읽어 preview/er-preview.html 생성."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
README = HERE / "README.md"
OUT_DIR = HERE / "preview"
OUT_HTML = OUT_DIR / "er-preview.html"


def main() -> None:
    text = README.read_text(encoding="utf-8")
    blocks = re.findall(r"```mermaid\n(.*?)```", text, re.DOTALL)
    if len(blocks) < 2:
        raise SystemExit(f"Mermaid 블록이 2개 미만입니다 (찾음: {len(blocks)})")
    full_mmd, summary_mmd = blocks[0].strip(), blocks[1].strip()

    full_js = json.dumps(full_mmd, ensure_ascii=False)
    summary_js = json.dumps(summary_mmd, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>erD ER 미리보기</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 1rem 1.5rem 3rem; background: #f6f8fa; }}
    h1 {{ font-size: 1.25rem; margin-top: 2rem; }}
    h1:first-of-type {{ margin-top: 0; }}
    .box {{ background: #fff; border: 1px solid #d0d7de; border-radius: 8px; padding: 1rem; overflow: auto; }}
    .err {{ color: #cf222e; white-space: pre-wrap; }}
    p.note {{ color: #57606a; font-size: 0.9rem; }}
  </style>
</head>
<body>
  <p class="note">로컬 파일입니다. 인터넷이 있어야 Mermaid CDN을 불러옵니다. 브라우저에서 이 파일을 열면 됩니다.</p>
  <h1>전체 ER (상세)</h1>
  <div class="box" id="full"></div>
  <h1>발표용 ER (축약)</h1>
  <div class="box" id="summary"></div>
  <script>
    (async function () {{
      mermaid.initialize({{ startOnLoad: false, securityLevel: "loose" }});
      const full = {full_js};
      const summary = {summary_js};
      async function render(id, source, mount) {{
        const el = document.getElementById(mount);
        try {{
          const {{ svg }} = await mermaid.render(id + "-" + Math.random().toString(36).slice(2), source);
          el.innerHTML = svg;
        }} catch (e) {{
          el.innerHTML = '<div class="err">' + (e && e.message ? e.message : String(e)) + '</div>';
        }}
      }}
      await render("full", full, "full");
      await render("sum", summary, "summary");
    }})();
  </script>
</body>
</html>
"""

    OUT_DIR.mkdir(exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    print("Wrote", OUT_HTML)


if __name__ == "__main__":
    main()
