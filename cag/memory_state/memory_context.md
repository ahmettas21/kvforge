# MEMORY_CONTEXT (Hafıza Sistemi)

## Durum / Hafıza
- Ana cevap üreten model: DeepSeek (OpenClaw)
- KV Forge: Qwen2.5-7B (8087) - 16K context, 4 thread
- Hafıza pipeline: SQLite (240 kayıt) → Qdrant → bge-small-en-v1.5

## Bileşenler
- **llama-server (Qwen2.5-7B, CPU, port 8087)**: 16K context, 4 thread, --cache-prompt, chatml
- **KV Forge provider**: OpenClaw'a tanımlı, /model ile seçilebilir
- **CAG**: Qdrant vektör DB, bge-small-en-v1.5 embedding, 5dk cron

## Bilinen Sorunlar
- GPU yok → real KV hook çalışmaz
- Qwen2.5-7B CPU'da çalışıyor, yavaş olabilir

## Yapılanlar (30 Mayıs 2026)
- Qwen3-4B (8086) tamamen kaldırıldı
- Qwen2.5-7B 32K→16K context, 8→4 thread düşürüldü
- Phi-4-mini service devre dışı bırakıldı
- Sadece 1 llama-server çalışıyor (8087)
