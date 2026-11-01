"""Build the Newo docs static site from source.md into ./docs (GitHub Pages folder)."""
import html, re, shutil, json
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
DS = Path("/Users/innacharlie/Library/Application Support/Claude/local-agent-mode-sessions/"
          "a9ae9e89-97ec-4daa-9fed-cd1dc57a3902/598c9057-bf9a-4015-b063-2e11c551b143/rpm/"
          "plugin_015BgnYL7sF7TZZPRFJUcdeH/design-system")

# Chapter heading in source.md -> (slug, nav label)
PAGES = {
    "Overview": ("index", "Overview"),
    "Getting started": ("getting-started", "Getting started"),
    "Voice and telephony": ("voice", "Voice"),
    "Billing": ("billing", "Billing"),
    "Reliability, support and security": ("security", "Reliability & security"),
    "Agents, integrations and partners": ("agents", "Agents & integrations"),
    "Frequently asked questions": ("faq", "FAQ"),
    "Glossary": ("glossary", "Glossary"),
    "About this guide": ("about", "About"),
}

CALL_PATH = """<figure class="flow" aria-label="How a voice call reaches a Newo agent">
<ol>
<li><strong>Caller</strong><span>Phone, web browser or contact-center platform</span></li>
<li><strong>Provider services</strong><span>Newo numbers, SIP provider or WebSocket audio stream the call audio</span></li>
<li><strong>Voice Service</strong><span>Listens, detects turns and speaks replies in real time</span></li>
<li><strong>AI models and the Newo platform</strong><span>Speech models plus the agent's flows, skills and integrations</span></li>
</ol>
<figcaption>Call path: every connection type streams audio to Voice Service. A backup provider can take over during an outage.</figcaption>
</figure>"""


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def inline(s):
    s = html.escape(s, quote=False).replace("&amp;#91;", "[")
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return s


def md_to_html(md):
    """Small converter for the subset the doc uses: h3, paragraphs, lists, task lists, tables."""
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
        elif ln.startswith("&#91;embedded content") or ln.startswith("[embedded content"):
            out.append(CALL_PATH); i += 1
        elif ln.startswith("### "):
            t = ln[4:].strip()
            out.append(f'<h3 id="{slugify(t)}"><a href="#{slugify(t)}">{inline(t)}</a></h3>'); i += 1
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            head, body = rows[0], rows[2:]
            t = "<div class=\"table\"><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in body:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table></div>")
        elif re.match(r"^(\d+\.|-) ", ln):
            ordered = ln[0].isdigit()
            items = []
            while i < len(lines) and re.match(r"^(\d+\.|-) ", lines[i]):
                items.append(re.sub(r"^(\d+\.|-) ", "", lines[i])); i += 1
            if all(x.startswith("[ ] ") for x in items):
                lis = "".join(f'<li><span class="box" aria-hidden="true"></span>{inline(x[4:])}</li>' for x in items)
                out.append(f'<ul class="checklist">{lis}</ul>')
            else:
                tag = "ol" if ordered else "ul"
                out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(###|\||\d+\. |- )", lines[i]):
                para.append(lines[i]); i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def parse(src):
    chapters, cur = [], None
    for ln in src.split("\n"):
        if ln.startswith("## "):
            cur = {"title": ln[3:].strip(), "md": []}; chapters.append(cur)
        elif cur is not None:
            cur["md"].append(ln)
    for c in chapters:
        c["md"] = "\n".join(c["md"]).strip()
        c["slug"], c["nav"] = PAGES[c["title"]]
        c["subs"] = re.findall(r"^### (.+)$", c["md"], re.M)
        first = next((p for p in c["md"].split("\n\n") if p and not p.startswith(("#", "|", "-", "1."))), "")
        c["desc"] = re.sub(r"\*\*", "", first)[:155]
    return chapters


LOGO = (DS / "assets/newo-logo.svg").read_text()
LOGO = re.sub(r"<!--.*?-->", "", LOGO, flags=re.S).replace('aria-label="newo"', 'aria-label="newo" class="logo"')


def page(c, chapters):
    nav = "".join(
        f'<li><a href="{x["slug"] if x["slug"] != "index" else "./"}{".html" if x["slug"] != "index" else ""}"'
        f'{" aria-current=page" if x is c else ""}>{x["nav"]}</a></li>' for x in chapters)
    toc = "".join(f'<li><a href="#{slugify(s)}">{inline(s)}</a></li>' for s in c["subs"])
    idx = chapters.index(c)
    prev_ = chapters[idx - 1] if idx else None
    next_ = chapters[idx + 1] if idx + 1 < len(chapters) else None
    href = lambda x: "./" if x["slug"] == "index" else f'{x["slug"]}.html'
    pager = '<nav class="pager" aria-label="Chapters">'
    pager += f'<a class="btn btn--white" href="{href(prev_)}">← {prev_["title"]}</a>' if prev_ else "<span></span>"
    pager += f'<a class="btn btn--filled" href="{href(next_)}">{next_["title"]} →</a>' if next_ else ""
    pager += "</nav>"
    eyebrow = "Newo Platform Documentation"
    h1 = "Newo Platform Documentation" if c["slug"] == "index" else c["title"]
    lead = "How the Newo platform answers calls, bills usage, stays secure and connects to your business." if c["slug"] == "index" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c['title']} · Newo Platform Documentation</title>
