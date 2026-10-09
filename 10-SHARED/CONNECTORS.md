# Connector routing (summary; full rules in skills/connector-router)

| Need | Use | Cost rule |
|---|---|---|
| Library or API docs before coding | Context7 | Free |
| Code, docs, PRs, Actions | GitHub (`gh`) | Free. Never merge |
| File archive, config mirror | Google Drive (`gws`) | Free. Never permanently delete |
| Visual hub, catalogs, dashboards | Notion | Free |
| Data, mirrors, roadmap, logs | Supabase (omnitask-portal) | Free tier. RLS with `is_admin()`. Run advisors after DDL |
| Tasks and next steps | Todoist (Free: section-per-project) | Free. Max 3 open roadmap tasks per project |
| Images: README heroes, Notion covers, project cards, screenshots | Cloudinary (`omni-hub/`) | Free plan; check usage monthly |
| Format conversion: md/html to pdf/docx, svg to png, merging PDFs | CloudConvert | Limited minutes; 1 job per run unless approved |
| Web data | Apify | Paid runs need approval |
| Image generation | Leonardo | Credits; ask first |
| Errors | Sentry (org chaosinc) | Free |
