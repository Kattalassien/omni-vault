---
id: mind-map
type: map
status: active
updated: 2026-10-04
---
# Mind map: the whole system

GitHub renders this diagram on iPhone and desktop.

```mermaid
mindmap
  root((Preston OS))
    Memory
      BRAIN.md canonical
      config.yaml settings
      LOG and CHANGELOG
      Perplexity memory
      Notion hub page
    Capture
      iPhone Shortcuts
      Gmail receipts and alerts
      Google Photos app uploads
      Jam bug recordings
    Store
      GitHub repos
      Drive archive
      Supabase portal DB
      Cloudinary media
      Dropbox and OneDrive spare
    Act
      Todoist board
        Needs you
        Computer
        Copilot
        Claude
      Perplexity automations
        Daily Gaming Digest
        Hardware deal tracker
      Apify collectors
      CloudConvert jobs
      Leonardo images
    Build
      OmniTask Mobile and Portal
      Steam Deck Ops
      PokeRogue and PokeVoid
      Pokemon hack tools
      Yungfloop generator
      Job automation suite
      Manga pipeline
    Watch
      Sentry errors
      Supabase advisors
      Context7 docs
      Digest of mods and patches
    Games
      BG3 on PS5
      Elden Ring and Dark Souls
      Pokemon and ROM hacks
      Up to 10 extras
```

## How the pieces feed each other
1. Capture (iPhone, Gmail, Jam) lands in 00-INBOX or Todoist "Needs you".
2. Computer triages: durable facts go to BRAIN.md, settings to config.yaml, work to Todoist, results to LOG.md.
3. Builders (Copilot, Claude, Computer) open PRs; you merge from GitHub mobile.
4. Watchers (Sentry, Supabase advisors, the digest) raise new items back into capture.