<meta name="description" content="{html.escape(c['desc'])}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="assets/newo-icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topnav">
  <a class="brand" href="./" aria-label="Newo docs home">{LOGO}<span>Docs</span></a>
  <button class="menu btn btn--white btn--sm" aria-expanded="false" aria-controls="chapters">Menu</button>
  <nav id="chapters" aria-label="Chapters"><ul>{nav}</ul></nav>
</header>
<div class="layout">
  <aside class="toc" aria-label="On this page">{('<p class="t-eyebrow">On this page</p><ul>' + toc + '</ul>') if toc else ''}</aside>
  <main id="main">
    <article data-chapter="{c['slug']}">
      <p class="t-eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      {f'<p class="lead">{lead}</p>' if lead else ''}
      {md_to_html(c['md'])}
    </article>
    {pager}
  </main>
</div>
<footer class="foot">
  <p class="foot__head">Questions about the Newo platform?</p>
  <p>Contact Newo support or your partner.</p>
  <p class="foot__meta">Describes the Newo platform as of 1 November 2026. Details may change.</p>
</footer>
<script>
const b=document.querySelector('.menu'),n=document.getElementById('chapters');
b.addEventListener('click',()=>{{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>
"""


def main():
    src = (ROOT / "source.md").read_text()
    src = re.sub(r"^Nov 1, 2026 · @.*\n", "", src, flags=re.M)  # drop personal byline
    chapters = parse(src)
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "fonts").mkdir()
    shutil.copy(DS / "tokens.css", OUT / "tokens.css")
    # Manrope only (SIL OFL allows redistribution); General Sans' license forbids passing it outside Newo.
    shutil.copy(DS / "fonts/Manrope-Variable.woff2", OUT / "fonts")
    shutil.copy(DS / "fonts/LICENSE-Manrope-OFL.txt", OUT / "fonts")
    shutil.copy(DS / "assets/newo-icon.svg", OUT / "assets")
    shutil.copy(ROOT / "site.css", OUT / "site.css")
    for c in chapters:
        (OUT / f"{c['slug']}.html").write_text(page(c, chapters))
    # Plain-text copies for RAG ingestion
    clean = re.sub(r"^&#91;embedded content.*$",
                   "Call path: Caller → provider services (Newo numbers, SIP provider, WebSocket audio) → Voice Service → AI models and the Newo platform.",
                   src, flags=re.M)
    (OUT / "newo-platform-documentation.md").write_text(clean)
    llms = "# Newo Platform Documentation\n\n> Public guide to the Newo platform: voice, billing, security, agents and integrations.\n\n## Pages\n\n"
    llms += "".join(f"- [{c['title']}]({c['slug']}.html): {c['desc']}\n" for c in chapters)
    llms += "\n## Full text\n\n- [Complete guide as Markdown](newo-platform-documentation.md)\n"
    (OUT / "llms.txt").write_text(llms)
    (OUT / "chunks.json").write_text(json.dumps([
        {"page": f"{c['slug']}.html", "chapter": c["title"], "section": s,
         "anchor": f"{c['slug']}.html#{slugify(s)}"} for c in chapters for s in c["subs"]], indent=1))
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    print("built", len(chapters), "pages,", sum(len(c["subs"]) for c in chapters), "sections")


if __name__ == "__main__":
    main()
