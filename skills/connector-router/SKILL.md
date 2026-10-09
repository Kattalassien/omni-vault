---
name: connector-router
description: "Pick and call the right connector for Preston's projects: Context7 docs, CloudConvert conversions, Cloudinary images, Notion hub pages, Supabase data, Google Drive files, GitHub PRs, Todoist tasks, with cost and safety rules. Use for 'look up the docs', 'convert this to PDF', 'host this image', 'save to Notion/Drive/Supabase'. Not for writing app code itself."
license: MIT
metadata:
  author: Kattalassien
  version: "1.0"
  source: "github.com/Kattalassien/omni-vault/skills/connector-router"
  perplexity:
    connectors:
      - id: context7
        reason: Live library docs before coding.
      - id: cloud_convert__pipedream
        reason: File format conversion.
      - id: cloudinary
        reason: Image hosting and transformations.
      - id: notion_mcp
      - id: supabase
      - id: google_drive
      - id: github_mcp_direct
      - id: todoist
---

# Connector router

Route each need to the cheapest connector that works. Check `omni-vault/08-CONFIG/config.yaml` and `08-CONFIG/projects.json` for IDs. Never put secrets in files, logs or chat.

## Route table
| Need | Connector | Do | Don't |
|---|---|---|---|
| API or library docs before code | Context7 | Resolve the library ID, then query the docs with one focused question | Code from memory for fast-moving libraries |
| md/html to pdf/docx, svg to png, merge PDFs | CloudConvert | Import from a public or Cloudinary URL, then convert, then export the URL. One job per run unless the user approves more | Convert things the sandbox can do for free (pandoc, rsvg) unless the user asks |
| Host an image (README hero, Notion cover, project card, screenshot) | Cloudinary | Upload to folder `omni-hub/<slug>/` with tags `omni-hub,<slug>`. Link the `secure_url` and use `f_auto,q_auto` | Upload private screenshots without redaction |
| Visual catalog or hub page | Notion | Update the "Omni Knowledge Hub" page and the "Omni Projects" database under "Preston Master Automation & Knowledge OS" | Create duplicate pages; search first |
| Structured data or mirrors | Supabase `zlxtnknbblgqhdsynjco` | `execute_sql` for upserts. Use `apply_migration` for DDL, then `get_advisors` (security) | Disable RLS or use service_role in clients |
| File archive or config mirror | Drive (`gws`) | Upload into "Omni Knowledge Hub" subfolders. Upload paths must be inside cwd | Permanently delete or empty trash |
| Code and docs | GitHub (`gh`) | Branch `omni/<topic>`, then a PR | Merge, force-push, or change visibility |
| Tasks | Todoist | "Dev Projects": one section per project. Dedupe by the `omni-key:` line | Create projects (Free plan cap) or more than 3 roadmap tasks per project |

## Cloudinary patterns
- Project card, with nothing stored per card (cloud `sewoj1wp`): `https://res.cloudinary.com/sewoj1wp/image/upload/l_text:DejaVu%20Sans_64_bold:<Title>,co_rgb:BB86FC,g_west,x_80,y_-40/l_text:Arial_34:<subtitle>,co_rgb:03DAC6,g_west,x_80,y_50/f_auto,q_auto/omni-hub/base/card-base.png`. URL-encode the text and double-encode commas as `%252C`. Ready-made URLs are in `08-CONFIG/projects.json` under `cloudinary_card`.
- README hero: `https://res.cloudinary.com/sewoj1wp/image/upload/f_auto,q_auto,w_1600/omni-hub/hub/omni-hub-diagram.png`.
- Check usage monthly. The free plan is limited, so delete only with approval.

## Cost and approval gates
- Free first. Ask before Apify paid runs, Leonardo generations, or more than one CloudConvert job.
- Before any write, confirm the target ID. Do a dry run or preview first when the tool supports it.
- Log every external write as one line: `YYYY-MM-DD HH:MM ET | actor | action | result`.

Read `references/recipes.md` when you need exact call shapes for CloudConvert jobs, Cloudinary signed uploads, or Supabase upserts.
