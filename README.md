# Modrinth's AI policy, applied twice

A single static page documenting one submission refused under Modrinth's AI policy (Content Rules §6.2b
for content and §6.2a for the icon), set against seventeen public projects that disclose the same or
heavier AI use and were approved after the policy's grace period ended on 27 September 2026.

Independent; not affiliated with or endorsed by Modrinth. No moderators are named.

## Check it yourself

Every cited project links to its Modrinth page, where the quoted disclosure can be read. Any project's
live status:

```
curl -s https://api.modrinth.com/v2/project/MrC0PXcn | jq '.status, .approved'
```

Content Rules §6 as archived a week before the refusal, and before the policy existed:

- http://web.archive.org/web/20261102101459/https://modrinth.com/legal/rules
- http://web.archive.org/web/20260802000307/https://modrinth.com/legal/rules

## Files

```
index.html                              the page (no JavaScript)
build_page.py                           generates index.html from one table of verified projects
evidence/corpus_ledger.csv              all 4,831 AI-disclosing projects: dates, status, disclosure note
evidence/post_grace_ai_authored_core.csv
evidence/post_grace_substantial_ai.csv  the post-deadline cases
evidence/page_image_ai_claims.csv       projects declaring AI-produced page images
evidence/corpus_stats.json              the figures on the page
```

Rebuild after editing the data in `build_page.py`: `python build_page.py index.html`.

## Corrections

Projects can be edited or removed after 2026-11-14, when every cited item was verified. If something is
out of date or misrepresented, open an issue and it will be corrected with a note on the page.

## Licence

Text CC BY 4.0. Data derived from Modrinth's public API v2/v3.
