# MEMORY_CONTEXT (Hafıza Sistemi)

## Durum / Hafıza
- Ana cevap üreten model: DeepSeek (OpenClaw)
- Qwen3-4B (8086) + Qwen2.5-1.5B (8087): hafıza işçileri, QT45 modunda
- Hafıza pipeline: SQLite (207 kayıt) → Qdrant (74+ vektör) → QT45 KV cache

## Bileşenler
- **llama-server (Qwen3-4B, CPU, port 8086)**: QT45 FULL, chat-template chatml, reasoning off
- **llama-server (Qwen2.5-1.5B, CPU, port 8087)**: QT45 FULL, chat-template chatml
- **QT45 codebook**: 4096 cluster, 128 dim, cosine 1.0, 64× compression
- **Chat UI**: Systemd service, port 5000, domain: chat.havaalanitransfer.gen.tr
- **CAG**: Qdrant vektör DB, bge-small-en-v1.5 embedding, 5dk cron

## Bilinen Sorunlar
- 1.5B codebook 96→128 padding uyumsuz → ara sıra decode hatası (restart düzeltir)
- 4B `<think>` tag'i üretiyor (--reasoning off yetersiz, model eğitiminden)
- Qwen provider OpenClaw'a eklendi ama memory context'siz (codebook hatası engelliyor)
- GPU yok → real KV hook çalışmaz, codebook yeniden eğitilemez

## Yapılanlar (30 Mayıs 2026)
- Chat template fix: --chat-template chatml eklendi (1.5B ve 4B)
- Endpoint fix: /completion → /v1/chat/completions
- night_load.sh: /v1/chat/completions + env variable (QT45_DB, QT45_PORT)
- Chat UI: FastAPI, systemd service, cloudflared tunnel, chat.havaalanitransfer.gen.tr
- Provider: qwen-1.5b ve qwen-4b OpenClaw'a eklendi
- Repo: 8 commit, private, PIPELINE.md dahil
- Cron: night load her 2 saatte bir, CAG worker her 5 dk
