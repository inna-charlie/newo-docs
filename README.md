# Newo Platform Documentation (RAG test site)

A static site built from the public-safe "Newo Platform Documentation" guide. Its purpose is to test retrieval (RAG) over a public docs site.

- `docs/`: the published site (GitHub Pages serves this folder)
  - 9 HTML pages, one per chapter, with an anchor id on every section heading
  - `newo-platform-documentation.md`: the whole guide as one Markdown file
  - `llms.txt`: a page index for LLM crawlers
  - `chunks.json`: a list of every section with its page and anchor, which can serve as ground truth for retrieval tests
- `source.md`: the guide exported from the doc
- `build.py`: regenerates `docs/` from `source.md` (`python3 build.py`)
- `site.css`: site styles, layered on the Newo `tokens.css`

Every page carries `noindex, nofollow`, so search engines leave it out while your own crawler can still fetch it. To let search engines index the site, remove that meta tag in `build.py`.

Fonts: Manrope is shipped under the SIL OFL (license in `docs/fonts/`). General Sans is deliberately not included, because its license does not allow redistribution outside Newo.

## Publish to GitHub Pages

1. Create an empty repository on GitHub, for example `newo-docs`.
2. Push this folder:
   ```bash
   git remote add origin https://github.com/<your-username>/newo-docs.git
   git push -u origin main
   ```
3. In the repository, go to Settings → Pages. Choose **Deploy from a branch**, then branch `main` and folder `/docs`.
4. The site appears at `https://<your-username>.github.io/newo-docs/` after about a minute.
