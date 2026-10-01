---
id: iphone-obsidian-shortcuts-only
type: guide
updated: 2026-10-01
---
# Obsidian on iPhone as a launcher only

Goal: Obsidian on the phone does nothing but open and trigger things. Everything durable lands in GitHub (omni-vault), Supabase, Drive or Todoist automatically.

## Where each thing is stored
| What you capture | Goes to | How |
|---|---|---|
| Quick thought, link, snippet | Portal inbox (Supabase) then omni-vault/00-INBOX | Shortcut POSTs to the portal webhook (works today) |
| Task | Todoist | Todoist share-sheet or Shortcut |
| Photo or screenshot | Google Photos (stays); note with link goes to inbox | Shortcut "Save to album" + note |
| File or PDF | Google Drive | Files app / Drive share sheet |
| Code, prompts, docs | GitHub | GitHub mobile or Copilot/Computer PRs |
| Long-term notes | omni-vault (Markdown) | PC with Obsidian + Git, or edit on GitHub mobile |

## One-time setup (iPhone, about 15 minutes)
1. Install Obsidian. Create a tiny local vault named Launcher (iCloud is fine). It holds only link notes: Portal, GitHub vault, Todoist, Drive, Roadmap.
2. In Obsidian: Settings > Files and links, keep defaults. Do not enable Obsidian Sync (paid) or any sync plugin.
3. Shortcuts app > New Shortcut "Capture":
   - Ask for Input (Text) -> Dictionary {text, source: "iphone", ts: Current Date}
   - Get Contents of URL: POST `https://zlxtnknbblgqhdsynjco.supabase.co/functions/v1/webhook/capture`
     Headers: `x-webhook-secret: [INSERT secret from Portal > Webhooks > Reveal]`, `Content-Type: application/json`. Request Body: JSON.
   - Show Notification "Captured".
   Save it to the Home Screen and Action Button / Back Tap if you like.
4. Shortcut "Open Launcher": Open URL `obsidian://open?vault=Launcher&file=Home`.
5. Shortcut "Quick Obsidian note" (optional, offline): Open URL `obsidian://new?vault=Launcher&name=Inbox%20{date}&content={text}` (URL-encode text). Obsidian URI actions: new, open, append/prepend, search ([Obsidian URI help](https://obsidian.md/help/uri)). The PC runner (or Obsidian Git on PC) moves these into omni-vault weekly.
6. Add the Portal to the Home Screen from Safari (Share > Add to Home Screen).

## Why this layout
- No sync plugin means no conflicts, no paid sync, no surprise data loss.
- Markdown stays canonical in Git: portable and diffable.
- Supabase gives search and automation; losing it never loses notes.

## PC side (optional, from remote desktop)
Open omni-vault in Obsidian with the Obsidian Git plugin (commit/push on a timer). The PC runner can also pull inbox rows from Supabase into 00-INBOX/*.md.

## Security
Shortcut stores the webhook secret on your phone only. If the phone is lost, rotate it in Portal > Webhooks.
