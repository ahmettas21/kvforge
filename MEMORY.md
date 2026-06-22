# MEMORY.md

## Defaults — Skill usage (Elif)

## PMSC IP / Licensing
- PMSC-Phase-Multiplexed-Spherical repo’nun yazarı İlker (Ege Berk Türk) — ticari kullanım kararı bizde. (2026-05-24)

## PMSC (Railway “brain” deployment)
- Personal (OpenClaw memory) endpoint: https://pmsc-api-personal-production.up.railway.app (2026-05-24)
- Prod (customer) endpoint: https://pmsc-api-production.up.railway.app (health: ok, version: 0.3.2) (2026-05-24)
- Storage: Railway Volume üzerinde SQLite (WAL) + API kuruldu; OpenClaw tarafında PMSC plugin/hook aktif (2026-05-24)

## Integrations (remember)
- NotebookLM CLI (`nlm`) is installed + authenticated on this machine (profile: default, account: ilkerturk2025@gmail.com).
- Google Docs knowledge base links are indexed in `memory/google-docs-index-2026-05-11.md`.
- Membrane connections to authorize (Linear/Notion/Railway) captured in `memory/2026-05-11.md`.

### Always / routine (ZORUNLU)
- **2nd-brain (brain)** — öğrenilen her şey brain/ altına, günlük dosyasına değil
- github
- tmux
- brave-search / web-browsing
- browser-use / agent-browser-2

### On-demand
- fast-io
- gog
- notion
- slack
- telegram-integration
- composio
- summarize-1-0-0
- test-runner
- cs-code-reviewer
- opencode
- claude
- notebook-lmskill-1-0-0

## Skill Rules
- **Kural:** Skill varsa → skill kullanılır, yoksa → düz işlem (exec/API)
- ClawHub'dan kur: `clawhub install <slug>` (login: @ahmettas21)
- Skill matrisi: `SKILLS.md`

## CliGate (2026-05-12)
- Install: GitHub source (cloned to `/home/turk/projects/cligate/`)
- Systemd service: root (`/etc/systemd/system/cligate.service`)
- Config: `/root/.cligate/accounts.json`
- Dashboard: `http://localhost:8081`
- ChatGPT account: ilkerturk2025@gmail.com (Team plan)
- **Stream fix applied:** `sendMessage()` in `direct-api.js` patched to use `stream: true`
- **Rate limit:** Team plan doluydu. Reset zamanı: 12 Mayıs ~20:28 UTC. Sağlık raporu 2 saatte 1 kontrol ediyor.
- **OpenCode default:** yuxor/claude-sonnet-4-6 (cligate/gpt-5.2 rate limitli)
- **Pipeline:** izgetour cronjob güncellendi → `yuxor/claude-sonnet-4-6`
- **Sağlık raporu:** 2 saatte 1 cronjob (18:05 raporu: ayakta, token refresh başarılı, 5 model)
- **ChatGPT Team Plan:** 12 Mayıs 20:28 UTC'de kota resetleniyor. Sonra cligate/gpt-5.2 deneriz.

## OpenCode (2026-05-12)
- CLI: v1.14.41 at `/home/turk/.npm-global/bin/opencode`
- Config: `~/.config/opencode/opencode.json`, MCP: `~/.config/opencode/mcp.json`
- MCP connected: notebooklm, chatprd, github, vercel
- OpenAI provider: yuxor (3 models: claude-opus-4-7, claude-sonnet-4-6, claude-haiku-4-5)
- Default model: yuxor/claude-sonnet-4-6
- **Membrane MCP:** HTTP/streamable MCP var ama OpenCode url-type desteklemiyor; stdio proxy gerekli (opsiyonel)

## Membrane (2026-05-12)
- CLI v1.18.0, login: ahmetilkerturk@gmail.com
- Kullanım: `membrane act --connectionKey <servis> --api '{...}'`
- Connected services: Gmail, GitHub, Linear, Notion, Vercel, Google Drive, Railway, N8n.io
- Disconnected: Box, Figma, Intercom, Supabase, WhatsApp, LinearB, Google Sheets, PostHog, Hubspot
- Cloud MCP: `api.getmembrane.com/mcp/integrate-anything`

---

## Araştırma Güncellemesi — 2026-06-20

**Perplexity MCP (pwm)** ile 3 konu araştırıldı. Detay: `workspace/memory/ai-news-2026-06-20.md`

### Öne Çıkanlar

1. **PPL Stabilizasyonu & Progressive Training:**
   - Ultra-low-bit quantization + corrective pathway hibriti trend — quantizasyon artık "yapısal regularizasyon" olarak görülüyor
   - Domain-specialized continual pretraining (CPT) ile LoRA high-rank adapter'lar PPL düşüşü sağlıyor
   - Stabilite odaklı fine-tuning: replay buffer + parameter-efficient tuning kombinasyonları

2. **CoTo (Come Together) — 2026 Gelişmeleri:**
   - Progressive activation: adapter aktivasyon olasılığı kademeli artırılıyor
   - Dynamic runtime merging: inference sırasında adapter'lar arası interpolasyon
   - Budget-aware merging: teorik performans garantileri (yeni 2026 makaleleri)
   - Diverse LoRA variantları ile uyumluluk arttı

3. **KV Cache Compression + Adapter Eğitimi:**
   - Cross-model KV cache reuse: adapter switch'te cache invalidation sorununu çözüyor
   - Layer/head adaptive compression: kritik token koruma + agresif sıkıştırma
   - Quantization + selective eviction hibriti en pratik yaklaşım

### Sonuç

KvForge (Base Encode + LoRA Decode + CoTo progressive training + 2-bit KV compression) literatürdeki **CoTo + KV cache compression** boşluğunu dolduran özgün bir yaklaşım. Rakip çalışma bulunamadı — hibrit yaklaşım hala keşfedilmemiş durumda.
