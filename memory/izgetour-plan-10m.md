\n---\n# izgetour plan report @ 2026-05-10T16:11:00Z\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md excerpt (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan
**Prioritized TODO Plan (from current repo state)**

1. **Stabilize Git State (pre-ship hygiene)**
   1. Decide what the single “ahead 1” commit is and whether it belongs in the upcoming milestone.
   2. Classify the many untracked additions (`components/`, `lib/`, `pages/`, `scripts/`, `src/components/*`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, etc.) into:
      1. Must-ship now (required for flights/checkout UX to function)
      2. Ship-later (nice-to-have modules: AR sizer, voice map, cuisine recommender, etc.)
      3. Docs/artifacts (`WIKI*.md`, `*LOG*.md`, `CHANGELOG.md`)
   3. Ensure no secrets or environment-specific artifacts are in untracked files (especially `scripts/`, `lib/`, logs).

2. **Flights Listing Page Hardening (highest product risk)**
   1. Review the large change in `src/app/[locale]/flights/page.tsx` (+290 lines): confirm it’s not mixing too many concerns (data, filters, UI, side effects).
   2. Validate core flows:
      1. Search params -> results render deterministically
      2. Filters and sort interact correctly (combinatorial edge cases)
      3. Empty/error states are intentional
      4. Performance: avoid re-render storms with large lists
   3. Define “done” acceptance criteria for Flights Listing (below).

3. **Flights Detail + Checkout Integration (ship value)**
   1. Confirm the linkage: Flight listing -> flight detail (`src/app/[locale]/flights/[slug]/`) -> checkout (`src/app/[locale]/checkout/`).
   2. Verify “price tracking” and saved items behavior aligns with PLAN claims (localStorage vs real notifications).
   3. Ensure cart/checkout summary shows correct itinerary and pricing breakdown.

4. **Scope Control: Experimental Modules**
   1. Most of the newly added components look like “feature inventory” (cool modules but high surface area).
   2. Pick 0-2 to include in the next milestone only if they directly increase conversion or reduce support burden (e.g., `FlightFilters`, `FlightSortSelect`, `FlightCard` are core; “VoiceInteractiveMap” is not).

5. **Documentation & Product Truthfulness**
   1. `PLAN.md` currently marks many items “✅ Tamamlandı”. Reconcile with reality of wiring and production readiness.
   2. Decide what `CHANGELOG.md` should represent: user-facing release notes vs internal dev log.
   3. Ensure wiki/sync logs are either excluded from shipping artifacts or formalized.

6. **Testing/Verification Checklist (pre-ship gate)**
   1. Basic regression pass: homepage, tours list/detail, flights list/detail, checkout success.
   2. i18n routing check (`[locale]`) across all the above.
   3. Mobile layout pass for listing + checkout (most likely to break).
   4. Build/lint pass (whatever the repo uses) and fix any type errors introduced by new components.

---

**Next Ship Milestone (recommended): “Flights MVP to Checkout”**

**Goal:** A user can search flights, filter/sort, view a flight detail, and complete checkout with a coherent summary. Everything else is deferred.

**In-scope**
- Flights listing UX that is correct and fast:
  - `FlightFilters`, `FlightSortSelect`, `FlightCard`
  - deterministic results for given inputs
- Flights detail page (slug) with the minimum necessary detail
- Checkout flow completion for flight purchase intent
- Local “Saved/Tracked flight” behavior if it’s already integrated and not flaky

**Out-of-scope (explicitly defer)**
- Voice map, AR luggage sizing, cuisine recommender, party planning, multi-city router (unless already required by routing), AI travel planner (unless it’s a thin UI wrapper with no risk)
- Predictive bundling (high complexity, unclear data dependencies)
- Real notifications/email integrations (Supabase/email) unless already production-ready

**Definition of Done**
- No broken navigation between listing/detail/checkout under at least:
  - direct navigation by URL
  - locale switching
- Filters/sort do not desync UI vs results
- Empty states are user-friendly (no blank screens)
- No obvious console errors during these flows
- Mobile layout is usable (filters accessible, checkout readable)

---

**Blockers / Questions (need your answers to proceed cleanly)**

1. **What is the intended contents of the “ahead 1” commit on `main`?**  
   Is it already pushed/PR’d elsewhere, and should the next milestone build on it or roll forward from it?

2. **Do you want the next milestone to include only Flights+Checkout, or also Hotels/Tours parity?**  
   I’m assuming “Flights MVP to Checkout” is the fastest shippable slice.

3. **What is the source of flight data right now?**  
   Is it purely `src/data/flights.ts` mock data, or is there a real provider/API planned for this milestone?

4. **How should we treat the many untracked folders (`components/`, `pages/`, `lib/`, `scripts/`)?**
   - Are these newly generated scaffolds?
   - Are `pages/` and `src/pages/` intentional (possible Next routing split), or accidental duplication?

5. **Any release process constraints?**
   - Are you deploying from `main` directly?
   - Do you require changelog entries and versioning per release?
\n## 2026-05-10 16:21 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### opencode plan output
**Next Ship Milestone (MVP): “Flights v1 usable end-to-end”**  
Goal: a user can search/browse flights, open a flight detail page, and complete checkout with stable routing and no dead UI paths. This is the smallest milestone that converts the current “lots of components exist” state into a coherent product slice.

---

## Prioritized TODO Plan

### 1) Stabilize Repo + Bound the Release (highest priority)
1. Decide what is actually part of “Flights v1” vs experimental modules.
2. Clean up the worktree so the release contents are intentional:
   1. Confirm which untracked docs are real deliverables: `CHANGELOG.md`, `WIKI*.md`, `SYNC_LOG.md` vs generated artifacts.
   2. Confirm which untracked code directories are expected in this app-router Next setup: `pages/`, `src/pages/`, top-level `components/`, top-level `lib/` (these can cause confusion/duplicate routing conventions).
3. Define “done” criteria for the milestone:
   1. `/[locale]/flights` loads with results and filters.
   2. `/[locale]/flights/[slug]` loads and can proceed to checkout.
   3. `/[locale]/checkout` completes and shows success/confirmation.
   4. No console errors, no broken imports, no route conflicts.

### 2) Risk-Reduce the Biggest Change: `src/app/[locale]/flights/page.tsx`
Your diff stat shows this file ballooned (+290 LOC). That’s the most likely source of regressions.
1. Do a “surface area audit” checklist for that page:
   1. Identify all new imports and ensure they exist where expected (many components are currently untracked).
   2. Verify it’s not importing from both `components/` and `src/components/` inconsistently.
   3. Check for client/server boundary issues (hooks used in server component, `use client` placement).
2. Confirm data source consistency:
   1. If using `src/data/flights.ts`, ensure listing and detail agree on IDs/slugs.
   2. Ensure filters/sort operate on the same schema the cards render.
3. Add minimal UX guardrails (definition only for now; implement later):
   1. Empty-state when filters remove all results.
   2. Loading skeleton (if any async).
   3. Error state when query params are invalid.

### 3) Make Routing Unambiguous (app router vs pages router)
There are signals of mixed routing approaches: untracked `pages/` and `src/pages/` plus `src/app/...`.
1. Decide: Are `pages/` directories intentional (legacy or for specific routes) or accidental?
2. If not intentional, plan to remove/relocate them before shipping to prevent:
   1. Duplicate route definitions.
   2. Conflicting i18n behavior.
   3. Different data fetching paradigms.
3. Validate i18n route behavior for the milestone:
   1. `/tr/flights` and `/en/flights` (or equivalent) work.
   2. Links between listing/detail/checkout preserve locale.

### 4) Integrate the “Ready Components” Carefully (don’t ship a museum)
You have many “component hazırlandı ✅” items. For the milestone, only wire in what improves conversion and doesn’t add external dependencies.
1. Include (if already truly working in codebase):
   1. `FlightFilters`, `FlightSortSelect`, `FlightCard` (core).
   2. `DynamicPriceChart` (nice-to-have if zero risk).
   3. Saved/follow price tracking (already marked ✅) only if it’s stable and not half-wired.
2. Defer to later milestone:
   1. AR luggage sizing, voice interactive map, party planning, etc. (high complexity, low relevance to Flights v1 conversion).

### 5) Checkout Coherence (Flights → Checkout)
You have `src/app/[locale]/checkout/` untracked, so checkout might exist locally but not committed/organized yet.
1. Define the data contract from flight detail to checkout:
   1. What fields are required (price breakdown, passengers, baggage, cancellation).
   2. How it’s passed (URL params vs state store vs server actions).
2. Ensure guest checkout is truly possible (PLAN says yes):
   1. No forced auth gate in the flow.
   2. If auth exists, it should be optional upsell.

### 6) Documentation + Release Hygiene (small but important)
1. `PLAN.md` excerpt claims lots are “✅ Tamamlandı”; reconcile with what’s actually committed and wired.
2. Decide what `CHANGELOG.md` should contain for the ahead-1 commit:
   1. Focus on user-visible features and breaking changes (especially routing structure).
3. If `SYNC_LOG.md` / `sync_log.md` both exist, pick one naming convention to avoid case/duplication confusion.

---

## Blockers / Questions (need your answers before implementing anything)

1. Are `pages/` and `src/pages/` meant to exist alongside `src/app/`, or are they accidental/uncommitted scaffolding?  
2. For “Flights v1”, do you want to ship the experimental modules (AITravelPlanner, ComparePanel, etc.) visible in UI, or keep them behind a feature flag / separate route for later?  
3. Should `SYNC_LOG.md`, `WIKI.md`, `WIKI_SYNC.md` be committed artifacts, or are they generated by your cron/wiki sync process? (Your PLAN mentions a cron-like monitoring cadence.)  
4. What is the expected locale segment format (`[locale]` values)? `tr/en` only, or more? This affects link building and canonical routing.  
5. Checkout expectations: should it accept only flights for this milestone, or flights + hotels/tours bundles already?

If you answer those 5, the next iteration of this TODO can be tightened into a “ship checklist” with exact acceptance tests per route.

## 2026-05-10 16:32:08 UTC

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (first 120 lines excerpt)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

### Opencode plan output
(see below)

**Prioritized TODO Plan (Read-Only, No Tools)**

1. Stabilize scope and branch hygiene
- Confirm what the ahead 1 commit is and whether it is meant to ship.
- Decide what to do with the large set of untracked files: ship now vs stage later vs split PRs.
- Define a minimum shippable slice for Flights Listing.

2. Make Flights Listing page shippable
- Ensure flights page compiles and renders with current conventions.
- Verify core UX path Landing to Flights Listing to optional Detail to Checkout.
- Validate listing data assumptions.
- Confirm filtering sorting correctness and empty states.

3. Decide integration strategy for new UI modules
- Inventory new components and map actual usage.
- Pick one integration target for this milestone (Flights Listing only recommended).
- Keep experimental widgets off by default unless needed.

4. Routing and locale correctness
- Confirm locale segment usage and defaults.
- Ensure new routes match app router conventions.
- Decide whether pages routes are intentional or leftovers.

5. Documentation and change management
- Align PLAN with actual implementation.
- Pick one canonical changelog and naming scheme.
- Decide if WIKI and sync logs belong in git.

6. Quality gates before ship
- Run typecheck lint test build and fix release blockers.
- Smoke test mobile layout.
- Sanity check performance.

Next Ship Milestone
- Flights Listing MVP plus Filters Sort plus Basic Compare

Blockers Questions
- Shipping intent prod vs demo.
- Untracked files commit now or artifacts.
- Routing architecture app router vs pages.
- Data source mock vs API.
- Docs ownership for wiki sync logs.
\n## 2026-05-10 16:42 UTC

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

### Plan report

### Plan report (opencode)
**Next Ship Milestone (MVP v0.1): “Flights Listing End-to-End Demo”**  
Ship a stable `/[locale]/flights` experience that: loads without errors, shows results from `src/data/flights.ts`, supports filter + sort + compare at minimum, and has a clear path into a flight detail (`/[locale]/flights/[slug]`) and checkout (`/[locale]/checkout`) even if those are “stubby” screens. Goal is a demo-quality, non-broken user flow rather than full product completeness.

## Prioritized TODO Plan

1. **Stabilize the repo state (ship hygiene)**
1. Decide what is in-scope for the milestone vs. “future modules”: the git status shows a very large surface area (new `components/`, `lib/`, `pages/`, `scripts/`, many `src/components/*`, plus new app routes).
1. Ensure only one routing paradigm is “authoritative” for this milestone: you currently have both `src/app/...` and `src/pages/...` plus a top-level `pages/` directory. Pick one for the milestone to avoid route conflicts and weird build behavior.

2. **Define the release slice for Flights**
1. Flights listing page must be the “golden path”: `/[locale]/flights/page.tsx` should render reliably on first load and on refresh (no client-only assumptions unless explicitly intended).
1. Lock the data contract for a “flight” object: what fields are required for `FlightCard`, filtering, sorting, compare, and slug routing.
1. Confirm “empty states”: no results, loading state (even if data is local), and error state (bad query params).

3. **Make filters/sort/compare coherent (minimal but correct)**
1. Filters: pick the minimal set that demonstrably works end-to-end (e.g., price range, stops, airline) and ensure they’re consistent with the data model.
1. Sort: implement 2-3 sorts that users expect (price asc, duration asc, best) and ensure stable sorting.
1. Compare: limit compare to 2-3 items, define what happens when user exceeds limit, and ensure comparison view doesn’t break mobile layout.

4. **Routing + Detail page contract**
1. Confirm slug format and generation (e.g., based on ID) to avoid collisions and broken links.
1. Ensure `/[locale]/flights/[slug]/` can render a selected flight deterministically (from local data or a fetch).
1. Add a “book/select” CTA that transitions into checkout route (even if checkout is minimal).

5. **Checkout happy path**
1. Ensure `/[locale]/checkout/` is reachable and doesn’t depend on auth.
1. Define the minimal “order summary” inputs: selected flight ID + pricing breakdown.
1. Confirm persistence strategy for selection (URL params vs. localStorage vs. in-memory state); for MVP, prefer URL-based or a single persisted key so refresh doesn’t lose the demo.

6. **Quality gates for shipping**
1. Build passes and routes don’t conflict (especially important with both `app` and `pages` present).
1. Mobile layout sanity check for listing, filters drawer/panel, compare view, and primary CTA.
1. Remove or quarantine “experimental” modules from the critical path (AI planner, AR sizer, voice map, etc.) so they can’t break the MVP.

7. **Documentation + tracking (lightweight)**
1. Decide whether `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md` are part of release artifacts or internal notes; if internal, keep them out of the main milestone criteria.
1. Update `PLAN.md` milestone status to reflect what is actually shippable vs. “component exists”.

---

## Blockers / Questions (need your decisions)

1. **Routing strategy:** Are we standardizing on `src/app` (App Router) for this repo right now, or is `src/pages`/`pages` intentionally included? Having both is the biggest “can’t ship safely” risk.
1. **Milestone scope:** For the next ship, do you want *only Flights* to be shippable, or do you expect Hotels/Tours/AI modules to be visible too?
1. **Data source:** Is `src/data/flights.ts` the intended MVP source, or should the UI already be shaped to accept an API response (even if mocked)?
1. **State persistence:** Should selected flights / saved searches persist across refresh (localStorage) for MVP, or is in-session acceptable?
1. **Locale behavior:** What’s the expected default locale and fallback behavior if `[locale]` is missing/invalid?

If you answer just the first two (routing strategy + milestone scope), the rest of the plan can be locked quickly and turned into an execution checklist for the next ship.
\n---\n# Izgetour Plan Report - 2026-05-10 16:52:29 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md excerpt (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan output
**Prioritized TODO Plan**

1. **Stabilize repo hygiene (pre-ship)**
   1. Decide what is “real product code” vs “scaffold/experiments”: right now there’s a very large set of new top-level dirs/files (`components/`, `lib/`, `pages/`, `scripts/`, extra `src/pages/`, duplicate-ish `sync_log.md` vs `SYNC_LOG.md`, multiple `WIKI*` files).
   2. Normalize naming and duplicates: pick one canonical casing for `SYNC_LOG.md` vs `sync_log.md` (case-sensitive FS will treat as different); confirm whether both should exist.
   3. Ensure routing architecture is consistent: having both `src/app/...` (App Router) and `pages/` / `src/pages/` (Pages Router) can be intentional, but commonly becomes confusing and can create unexpected route resolution conflicts.

2. **Scope the change set for the next ship**
   1. Define the deliverable for `src/app/[locale]/flights/page.tsx` changes: what exactly should users see/do now that wasn’t possible before?
   2. Identify which of the many new UI components are actually integrated into runtime routes vs just added to the tree.
   3. Confirm whether the new untracked `src/app/[locale]/flights/[slug]/` and `src/app/[locale]/checkout/` are meant to ship in this milestone, or are future work.

3. **Quality gates (must pass before merging)**
   1. Run typecheck/lint/test/build locally and fix any failures (especially important given the 290-line delta in a core page and many new components).
   2. Verify i18n behavior for `[locale]` routes: route generation, links, and any locale-specific formatting (currency, dates).
   3. Verify “happy path” UX on flights listing: load, filter, sort, card interaction, navigation to detail, add-to-checkout flow (if present).

4. **Product correctness checks for flights listing**
   1. Confirm data source expectations: is `src/data/flights.ts` mock-only or intended as a stable seed? If mock, ensure it’s clearly isolated and swappable.
   2. Validate filtering/sorting semantics: stops, airline, time windows, cancellation, price bounds, etc. (PLAN indicates these are “done”, but ensure behavior matches labels and doesn’t silently mis-filter).
   3. Confirm persistence behavior where promised (PLAN mentions localStorage price tracking, bell UI): ensure it works across refresh and locale routes.

5. **Documentation + changelog discipline**
   1. Decide whether `CHANGELOG.md` is now authoritative, and what release note granularity you want.
   2. If `PLAN.md` is cron-updated “every 10 minutes”, decide whether it belongs in git history (it can create noisy diffs and conflict churn).

---

**Next Ship Milestone (Recommended)**

**Milestone: “Flights Listing MVP Hardening + Route Consistency”**

Goal: ship a clean, predictable flights listing experience that compiles, routes correctly under `[locale]`, and doesn’t introduce ambiguous routing/layout structure.

Included:
1. `src/app/[locale]/flights/page.tsx` finalized UX (filters/sort/cards/empty states).
2. Only the components actually used by flights listing and its immediate navigation (detail/checkout only if already wired and stable).
3. Repo structure clarified (one router strategy or clearly documented hybrid).

Excluded (defer):
1. “Trend modules” not wired into critical paths (planner, AR sizer, voice map, etc.) unless they are already integrated and tested.
2. Any wiki/sync automation artifacts unless you explicitly want them versioned.

Success criteria:
1. `pnpm/npm/yarn build` (whatever the repo uses) succeeds.
2. No route duplication surprises between `app/` and `pages/`.
3. Flights list page works on mobile and desktop and matches PLAN’s promised behaviors at least for the core flows.

---

**Blockers / Questions (Need Your Answers Before Implementation)**

1. **Ship scope**
   1. Which routes are you trying to ship *now*: only flights listing, or also flight detail (`/flights/[slug]`) and checkout (`/checkout`)?
   2. Are the many untracked components meant to be shipped now, or staged for future work?

2. **Routing strategy**
   1. Is this repo intentionally hybrid (App Router + Pages Router), or should `pages/` / `src/pages/` be removed/ignored?
   2. If hybrid is intentional, which set is canonical for new features?

3. **Docs/sync artifacts**
   1. Should `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md` be committed as part of the product, or are they internal tooling outputs?
   2. Do you want `PLAN.md` treated as a living document in git despite frequent automated edits?

4. **Case-sensitive duplicates**
   1. Do you confirm both `SYNC_LOG.md` and `sync_log.md` exist and should remain separate? (This will cause pain across OSes and CI.)

5. **Data + behavior**
   1. Is `src/data/flights.ts` mock data only, or is it intended as the first real dataset layer?
   2. Any expected currency/timezone rules per locale (TRY vs EUR, etc.) for flights pricing and time display?

If you answer just (1) ship scope and (2) routing strategy, the rest can be resolved as part of tightening the milestone.

=== IZGETOUR PLAN REPORT @ 2026-05-10T17:01:00Z ===

GIT_STATUS
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

DIFF_STAT
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT (first 120 lines)
(see repo PLAN.md; excerpt captured in prior run output)

OPENCODE_PLAN_OUTPUT
Prioritized TODO Plan
1 Stabilize repo state
- Decide what the ahead 1 commit on main is and whether to keep or reset.
- Bucket untracked additions: core product code vs legacy routing risk (pages/src pages) vs docs meta.
- Resolve duplicates conflicts: SYNC_LOG.md vs sync_log.md; pages vs src/pages vs src/app.
2 Make Flights page shippable
- Review flights page change for data source, scope creep, perf, a11y and i18n.
- Define MVP for flights listing: search params, sort filter, empty error loading, navigation to detail.
3 Close route flow listing detail checkout
- Validate intended flow and ensure flights slug and checkout stubs are coherent.
4 Consolidate components
- Triage ship now vs later and pick canonical components path.
5 Documentation hygiene
- Update PLAN.md scope, decide docs placement, changelog strategy.

Next Ship Milestone
Flights MVP end to end listing to detail to checkout stub.

Blockers Questions
Routing decision pages vs app router; canonical components dir; data strategy mock vs api; slug strategy; case conflict policy; main ahead 1 release intent.
\n---\n## 2026-05-10 17:11 UTC\n
Branch: main (ahead 1)

### git status -sb


### git diff --stat


### PLAN.md (lines 1-120)


### Plan report (opencode plan agent)
src/app/[locale]/flights/page.tsxsrc/data/flights.tspages/src/pages/src/appsrc/app/[locale]/flights/[slug]/src/app/[locale]/checkout/CHANGELOG.mdSYNC_LOG.mdsync_log.mdWIKI.mdWIKI_SYNC.mdPLAN.mdpages/src/pages/src/app/src/data/flights.ts[locale]flights/[slug]

---
## 2026-05-10 17:11 UTC

Branch: main...origin/main [ahead 1]

GIT_STATUS
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

GIT_DIFF_STAT
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT_FIRST_120_LINES
(see PLAN.md; captured in this run)

PLAN_REPORT
- Next ship milestone: M1 Flights MVP (listing hardening, filter+sort, basic detail and optional checkout stub)
- Top TODOs:
  1) Stabilize flights listing page change (page.tsx +290 LOC): correctness, empty/loading, perf, URL query sync
  2) Scope control: triage many untracked components and only wire core flights ones (FlightCard/Filters/SortSelect) for M1
  3) Routing risk: decide app router vs pages router (pages/ and src/pages exist alongside src/app). Avoid route conflicts.
- Blockers/questions:
  - Is routing strategy app router only, or hybrid with pages? Are pages/ and src/pages intentional?
  - Flights data source: src/data/flights.ts mock only or stepping stone to API?
  - Locale list/default and slug semantics for flights/[slug]

## 2026-05-10 17:21 UTC

### Git
- branch: main (ahead 1)
- status: M PLAN.md; M src/app/[locale]/flights/page.tsx; many untracked (docs + dirs + src/components/* etc)
- diffstat:
  - PLAN.md | 15
  - src/app/[locale]/flights/page.tsx | 290
  - total: 293 insertions, 12 deletions

### PLAN.md excerpt (1-120)
(see repo PLAN.md; excerpt was read during cron)

### Plan (prioritized TODO)
1) Stabilize repo hygiene: clarify ahead-1 on main; pick canonical docs/log filenames (SYNC_LOG.md vs sync_log.md); decide what to do with large untracked dirs (components/lib/pages/scripts/src/pages).
2) Flights listing page correctness: review page.tsx changes; verify filters/sort/cards integration; add/verify empty-error-loading states; verify locale routing.
3) Routing duplication risk audit: App Router (src/app) vs Pages Router (pages or src/pages) decide one; smoke check listing->detail->checkout routes.
4) Define MVP slice + freeze scope: ship Flights listing+detail+checkout+price follow; push other trend modules behind later flags.
5) Quality gates: typecheck/lint/tests; prod build; smoke test key routes; ensure no secrets in new log/wiki files.

### Next ship milestone
Flights MVP end-to-end (browse -> detail -> checkout).

### Blockers/questions
- Are components/, pages/, lib/, scripts/, src/pages/ intentional or duplicates?
- App Router only or also Pages Router?
- Which sync/wiki/log files are intended to ship (case collision risk)?
- Ship from main or branch workflow?
- Trend modules user-facing now or placeholders?
\n---\n# izgetour plan report - 2026-05-10 17:33 UTC\n
BRANCH_STATUS: main...origin/main [ahead 1]
\nGIT_DIFF_STAT:\nPLAN.md | 15 +-\nsrc/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-\n2 files changed, 293 insertions(+), 12 deletions(-)
\nPLAN_OUTPUT:\n
**Onceliklendirilmis TODO Plani**

1. Stabilizasyon ve temizlik (hemen)
1. Git durumunu netlestir: `main` dalinda `ahead 1` var, ama cok sayida untracked dosya var. Neyi ship edecegiz listesini kesinlestir.
1. Duplikasyon kontrolu: `SYNC_LOG.md` ve `sync_log.md` birlikte gorunuyor. Linux ortaminda ikisi farkli dosya; bu ileride karisiklik ve CI sorunlari yaratir. Tek isim standardi sec.
1. Dokumantasyon kapsamini ayir: `PLAN.md` degisikligi, `CHANGELOG.md`, `WIKI.md`, `WIKI_SYNC.md` ship paketine girecek mi karar ver.
1. Klasor sprawl kontrolu: kokte `components/ lib/ pages/ src/pages/` gibi paralel yapilar var. Next proje yapisinda routing ve importlarin karismasi olasi. Simdilik ship kapsaminda degilse, en azindan hangi klasorlerin aktif oldugunu listele.

2. Flights sayfasi MVP kapanisi (bir sonraki milestone)
1. `src/app/[locale]/flights/page.tsx` icin kabul kriterlerini belirle: 
1. Ucus listesi gorunur
1. Filtrele ve sirala calisir
1. Kart komponentleri dogru veriyle render olur
1. Empty state, loading state, error state var
1. Mobil ve desktop temel UX tamam
1. Performans kontrolu: 290+ satir eklenmis. Render maliyeti, gereksiz re render, buyuk liste (virtualization yoksa) ve bundle boyutu risk. Minimum performans hedefi koy (ornegin ilk yukleme, etkilesim gecikmesi).
1. I18n dogrulama: route `[locale]` altinda. Tarih, para birimi, metinler, sagdan sola gibi konulara gerek var mi? En azindan formatlama ve metin kaynaklari belirgin olmali.

3. Yeni eklenen komponentlerin kapsam secimi (MVP vs backlog)
1. Ucusla dogrudan ilgili olanlari MVPye dahil et:
1. `FlightCard`, `FlightFilters`, `FlightSortSelect`, `DynamicPriceChart`, `ComparePanel`, `SavedSearches` (eger basit)
1. Deneysel veya scope sisirenleri backloga it:
1. `VoiceInteractiveMap`, `AITravelPlanner`, `GamificationBadges`, `LoyaltyTierSystem`, `LuggageArSizer`, `MoodDestinationPicker`, `PartyPlan`, `SmartItinerary`, `SocialProofToast`, `SustainabilityScore`, `MultiCityRouter` (bunlarin her biri ayri urun alani)
1. Checkout yeni klasor var: `src/app/[locale]/checkout/`. Flights MVP ile baglantisi net degilse bir sonraki milestonea birak.

4. Routing ve mimari netligi
1. Next App Router mi Pages Router mi: `src/app/...` var, ama `pages/` ve `src/pages/` da var. Hangi routing aktif, hangisi legacy kararini yaz.
1. Import path standardi: `src/components/` zaten var, ama kokte de `components/` var. Tek kaynak belirle, digerini deprecated et (hemen tasimaya gerek yok, ama policy yaz).
1. Data katmani: `src/data/flights.ts` ile mock mu, yoksa API mi gelecek? Mock ise cikis icin yeter, ama API planini yaz.

5. Test ve kalite kapisi (ship oncesi)
1. Lint ve typecheck kosullari: ship oncesi minimum kapilar
1. E2E yoksa bile smoke senaryolari: flights sayfasi acilir, filtre uygulanir, sort uygulanir, detay sayfasina gider (slug route var)
1. Build ve bundle kontrolu: buyuk yeni komponent listesi tree shaking ile disarida kaliyor mu, yoksa istemeden bundlea giriyor mu?

---

**Bir Sonraki Ship Milestone (onerim)**

Milestone adi: Flights Search MVP v1 (locale destekli)

Hedef:
1. `/[locale]/flights` sayfasi kullanilabilir ve stabil
1. Listeleme + filtre + siralama calisir
1. `src/app/[locale]/flights/[slug]/` detay sayfasi en azindan temel skeleton ile acilir (eger zaten planlandiysa)
1. Dokumantasyon: `CHANGELOG.md` ile bu MVPde ne var net

Cikis kriterleri:
1. Tip hatasi yok
1. Lint temiz
1. Mobil gorunum kabul edilebilir
1. Mock veri ile dahi olsa core akis tamam

---

**Blokajlar ve Sorular**

1. Ship kapsaminda neler var?
1. Sadece flights mi, yoksa checkout ve diger AI ve gamification komponentleri de mi?
1. Bu kadar cok untracked dosyayi ayni cikisa almak riskli; secim gerekiyor.

2. Routing karari gerekli
1. `src/app` ile `pages/` birlikteyse, calisma zamani davranisi ve deploy ayari net olmali.
1. Hangi routeri resmi kabul ediyoruz?

3. Dosya isim standardi
1. `SYNC_LOG.md` ve `sync_log.md` ikisi de kalsin mi? Kalirsa ekipte Windows kullanimi varsa merge ve case conflict cikabilir.

4. Veri kaynagi ve urun beklentisi
1. `src/data/flights.ts` kalici mock mu, yoksa API entegrasyonu milestone icinde mi?
1. Fiyat, para birimi, tarih formatlari locale bazli mi olacak?

5. UI hedefi
1. Kayak benzeri deneyimde olmazsa olmazlar neler: tarih secimi, havalimanlari, cabin class, stop sayisi, bagaj, esnek tarih, price graph?
1. MVP icin hangileri sart?
\n---\n# Izgetour Plan Report - 2026-05-10 17:41 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## Plan output
**Prioritized TODO Plan (Read-only, no tools, no code)**

1. **Define what “shipping” means for the current increment**
   1. Pick the single user-facing slice to ship next: `Flights listing UX` vs `Checkout flow` vs `Predictive Trip Bundler`.
   1. Freeze scope for the milestone (what is explicitly in, what is explicitly out).
   1. Decide target environment: staging only vs production.

2. **Stabilize repository hygiene for a shippable PR**
   1. Decide what belongs in the PR vs what is local/WIP:
      1. Tracked modifications: `PLAN.md`, `src/app/[locale]/flights/page.tsx`
      1. Many new untracked files: `components/`, `lib/`, `pages/`, `scripts/`, `src/components/*`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, `src/data/flights.ts`, multiple wiki/log files.
   1. Create an inclusion/exclusion list:
      1. Product/code: components, lib, src/app routes, src/data
      1. Process/docs: PLAN, CHANGELOG (maybe), WIKI (maybe)
      1. Never ship: sync logs and automation artifacts unless intentionally part of the repo (`SYNC_LOG.md`, `sync_log.md`, `WIKI_SYNC.md`)
   1. Align naming conventions: you currently have both `SYNC_LOG.md` and `sync_log.md` which is a cross-platform footgun (macOS/Windows case-insensitive filesystems).

3. **Flights listing: convert “feature-complete UI” into “release-ready UX”**
   1. Confirm the flights page contract:
      1. Inputs: locale routing, query params, search state
      1. Outputs: list results, filter/sort interactions, empty states
   1. Validate critical UX paths:
      1. First load (default results or requires search?)
      1. Filtering and sorting correctness
      1. No-results state and reset filters
      1. Loading state and perceived performance
   1. Verify “compare / save / price tracking” features don’t regress:
      1. localStorage persistence behavior (quota, serialization, versioning)
      1. hydration mismatch risks (server vs client state)
   1. Accessibility and mobile sanity pass:
      1. Keyboard navigation for filters and sort
      1. Sticky panels and scroll traps on mobile
      1. Color contrast for tags/badges/toasts

4. **Checkout route readiness (if intended for this milestone)**
   1. Confirm route structure under `src/app/[locale]/checkout/`:
      1. Entry page, success page, error/cancel paths
   1. Validate guest checkout path is coherent end-to-end.
   1. Payment UI is presentational vs actually wired; decide what “done” means now.

5. **Documentation and changelog discipline**
   1. Decide whether `PLAN.md` is “living product plan” (kept) or “internal notes” (kept elsewhere).
   1. If `CHANGELOG.md` is new, define format (Keep a Changelog vs simple release notes) and start with the next milestone entry.
   1. If WIKI files are intended, decide whether they live in-repo or in GitHub Wiki/Docs site.

6. **Verification checklist before shipping**
   1. Build passes.
   1. Lint/typecheck passes.
   1. Basic smoke test:
      1. Navigate homepage → flights → detail → checkout → success
      1. Locale switch doesn’t break routes
      1. No console errors on the flights page

---

## Next Ship Milestone (Proposed)

**Milestone: “Flights v1 Release Candidate” (UI + core interactions)**

**Scope**
1. Flights listing page is stable on desktop and mobile.
2. Filters + sort work predictably with clear empty/loading states.
3. Flight detail navigation exists (slug route) and is reachable from listing.
4. Price tracking / save flight works locally (localStorage), clearly labeled as “alerts are local-only” unless backend notifications are included.

**Explicitly Out of Scope (for this milestone)**
1. Predictive Trip Bundler (Phase 11) unless you confirm it’s the focus.
2. Real notification delivery (Supabase email) for price alerts.
3. Advanced experiments (voice map, AR sizer, etc.) unless already integrated and stable.

---

## Blockers / Questions (Need Your Answers)

1. **What do you want to ship next: Flights, Checkout, or Predictive Trip Bundler?** Pick one as the milestone owner.
2. **Are the many untracked folders (`components/`, `lib/`, `pages/`, `scripts/`) intentionally new product code, or generated/experimental?** This determines whether we stage them or ignore them.
3. **Should wiki and sync log files be committed?**
   1. `SYNC_LOG.md` vs `sync_log.md`: which one is canonical?
   1. Are these produced by a cron and expected in git, or should they be `.gitignore`’d?
4. **Is the flights experience expected to be server-rendered from real APIs now, or still using `src/data/flights.ts` mock data?** “Ship” criteria differs a lot.
5. **What is your definition of “done” for checkout right now?**
   1. Pure UI flow is fine?
   1. Or must it be integrated with a payment provider?
## 2026-05-10 17:51 UTC

GIT_STATUS
main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

GIT_DIFF_STAT
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT
(first 120 lines read; excerpt omitted here for brevity in log)

OPENCODE_PLAN_OUTPUT
**Prioritized TODO Plan (Ship-First)**

1. **Stabilize the flights listing page (`src/app/[locale]/flights/page.tsx`)**
1. **Define and lock the data contract** between `src/data/flights.ts` and UI components:
   - Required fields (id, price, airline, times, stops, duration, baggage, etc.)
   - Sorting keys (price, duration, departure time, “best” score)
   - Filter facets (stops, airlines, time windows, price range)
1. **Make the list page shippable as an MVP**:
   - Listing renders on first load with realistic sample data
   - Filters + sort work deterministically
   - Empty states, loading states, “no results” state
   - Mobile layout sanity check (filters UX especially)
1. **Error-proofing**:
   - Guard against undefined fields / malformed flight objects
   - Ensure stable keys and predictable ordering
   - Avoid hydration/client-only pitfalls if any components assume `window`

2. **Integrate the core listing components as a cohesive UX**
1. Wire together (at minimum): `FlightCard`, `FlightFilters`, `FlightSortSelect`
1. Decide what’s MVP vs later for these “nice-to-have” components:
   - `DynamicPriceChart`, `SocialProofToast`, `SustainabilityScore`, `SavedSearches`
1. Confirm the “Compare” interaction:
   - `ComparePanel` selection model (max items? persist across filters?)
   - What happens on route change?

3. **Implement “Detail + Checkout” spine (thin slice)**
1. Detail route: `src/app/[locale]/flights/[slug]/`
   - Minimal detail page from listing selection (slug strategy: id-based)
   - CTA: “Continue to checkout”
1. Checkout route: `src/app/[locale]/checkout/`
   - Minimal passenger + contact form (even stubbed)
   - Summary of selected flight
   - Confirmation page/state (even if it’s a fake “success”)

4. **Repo hygiene to enable shipping**
1. Decide what untracked docs belong in repo:
   - Keep **one** canonical changelog/log (`CHANGELOG.md` vs `SYNC_LOG.md` vs `sync_log.md`)
   - `WIKI*.md` policy (generated or curated?)
1. Ensure new directories (`components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`) have a clear purpose; avoid parallel “two app routers” confusion if this is Next.js App Router based.

---

## Next Ship Milestone (1 sprint / 1-2 days depending on scope)

**Milestone: “Flights MVP: Search, Filter, Sort, Compare, and Start Checkout”**

**Definition of Done**
1. `/[locale]/flights` page renders a usable results list from `src/data/flights.ts`
1. Filters + sort are functional, predictable, and fast enough for sample dataset
1. Users can select a flight and navigate to `/[locale]/flights/[slug]`
1. From detail, users can start `/[locale]/checkout` and see selected flight summary
1. Mobile experience is acceptable (filters interaction is the usual breaker)
1. Basic empty/error states exist

---

## Blocker / Clarifying Questions (answer these to de-risk execution)

1. **Next.js architecture:** Is this repo intended to be App Router only (`src/app/...`) or are `pages/` + `src/pages/` intentionally present? If not intentional, we should avoid expanding the wrong routing system.
1. **Data source direction:** Is `src/data/flights.ts` purely mock data for now, or should we design it to match a future API response (and if yes, which provider shape)?
1. **Slug strategy:** Should flight detail use a stable `id` (recommended) or a human-readable slug (airline-from-to-date)? Any SEO requirement now?
1. **MVP scope for “compare”:** How many flights can be compared (2-4)? Should selection persist if filters change?
1. **Locale behavior:** How many locales are supported today, and do we need currency/number/date formatting in MVP?
1. **Checkout realism:** Is checkout just a UI flow (no payments) for now, or do we need integration points (payment provider, booking engine) stubbed cleanly?

\n---\n## 2026-05-10 18:02:52 UTC\n
### git status -sb\n\n```\n
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n```\n
### git diff --stat\n\n```\n
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n```\n
### PLAN.md (1-120)\n\n```\n
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n```\n
### plan report\n\n
**Onceliklendirilmis TODO Plani (Ship odakli)**

1. Calisan durumu netlestir (hizli triage)
   1. Ucus listeleme sayfasi (`src/app/[locale]/flights/page.tsx`) yeni eklenen 290+ satirin ana akisini belirle: filtreleme, siralama, kartlar, state yonetimi, URL parametreleri, performans.
   2. `PLAN.md` degisikliklerinin amaci: roadmap guncellemesi mi yoksa davranissal degisiklikleri mi dokumante ediyor, ayir.
   3. Untracked dosyalarin kapsamini siniflandir: dokumantasyon (CHANGELOG/WIKI), yeni feature kodu (components/lib/pages/scripts/src/app/...).

2. Ucus modulu icin "Minimum Shippable" hedefini sabitle
   1. Listeleme: arama sonucu gorunur, filtreler calisir, siralama calisir, bos sonuc durumu.
   2. Detay sayfasi (`src/app/[locale]/flights/[slug]/` var gorunuyor): route calisir, fiyat takibi/localStorage, yan panel.
   3. Checkout baglantisi: secilen ucus checkout akisini aciyor (`src/app/[locale]/checkout/` var gorunuyor).

3. Stabilizasyon ve regresyon onleme
   1. TypeScript hatalari: yeni eklenen bilelsenler ve sayfalar compile ediyor mu.
   2. Server/Client boundary: App Router dosyalarinda `use client` gereken yerler dogru mu.
   3. i18n/locale routing: `[locale]` altinda linkler ve navigation tutarli mi.
   4. UI durumlari: loading, error, empty, filter reset, mobile responsive.

4. Kod organizasyonu ve bagimlilik hijyeni
   1. Duplicated path riski: hem `pages/` hem `src/pages/` hem de `app/` var. Next davranisi karisabilir.
   2. `components/` root ile `src/components/` ayni anda var: import yol standardi belirle, cakisma riskini azalt.
   3. `lib/` ve `scripts/` eklemeleri: runtime mi build-time mi netlestir.

5. Dokumantasyon ve release hazirligi
   1. `CHANGELOG.md` girisini "Flights module listing+detail+checkout" odakli yap.
   2. `SYNC_LOG.md` ve `WIKI_SYNC.md` otomasyon urunu mu: repoda kalmali mi yoksa ignore mu edilmeli.
   3. `WIKI.md`: product spec mi, developer guide mi ayir.

---

**Sonraki Ship Milestone (1 sprintlik hedef)**

**Milestone: Flights v1 (Search + Listing + Detail + Checkout handoff)**

Kabul kriterleri:
1. `/[locale]/flights` sayfasi: filtrele + sirala + kartlar calisiyor, mobilde bozulmuyor.
2. `/[locale]/flights/[slug]` sayfasi: secilen ucus detayi, fiyat takibi (localStorage), CTA ile checkout gecisi.
3. Checkout sayfasi: ucus secimi summary olarak gorunuyor, odeme akisi tamamlanabiliyor (mock bile olsa).
4. Build/Typecheck: hatasiz.
5. Basit e2e manuel senaryo: arama -> filtre -> detay -> checkout.

---

**Blockerlar / Riskler**

1. Next routing cakismasi riski: `pages/` + `src/pages/` + `src/app/` birlikteyse build davranisi beklenmedik olabilir.
2. Import path ve component duplikasyonu: `components/` ve `src/components/` paralel olmasi "hangi component kullaniliyor" belirsizligi yaratir.
3. Untracked dosya sayisi cok fazla: bunlarin hepsi ayni release icin mi, yoksa bir kismi deneysel mi ayiklamak gerekir.
4. Plan dosyasinda "cron her 10 dk" notu var: repoda otomatik degisen dosyalar CI ve diff gurultusu yaratabilir.

---

**Soru Listesi (Karar icin gerekli)**

1. Bu ship icin hedefin nedir: sadece Flights (listing+detail+checkout) mi, yoksa bu untracked modullerin tamami mi?
2. `pages/` ve `src/pages/` bilerek mi eklendi? Bu proje App Router uzerinden mi ilerleyecek, yoksa hibrit mi?
3. `SYNC_LOG.md`, `sync_log.md`, `WIKI_SYNC.md` dosyalari repoda kalacak mi yoksa gitignore mu istiyorsun?
4. Componentler icin tercih: `src/components/*` tek kaynak olsun mu, yoksa root `components/` kalacak mi?
5. Checkout akisi: gercek odeme entegrasyonu hedef mi, yoksa su an sadece UI/flow mu?
## 2026-05-10 18:12 UTC

GIT_STATUS:
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

GIT_DIFF_STAT:
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT (1-120):
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

OPENCODE_PLAN_REPORT:
Onceliklendirilmis TODO Plani (izgetour)

1. Repo hijyeni ve degisiklik siniri belirleme (hemen)
1. Calisma kapsaminda hangi hedefi ship edecegimizi netlestir: Flights listing mi, Flights detail mi, Checkout mu?
1. Untracked cok sayida dosya/klasor var: components/, lib/, pages/, scripts/, src/app/[locale]/checkout/, src/app/[locale]/flights/[slug]/, bircok src/components/*.tsx, src/data/flights.ts, dokumanlar (CHANGELOG.md, WIKI*.md, SYNC_LOG.md, sync_log.md).
1. Iki farkli log dosyasi var gibi: SYNC_LOG.md ve sync_log.md (case farki). Tek standarda indirilecek mi karar ver.
1. Ship edilecek milestone icin minimum gerekli dosyalar listesini cikar ve digerlerini sonraya it (aksi halde PR/commit cok buyur, review zor).

2. Flights sayfasi (listing) stabilizasyonu
1. src/app/[locale]/flights/page.tsx icin hedef davranisi tanimla: filtreleme, siralama, kart tasarimi, mock data mi gercek data mi.
1. UI/UX kabul kriterleri yaz: bos durum, loading, hata durumu, mobil/desktop kirilimlari, pagination veya infinite scroll var mi.
1. Filtre ve sort state yonetimi: URL query params ile senkron olacak mi (shareable link) karar ver.
1. Performans: listingte agir komponentler varsa (chart, AI planner, voice map) lazy load / progressive disclose stratejisi belirle.
1. i18n: [locale] rotasinda metinlerin ve para/tarih formatlarinin locale uyumu kontrol listesi.

3. Flights detail rotasi ve data modelleme
1. src/app/[locale]/flights/[slug]/ icin route kontratini belirle: slug neyi temsil ediyor (id, route-key, SEO slug)?
1. src/data/flights.ts veri semasini kilitle: zorunlu alanlar (price, times, stops, baggage, airline, deeplink) ve opsiyoneller.
1. Listing -> detail navigasyonunun tekil kaynakla calismasi: karttaki veriler detailde tutarli mi.

4. Checkout akisi (MVP)
1. src/app/[locale]/checkout/ icin MVP scope: yolcu bilgileri, odeme (mock), onay sayfasi, email/PNR (mock) netlestir.
1. Form dogrulama ve hata mesajlari: accessibility (aria, keyboard) kabul kriterleri.
1. State guvenligi: refresh olunca sepet/rezervasyon bilgisi kaybolacak mi? (session/local storage vs server) karar sorusu.

5. Yeni komponentlerin rasyonalizasyonu (cok sayida yeni fikir)
1. Untracked komponentleri kategorize et:
1. Flights core: FlightCard, FlightFilters, FlightSortSelect, ComparePanel, DynamicPriceChart, SavedSearches, MultiCityRouter
1. Cross-sell/engagement: GamificationBadges, LoyaltyTierSystem, SocialProofToast, TripCountdownWidget, SustainabilityScore
1. Novelty/expensive: VoiceInteractiveMap, AITravelPlanner, SmartItinerary, DynamicCuisineRecommender, MoodDestinationPicker, LuggageArSizer, PartyPlan
1. MVP icin core disindakileri default kapali/sonraya planla. Aksi halde scope patlar.

6. Dokumantasyon ve release notlari
1. PLAN.md degisikliklerini ship edilecek milestone ile uyumlu hale getir (fazlar, modul listesi, tamamlandi/devam ediyor durumu).
1. CHANGELOG.md icin format karari: semver mi, tarih tabanli mi, Keep a Changelog mi.
1. WIKI.md ve WIKI_SYNC.md amaci: internal onboarding mi, otomasyon mi? Tek kaynaga indirilecek mi.

7. Test ve kalite kapilari
1. En azindan smoke test listesi: flights listing render, filter/sort, detail route, checkout first step.
1. Lint/typecheck/build kapilari: CI var mi? yoksa lokal komutlarla minimum dogrulama tanimi.
1. Basit e2e hedefi: listing -> detail -> checkout navigation.

Next Ship Milestone (onerilen): Flights MVP v1
- Kapsam: flights listing (filter+sort+card+states), flights detail temel, checkout ilk adim + onay (mock)
- Dis kapsam: AI planner, voice map, AR sizer, gamification/loyalty, cuisine, sustainability (sonraki milestone)

Blockerlar / Sorular
1. Oncelik: Flights MVP mi yoksa Predictive Trip Bundler (Faz 11) mi?
1. Data kaynagi: src/data/flights.ts kalici mock mu, API yakinda mi?
1. pages/ ve src/pages/ birlikte: hedef app router mi pages router mi?
1. SYNC_LOG.md ve sync_log.md ikisi de kalacak mi?
1. Checkout odeme: tamamen mock mu, provider hedefi var mi?
1. i18n: hardcoded mi, message catalog bekleniyor mu?
1. Untracked komponentler: hepsi kullaniliyor mu, prototip mi, MVP icin hangileri gerekli?

---


---
TIMESTAMP: 2026-05-10 18:21 UTC
REPO: /home/turk/projects/izgetour
GIT_STATUS:
main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

GIT_DIFF_STAT:
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT_1_120:
(see repo file; excerpt captured in run logs; no secrets detected)

PLAN_REPORT:
Prioritized TODO Plan (Read-Only, No Tools, No Code)

1. Decide Scope for Next Ship
- Lock the ship target to one thin vertical slice: Flights listing (filters + sort) -> flight detail -> checkout.
- Define done for this slice: user can search/browse, filter/sort, open detail, proceed through checkout with clear success/failure states.
- Freeze everything else (AI travel planner, AR sizer, gamification, social proof, multi-city) as post-ship unless already wired and stable.

2. Stabilize the Current Flights Listing Page Change
- Review the large src/app/[locale]/flights/page.tsx expansion and identify: data source, state shape, filters, sort, pagination/infinite scroll, and any client/server component boundaries.
- Ensure the page has a predictable empty / loading / error / results state model.
- Confirm filter logic correctness (idempotent, composable, no contradictory states) and sort determinism.
- Validate perf risks: large in-memory filtering/sorting, rerender loops, expensive derived state.

3. Rationalize the New File/Folder Explosion
- Triage untracked additions into buckets: needed for ship slice vs not needed vs docs/meta.
- Decide explicitly what will be included in the next milestone branch/PR vs deferred.

Next Ship Milestone (Suggested)
Milestone: Flights MVP v1
Deliverables: /[locale]/flights, /[locale]/flights/[slug], /[locale]/checkout end-to-end (checkout can be mocked).

Blockers / Questions
- Router choice: ship App Router (src/app) only? What about pages/ and src/pages/?
- Scope control: only flights + checkout, or include other verticals?
- Data realism: mock flights.ts vs real API now?
- Checkout realism: payment out of scope vs integrate now?
\n---\n## 2026-05-10 18:32:51 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (first 120 lines excerpt)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### Plan report
**Next Ship Milestone (v0.1 “Flights Listing MVP”)**  
Ship a stable, production-ready Flights listing page with the new UI (filters, sorting, cards) that is responsive, accessible, i18n-correct, and wired to the current data model (even if it is still mocked). Success = page loads without runtime errors, filters/sort work end-to-end, and navigation into flight detail (or a clearly marked “coming soon” state) is consistent.

---

**Prioritized TODO Plan**

1. **Stabilize the current worktree for a clean ship**
1. Decide what is “shipping now” vs “experimental”: Right now `src/app/[locale]/flights/page.tsx` is the only big diff, but there is a large set of new untracked modules/components. Confirm which of these are intended to land in the next milestone vs held back.
1. Ensure the repo doesn’t accidentally ship docs/logs: `SYNC_LOG.md`, `sync_log.md`, `WIKI*.md`, and `CHANGELOG.md` likely need a clear policy (commit or ignore). Duplicate casing (`SYNC_LOG.md` vs `sync_log.md`) is a release risk on case-insensitive filesystems and in CI caches.

2. **Make Flights page production-grade (core UX correctness)**
1. Validate state model: filters + sort + result list must be deterministic and composable (no contradictory state, no double-filtering, no “filter UI changes but list doesn’t update”).
1. Confirm the page is locale-safe: `[locale]/flights/page.tsx` must not hardcode strings, formats, currency, dates, or routes that break i18n routing.
1. Responsive behavior: sidebar filters should degrade cleanly on mobile (drawer/sheet pattern or collapsible sections) without layout shift.
1. Accessibility pass: keyboard navigation for filter controls, visible focus, proper labels, and no “click-only” controls.

3. **Data contract and edge cases (even with mocked data)**
1. Define/confirm a single “Flight” type shape and normalize data access (price, stops, times, cancellation, airline).
1. Handle empty/error states: zero results, invalid query params, missing data fields, and “loading” if any async is introduced later.
1. Confirm sort stability and tie-breakers (e.g., same price then shortest duration).

4. **Routing consistency**
1. If flight detail exists (`src/app/[locale]/flights/[slug]/` is present as untracked), decide whether listing cards should link to it now.
1. If not ready, enforce a consistent “disabled link / coming soon” behavior to avoid broken navigation.

5. **Project hygiene (so the next features don’t slow you down)**
1. Decide folder strategy: you currently have `pages/` and `src/pages/` untracked in a Next app that already uses `src/app/…`. Mixing routing paradigms can cause confusing behavior and build conflicts.
1. Decide component placement: there is both `components/` and many under `src/components/…`. Pick one convention to prevent import churn.
1. Decide which “2026 trend” modules are shipping artifacts vs backlog; otherwise the repo accumulates a lot of unused UI that increases bundle risk and maintenance cost.

6. **Verification gates before shipping**
1. Local build + typecheck + lint (whatever the repo uses).
1. Quick manual QA script:
   - Open flights listing in 1 locale and at least one alternate locale.
   - Apply multiple filters, clear filters, change sort, verify results update.
   - Mobile viewport smoke test.
   - Click first card to verify navigation behavior (detail or expected placeholder).
1. If there is CI, ensure it passes on a clean checkout (case-sensitivity issues show up here).

---

**Blockers / Questions (need your decision to proceed cleanly)**

1. **Scope decision:** Should the many untracked components/modules land in the next milestone, or should the next ship only include the flights listing page changes?  
   - If “only flights listing”, I’d treat the other modules as backlog and keep them out of the ship to reduce risk.
2. **Routing decision:** Are you committing to `app/` router only, or do you intentionally want `pages/` and `src/pages/` present too? (This is a common source of subtle conflicts.)
3. **Docs/log policy:** Should `SYNC_LOG.md`, `sync_log.md`, and `WIKI*.md` be committed, or ignored (generated by cron)? Also which casing is canonical to avoid duplicates?
4. **Detail page readiness:** Should flight cards link into `/flights/[slug]` now, or do you want listing-only for this milestone?
5. **Data source:** Is `src/data/flights.ts` the canonical mocked data for now, or do you want the listing page to be built to accept server-fetched data immediately (even if stubbed)?

If you answer just (1) shipping scope and (2) routing strategy, the rest of the plan can be locked quickly into a tight milestone without accidental repo sprawl.
\n---\n# 2026-05-10 18:42:42 UTC
\n## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## Plan report
**Prioritized TODO Plan (Ship-First)**

1. **Stabilize the current flight listing page change (src/app/[locale]/flights/page.tsx)**
   1. Confirm it compiles in isolation: no missing imports, no unused/implicit `any`, no server/client boundary violations (common in App Router).
   2. Ensure the page has a single clear “happy path”: search params in → list renders → filters/sort update deterministically.
   3. Verify any new components used by the page are actually in the correct folder (`src/components/...` vs `components/...`) and import paths match the repo conventions.
   4. Make sure the listing doesn’t regress on mobile: filter drawer behavior, sort control accessibility, long card layout overflow.

2. **Define “module completion” for Flights and lock the scope**
   1. Decide what “done” means for this milestone: “Flight listing page + filtering + sorting + basic detail navigation” vs “all the new trend components integrated.”
   2. Defer anything that’s “nice-to-have / trend module” unless it directly improves conversion on the flight listing.

3. **Integrate only the minimum required new assets/data**
   1. If `src/data/flights.ts` is the backing data, make it the single source of truth for the listing and remove duplicate mock data sources (even if only conceptually for now).
   2. Ensure filters/sort options align with available data fields (airline, stops, price, time, cancellation) to avoid “filter does nothing” UX.

4. **Route integrity: listing → detail → checkout**
   1. Confirm expected navigation paths exist: `src/app/[locale]/flights/[slug]/` and `src/app/[locale]/checkout/`.
   2. Make sure slugs are stable and reproducible (derived from flight ID) so bookmarks and saved searches don’t break.
   3. Validate checkout accepts a selected itinerary/flight reference and renders an order summary without relying on ephemeral client state.

5. **Documentation + release hygiene (fast)**
   1. Decide what `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`, `sync_log.md` are for, and whether they are meant to be committed or are generated artifacts.
   2. Ensure `PLAN.md` remains high-level and does not drift into “implemented ✅” without a verifiable checklist.

6. **Quality gates (pre-ship)**
   1. Typecheck + lint + build (whatever your standard commands are).
   2. Smoke test: flights listing render, filter, sort, navigate to detail, enter checkout.
   3. Basic accessibility: keyboard navigation for filters/sort, focus states, aria labels where needed.

---

**Next Ship Milestone (1 release)**

**Milestone: “Flights MVP End-to-End”**
- Flight listing page (`/flights`) renders from a single data source.
- Filters + sort work and are reflected in URL/search params (or a consistent state model).
- Flight detail (`/flights/[slug]`) renders key details (baggage, aircraft, refund/cancel rules) and supports “price tracking” (localStorage-based is fine for MVP).
- Checkout flow accepts a selected flight and shows a stable summary.

This is the smallest milestone that is user-facing, testable, and monetizable without pulling in the rest of the “trend modules.”

---

**Blockers / Questions (need your decision to proceed cleanly)**

1. **Which untracked directories are real product code vs generated/vendor content?**
   - You have both top-level `components/`, `lib/`, `pages/` and also `src/components/`, `src/pages/`. Is this intentional (migration in progress), or accidental duplication? This impacts imports, routing, and build output.

2. **Should wiki/sync logs be committed?**
   - `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md`, `sync_log.md` look like automation outputs. Are these intended to live in git, or should they be ignored via `.gitignore`?

3. **Source of truth for routing: App Router vs Pages Router**
   - Presence of `src/app/...` plus `pages/`/`src/pages/` suggests mixed routing. Is the app fully App Router now, or partially? This affects how `page.tsx` is expected to behave (server vs client components).

4. **What is the acceptance criteria for “Predictive Trip Bundler” (currently 🔄)**
   - Is it part of the next ship, or explicitly out-of-scope until Flights MVP is stable? Without this decision, scope creep is likely.

5. **i18n expectations for Flights**
   - Should filters/sort labels and currency formatting be locale-aware now, or can we ship Turkish-first and retrofit?

If you answer (1) and (2) alone, the plan becomes much more executable because it clarifies what should be staged/committed for the next release.
\n## 2026-05-10 19:02:48 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md excerpt (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### Plan report
**Onceliklendirilmis TODO Plani (Ship odakli)**

1. Degisiklik kapsamini netlestir ve stabilize et
1. Mevcut degisim setini sinirla: `PLAN.md` ve `src/app/[locale]/flights/page.tsx` icindeki 293 yeni satir hangi kullanici hikayelerini tamamliyor, hangileri deneysel, ayristir
1. Untracked cok sayida dosya var: `components/`, `lib/`, `pages/`, `scripts/`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, `src/components/*`, `src/data/flights.ts`, `src/pages/`, `sync_log.md` gibi. Bunlari ship icin zorunlu olanlar ve sonraya kalacaklar diye ayir
1. Repo yapisi riski: hem `pages/` hem `src/pages/` hem de `src/app/` gorunuyor. Routing ve build cakismasi yaratabilecek noktalari listele

1. Ucus listeleme sayfasi icin Minimum Shippable Slice tanimla
1. Flights listing icin hedef davranisi yaz: arama girisi -> sonuclari goster -> filtrele -> sirala -> karttan detay/checkout akisi
1. Kullaniciya gorunen ana kabul kriterleri: hizli yuklenme, filtre/siralama dogru calisiyor, bos sonuc durumu, hata durumu, mobil uyum

1. Entegrasyon ve veri akislarini netlestir
1. Ucus verisi kaynagi: `src/data/flights.ts` mock mu kalacak, yoksa API adapter var mi
1. Filtre ve siralama state yonetimi: URL query ile mi, client state ile mi. SEO ve shareable link ihtiyacini belirle
1. i18n: `[locale]` altinda metinler nasil yonetiliyor, stringler hardcoded mi, ceviri dosyalari mi var

1. Kalite ve risk azaltma
1. Tip guvenligi: flights data sekli ile `FlightCard`, `FlightFilters`, `FlightSortSelect` prop tipleri uyumlu mu
1. Performans: 290 satirlik `flights/page.tsx` icinde gereksiz re-render, buyuk liste renderi, expensive hesaplar var mi. Gerekirse sayfayi parcalara bolme ihtiyacini not et (ama ship icin minimum)
1. UI durumlari: loading, empty, error, no-match filter, reset filters
1. Checkout baglantisi: listingten checkouta giden pathler ve parametreler stabil mi

1. Dokumantasyon ve release hijyeni
1. `CHANGELOG.md` ve `SYNC_LOG.md` / `sync_log.md` adlandirma ve tekrar problemini cozu: tek kaynak belirle
1. `WIKI.md` ve `WIKI_SYNC.md` ne icin: otomasyon mu, manuel mi. Ship icin gerekli degilse sonraya ertele
1. `PLAN.md` guncellemesi: tamamlanan fazlar ile gercek durum uyusuyor mu

---

**Bir Sonraki Ship Milestone (onerilen)**

Milestone adi: **Flights Listing MVP v1**

Kapsam (shipte mutlaka):
1. `/[locale]/flights` sayfasi stabil aciliyor
1. Mock veri ile ucus kartlari listeleniyor (en azindan demo kalitesi)
1. Temel filtreler calisiyor: fiyat araligi, airline, stops gibi en kritik 2-3 filtre
1. Temel siralama calisiyor: en ucuz ve en kisa gibi
1. Empty state ve reset filters var
1. Mobilde bozulma yok (liste, filtre paneli)

Ship disi (hemen sonraya):
1. Compare panel, price chart, AI planner gibi advanced moduller
1. Real API entegrasyonu ve price alert bildirim altyapisi
1. Multi-city router ve voice map gibi deneysel ozellikler

Cikis kriteri:
1. Demo akisi 2 dakikada sorunsuz: listing -> filtrele -> sirala -> kart detayina git veya checkout baslat
1. Build ve basic lint/test (varsa) temiz

---

**Blokerler ve Sorular (cevaplarina gore plan netlesecek)**

1. Ship hedefi nedir: sadece demo mu, yoksa prod kullanicisi gorecek mi
1. Su an `main...origin/main [ahead 1]`: bu 1 commitin icerigi flights degisiklikleri ile uyumlu mu, yoksa baska bir sey mi
1. Untracked klasorler cok genis: bunlarin hepsi yeni feature set mi, yoksa generator/cron ciktilari mi
1. Routing karari: Bu repo App Router mi kullaniyor, yoksa Pages Router da aktif mi. `pages/` ve `src/pages/` ne kadar kritik
1. Flights data kaynagi: `src/data/flights.ts` kalici mock mu, gecici mi. API planiniz var mi
1. Checkout entegrasyonu: listingten checkouta hangi bilgi seti aktarilmali (flight id, price breakdown, baggage, cancellation)
1. i18n kalite beklentisi: EN ve TR her ikisi shipte zorunlu mu, yoksa tek locale ile mi cikiyoruz
1. Changelog ve wiki dosyalari shipte isteniyor mu, yoksa cleanup sonraya mi kalsin
\n## 2026-05-10 19:11 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (lines 1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### Plan report
**Prioritized TODO Plan (Next 1-3 Days)**

1. **Stabilize repo state and scope what’s “real” vs scaffolding**
1. Decide what to do with the large set of untracked additions (`components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, many `src/components/*`, new `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, `src/data/flights.ts`, plus docs/log files).
1. Confirm which of these are intended to ship now vs future/prototype. This prevents a huge, risky merge of unrelated features.

2. **Flights listing page hardening (high risk surface)**
1. Review `src/app/[locale]/flights/page.tsx` for correctness and performance (290+ LOC added suggests substantial UI and logic).
1. Validate key UX flows: search parameters, filtering, sorting, pagination/infinite, empty/error states, mobile layout, and i18n behavior under `[locale]`.
1. Ensure no client-only APIs (e.g., `localStorage`, `window`) are used in a way that breaks SSR or causes hydration issues, especially inside `app/` routes.

3. **Route structure consistency (Next.js + app router vs pages)**
1. Choose one routing strategy for production: `src/app` (App Router) vs `pages/` or `src/pages/`.
1. If both exist intentionally, define clear ownership: what lives where, and ensure no conflicting routes (e.g., `/flights` defined twice).

4. **Checkout path sanity**
1. Confirm the new `src/app/[locale]/checkout/` aligns with the stated “Faz 6/7 completed” claim in `PLAN.md`.
1. Verify the checkout entry points from flights/tours/hotels go to a single canonical checkout flow (avoid multiple partially implemented versions).

5. **Documentation hygiene for shipping**
1. Decide whether `CHANGELOG.md`, `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md` and `sync_log.md` are meant to be committed.
1. If they are automated/cron artifacts, consider excluding them from the release payload and ensuring they do not churn diffs.

6. **Feature flagging / release slicing for “trend modules”**
1. Many components look “ready” but likely not integrated or tested end-to-end (AI planner, voice map, AR sizer, sustainability, loyalty, etc.).
1. Gate non-core modules behind an explicit “disabled by default” integration approach so the shipped milestone stays stable.

---

**Next Ship Milestone (Recommended)**

**Milestone: “Flights v1 Public Beta (Stable UI + Checkout Entry)”**

- Ship a stable `/[locale]/flights` listing experience with:
  - reliable filter + sort behavior
  - solid mobile layout
  - clear empty/error states
  - deterministic SSR/hydration behavior
- Ensure a single, working transition from a selected flight to checkout (even if payment integrations are mocked/stubbed, the flow and data passing should be correct).
- Keep “trend” modules (AI bundler, AR sizer, voice map, etc.) out of the default UI unless already fully integrated and tested.

---

**Blockers / Questions (Need Your Decisions)**

1. **What is the intended shipping set right now?**
   - Are the many untracked directories/files meant to be included in the next release, or are they experimental scaffolds?

2. **Routing decision: App Router only, Pages Router only, or hybrid by design?**
   - The presence of both `pages/` and `src/pages/` alongside `src/app/...` is a major ambiguity that can create route conflicts and maintenance debt.

3. **Are the new docs/log files canonical?**
   - Should `SYNC_LOG.md`, `sync_log.md`, `WIKI_SYNC.md` be committed, or are they generated outputs that should be excluded?

4. **What does “Predictive Trip Bundler is continuing” mean in concrete terms?**
   - Is it already wired into selection -> checkout, or only a standalone component? If standalone, should it be in the next milestone or deferred?

5. **Quality bar for this ship**
   - Do you want a “demo-ready” release (best visuals, some rough edges OK) or “beta-ready” (fewer features, stronger correctness and testing)?
\n## 2026-05-10 22:57 UTC

Branch: ## main...origin/main [ahead 1]

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

### Plan report
**Prioritized TODO Plan (Ship-focused)**

1. **Stabilize the repo state (scope control)**
   1. Decide what is “in-scope” for the next release: right now you have 1 ahead commit plus a large set of new untracked directories (`components/`, `lib/`, `pages/`, `scripts/`, new routes under `src/app/[locale]/...`, and many new components).
   1. Define a “ship set” by answering: are these untracked directories real new product work, or generated / experimental / sync artifacts?
   1. If anything is generated or sync-only: move it out of the app bundle (or exclude later), but first classify it.

2. **Make the flights listing page production-safe**
   1. Review `src/app/[locale]/flights/page.tsx` changes (large diff: +290 lines) for:
      1. Data source: static mock vs real integration points.
      1. Client/server boundaries: ensure no accidental client-only APIs in a server component (or vice versa).
      1. Performance: large in-memory filtering/sorting can be OK for mock data but must be structured for server-side pagination later.
      1. URL-driven state: filters/sort should be reflected in query params (or intentionally not), to support shareable searches.
   1. Confirm the “✅ Tamamlandı” status in `PLAN.md` matches reality for flights: listing, filters, sort, card components, detail link behavior.

3. **Route hygiene and Next.js structure sanity**
   1. Validate you are not mixing incompatible routing paradigms:
      1. You have `src/app/...` plus an untracked `pages/` and `src/pages/` simultaneously. That is a major risk area (double routing, unexpected precedence, build/runtime confusion).
   1. Decide one:
      1. App Router only (likely, given `src/app/[locale]/*`), and treat `pages/` as legacy and remove/ignore.
      1. Or explicitly support both (rarely worth it unless already committed architecture).
   1. Inventory what the new untracked routes under `src/app/[locale]/checkout/` and `src/app/[locale]/flights/[slug]/` contain and whether they duplicate already-completed work.

4. **Checkout end-to-end verification**
   1. Since checkout is marked complete across multiple phases, confirm:
      1. Happy path: select flight -> go to checkout -> payment success screen.
      1. Guest checkout works.
      1. i18n locale routing doesn’t break checkout state.
   1. If “payment” is stubbed, ensure UX clearly indicates demo state (no false claims).

5. **Documentation and project hygiene**
   1. Decide what `CHANGELOG.md`, `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md`/`sync_log.md` are for:
      1. If these are operational/sync artifacts, keep them but ensure they do not ship into runtime or confuse contributors.
      1. Resolve case-duplication risk: having both `SYNC_LOG.md` and `sync_log.md` can break cross-platform checkouts (macOS default case-insensitive).
   1. Update `PLAN.md` to reflect what is truly shipped vs prototyped (it currently reads very “everything is done”).

6. **Minimum test/QA bar (even without adding new tests yet)**
   1. Run a minimal acceptance checklist (manual is fine for first ship milestone):
      1. Build succeeds.
      1. Flights page loads in at least 2 locales.
      1. Filters/sort do not throw and have deterministic output.
      1. Flight detail page loads for at least 1 slug.
      1. Checkout flow renders without runtime errors.
   1. Identify the first automated test you actually want (later): usually one smoke test for routing and one for a critical UI state transition.

---

**Next Ship Milestone (Recommended)**

**Milestone: “Flights MVP + Checkout Demo Flow (App Router-only)”**

Definition of Done:
1. `src/app/[locale]/flights` listing is stable, responsive, and shareable (either via URL params or a clear non-shareable stance).
2. Flight detail (`/flights/[slug]`) renders from the same data model as listing (even if mocked).
3. Checkout route works end-to-end from a selected flight.
4. Repo routing structure is unambiguous (no accidental `pages/` routing conflicts).
5. Non-product artifacts (`WIKI_SYNC`, sync logs) are clearly separated from shipping code and do not introduce platform conflicts.

---

**Blockers / Questions (Need your decisions to proceed cleanly)**

1. **Routing decision:** Are you intentionally using both App Router (`src/app`) and Pages Router (`pages/` or `src/pages/`), or should `pages/` be removed/ignored as legacy?
2. **Source-of-truth for flights:** Is `src/data/flights.ts` the intended mock source, or do you already have an API/Supabase table schema to target next?
3. **What is “ship-worthy” vs “prototype components”?** Many components are introduced as “ready ✅”. Do you want them included in the app UI now, or kept as a component library for future wiring?
4. **Sync artifacts:** What creates `WIKI_SYNC.md`, `SYNC_LOG.md`, and `sync_log.md`? Can we standardize to one file name to avoid case-sensitivity issues?
5. **Locale strategy:** Which locales must be correct for the milestone (e.g. `tr` and `en`), and are there any hard requirements for SEO (localized metadata, canonical URLs) at this stage?
\n---\n# izgetour plan report\nTime: 2026-05-10 23:08:29 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md first 120 lines
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan output
**Onceliklendirilmis TODO Plani (Ship odakli)**

1. Calisma agacini temizle ve kapsam daralt  
- Bu branch ana dala gore ahead 1, ayrica cok sayida untracked var. Ilk hedef: tek bir milestone icin gerekli minimum dosyalari secmek, geri kalanini ayirmak.  
- Untracked dokumantasyon dosyalari (CHANGELOG.md, WIKI*.md, SYNC_LOG*.md) ile urun kodu degisikliklerini ayni teslimatta karistirmamayi hedefle.

2. Ucus listeleme sayfasi degisikliklerini urun seviyesinde dogrula  
- `src/app/[locale]/flights/page.tsx` icin beklenti: performans, filtreleme, siralama, kart renderi, state yonetimi, i18n uyumu.  
- Kabul kriterleri: sayfa acilis hizi kabul edilebilir, filtreler deterministik, siralama dogru, bos durumlar ve hata durumlari net.

3. Veri ve component bagimliliklarini netlestir  
- Yeni `src/data/flights.ts` ve `src/components/*` altindaki FlightCard, FlightFilters, FlightSortSelect gibi dosyalarin hangi sayfalarda kullanildigini tek tek haritalandir.  
- App Router ile `pages/` klasoru birlikte gelmis gorunuyor. Hangi router kullanilacak, iki yapi bir arada mi kalacak, yoksa biri kaldirilacak sorusunu yanitla.

4. Route yapisi ve URL sozlesmesi  
- Yeni `src/app/[locale]/flights/[slug]/` ve `src/app/[locale]/checkout/` var. Ucus secimi ile checkout akisi arasinda net bir gecis tanimla.  
- Kabul kriterleri: listing ten detail e, detail den checkout a navigasyon calisir, locale parametresi kaybolmaz.

5. Minimal test ve smoke dogrulama listesi hazirla  
- Manuel smoke: listing, filtre, sort, detail, checkout route aciliyor mu.  
- Otomatik: varsa lint ve typecheck, en azindan build calisiyor mu.

6. Dokumantasyon ve plan dosyasi revizyonu  
- PLAN.md degisikligi ship edilen milestone ile uyumlu mu kontrol et.  
- Dokumantasyon dosyalarini ship ile beraber mi, yoksa ayri PR mi karar ver.

7. Teslimat stratejisi  
- Milestone icin gerekli dosyalari commit e dahil et.  
- Geri kalan buyuk untracked seti icin ikinci milestone veya ayri dal oner.

---

**Sonraki Ship Milestone (onerim)**  
Milestone 1: Ucus listeleme deneyimini tek parca olarak ship et  
- Flights listing sayfasi: filtre, siralama, kart gorunumu  
- Ucus data kaynagi (mock ya da statik) ve gerekli componentler  
- Listing to detail temel akisi, en azindan sayfa aciliyor ve karttan gecis var

Bu milestone, kullaniciya gorunur deger uretir ve mevcut degisikliklerin ana govdesi `flights/page.tsx` buyuk eklemeyle uyumlu.

---

**Blokerler ve Sorular (yanit gerekir)**

1. Router karari  
- `pages/` ve `src/pages/` klasorleri var. Proje App Router mi kullanacak, yoksa legacy Pages Router da aktif mi kalacak

2. Untracked kapsam  
- Bu kadar cok yeni component ve klasor tek seferde mi ship edilecek, yoksa sadece flights modulu mu hedef  
- Dokumantasyon dosyalari ayni teslimatta isteniyor mu

3. Veri kaynagi gercekligi  
- `src/data/flights.ts` mock mu, yoksa gercek API entegrasyonuna baglanacak mi  
- Filtre ve siralama kurallari hangi is kurallarina gore kesinlesecek

4. i18n beklentisi  
- Locale parametresi tum yeni route larda zorunlu mu  
- Metinler hardcoded mu kalacak, yoksa i18n dosyalarina tasinacak mi

5. Performans ve kalite hedefi  
- Listing sayfasinda hedeflenen max render suresi veya max kart sayisi var mi  
- Mobil oncelik seviyesi nedir

Bu sorulara net yanit verirsen, sonraki adimda TODO listesini tek bir milestone icin daha da daraltip uygulanabilir, sirali bir teslim akisi haline getirebilirim.
\n---\n## 2026-05-10 23:17 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md head (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### Plan report (opencode plan agent)
**Onceliklendirilmis TODO Plani**

1. Calisan surum kriterlerini netlestir (ship scope kilitle)
- Flights listeleme sayfasi (src/app/[locale]/flights/page.tsx) icin hedef: gercek arama entegrasyonu mu, yoksa demo/mock veri ile UI stabilizasyonu mu?
- Ucus detayi (src/app/[locale]/flights/[slug]/) ve checkout akisi (src/app/[locale]/checkout/) ile minimum entegre yol: liste -> detay -> checkout

2. Repo hijyeni ve dosya envanteri (ship oncesi risk azaltma)
- Cok sayida yeni klasor/dosya var (components/, lib/, pages/, scripts/, src/pages/, wiki/sync log dosyalari). Bunlarin hangileri urun kodu, hangileri dokumantasyon/otomasyon ayir.
- Duplicate/karisik isimleri toparla: `SYNC_LOG.md` ile `sync_log.md` ayni amac mi? Case-sensitive dosya sistemlerinde iki farkli dosya gibi davranir, CI ve deployda surpriz yaratir.

3. Flights listeleme sayfasi icin kalite bariyeri
- `src/app/[locale]/flights/page.tsx` icin: performans (render maliyeti), state karmaşıkligi, UX tutarliligi (filter/sort/pagination/empty states/loading/error)
- Filtre ve siralama: secimlerin URL parametrelerine yansimasi (paylasilabilir link) ve i18n uyumu
- A11y: klavye ile filtreleme/siralama, odak yonetimi, aria etiketleri

4. Checkout akisi icin minimum guven ve dogrulama
- Guest checkout senaryosu, form validasyonlari, hata mesajlari (i18n)
- Siparis ozeti ve fiyat hesaplari: tek kaynak (tek truth) mantigi ve tutarlilik
- Basarili odeme ekraninda sonraki adimlar: bilet/fatura, e-posta teyidi, dashboard yonlendirme

5. i18n ve routing tutarliligi
- `[locale]` rotalari ile `pages/` ve `src/pages/` klasorleri birlikte duruyor. Hangi router yaklasimi aktif? Cakisma riski var.
- Locale bazli SEO: canonical, hreflang, metadata stratejisi (minimum)

6. Dokumantasyon ve degisiklik kaydi
- `CHANGELOG.md` temelini: milestone bazli, kullaniciya donuk degisimler + teknik notlar
- `PLAN.md` guncel durum isaretleri: "tamamlandi" yazan moduller gercekten entegre mi, yoksa component hazir mi? Etiketleri ayir (Hazir component / Entegre / Prod-ready)

7. Test ve release disiplini (minimum)
- En azindan smoke test senaryolari: flights listeleme acilir, filtre/sort calisir, detay sayfasi acilir, checkout formu gecer
- Build/CI kontrolu: typescript, lint, basic runtime hata taramasi

---

**Bir Sonraki Ship Milestone (onerilen: "Flights v1 End-to-End")**

Hedef: Kullanici flights listeleme sayfasindan bir ucusu secip detaya gidebilsin ve checkout akisini tamamlayabilsin (odeme simulasyonu veya placeholder kabul).

Milestone kapsaminda "Done" kriterleri:
1. Flights listing:
- Filtreler ve siralama tutarli calisir
- Empty/loading/error durumlari var
- URL ile state paylasimi (en azindan temel parametreler)

2. Flight detail:
- Secilen ucusun net ozeti (kalkis/varis, saatler, bagaj, iade kosulu)
- Fiyat takibi (localStorage) davranisi tutarli

3. Checkout:
- Guest checkout calisir
- Siparis ozeti dogru gorunur
- Basari ekrani ve yonlendirme mevcut

4. Dokumantasyon:
- CHANGELOG.md: milestone notu
- PLAN.md: milestone status guncel

---

**Blokerler / Sorular**

1. Flights verisi kaynagi ne olacak?
- `src/data/flights.ts` mock mu, yoksa gecici mi? Gercek API/entegrasyon (Amadeus, Kiwi, Duffel vb.) planlandi mi?

2. Router mimarisi net mi?
- `src/app/[locale]/...` var ama ayni zamanda `pages/` ve `src/pages/` gorunuyor. Hangisi aktif, hangisi legacy? Cakisma ve deploy riski yuksek.

3. Yeni eklenen klasorlerin amaci
- `components/` ile `src/components/` ayni anda var. Hedef klasor yapisi hangisi?
- `lib/` ve `scripts/` icerigi nedir: runtime dependency mi, sadece dev tooling mi?

4. Wiki/sync dosyalari ship’e dahil mi?
- `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md`, `sync_log.md` deployda kalacak mi? Yoksa sadece repo ici dokumantasyon mu?

5. "Prod-ready" tanimi
- "Tamamlandi" isaretli moduller icin beklenti: sadece UI/component mi, yoksa tam entegrasyon + test + a11y + i18n mi?

Bu sorulara yanit verirsen, TODO listesini daha kesin bir scope ve sira ile "milestone backlog" formatina indirgerim (kesin kabul kriterleriyle).
\n---\n# izgetour plan report - 2026-05-10 23:28 UTC\n
## git status -sb
```
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
```\n
## git diff --stat
```
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
```\n
## PLAN.md (first 120 lines)
```
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
```\n
## opencode plan output
```
**Prioritized TODO Plan (Ship-Oriented)**

1. **Stabilize repo state and scope the change**
1. Confirm what the single “ahead 1” commit contains and whether it’s intended to land with this batch or should be split.
1. Decide whether the many untracked paths (`components/`, `lib/`, `pages/`, `scripts/`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, many `src/components/*`) are all part of the same feature set or include experiments/spikes that should be excluded from the next milestone.
1. Resolve duplicate/ambiguous logs (`SYNC_LOG.md` and `sync_log.md`) to avoid case-sensitivity issues across OSes.

2. **Make flights listing page shippable (the only clearly modified app surface)**
1. Validate `src/app/[locale]/flights/page.tsx` responsibilities: ensure it’s not doing too much (data, filters, sorting, rendering, side effects) in one file in a way that will be brittle.
1. Ensure the page works without the new component tree (graceful degradation): if any untracked components are missing or not yet wired, the page should still render a minimal list.
1. Verify routing/locale handling: confirm `[locale]` segment behavior for loading, params, and links to details pages.

3. **Define the minimum viable “Flights Search v1” product slice**
1. Confirm data source for v1: static `src/data/flights.ts` vs API; pick one for the milestone.
1. Lock the v1 UX: filter set, sort options, result card fields, empty state, error state, loading state.
1. Ensure mobile layout is acceptable (list density, filter UI, sticky controls).

4. **Integrate only essential components for v1**
1. Prioritize core components: `FlightCard`, `FlightFilters`, `FlightSortSelect`, `DynamicPriceChart` (only if it’s already stable and fast).
1. Defer novelty/secondary features: `GamificationBadges`, `SocialProofToast`, `VoiceInteractiveMap`, `AITravelPlanner`, `LuggageArSizer`, etc., unless they are already complete and low-risk.

5. **Detail page + checkout: explicitly gate or exclude**
1. Decide whether `src/app/[locale]/flights/[slug]/` is part of the next milestone. If yes, define the minimum detail page contract (what comes from listing vs what is fetched by slug).
1. Decide whether `src/app/[locale]/checkout/` is part of the next milestone. If yes, define the smallest “reserve intent” flow (traveler info + price summary + confirmation). If no, ensure listing/detail CTAs are clearly “coming soon” and don’t dead-end.

6. **Quality gates (before merging/shipping)**
1. Run typecheck/lint/test/build locally and fix blocking failures.
1. Sanity-check Next.js “breaking changes” constraints in this repo: confirm that any new routing/page conventions match the installed Next version.
1. Add minimal smoke coverage: at least one render test (or story/manual checklist) for listing page states.

7. **Documentation and change hygiene**
1. Update `CHANGELOG.md` with a user-facing entry for the shipped milestone.
1. Update `PLAN.md` to reflect what actually shipped vs what is staged (avoid roadmap drift).
1. Clarify wiki sync artifacts (`WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md`) and ensure they’re not accidentally treated as runtime assets.

---

**Next Ship Milestone (Recommended): “Flights Listing v1 (Localized) + Stub Detail/Checkout”**

Scope:
1. `/[locale]/flights` renders reliably with stable filtering + sorting, using a single agreed data source (static or API).
1. Flight cards link somewhere deterministic:
1. Either a minimal `/[locale]/flights/[slug]` detail stub with key info and CTA.
1. Or no link, but a clear CTA behavior (save/share) that doesn’t break navigation.
1. Exclude checkout unless it’s already end-to-end; otherwise provide a non-broken placeholder flow.

Exit criteria:
1. Typecheck + build passes.
1. No console errors on listing page.
1. Mobile usable.
1. Empty/error/loading states present.

---

**Blockers / Questions (Need Your Decisions to Avoid Thrash)**

1. **Release slicing:** Should the untracked folders/files be considered part of the next release, or should we ship only the flights listing changes first and stage the rest?
1. **Data source:** For flights v1, do you want to commit to `src/data/flights.ts` (static) or wire to an API now?
1. **Routing contract:** Do you want flight details (`/[locale]/flights/[slug]`) in the next milestone, or defer?
1. **Checkout commitment:** Is `/[locale]/checkout` expected to work end-to-end next milestone, or be explicitly out of scope?
1. **Repo structure:** There are both `pages/` and `src/app/` trees. Is this intentionally hybrid, or should we converge to one to avoid routing ambiguity?
1. **Case-sensitive files:** Why both `SYNC_LOG.md` and `sync_log.md`? Which one is canonical?
1. **Commit intent:** The branch is `ahead 1` while also having many untracked items. Is that ahead commit already pushed somewhere/reviewed, or should it be folded into a clean series?
```\n
## 2026-05-10 23:38:48 UTC

### git status -sb
main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md excerpt (first 120 lines)
(see repo file; vision, user flow, roadmap; Faz 11 Predictive Trip Bundler devam ediyor; yeni moduller listesi)

### Plan report (opencode)
**Onceliklendirilmis TODO Plani (ship odakli, somut)**

1. **Calisan minimal flight listing (MVP) stabilizasyonu**
1. Flights list sayfasi `src/app/[locale]/flights/page.tsx` icin hedef davranisi netlestir: ilk acilista liste gorunur, filtre ve siralama bozmadan calisir, bos state ve loading state tutarli.
1. Data kaynagi karari: `src/data/flights.ts` gibi statik mock mu, API mi. MVP icin mock + net tipler ile kilitle.
1. Filtreler: fiyat araligi, aktarma sayisi, havayolu, kalkis varis saat penceresi gibi 3-5 ana filtre ile sinirla. Geri kalanlari backlog a at.
1. Siralama: fiyat, sure, kalkis saati. Varsayilan siralama ve URL parametre uyumu.

2. **Flight detail sayfasi ve route butunlugu**
1. Listing kartindan detail route a gecis net olsun: `src/app/[locale]/flights/[slug]/` altinda sayfa yukleniyor mu, slug nasil uretiliyor.
1. Detail sayfasinda minimum bilgiler: fiyat, segmentler, bagaj, iade kurali placeholder, sec ve devam et CTA.

3. **Checkout akisi (tek basina ship edilebilir)**
1. `src/app/[locale]/checkout/` icinde minimum akisi kur: yolcu bilgileri, iletisim, odeme placeholder, onay.
1. State yonetimi karari: URL query + local state mi, yoksa global store mu. MVP icin en az kompleks olan.
1. Form validasyonlari: zorunlu alanlar, email format, telefon basit kontrol.

4. **UI bilesenleri konsolidasyonu ve tekrarlar**
1. Su an cok sayida yeni component var: `src/components/*` ve `components/` ve `pages/` ve `src/pages/` gibi farkli kokler gorunuyor. MVP icin tek kanonik yer belirle.
1. En kritik 5-8 component disindakileri backlog a al: `FlightCard`, `FlightFilters`, `FlightSortSelect`, belki `DynamicPriceChart` kapali feature flag ile.

5. **Guardrail: performans, hata ve analytics (hafif)**
1. Liste buyukse render maliyeti: pagination veya basit virtualize karari.
1. Hata yakalama: bos data, hatali parametre, 404 slug.
1. Basit event isimleri: search_performed, filter_changed, checkout_started, booking_submitted.

---

**Sonraki Ship Milestone (en yakin teslim paketi)**

**Milestone: Flights Listing -> Detail -> Checkout end to end demo**
- Kullanici flights listing sayfasina girer.
- Filtre ve siralama ile listeyi duzenler.
- Bir flight secer, detail sayfasini gorur.
- Checkout a gider, temel formu doldurur, confirmation ekranini gorur.
- Data mock olabilir, ama akisin kopmamasi ve URL lerin stabil olmasi sart.

Kapsam disi (bu milestone icin): AITravelPlanner, VoiceInteractiveMap, GamificationBadges, SustainabilityScore, AR luggage sizer, multi city router. Bunlari feature flag veya tamamen kapali tut.

---

**Riskler ve Teknik Borc Alanlari**

- **Kok dizin karmasasi**: `pages/`, `src/pages/`, `src/app/` ve `components/`, `src/components/` ayni repo icinde. Next routing ve importlar cakisabilir, build ve davranis farklari dogurur.
- **Asiri feature ekleme**: 290 satirlik buyuk ekleme listing sayfasina. MVP icin en kritik akisi stabilize etmeden yeni modul eklemek regresyon riski.
- **Tip ve veri sozlesmesi belirsizligi**: flight modeli net degilse filtre, kart, detail ve checkout arasi uyumsuzluk olur.
- **Locale route**: `[locale]` yapisi ile linkler ve slug uretilmesi hassas. Yanlis linkler 404 uretebilir.
- **Test yoklugu**: En azindan smoke test senaryosu olmadan refactor zor.

---

**Blocker Sorular (cevaplar onceligi belirler)**

1. Next mimarisi: Bu repo da asil routing `src/app` mi, yoksa `pages` de hala aktif mi. Ikisi birden calisiyor mu, yoksa biri legacy mi.
1. Flights verisi: MVP de veri kaynagi ne olacak. Statik mock kabul mu, yoksa bir endpoint zorunlu mu.
1. Flight slug stratejisi: slug unique ve deterministik mi (id bazli) yoksa ad bazli mi.
1. Checkout: Gercek odeme yok, sadece placeholder ile ship kabul mu.
1. Tasarim sistemi: Var olan UI kit veya tailwind gibi standart var mi, yoksa serbest mi.
1. Feature flag yaklasimi: Deneysel moduller varsayilan kapali mi olmali.

---

**Net Next Steps (uygulanabilir sirayla)**

1. Milestone icin kapsam kilitle: listing detail checkout disi modulleri backlog a at.
1. Data modeli ve route contract yaz: flight entity alanlari, slug, query parametreleri.
1. Listing sayfasini MVP kriterlerine gore temizle: filtre siralama URL uyumu, empty loading error state.
1. Detail sayfasi ve checkout sayfasi arasi linkleri garanti altina al.
1. Son olarak kok dizinleri icin karar ver: tek routing sistemi ve tek components dizini.


\n---\n## 2026-05-10T23:47:00Z\n
### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### Plan report
**Onceliklendirilmis TODO Plani**

1. Derleme ve calisma dogrulamasi
1. `src/app/[locale]/flights/page.tsx` icin lokal build ve runtime kontrolu: sayfa aciliyor mu, hydration hatasi var mi, console error var mi
1. Ucus listeleme sayfasi temel akisi: filtre degisince liste guncelleniyor mu, siralama dogru mu, kartlar dogru veri gosteriyor mu
1. i18n parametresi: `[locale]` route icinde flights sayfasi tum locale lerde calisiyor mu, fallback var mi

1. Degisiklik hijyeni ve repo duzeni
1. Untracked dosya ve klasorlerin envanteri: hangileri gercek urun kodu, hangileri dokumantasyon, hangileri script veya deneme
1. Yeni eklenen `components/ lib/ pages/ scripts/ src/pages/` gibi paralel klasorlerin amaci netlestirme: Next App Router ile cakisma riski var (pages vs src/app)
1. `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI.md`, `WIKI_SYNC.md`, `sync_log.md` adlandirma standardi belirleme (tek isim, tek format, dupeleri kaldirma)

1. Ucus modulu MVP sertlestirme (ship edilebilirlik)
1. Data kaynagi stratejisi: `src/data/flights.ts` mock mu kalacak, API ye mi gecilecek; en azindan arayuz/contract sabitleme
1. Filtre ve sort davranislari icin kabul kriterleri: price, stops, time window, airline, cancellation gibi
1. Empty state ve error state: sonuc yoksa, veri bozuksa, parametre eksikse ne gorunecek
1. Performans: flights page icindeki 290+ satirlik buyume icin rendering maliyeti ve client component oranini kontrol etme (list virtualization gerekip gerekmedigi)

1. Navigasyon ve detay sayfasi tutarliligi
1. `src/app/[locale]/flights/[slug]/` ile listing arasinda parametre tasima: secilen ucus detaya dogru gidiyor mu
1. Checkout entegrasyonu: `src/app/[locale]/checkout/` akisi ile flights secimi uyumlu mu (sepet/summary)
1. Price tracking localStorage ozelliginin listing ve detail arasinda tutarliligi

1. Dokumantasyon ve roadmap bakimi
1. `PLAN.md` guncellemeleri: Faz 11 Devam Ediyor ifadesi ile gercek durum uyusuyor mu
1. Moduller listesi: "Component hazirlandi" yazanlarin gercekten kullanildigi sayfalar ve feature flag durumu
1. Minimum ship dokumani: README veya WIKI uzerinde nasil calistirilir, env var gerekiyor mu, mock data nasil degistirilir

---

**Sonraki Ship Milestone (1 sprint hedefi)**

Milestone adi: Flights Listing MVP Stabilizasyonu

Kapsam:
1. Flights listing sayfasi (route: `src/app/[locale]/flights/page.tsx`) tum locale lerde hatasiz acilacak
1. Filtre ve sort kombinasyonlari deterministik calisacak, empty state ve error state tanimli olacak
1. FlightCard, FlightFilters, FlightSortSelect gibi temel componentler tek bir import stratejisi ile kullanilacak (duplicate/alternatif klasorler netlestirilecek)
1. Repo yapisi: `pages/` ve `src/pages/` gibi App Router ile cakisan yapilarin durumu netlesecek (kullanilmiyorsa kaldirilacak ya da tasinacak; kullaniliyorsa neden gerek oldugu yazilacak)
1. Dokumantasyon: untracked dokumanlar tek standarda indirgenecek ve ship notlari CHANGELOG a eklenecek

Cikis kriteri:
1. Lokal build pass
1. Manuel smoke test pass: flights list, filter, sort, detail nav, checkout entry
1. CI varsa: lint/test pass

---

**Blokerler ve Sorular (cevap gerekli)**

1. Untracked klasorler (components/, lib/, pages/, scripts/, src/pages/) bilincli mi?
1. Next App Router kullaniyorsak `pages/` veya `src/pages/` bilincli kullaniliyor mu, yoksa eski kalinti mi? Bu karar, ship oncesi en buyuk risk.
1. `CHANGELOG.md`, `SYNC_LOG.md`, `sync_log.md` uc tane log dosyasi gorunuyor: hangisi source of truth?
1. Flights verisi su an mock mu (`src/data/flights.ts`), yoksa gercek entegrasyon planlaniyor mu? Ship milestone icin mock ile cikmak kabul mu?
1. Branch `main...origin/main [ahead 1]`: Bu tek commit ship icin hazir mi, yoksa daha commitlenmemis buyuk eklemeler mi var (cunku cok untracked var)?
1. Hedef platform: sadece web mi, yoksa mobil responsive MVP zorunlu mu? Flights listing UI kararlarini etkiler.
1. Auth ve checkout "tamamlandi" denmis: flights secimi checkout a bagli mi, yoksa bagimsiz demo mu olacak?
\n## 2026-05-10 23:57 UTC
branch: main (ahead 1)
git status: main...origin/main [ahead 1]; modified: PLAN.md, src/app/[locale]/flights/page.tsx; many untracked files
diff stat: PLAN.md (+/- 15 lines), flights page +290 lines
PLAN excerpt (1-120): vision + user flow + roadmap; focus now on Predictive Trip Bundler (in progress)
\nPlan report:
- Prioritized TODO:
  1) Define release boundary for next ship (Flights listing only vs include new modules).
  2) Triage untracked files into keep/postpone/delete; watch for duplicates (pages vs src/pages, components vs src/components, sync_log vs SYNC_LOG).
  3) Stabilize src/app/[locale]/flights/page.tsx (server/client safety, i18n, data deps like src/data/flights.ts, perf).
  4) Resolve directory convention conflicts (App Router vs Pages Router) before shipping more.
  5) Prepare clean minimal commit series (A: flights listing + required deps; B optional: docs).
  6) Defer nice-to-have modules behind flags or separate branch.
- Next ship milestone: Flights MVP Listing Refresh (stable /[locale]/flights; filters/sort; no routing conflicts; build passes).
- Blockers / questions:
  - Is routing strictly App Router (src/app) or also Pages Router? (pages/ and src/pages/ intent)
  - Components source of truth: src/components only or also root components/?
  - Does flights/page.tsx import any untracked files (must be included or page breaks)?
  - Should wiki/sync logs live in repo or stay internal?
\n---\n# izgetour plan report - 2026-05-11 00:08 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md excerpt (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## Plan output
**Priority TODO Plan (ship-focused, minimal risk)**

1. **Stabilize the worktree into “what are we shipping?”**
   1. Decide scope for next milestone: “Flights listing v1 polish” vs “Big-bang feature dump”.
   2. Classify the large set of untracked additions into:
      1. Required for the milestone (must ship)
      2. Nice-to-have (defer)
      3. Experimental/demo components (keep out of prod build for now)
   3. Ensure there’s exactly one coherent product story in `src/app/[locale]/flights/page.tsx` (it currently looks like a big expansion: +290 LOC).

2. **Make Flights listing page production-grade (core UX + correctness)**
   1. Define the canonical data model for flights:
      1. What fields are guaranteed? (price, times, stops, airline, cancellation, baggage, fare class)
      2. Source of truth: `src/data/flights.ts` (mock) vs API (future)
   2. Verify filters/sorting correctness:
      1. Filters: airline/stops/price/time/cancellation. Confirm the filter logic matches displayed chips/UI.
      2. Sorting: “best”, “cheapest”, “fastest” and tie-breakers.
      3. Empty states: no matches, missing fields, invalid query params.
   3. Performance guardrails:
      1. Listing page should not re-render excessively (especially if many dynamic widgets are mounted).
      2. Avoid shipping all “trend” components on the listing by default; lazy-load or keep behind toggles.

3. **Route integrity + navigation**
   1. Confirm the `[slug]` flight detail route is wired to cards (click-through works, locale preserved).
   2. Confirm checkout route is reachable and accepts an itinerary selection shape that is consistent with cards/detail.
   3. Ensure all new `pages/` additions are intentional (Next “app router” vs “pages router” conflicts are a common source of subtle routing bugs).

4. **Product hygiene for a real release**
   1. Decide what `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`, `sync_log.md` are:
      1. Human-authored release notes vs generated artifacts.
      2. If generated: exclude from git or put under a dedicated tracked path with clear rules.
   2. Basic quality gates:
      1. Typecheck passes
      2. Lint passes
      3. Build succeeds
      4. Minimal smoke test: load flights list, filter, open detail, proceed to checkout.

5. **Scope the “Predictive Trip Bundler” work (currently marked in-progress)**
   1. Treat it as a separate milestone unless it is already integrated cleanly.
   2. If included, define a thin vertical slice:
      1. User selects a flight
      2. Bundler suggests 1-3 hotels/tours
      3. Add bundle to checkout summary
      4. No external APIs required for v1 (use mock data and clear “beta” labeling)

---

**Next Ship Milestone (recommended): “Flights Module v1 Release Candidate”**

**Definition of Done**
1. Flights listing page is stable, fast, and consistent (filters/sort + empty states).
2. Flight card → flight detail → checkout flow works end-to-end in at least one locale.
3. No routing ambiguity between `app/` and `pages/` for the shipped paths.
4. Only the intended UI modules are enabled in the default UX; experimental widgets are not bundled into the critical path.
5. `CHANGELOG.md` has a clean entry describing what users get in this release.

---

**Blockers / Questions (need your decision to proceed safely)**

1. What is the intended shipping surface for the many new components?
2. Is `pages/` intentionally being (re)introduced?
3. What is the canonical route architecture (app router vs pages router)?
4. What is the data source for flights today (mock vs real provider)?
5. Are SYNC/WIKI logs supposed to be committed?
6. Ship as one chunk or split into multiple commits/PRs?
\n## 2026-05-11 00:17 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### plan report (opencode)
**Durum Ozeti (hizli)**
- Branch: `main` origin main uzerinde 1 commit ileride.
- Degisen dosyalar: `PLAN.md`, `src/app/[locale]/flights/page.tsx`
- Yeni eklenen cok sayida dosya ve klasor var: `src/components/*` (bir suru yeni modul), `lib/`, `pages/`, `scripts/`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, dokumantasyon ve log dosyalari (`CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`, `sync_log.md`).
- Diffstat: flights page icin buyuk bir artis var (yaklasik 290 satir). Bu genelde tek sayfaya cok fazla UI ve state yigildigini gosterir.

---

**Oncelikli TODO Plani (P0 P1 P2)**

1. P0 Release bloklayanlari temizle
- Hedef: Uretime cikabilir, calisan, tutarli bir build ve rota seti.
- Tek seferde kontrol edilecekler:
  1. Routing uyumu: `src/app` altinda yeni `[locale]` sayfalari ve `pages/` veya `src/pages/` ayni anda varsa routing cakismasi riski. Hangisi kaynak gercek olacak karari.
  2. `src/app/[locale]/flights/page.tsx` icin:
     - Rendering modu: server client ayrimi (client component mi, data nereden geliyor)
     - Performans: 290 satirlik sayfada filtre sort kartlar ve ek moduller ayni yerdeyse ilk yukleme agirlasir
     - Error empty state ve loading state var mi
  3. Yeni eklenen bileşenlerin import grafiği: flights liste sayfasi kac yeni component cekiyor, bazi moduller demo seviyesinde mi.
  4. Lint typecheck test: repo standartlari neyse o (en azindan typecheck ve build).

2. P0 Scope kilidi ve feature flag
- Hedef: Bu kadar yeni modulun hepsini ayni anda ship etmeyelim.
- Yapilacaklar:
  1. Ship edilecek MVP listesi: Flights listing, flight detail, checkout temel akis.
  2. Diger trend moduller: AI planner, voice map, gamification, dynamic cuisine, sustainability vs. hepsi icin feature flag veya sadece hidden route.
  3. Demo data kaynaklari: `src/data/flights.ts` gibi mock data prod a cikacaksa acikca etiketle.

3. P0 Dokumantasyon ve degisiklik kaydi duzeni
- Hedef: CHANGELOG ve WIKI dosyalari gercek degisiklikleri takip etsin, log dosyalari repoya girmesin.
- Yapilacaklar:
  1. `CHANGELOG.md` bir release notu gibi: neler ship oldu, neler behind flag.
  2. `SYNC_LOG.md` ve `sync_log.md` ikisi birden varsa tekine indir.
  3. WIKI dosyalari: tek kaynak dogru mu, yoksa guncelleme otomasyonu mi var. Otomasyon varsa hangi dosyalar git e girmeli.

4. P1 Kod sagligi ve mimari duzenleme
- Hedef: Flights page gibi buyuk sayfalari parcalamak, tekrar kullanilabilirlik.
- Yapilacaklar:
  1. `FlightFilters`, `FlightSortSelect`, `FlightCard` zaten ayrilmis gorunuyor, sayfada sadece orchestration kalsin.
  2. State yonetimi: filtre sort compare saved searches vs. karmasa tek yerdeyse basit store yaklasimi veya URL search params standardi sec.
  3. UI tutarliligi: hotel ve flight kart filtreleri benzer API ile calissin.

5. P1 Ucus ve checkout entegrasyon dogrulama
- Hedef: listing den detail a, detail den checkout a kesintisiz akıs.
- Yapilacaklar:
  1. `src/app/[locale]/flights/[slug]/` slug param kaynaklari ve veri bulamazsa 404 davranisi.
  2. Checkout route u: `src/app/[locale]/checkout/` adimlari, guest checkout, summary, basarili odeme ekranlari.
  3. localStorage ozellikleri: price tracking saved searches gibi seylerde SSR uyumu.

6. P2 Urunlesme ve olcumleme
- Hedef: gercek kullanicida deger yaratan metrikler.
- Yapilacaklar:
  1. Event tracking plani: search submit, filter apply, sort change, card click, checkout start, payment success.
  2. Basit performans butcesi: flights listing TTI, bundle boyutu.

---

**Sonraki Ship Milestone (Oneri)**
Milestone: Flights ve Checkout MVP v0.1
- Icinde:
  1. Flights listing calisir, filtre sort stabil, empty ve error state var
  2. Flight detail sayfasi slug ile acilir, price tracking basic calisir
  3. Checkout guest akisi calisir ve success sayfasi gorulur
  4. Sadece gerekli moduller acik, digerleri kapali veya gizli
  5. Build typecheck ve lint temiz

Teslim kriteri:
- Prod build basarili
- En az 3 temel akıs manuel test: search to listing, listing to detail, detail to checkout to success
- Basit release notu: CHANGELOG

---

**Blokerler ve Sorular (Cevaplarina gore plan netlesecek)**
1. `pages/` ve `src/pages/` klasorleri bilerek mi eklendi
- Next App Router ile birlikte Pages Router ayni repoda ise routing cakismasi riski var. Hedef mimari hangisi

2. Bu yeni componentlerin hepsi gercekten kullaniliyor mu
- Yoksa bir kismini sadece hazir dursun diye mi eklediniz. Ship icin hangileri zorunlu

3. `SYNC_LOG.md` `sync_log.md` ve `WIKI_SYNC.md` ne amacla repoda
- Otomasyon cron her 10 dk kontrol ediyor denmis. Bu otomasyon dosyalari git e koymali miyiz yoksa ignore mu olmali

4. Ucus verisi kaynagi ne olacak
- `src/data/flights.ts` demo mu, yoksa MVP de mock ile mi cikiyoruz. API entegrasyonu yakinda mi

5. Lokalizasyon stratejisi
- `[locale]` routing var. Default locale ne, fallback davranisi ne, SEO icin canonical plan var mi

Bu 5 soruya cevap verirsen, TODO listesini daha da daraltip direkt bir sprint backlog formatina ceviririm ve hangi dosyalarin ship e girecegini netlerim.
\n---\n# Izgetour plan report - 2026-05-11 00:27 UTC\n
## Git status
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## Git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md excerpt (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## Opencode plan output
Prioritized TODO Plan (Read-Only, No Tools, No Code)

1. Stabilize the worktree and define what ship means for this increment
   1. Confirm the target milestone scope: Flights listing + detail + checkout skeleton vs Flights MVP end-to-end.
   2. Decide what to do with the large set of untracked directories/files (components/, lib/, pages/, scripts/, src/pages/, many src/components/*): generated, experimental, or intended to land now?

2. Triaging: separate core product vs prototype library changes
   1. Core: src/app/[locale]/flights/page.tsx (big change) and PLAN.md.
   2. Potentially core (but currently untracked): src/app/[locale]/flights/[slug]/, src/app/[locale]/checkout/, src/data/flights.ts, src/components/Flight*, src/components/Hotel*.
   3. Likely non-core for next ship: gamification, sustainability score, voice map, party planner, cuisine recommender, etc. Defer unless wired into flights flow.

3. Make the Flights MVP coherent and shippable
   1. Ensure flights listing page has a clear contract: data source (static vs API), state model (filters/sort/pagination), URL sync, locale behavior.
   2. Minimum UX: search input or query header, filter sidebar/drawer, sort control, results list with consistent cards, empty/loading/error states.
   3. Define navigation to detail: route exists, stable identifier/slug format locked now.

4. Confirm Next.js App Router conventions and avoid structural duplication
   1. Untracked pages/ and src/pages/ plus src/app usage is high risk.
   2. Decide if both routers are supported or duplication.
   3. Pick one primary routing approach for Flights (likely src/app) and quarantine the other folders for this milestone.

5. Documentation and changelog hygiene
   1. Decide if CHANGELOG.md, SYNC_LOG.md, WIKI*.md, sync_log.md are release artifacts.
   2. Unify naming (SYNC_LOG.md vs sync_log.md) to avoid case-sensitive dupes.
   3. Ensure PLAN.md reflects what is actually wired, or add a clear status legend.

6. Quality gates before shipping
   1. Definition of done for Flights MVP: builds, listing->detail->checkout navigation, mobile filters usable, no obvious runtime errors.
   2. Minimal smoke tests or at least a manual checklist.

7. Reduce scope: move optional modules behind flags or backlog
   1. AITravelPlanner, GamificationBadges, LoyaltyTierSystem, VoiceInteractiveMap, etc should not ship unless directly supports conversion.

Next Ship Milestone (Proposed): Flights MVP v1

Goal: user can browse flights, apply basic filters/sort, open detail, proceed to checkout (placeholder ok), locale routing intact.

Deliverables:
1. flights listing page production-safe.
2. flights detail route exists with stable identifier.
3. checkout route exists and accepts selected flight data.
4. minimal data strategy decided and consistent.
5. repo hygiene: only intended files tracked; logs/wiki handled intentionally.

Blockers / Questions:
1. Are pages/ and src/pages/ intentional?
2. Which untracked components are actually wired into flights/page.tsx?
3. Data source for flights now?
4. URL/state behavior for filters/sort?
5. What does ahead 1 represent?
6. Should next ship include hotels modules too?
\n---\n# izgetour plan report - 2026-05-11 00:38:22 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md excerpt (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan output
**Prioritized TODO Plan (Read-only, no tools/code)**

1. **Stabilize repo state and scope the release**
   1. Decide what’s intended to ship now vs. what’s experimental: right now the worktree includes a very large set of untracked modules (`components/`, `lib/`, `pages/`, `scripts/`, new `src/app/...` routes). That’s “big-bang” scope unless you explicitly slice it.
   2. Pick a single product slice as the release target (recommended: Flights listing + flight detail + checkout flow already marked ✅ in PLAN.md).
   3. Define “ship criteria” in 5 bullets (examples below under Milestone).

2. **Resolve repo hygiene and duplication risks (high impact)**
   1. Investigate directory duplication: you have both `pages/` and `src/pages/` and also `src/app/...` which suggests mixed Next routing paradigms. This is the highest risk for build/runtime conflicts and unexpected route resolution.
   2. Decide the canonical routing approach for this codebase (App Router only vs mixed). Then explicitly quarantine or delete the unused tree (or move it out of build scope).
   3. Normalize docs/log files: there is both `SYNC_LOG.md` and `sync_log.md` (case-sensitive on Linux; can become a cross-platform trap if collaborators use macOS/Windows). Pick one name.

3. **Bring Flights listing page to “production-ready”**
   1. Review the large change in `src/app/[locale]/flights/page.tsx` (+290 lines). Ensure:
      1. It compiles.
      2. It does not rely on browser-only APIs in a server component context (localStorage, window, etc.) unless it is a client component.
      3. Any new UI components referenced are actually wired, typed, and exported consistently.
   2. Validate the filters/sort behavior matches the roadmap items you marked ✅ (FlightFilters, FlightSortSelect, FlightCard).
   3. Confirm empty states and error states: no results, missing params, invalid locale, etc.

4. **Integrate untracked modules intentionally**
   1. Inventory which untracked items are truly required for the flights experience:
      1. `src/data/flights.ts` (data source)
      2. `src/components/Flight*` (listing UI)
      3. `src/app/[locale]/flights/[slug]/` (detail page)
      4. `src/app/[locale]/checkout/` (checkout route)
      5. Any shared UI/utilities in `lib/`, `components/checkout/`
   2. Everything else (AI planner, AR sizer, voice map, loyalty tiers, etc.) should be deferred unless it’s already integrated and tested. Shipping them as “present but unused” is ok only if it doesn’t add routing/build risk.

5. **Add minimal verification gates (even if lightweight)**
   1. Run build/lint/test passes before ship (whatever is standard for this repo).
   2. Smoke test critical flows:
      1. Flights listing renders.
      2. Filters + sort work.
      3. Click flight -> detail page.
      4. From detail -> checkout -> success screen.
      5. i18n locale segment works for at least 1-2 locales.

6. **Release documentation + changelog discipline**
   1. `CHANGELOG.md` exists untracked: decide if you maintain it manually. If yes, add an entry for this milestone (what users get).
   2. `WIKI.md / WIKI_SYNC.md / SYNC_LOG.md`: decide whether these belong in-repo or are internal automation artifacts. If they’re cron-generated “every 10 minutes” as PLAN.md says, define whether they should be committed or gitignored to avoid perpetual noise.

---

**Next Ship Milestone (Recommended): “Flights MVP v1”**

Goal: a coherent, stable flights search/listing and purchase flow.

Ship criteria (suggested):
1. `/[locale]/flights` listing page renders with mock/static data and is responsive.
2. Filtering and sorting work deterministically (no crashes, no hydration issues).
3. `/[locale]/flights/[slug]` detail page works and shows key flight info + price tracking UI if already implemented.
4. Checkout route completes end-to-end to a success screen (even if payment is mocked).
5. No routing conflicts (App Router vs Pages) and no duplicate route trees causing ambiguity.

What not to include in this milestone:
- Predictive bundling, AI concierge, collaborative boards, AR, voice map, etc., unless already integrated and proven not to destabilize routing/build.

---

**Blockers / Questions (Need your answers to proceed cleanly)**

1. Do you intend to ship all untracked modules now, or do you want a tight “Flights MVP” release and defer the rest?
2. Is this codebase supposed to be **App Router only** (`src/app/...`) or a hybrid with `pages/`? Right now the presence of `pages/`, `src/pages/`, and `src/app/` is a major risk.
3. Are `SYNC_LOG.md`, `WIKI_SYNC.md`, and the “cron updates PLAN.md every 10 minutes” behavior meant to be committed to git, or should they be ignored/generated elsewhere?
4. Which locales are “must ship” for this milestone (e.g., `tr` only vs `tr+en`)?
5. What’s the expected data source right now for flights: static mock (`src/data/flights.ts`) vs API integration? If API is planned later, we should explicitly treat current as mock-driven.

If you answer #1 and #2, the plan can be tightened into a concrete “ship this week” checklist with exact inclusion/exclusion decisions.
\n---\n# izgetour plan report - 2026-05-11 00:47 UTC
\n## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan output
**Prioritized TODO Plan (Ship-Focused)**

1. **Stabilize the repo state (before any further work)**
   1. Decide what belongs in git right now vs what is generated/synced.
   2. Create/confirm `.gitignore` policy for “sync artifacts” and large content:
      1. Likely ignore: `SYNC_LOG.md`, `sync_log.md`, `WIKI_SYNC.md` (and any cron outputs).
      2. Likely keep: `PLAN.md`, `CHANGELOG.md`, `WIKI.md` (if it is authoritative product/docs).
   3. Resolve duplication risk: both `SYNC_LOG.md` and `sync_log.md` exist (case-only difference can break on macOS/Windows and cause nasty merges). Pick one canonical name.

2. **Define the “Flights v1” shipped slice (tight scope)**
   1. Confirm what the customer-visible promise is for `/[locale]/flights`:
      1. Search inputs supported (from/to, dates, pax).
      2. Filters supported (airline, stops, price, time, cancellation) and expected behavior.
      3. Sort options and default sort.
      4. Empty state and error state behaviors.
   2. Freeze “nice-to-haves” (AI planner, AR sizer, badges, social proof, etc.) behind flags or keep out of the listing page until v1 is reliable.

3. **Audit `/src/app/[locale]/flights/page.tsx` change (290 lines added)**
   1. Ensure it’s not doing too much client-side work by accident:
      1. Confirm `use client` usage (if present) is intentional.
      2. Check for heavy components imported into the listing route (bundle bloat risk).
   2. Validate data flow:
      1. Where flight data comes from (`src/data/flights.ts` exists as untracked).
      2. Whether filtering/sorting is deterministic and URL-driven (important for shareable links and SSR).
   3. Confirm i18n correctness:
      1. Locale segment is respected.
      2. Any currency/date formatting is locale-aware.

4. **Routing consistency and Next.js structure hygiene**
   1. There are both `pages/` and `src/pages/` and `src/app/…` present as untracked. Decide one routing paradigm:
      1. If this project is app-router-first, `pages/` should likely be removed or isolated.
      2. If legacy pages are required, define boundaries clearly to avoid route collisions.
   2. Confirm `src/app/[locale]/flights/[slug]/` and `src/app/[locale]/checkout/` integrate cleanly with listing links and checkout CTAs.

5. **Minimal quality gates for shipping**
   1. Decide the required checks for “ship”:
      1. Typecheck passes.
      2. Lint passes.
      3. Build succeeds.
      4. Smoke test flows: open flights listing, apply filters, open flight detail, proceed to checkout page.
   2. Add a lightweight test plan in `PLAN.md` or `WIKI.md` (even manual checklist is fine if no test harness).

6. **Documentation alignment**
   1. `PLAN.md` already claims many modules are “✅ Tamamlandı”; reconcile that with what’s actually wired into routes and navigable.
   2. Start `CHANGELOG.md` discipline:
      1. “Unreleased” section.
      2. Record only user-facing changes for the milestone.

---

**Next Ship Milestone (Recommendation)**

**Milestone: “Flights v1 Public Beta” (1-week scope, but can be shorter if already mostly done)**

Acceptance criteria (ship gate):
1. `/[locale]/flights` renders reliably and fast (no blank states, no console errors).
2. Filters and sorting work on the current dataset and are reflected in the URL (or explicitly decided not to, but then define behavior).
3. Clicking a flight card navigates to `/[locale]/flights/[slug]` and the detail page loads consistently.
4. A clear CTA from detail to `/[locale]/checkout` with a stable summary (even if mock data).
5. Repo hygiene: no case-duplicate files, and sync/generated logs are not committed.

---

**Blockers / Questions (Need Your Decisions)**

1. **What is the authoritative routing approach?**
   1. Should we remove/ignore `pages/` and `src/pages/` entirely and use only `src/app`?
   2. Or do you intentionally support both (if so, what routes must remain in `pages/`)?

2. **What should be committed from the untracked set?**
   1. Should `CHANGELOG.md` be committed now?
   2. Should `WIKI.md` be treated as product documentation (commit), or is it sync output (ignore)?
   3. Confirm which of `SYNC_LOG.md` vs `sync_log.md` is canonical, and whether any of them should ever be committed.

3. **Data source for flights**
   1. Is `src/data/flights.ts` the intended temporary fixture, or do you already have an API/Supabase source planned?
   2. For v1, do you want SSR listing results or client-side filtering on a static dataset?

4. **Definition of “done” for the many “✅ Component hazırlandı” modules**
   1. Are these meant to be present in UI now (even if behind toggles), or just staged components not yet integrated?
   2. Which 1-2 of these are highest leverage to include in Flights v1 without risking stability?

If you answer just #1 (routing choice) and #2 (what to commit/ignore + the log filename decision), I can turn this into a concrete, ordered execution checklist for the next working session with exact files to touch and the minimal set of commits to produce.
\n---\n## 2026-05-11 00:58:42 UTC
\n### git status -sb
\n```
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
```
\n### git diff --stat
\n```
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
```
\n### PLAN.md (first 120 lines)
\n```
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
```
\n### Plan report
\n```
**Next Ship Milestone (recommended): "Flights v1: Browse + Filter + Sort + Details Shell"**  
Goal: deliver a coherent end-to-end flights browsing experience that is stable, instrumented, and ready to iterate. This matches your current delta (large `flights/page.tsx` work + many new flight UI components) and prevents spreading into checkout/gamification/AI extras before the core is solid.

Success criteria (ship gate):
1. Flights list page loads fast and renders reliably on mobile/desktop.
2. Filters + sort produce correct, predictable results (including edge cases: empty results, reset, multi-filter).
3. Each flight card has a clear CTA (view details / select) and stable routing to `[slug]` (even if details page is a stub).
4. No console errors, no hydration warnings, no obvious a11y regressions.
5. Minimal analytics hooks or logs in place (even if just internal events) to guide next iterations.

---

## Prioritized TODO Plan (highest leverage first)

### 1. Stabilize Scope and Baseline (must do before more features)
1. Confirm what the "ahead 1" commit contains and whether it is part of this feature set.
2. Decide what to include in the next commit/PR scope:
- Include: flights list page + essential components + `src/data/flights.ts`.
- Exclude for now: checkout flows, AI planner, gamification, voice map, cuisine recommender, etc., unless already tightly integrated.
3. Decide routing contract now:
- What is a flight `slug` format (stable ID vs derived string)?
- What does the `[slug]` page need to minimally render (title, key facts, back link, select button)?

### 2. Make Flights List Page Production-Ready (core UX + correctness)
1. Data model sanity:
- Ensure `src/data/flights.ts` has a consistent schema (price, segments, duration, stops, airline, departure/arrival times, currency).
- Decide how to handle missing fields (e.g., unknown baggage, missing airline logo).
2. Filtering correctness:
- Define filter semantics explicitly:
  - Stops: exact (0, 1, 2+) or max stops.
  - Time windows: local time vs absolute.
  - Price range: inclusive bounds; currency assumptions.
  - Airlines: OR within selected airlines.
- Implement consistent "Clear all" behavior and ensure derived UI state matches applied filters.
3. Sorting correctness:
- Define sort keys and ties:
  - Price ascending
  - Duration ascending
  - Departure time ascending
  - Best value (if present) must be deterministic or postponed.
4. Empty / loading / error states:
- Empty results: show explanation + quick reset CTA.
- Loading: only if there is async data; otherwise avoid fake spinners.
- Error: if any parsing or route param issues occur, fail gracefully.
5. Performance and rendering:
- Avoid expensive recomputation per render if the list is large (use memoization only if needed and consistent with repo patterns).
- Ensure responsive layout is not over-complex; prevent layout shift in cards (reserve space for images/badges).

### 3. FlightCard + List Interaction Quality (conversion)
1. FlightCard:
- Make primary CTA unambiguous ("View details" or "Select").
- Ensure the card is keyboard accessible and focus-visible.
- Standardize price display and currency.
2. Compare / saved searches:
- If `ComparePanel` and `SavedSearches` are present, keep them minimal:
  - Limit compare to N items.
  - Clear remove behavior.
  - Persist or do not persist: decide now to avoid half-state.
3. URL state (optional but high value):
- If filters/sort are intended to be shareable:
  - Define query params and encode/decode rules.
  - Otherwise explicitly keep state local and do not leak incomplete URL formats.

### 4. Details Page `[slug]` Minimal Shell (to complete the flow)
1. Render a deterministic details view from the same dataset:
- If real backend not ready, map slug -> flight in `src/data/flights.ts`.
2. Add guardrails:
- Unknown slug -> 404-like state with link back to list.
3. CTA path:
- Decide whether "Select flight" goes to checkout now or later.
- If checkout is not ready, route to a placeholder with clear messaging rather than a broken path.

### 5. Checkout Folder and Other New Areas (defer unless needed for milestone)
You have untracked new directories: `src/app/[locale]/checkout/`, `pages/`, `components/`, `lib/`, `scripts/`, plus many new feature components. For the next ship milestone:
1. Identify which of these are required dependencies for flights browsing.
2. Park the rest behind a feature flag or keep them unmerged until flights v1 lands, to reduce review and regression risk.

### 6. Documentation Hygiene (small but important)
1. `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`:
- Decide what is authoritative (one changelog, one sync log).
- Avoid duplicating `sync_log.md` vs `SYNC_LOG.md` unless both are intentional.
2. Update `PLAN.md` only with what is actually in this ship milestone:
- Clearly label "in progress" vs "planned" modules to avoid scope creep.

### 7. Quality Gates (before shipping)
1. Basic test plan (even if no automated tests yet):
- Mobile: narrow width, long airline names, long city names.
- Edge cases: no flights, all filtered out, extreme prices, same price ties.
- Locale: check `[locale]` routing and formatting expectations.
2. Accessibility pass:
- Keyboard navigation through filters, sort, cards.
- Proper label association for filter controls.
3. Telemetry (minimal):
- Log events for filter change, sort change, select flight, view details.
- Keep it internal/no secrets.

---

## Blockers / Questions (answering these will prevent rework)
1. What is the intended "next ship" target: internal demo, production release, or PR for review?
2. Should the flights dataset be static (mock) for now, or do you already have an API contract?
3. Are filters intended to be reflected in the URL query params (shareable links) or purely local state?
4. What is the canonical flight identifier:
- `id` (recommended) -> slug derived from id
- or slug derived from route/airline/time (fragile)
5. What is the checkout expectation for this milestone:
- Link to checkout, or explicitly defer checkout and only show a selection confirmation?
6. Locale behavior:
- Should currency/number/date formatting follow locale automatically, or is it fixed for now?
7. You have both `pages/` and `src/pages/` plus `src/app/...`:
- Is this intentional (hybrid routing), or should we avoid introducing more into `pages/`?

If you answer the 7 questions above, I can turn this into a tight "Milestone 1 checklist" with exact inclusion/exclusion, acceptance criteria, and a second milestone proposal (e.g., "Trip Bundler v0" or "Checkout v0") without adding scope.
\n```

## 2026-05-11 01:07 UTC

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

### plan report
**Onceliklendirilmis TODO Plani (mevcut durum: main dalinda 1 commit ahead, cok sayida yeni dosya ve component var)**

1. **Degisiklik kapsamini netlestir ve paketle**
1. Flights modulu: `src/app/[locale]/flights/page.tsx` icindeki 290+ satirlik artis hangi ozellikleri aktif ediyor, hangileri sadece UI stub: filtre, siralama, kart, karsilastirma, fiyat grafikleri, kaydetme vb.
1. Yeni eklenen klasorlerin amaci: `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/` birbirini tekrar ediyor mu, Next router yapisina aykiri paralel sistem var mi.
1. Dokumantasyon dosyalari: `CHANGELOG.md`, `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md`, `sync_log.md` adlandirma ve tek kaynak gercegi (single source of truth) belirle.

2. **Minimum ship edilebilir Flights milestone (MVP) secimi**
1. Flights listing sayfasi: arama parametrelerini al, sonuc listesini stabil render et, temel filtreler (price, stops, airline) ve siralama (price, duration) calissin.
1. Flight card: fiyat, saat, havayolu, bagaj, iptal politikasi gibi temel alanlar dogru gosterilsin.
1. Navigasyon: listing -> detay (slug) gecisi ve geri donus stabil olsun.
1. Performans: listing sayfasinda gereksiz client state ve agir componentler kapali ya da lazy olsun.

3. **Kalite ve urun risklerini kapat (ship oncesi)**
1. i18n/locale: `[locale]` altinda flights ve checkout rotalari tutarli mi, hardcoded string var mi.
1. Veri kaynagi: `src/data/flights.ts` mock mu, gercek API entegrasyonuna gecis icin arayuzler sabit mi.
1. Eriisilebilirlik: filtre paneli, sort select, kart aksiyonlari klavye ile kullanilabilir mi.
1. Analitik/olcum: fiyat takibi, kaydetme, karsilastirma gibi aksiyonlar icin event isimleri ve minimum telemetry planla (eger projede var).

4. **Repo hijyeni ve yayinlanabilirlik**
1. Fazla/tekrar router yapisi: `pages/` ve `src/pages/` var; App Router ile cakisma riski var. Hangisi aktif, hangisi eski? Kaldirma ya da ayirma karari.
1. Component envanteri: cok sayida yeni component var (AITravelPlanner, ComparePanel, DynamicPriceChart, vs). Ship milestone icin hangileri dahil, hangileri feature-flag ya da sonraya.
1. Dokumanlar: PLAN.md guncellemesi ile gercek kod durumu uyusuyor mu. Roadmap tablosunda "tamamlandi" isaretleri ile repo gercegi arasinda fark varsa duzelt.

---

**Sonraki Ship Milestone (onerilen): "Flights MVP v1")**
- Hedef: Flights listing + basic filters/sort + flight detail (slug) + checkout akisi ile en az 1 happy-path rezervasyon deneyimi.
- Kapsam:
  1. Listing: stabil veri gostermi, filtreleme, siralama
  2. Detail: secilen flight icin detaylar + fiyat takibi (local) varsa
  3. Checkout: secilen flight ile sepet/checkouta gecis
- Kapsam disi (milestone sonrasi):
  1. ComparePanel (split view) ve multi-city router
  2. DynamicPriceChart, AR luggage sizer, voice map, sustainability score gibi "nice-to-have" moduller
  3. Predictive trip bundler (devam ediyor gorunuyor)

---

**Blockerlar / Sorular (cevaplar gelmeden dogru ship plani cikmaz)**
1. Next.js routing: Proje App Router mi kullaniyor, yoksa pages router mi. `pages/` ve `src/pages/` klasorleri bilerek mi var, yoksa artifakt mi?
1. Ship hedefi: Bu degisiklikler demo amacli mi (mock data ile), yoksa prod release mi (API, odeme, auth gercek)?
1. Flights data source: `src/data/flights.ts` kalici mock mu, yoksa yakinda API gelecek mi? API gelecekse tip/contract sabitleme gerekiyor.
1. Feature set: Flights sayfasinda su an eklenmis cok sayida component var. Hangileri zorunlu: filters, sort, card, saved searches, compare, price chart?
1. Dokumantasyon sahipligi: `SYNC_LOG.md` ve `sync_log.md` ikisi birden niye var? Cron ile plan guncelleniyor denmis; bu repo icinde otomasyon mu var, yoksa disaridan mi?
1. Checkout entegrasyonu: Odeme saglayici kim (Stripe vb) ve "guest checkout" gercek mi, yoksa UI mi? Flights checkout ile tours checkout ayni mi?

Bu sorulara yanit verirsen, "Flights MVP v1" icin net scope (hangi componentler aktif, hangileri kapali) ve 1-2 haftalik teslim takvimi (gun gun degil, is paketleri bazinda) cikartabilirim.

---
TIMESTAMP: 2026-05-11 05:03 UTC
REPO: /home/turk/projects/izgetour

GIT_STATUS:
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

DIFF_STAT:
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT (first 120 lines captured separately in cron run)

PLAN_REPORT:
Prioritized TODO:
1) Repo hygiene: decide which wiki/sync artifacts are real deliverables vs generated (SYNC_LOG.md vs sync_log.md, WIKI files) and confirm routing strategy (src/app vs pages).
2) Flights list shippable: define MVP acceptance criteria; reduce scope creep in src/app/[locale]/flights/page.tsx; ensure consistent component imports; check app router server/client boundaries.
3) Component organization: bundle by feature (Flights, Hotels, Checkout, Experiments) and standardize conventions (src/components, data contracts, mock data location).
Next ship milestone: Flights MVP v0.1 (stable listing + filters/sort + consistent flight cards + mock data + minimal docs).
Blockers/questions:
- Canonical routing strategy (app router vs pages)?
- Should sync/wiki logs be committed or ignored?
- Milestone scope: flights list only vs include detail and minimal checkout entry?
- Mock data only vs any API stub?
- Standardize on src/components vs root components?

---
TIMESTAMP: 2026-05-11 05:13 UTC
REPO: /home/turk/projects/izgetour
GIT_STATUS:
main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
DIFF_STAT:
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)
PLAN_MD_EXCERPT: (first 120 lines captured in cron run)
PLAN_REPORT:
Onceliklendirilmis TODO Plani
1) Degisikligin hedefini netlestir (flights page + yeni klasorler + PLAN update)
2) Flights list MVP build rotasini stabil hale getir (list, filtre, siralama; mock data ile ship)
3) Scope cut: ship icin gerekli componentleri tut, nice-to-have moduleri sonraya it
4) Route/mimari uyumu: app router vs pages karari, /[locale]/flights, /[locale]/flights/[slug], /[locale]/checkout
5) Dokumantasyon duzeni: changelog, wiki/sync log tek standarda
6) Minimum kalite: manual checklist + build/smoke test
Next ship milestone onerisi: Faz 1a Flights MVP (list + detail minimal + checkout placeholder)
Blockers/questions:
- Bu degisiklik flights MVP mi yoksa genis paket mi
- Next app router mi, pages de aktif mi
- Data source mock ile ship OK mi, yoksa API sart mi
- Locale stratejisi (diller, fallback)
- Checkout hedefi (odeme mi, lead mi)
\n---\n# izgetour plan report - 2026-05-11 05:24:46 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan output
**Prioritized TODO Plan (Ship-Focused)**

1. **Stabilize repo shape (high risk, blocks shipping)**
   1. Decide the routing strategy: `app/` router vs `pages/` router, and enforce it.
   1. Confirm whether `components/`, `lib/`, `pages/`, `scripts/` at repo root are intentional duplicates or should be moved under `src/` (you currently have both root-level and `src/`-level structures).
   1. Define what is allowed to be tracked: right now a large set of new directories/files are untracked; that is a release-risk (CI noise, accidental commits, duplicated code paths).

2. **Make flights listing page production-ready (`src/app/[locale]/flights/page.tsx`)**
   1. Identify what the +290 lines added actually introduced: feature UI vs data mocking vs side effects.
   1. Validate SSR/CSR boundaries: ensure no direct `window/localStorage` usage in server components; mark client components explicitly if needed.
   1. Ensure the page does not import from `pages/` or root `components/` inconsistently (this is where Next routing mismatches often surface).
   1. Confirm data source: `src/data/flights.ts` exists untracked; decide whether listing uses mock data now and what the contract will be for real API integration.

3. **Unify component ownership and public API**
   1. Decide canonical component location: `src/components/**` vs `components/**`.
   1. Create an explicit barrel/export policy (even if minimal): which components are “product UI” vs “experiments”.
   1. Confirm which of the many new feature components are actually used on the flights page vs just present in repo (dead code increases bundle and review burden).

4. **Document and enforce milestone scope in PLAN / CHANGELOG**
   1. PLAN.md currently signals “everything is done”; reconcile with actual production readiness (tests, API wiring, error handling, perf, analytics).
   1. Establish a “Definition of Done” for modules labeled ✅ (e.g., “wired to data source”, “responsive”, “a11y baseline”, “no console errors”, “passes build”).

5. **Hygiene: naming + duplication**
   1. Resolve duplicate `SYNC_LOG.md` and `sync_log.md` (case-sensitive filesystems will treat them as different files; this can break collaborators across OSes).
   1. Decide what `WIKI.md`/`WIKI_SYNC.md` are for (source of truth vs generated artifacts). Generated files should usually not be committed unless intentional.

6. **Pre-ship verification checklist (should happen before next push/release)**
   1. Ensure `next build` passes in CI config.
   1. Validate locale routing for `/[locale]/flights` and `/[locale]/flights/[slug]` end-to-end.
   1. Smoke test mobile layout for listing + detail + checkout entrypoints.
   1. Basic performance sanity: avoid rendering huge lists without virtualization, avoid heavy client components at top-level.

---

**Next Ship Milestone (recommended)**  
**Milestone: “Flights MVP Release Candidate” (1-2 days of focused cleanup depending on repo state)**

Success criteria:
1. `/[locale]/flights` loads without runtime errors and is consistent across SSR/CSR.
2. Flight listing uses a single, agreed data source (mock or API) with a clear interface.
3. No ambiguous routing: either commit to `app/` routing or explicitly support both with a documented reason.
4. Repo structure is deterministic: one canonical `components/` + `lib/` location, and only intended files are tracked.
5. Build passes and basic navigation to flight detail + checkout works.

---

**Blockers / Questions (need your decisions to proceed safely)**

1. **Routing choice:** Are we fully on Next `app/` router, or do we still intentionally support `pages/`?  
2. **Canonical directories:** Should root-level `components/`, `lib/`, `pages/`, `scripts/` exist, or must everything live under `src/`?  
3. **What is shippable scope for flights page?**  
   1. Listing + filters + sort only, or also compare panel, gamification, itinerary, price chart, etc.?  
4. **Data strategy:** Is `src/data/flights.ts` purely mock seed data, or intended as a local dataset for demo mode?  
5. **Tracking policy for docs/logs:** Should `SYNC_LOG.md`, `sync_log.md`, `WIKI_SYNC.md` be committed outputs, or should they be gitignored/generated?  
6. **Ahead by 1 commit:** Is that commit intended to be on `main`, or should we branch before doing repo-structure cleanup?

---
Timestamp: 2026-05-11 05:35 UTC
Repo: /home/turk/projects/izgetour

## git status -sb
main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

## git diff --stat
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

## PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

## Plan report (opencode)
**Prioritized TODO Plan (Read-only, No Tools)**

1. **Stabilize repo state for a shippable branch**
1. Decide what *must* ship now vs. what’s experimental.
1. Confirm whether the large set of untracked files (`components/`, `lib/`, `pages/`, `scripts/`, many `src/components/*`, new `src/app/[locale]/...` routes) are intended to be part of the next release or are local scaffolding.
1. Ensure `main...origin/main [ahead 1]` is intentional: identify what that one commit contains and whether it’s ready to remain ahead before shipping.

2. **Define “Flights Listing MVP” acceptance criteria**
1. Flights listing page should: render without runtime errors, show results, allow filter/sort, and link to flight detail (`/flights/[slug]`) reliably.
1. Define “must-have” vs “nice-to-have” for the new UI elements that appear to have been added to `src/app/[locale]/flights/page.tsx` (+290 lines suggests major UI expansion).

3. **Sanity-check architecture boundaries**
1. Confirm which routing system is authoritative: you have both `src/app/...` and an untracked `pages/` plus `src/pages/`. Pick one as the product direction to avoid double-routing, duplicated bundles, and confusing deploy behavior.
1. Confirm component placement conventions: you now have `components/` and `src/components/` both untracked. Decide one canonical home.

4. **Content and documentation hygiene (release readiness)**
1. Decide whether to ship `CHANGELOG.md`, `WIKI.md`, `WIKI_SYNC.md`, `SYNC_LOG.md` (and `sync_log.md` lowercase duplicate) in the product repo.
1. Resolve casing duplication risk: `SYNC_LOG.md` vs `sync_log.md` is a deployment footgun on case-sensitive vs case-insensitive filesystems.

5. **Functional verification checklist (pre-ship)**
1. Flights listing page: filtering, sorting, compare panel, saved searches, price chart, etc. (based on newly added components) should not break SSR/CSR boundaries.
1. Navigation: links from listing to detail pages and to checkout flow should be consistent with `[locale]` routing.
1. i18n: ensure locale segment is preserved across listing → detail → checkout routes.
1. Data: `src/data/flights.ts` exists (untracked). Decide if this is mock data (ship ok) or needs replacement with real API integration (blocker for “production”).

6. **Bundle and performance guardrails (if shipping to real users)**
1. Identify any heavy “trend modules” (voice map, AR sizer, AI planner) now included in listing page; ensure they are lazy-loaded or gated so flights listing stays fast.
1. Ensure no secrets or API keys were added in any of the new `lib/` or `scripts/` files (untracked scope is large).

---

## Next Ship Milestone (Recommended)

**Milestone: “Flights Module MVP v1 (Listing + Detail + Checkout Path)”**

**Goal:** A user can search/browse flights, filter/sort, open a flight detail page, and proceed into checkout without dead ends; feature extras are present only if they don’t destabilize core flow.

**Exit criteria**
1. `Flights listing` is stable and fast enough (no console/runtime errors, no hydration issues).
1. `Flight detail` loads reliably by slug and preserves `[locale]`.
1. `Checkout entry` from a selected flight works end-to-end (even if payment is stubbed).
1. No duplicate routing frameworks included accidentally (`pages/` vs `app/`).
1. No duplicated/casing-colliding docs/log files that will create CI/deploy noise.

---

## Blockers / Questions (Need Your Decision)

1. **Do you intend to ship all untracked directories/files now?**  
   Specifically `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, and the many new `src/components/*`. If “no”, we should define a minimal inclusion set.

2. **Which router is the real product direction: `app/` router only, or do you still need `pages/`?**  
   Having both tends to cause confusion and accidental route collisions.

3. **Are `SYNC_LOG.md` / `sync_log.md` and `WIKI*` files part of the product repo, or internal ops artifacts?**  
   If internal, they should not ship in the release milestone.

4. **Is `src/data/flights.ts` mock data meant for demo, or should this milestone require a real backend/API?**  
   This single decision changes scope dramatically.

5. **What’s inside the one local commit (ahead by 1)?**  
   Is it part of this flights work, or unrelated? If unrelated, it’s a release risk.
\n## 2026-05-11 05:44 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### plan report
**Prioritized TODO Plan (Ship-focused, minimal scope first)**

1. **Stabilize Flights Listing Page (highest priority)**
1. Define the intended “v1” UX for `/[locale]/flights` given the large diff:
   - What is the primary job: search results listing, discovery browsing, or “demo showcase” of many advanced widgets?
1. Ensure the page has one clear “happy path”:
   - User lands, sees results, can filter/sort, can open a flight detail (`/[locale]/flights/[slug]`) or proceed to checkout.
1. Identify and remove or gate anything that risks shipping:
   - Experimental widgets that pull in heavy client code, randomization, timers/toasts, voice/map, AR sizing, etc.
   - Anything that breaks SSR expectations or causes hydration mismatch.
1. Confirm data flow for flights:
   - `src/data/flights.ts` is currently the source of truth; confirm it matches the UI assumptions (fields for stops, cancellation, baggage, airline, price trend, etc.).
1. Harden empty/error states:
   - No results for current filters, invalid query params, missing locale, missing slug mapping.

2. **Route Integrity & Navigation**
1. Confirm that these routes are coherent and linked:
   - `/[locale]/flights` (listing)
   - `/[locale]/flights/[slug]` (detail)
   - `/[locale]/checkout` (checkout)
1. Ensure each route has a minimal, consistent contract:
   - “Selecting a flight” must produce a stable payload (id/slug, price, segments) that checkout can consume.

3. **Performance and Bundle Risk Control**
1. Audit what is imported into `src/app/[locale]/flights/page.tsx`:
   - If the file is now a “kitchen sink” page, split by making only essential components load by default.
1. Decide gating rules:
   - Feature flags (env-based) or “progressive disclosure” (only render advanced modules after a user action).
1. Ensure the listing page is not dominated by client-only components.

4. **Content/Repo Hygiene for a Clean Ship**
1. Decide what to do with the untracked documentation/log files:
   - `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`, `sync_log.md`
1. Decide what directories are real product code vs scaffolding:
   - untracked `components/`, `pages/`, `lib/`, `scripts/`, `src/pages/`
   - Avoid duplicate “Next.js-era” structures (`pages/` vs `src/app/`) unless intentionally used.
1. Establish what belongs in the next release vs parked prototypes.

5. **QA Pass (pre-ship)**
1. Minimal acceptance checks (manual):
   - Flights listing loads on mobile + desktop.
   - Filtering and sorting change visible results correctly.
   - Clicking a card goes to detail, and checkout is reachable.
1. Regression checks:
   - Locale switching doesn’t break routes.
   - No console errors on first load.

---

**Next Ship Milestone (proposed): “Flights v1: Listing → Detail → Checkout”**

Deliverable definition:
- `/[locale]/flights` is stable, fast, and focused on searching/browsing flights.
- Filters + sort work and are understandable.
- Users can open a flight detail and proceed to checkout with a consistent data contract.
- Advanced “trend” modules remain present only if they don’t endanger performance/reliability (otherwise gated off for the next milestone).

Success criteria:
- One clear conversion path works end-to-end.
- No major hydration/runtime errors.
- Page remains performant enough to be credible as a Kayak-style listing baseline.

---

**Blockers / Questions (need your decision to finalize scope)**

1. **What is the intended scope of `src/app/[locale]/flights/page.tsx` right now?**
   - Is it meant to be the production listing page or a “feature showcase” page that includes many 2026-trend modules?

2. **Which features are in-scope for the next release? Pick one set:**
   - A: Core only (listing + filters + sort + detail + checkout)
   - B: Core + 1 advanced widget (e.g., DynamicPriceChart OR SavedSearches)
   - C: Core + multiple advanced widgets (higher ship risk)

3. **Data contract question:**
   - Should checkout be driven by a query string / route state, localStorage, or a global store? (Pick one; mixing will cause edge cases.)

4. **Repo structure:**
   - Are `components/`, `pages/`, `lib/`, `scripts/`, `src/pages/` intended to exist alongside `src/app/`?
   - If yes, what is the rule for where new code goes?

5. **Docs/log files:**
   - Should the wiki/sync logs be committed, or are they local artifacts that should be `.gitignore`’d?

## 2026-05-11 05:53 UTC

### git status -sb
```
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
```

### git diff --stat
```
PLAN.md                           |  15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
```

### PLAN.md (1-120)
```text
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

### opencode plan output
```text
**Prioritized TODO Plan**

1. Stabilize flights list page
1. Verify `src/app/[locale]/flights/page.tsx` renders with no runtime errors on server and client
1. Confirm data contract for flight items: required fields, optional fields, default fallbacks
1. Validate filter and sort behavior: empty state, no results state, large result sets, and edge cases like missing prices or dates
1. Ensure locale routing works: `locale` param present, correct strings, correct currency and date formatting expectations
1. Check navigation paths: from flights list to flights slug page and to checkout flow, including back navigation

2. Integrate new feature components with minimal scope
1. Identify which of the many new components are actually used by the flights page now versus staged for later
1. Remove or postpone any unused imports or dead UI paths in the flights page to reduce bundle and risk
1. Ensure shared UI primitives in `components/` and `src/components/` do not conflict in naming, import paths, or style assumptions

3. Define and ship Predictive Trip Bundler milestone slice
1. Confirm what "component hazirlandi" means in deliverable terms: visible UI, working bundling logic, or just scaffolding
1. Implement the smallest shippable bundler flow: show recommended bundles for a selected flight with transparent pricing explanation
1. Add telemetry plan for conversion funnel: impressions, clicks, add to checkout, purchase completion

4. Checkout readiness and correctness
1. Confirm `src/app/[locale]/checkout/` routes compile and have a basic happy path
1. Validate pricing consistency: selected flight price matches checkout summary and does not change unexpectedly
1. Validate persistence: selected flight stored in URL, state store, or session and survives refresh

5. Content and documentation hygiene
1. Reconcile `SYNC_LOG.md` and `sync_log.md` naming duplication risk on case sensitive vs case insensitive systems
1. Decide whether `WIKI.md` and `WIKI_SYNC.md` are meant to be shipped or internal
1. Ensure `CHANGELOG.md` reflects the milestone, not the full backlog of components

6. Repository structure cleanup decisions
1. Decide on single source of truth for routing: `src/app/` vs `pages/` vs `src/pages/` and avoid parallel routing systems unless intentional
1. Decide on components folder conventions: `components/` vs `src/components/` and enforce one import root for consistency
1. Confirm `lib/` and `scripts/` additions are required for this milestone and do not introduce deployment or CI fragility


**Next Ship Milestone**

Milestone name: Flights V1 with Predictive Trip Bundler Preview

Exit criteria:
1. Flights list page works end to end: list, filter, sort, open a flight detail, proceed to checkout
1. Predictive Trip Bundler appears in one place only: either flights detail page or checkout upsell section
1. Checkout displays consistent selected itinerary and price with a clear summary
1. No broken routes across locales
1. No duplicate routing systems used for the same feature path
1. Basic docs updated: CHANGELOG entry plus a short WIKI section describing the shipped slice


**Blockers and Risks**

1. Scope explosion risk
1. Large number of new components and new directories are present, likely beyond what can be safely shipped at once

2. Routing ambiguity risk
1. Presence of `pages/` and `src/pages/` alongside `src/app/` suggests potential mixed routing that can cause unexpected behavior or build warnings

3. Path and casing risk
1. Both `SYNC_LOG.md` and `sync_log.md` may create confusion and merge conflicts across different OS filesystems

4. Integration risk
1. Flights page changed heavily, but only two tracked files show modifications while many new files are untracked, suggesting incomplete wiring or partially staged work

5. Build and deployment risk
1. Untracked `scripts/` and `lib/` may add runtime assumptions not covered by current deployment environment


**Questions to Unblock**

1. What is the intended base routing system for this project right now: app router only, pages router only, or mixed by design
1. Which single user journey should be shipped next: flights list to detail to checkout, or flights list to checkout directly
1. Predictive Trip Bundler target placement: flights detail page or checkout upsell, pick one for the milestone
1. Which of the new components are required for the milestone versus experimental backlog
1. Should we keep both `components/` and `src/components/`, or consolidate to one
1. Confirm naming decision for sync logs: keep only one of `SYNC_LOG.md` or `sync_log.md`
1. Do you want a strict minimal ship that ignores most new untracked files, or a broader ship that includes them after integration and cleanup
```
\n## 2026-05-11 06:03 UTC
branch: main (ahead 1)

git status -sb:
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

git diff --stat:
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

PLAN.md excerpt (1-120):
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

opencode plan output:
**Prioritized TODO Plan (Ship-Focused)**

1. **Stabilize Repo Structure (Highest Priority)**
1. Decide and enforce routing convention: `src/app` vs `pages/` vs `src/pages/` currently all appear present.
1. Remove/avoid duplicate top-level directories (`components/`, `lib/`, `pages/`) if they are accidental or transitional.
1. Confirm Next.js version and expected structure (your `AGENTS.md` warning implies nonstandard Next). This affects everything else: routing, data fetching, i18n, builds.

2. **Get Flights Listing to a “Production-OK” Baseline**
1. Define the flights listing contract: URL params, filters, sorting, pagination/infinite scroll, empty states, loading states, error states.
1. Ensure `src/app/[locale]/flights/page.tsx` is not a “god page”:
1. Identify what is presentational vs business logic vs data.
1. Decide what must be server-rendered vs client-interactive.
1. Lock down performance budget:
1. Avoid huge client bundles from importing many optional “trend” components.
1. Ensure flight data (`src/data/flights.ts`) is treated as stub/mocked and is easy to swap for real API later.

3. **Define Detail Page + Checkout Hand-off (MVP Path)**
1. Confirm canonical flow: Listing -> Flight Detail (`src/app/[locale]/flights/[slug]/`) -> Checkout (`src/app/[locale]/checkout/`).
1. Decide how selection is persisted between steps:
1. URL-only (preferred for shareability), or
1. localStorage/sessionStorage, or
1. server session.
1. Ensure checkout can render with only that persisted selection data, and has a clear fallback when missing.

4. **Gate Optional “Phase 8-11” Modules Behind a Strategy**
1. Pick a feature-flag approach (even if manual constants) so the UI doesn’t become unstable.
1. Create a “demo mode” vs “prod mode” policy:
1. Demo mode can show AI planners, gamification, social proof toasts.
1. Prod mode only shows what’s wired end-to-end.

5. **Documentation + Hygiene (Fast Wins, Prevents Drift)**
1. Clarify in `PLAN.md` what is actually shipped vs “component exists”.
1. Establish a single source of truth for sync logs: you have both `SYNC_LOG.md` and `sync_log.md` plus wiki sync files.
1. Decide whether `CHANGELOG.md` is user-facing release notes or dev log.

---

**Next Ship Milestone (Recommend): “Flights MVP Beta”**

Goal: A user can search/filter/sort flights, open a flight detail, and complete checkout with a confirmation state, in the correct locale routing, without relying on placeholder-only flows.

Deliverables:
1. Flights listing: working filters + sorting + stable UI states (loading/empty/error).
1. Flight detail: shows itinerary + baggage/cancellation + price tracking UI if you want, but must not break flow.
1. Checkout: accepts selected flight, shows order summary, and reaches success screen (even if payment is mocked).
1. Routing/i18n: `[locale]` routes work consistently; no duplicate router conflicts (`pages` vs `app`).
1. Build baseline: one command to run locally, one command to build, both succeed.

Non-goals for this milestone:
1. Predictive bundler, AI concierge, AR luggage sizing, voice maps, etc. Keep them off by default.

---

**Blockers / Clarifying Questions (Need Answers Before Execution)**

1. **Next.js architecture decision**
1. Is the intended routing system App Router only (`src/app`), or do you still need Pages Router (`pages/` / `src/pages/`)?
1. Are `components/`, `lib/`, `pages/`, `scripts/` newly added and meant to stay, or accidental copies?

2. **What is the actual “source of truth” for flight data right now**
1. Should `src/data/flights.ts` remain a static mock for now, or are you planning an API integration next?
1. If API soon: what backend (Supabase? custom?) and what data shape?

3. **Definition of “done” for the next milestone**
1. Is the milestone strictly UI/UX demo, or must checkout produce a persisted booking record (Supabase)?
1. Do you need authentication for checkout in this milestone, or guest-only is acceptable?

4. **Locale expectations**
1. Which locales are supported today, and do you want locale-specific content or just translated UI chrome?
1. Should URLs be shareable and stable across locales?

5. **Repo hygiene**
1. Do you want to commit currently untracked files (`WIKI*.md`, `SYNC_LOG.md`, new directories), or are some generated and should be ignored?

If you answer the 5 sections above (even briefly), I can turn this into an execution-ready, step-by-step implementation checklist scoped to your exact architecture and “definition of shipped.”
\n---\n# 2026-05-11 06:15:04 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## Plan report
**Prioritized TODO Plan (Ship-Driven)**

1. **Stabilize the baseline (before shipping anything)**
1. Decide what the current “product surface” is: Flights listing only, or listing + flight detail + checkout.
1. Define the single source of truth for routing: confirm whether this repo is fully App Router (`src/app/...`) or still relies on `pages/` for some routes. The current tree shows both `src/app/...` and `pages/` plus `src/pages/` (risk of duplicate routes and build/runtime ambiguity).
1. Confirm i18n expectations: what locales exist, what is the default, and whether `[locale]` routes must be exhaustive.

2. **Get the Flights listing to “release quality”**
1. Validate the new `src/app/[locale]/flights/page.tsx` work: ensure it’s not doing too much client-only work, avoid hydration pitfalls, and keep the UX coherent with filters/sort/cards.
1. Confirm data contract for flights: `src/data/flights.ts` exists untracked; decide whether it is demo seed data or intended as the initial production adapter. If demo, clearly separate “mock” vs “provider”.
1. Ensure core UX is complete:
   - Loading/empty/error states
   - Filter + sort interaction rules (e.g., sort stable, filters combinable, reset behavior)
   - URL query params: decide if filters/sort are encoded in the URL for shareability and back/forward correctness

3. **Route integrity and duplication cleanup**
1. Inventory routes likely to collide: `pages/`, `src/pages/`, and App Router segments under `src/app/`.
1. Decide one routing strategy for each feature area (flights, checkout, flight detail). If both systems remain, explicitly document what owns what and why.
1. Confirm the dynamic route for flight detail exists and is wired: `src/app/[locale]/flights/[slug]/` is untracked, but PLAN claims flight detail is “done”. Verify it actually renders and links from listing.

4. **Checkout integration sanity**
1. Confirm checkout route existence and path: `src/app/[locale]/checkout/` is untracked.
1. Define the minimal checkout contract for the milestone: what a user can do end-to-end (select flight -> proceed -> confirmation screen).
1. Decide auth requirement: PLAN says guest checkout allowed; ensure flows don’t accidentally require login.

5. **Scope control: quarantine “trend modules”**
1. All the novelty components (AI planner, AR sizer, voice map, gamification, etc.) should be treated as “behind a feature flag” or “not wired yet” for the next ship milestone.
1. Decide whether to keep them untracked/unshipped or add them with an explicit `EXPERIMENTAL/` or `lab/` style boundary plus documentation.
1. If any of these are already imported into `flights/page.tsx`, remove from the release path or gate them.

6. **Repo hygiene (so it’s shippable to others)**
1. Decide what `CHANGELOG.md`, `SYNC_LOG.md`, `sync_log.md`, `WIKI*.md` are for:
   - If generated by cron, they should not be versioned or should be in a controlled format/location to avoid churn.
   - Pick one canonical filename casing (`SYNC_LOG.md` vs `sync_log.md`) to avoid cross-platform issues.
1. Decide which untracked directories are real product code vs accidental copies (`components/`, `src/components/` both exist; same for `pages/` vs `src/pages/`, `lib/`, `scripts/`).

7. **Verification gates (minimum bar before ship)**
1. Define “green” criteria: `lint`, `typecheck`, `build`, and a basic smoke navigation of flights -> detail -> checkout.
1. Add at least one minimal UI test strategy decision: none for now (manual smoke), or a tiny set of route render tests.

---

**Next Ship Milestone (Recommended): “Flights MVP v1” (1-week target)**

Deliver a coherent, demoable user journey:

1. Flights listing page at `/<locale>/flights`
1. Working filter + sort + flight card rendering (no broken states)
1. Click a flight card to a flight detail route `/<locale>/flights/<slug>` (even if data is mock)
1. A “Continue to checkout” CTA that navigates to `/<locale>/checkout` and shows an order summary placeholder + success confirmation

Explicitly out of scope for this milestone:
- AI planner, gamification, AR sizing, voice map, sustainability scoring, social proof toasts, loyalty tiers, collaborative boards
- Real flight provider integration (unless you confirm you already have one ready)

---

**Primary Blockers / Risks**

1. **Routing ambiguity**
- Presence of `pages/`, `src/pages/`, and `src/app/` strongly suggests potential route collisions and unpredictable behavior depending on Next config/version.

2. **Large untracked surface area**
- Many new components and directories are untracked; without reviewing their wiring, risk is shipping a broken build or dead code bulk.

3. **PLAN vs repo reality mismatch**
- PLAN shows many modules “completed”, but git indicates only `flights/page.tsx` and `PLAN.md` are modified, while the claimed completed modules appear untracked (not actually in version control yet).

4. **Generated docs/log churn**
- `SYNC_LOG.md`/`sync_log.md` plus WIKI sync files indicate automation. If these are committed, they can cause constant diffs and noisy history.

---

**Questions I Need Answered (to unblock execution order)**

1. Do you intend to ship using **App Router only** (`src/app`) or keep **Pages Router** (`pages`/`src/pages`) for some areas?
1. For the next milestone, do you want **Flights-only** or **Flights + detail + checkout**?
1. Are `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI.md`, `WIKI_SYNC.md` meant to be committed artifacts, or should they be ignored/generated?
1. Is `src/data/flights.ts` authoritative demo data, or should we design an adapter boundary (so swapping to real API later is trivial)?
1. Should filters/sort be **URL-driven** (shareable links) or local UI state for now?
\n---\n# Izgetour Plan Report - 2026-05-11 06:23 UTC\n
Branch: main (ahead 1)

## git status -sb
```
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
```

## git diff --stat
```
PLAN.md | 15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)
```

## PLAN.md (first 120 lines excerpt)
```
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
```

## Plan output
```
I can’t produce a grounded, prioritized TODO plan from “git status/diff stat/PLAN excerpt above” because that context is not present in this chat. With “no tools” I also can’t inspect your workspace to reconstruct it.

Paste the following (raw text) and I’ll turn it into a prioritized plan with a ship milestone and a blockers/questions list:

1. `git status` output  
2. `git diff --stat` (or `git diff --stat --staged` if you have staged changes)  
3. The PLAN excerpt you referenced (even partial is fine)  
4. Any explicit deadline / target environment (prod/staging) and “definition of done”

In the meantime, here’s the exact structure I’ll produce once you paste it (so you can see what you’ll get):

**Prioritized TODO (P0/P1/P2)**
1. P0: Ship-blocking correctness/security issues surfaced by diff/status (breaks build, failing tests, env/config, auth, data loss).
2. P0: Complete any partially implemented flows implied by PLAN excerpt (missing handlers, migrations, routing, permissions).
3. P0: Add/repair minimal validation, error handling, and rollback strategy for risky operations.
4. P1: Close integration gaps (API contracts, types, UI wiring, feature flags, telemetry).
5. P1: Add targeted tests for the changed behavior (smoke + regression around the touched modules).
6. P2: Refactors and cleanup only if they reduce near-term risk (dead code, rename consistency, docs).

**Next Ship Milestone**
- Milestone name: `vNext: <theme from PLAN>`
- Scope: only P0 items + the smallest P1 needed to de-risk release
- Exit criteria:
  1. Working tree clean except known follow-ups
  2. Tests passing (or explicitly waived with rationale)
  3. Manual smoke checklist for the changed user flows
  4. Rollback/feature flag plan confirmed

**Blockers / Questions (to unblock execution)**
- What is the release target date/time?
- Are there any “must-not-change” areas (schemas, URLs, public APIs)?
- Are staged changes intended for this milestone, or are there WIP/unrelated diffs?
- Any known failing tests, CI failures, or runtime errors right now?
- Environments and secrets handling: do we need migrations, new env vars, or service credentials?

Paste the three artifacts and I’ll fill this in with concrete, file- and change-aware TODOs (including sequencing and ownership suggestions if multiple people are working).
```

## 2026-05-11 06:33 UTC

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (first 120 lines)
(see repo file; excerpt captured in cron run)

### Plan report (opencode)
**Prioritized TODO Plan (Read-Only, No Tools)**

1. **Stabilize scope for “Phase 11: Predictive Trip Bundler” (ship slice, not the universe)**
1. Define the exact user-visible outcome for Phase 11 on the Flights page:
   - Example outcomes: “recommended bundle: flight + hotel + luggage + insurance” or “smart add-ons + savings estimate”
1. Decide acceptance criteria (3-7 bullet points) that can be tested manually in under 5 minutes.
1. Freeze the UI surface area for this milestone:
   - Which components are allowed to render on `src/app/[locale]/flights/page.tsx`
   - Which “ready” components are explicitly deferred

2. **Audit the current Flights page integration (risk control)**
1. Identify what `src/app/[locale]/flights/page.tsx` is doing now (it grew by ~290 lines): data sourcing, filtering/sorting, rendering, bundler logic, and any client/server boundary.
1. Confirm which of these are “demo-only” vs “production path” (mock data, static arrays, placeholder pricing).
1. Check for Next.js app-router correctness risks:
   - Client Components vs Server Components boundaries
   - Use of hooks only in client components
   - Any `window`/browser-only APIs used in server context
1. Confirm i18n/`[locale]` is still respected (routing + text + currency formatting assumptions).

3. **Define “bundler” inputs/outputs contract (so components don’t sprawl)**
1. Write down the minimal data model needed for bundling:
   - Flight selection (or candidate list)
   - Dates, party size, cabin, budget constraints
   - Hotel location constraints (airport/city/region)
1. Decide the bundler output structure:
   - A ranked list of bundles with reasons, savings estimate, confidence score
1. Decide what is computed deterministically vs heuristic/AI-assisted (keep first ship deterministic unless there’s already a safe AI path).

4. **Establish a single source of truth for flight data**
1. If `src/data/flights.ts` is the source, decide whether filters/sorts operate directly on that or through a normalized layer.
1. Ensure `FlightFilters`, `FlightSortSelect`, `FlightCard`, and `ComparePanel` agree on the same shape (avoid “prop drift”).
1. Decide how “slug page” (`src/app/[locale]/flights/[slug]/`) maps to the list page object identity (stable ID/slug generation).

5. **Shipping UX: make Phase 11 feel real even if it’s mocked**
1. Ensure the bundler area has:
   - Clear call-to-action (“Build my trip bundle” / “Optimize my trip”)
   - Empty/loading/error states (even if fake)
   - Explanation text that sets expectations (“Estimates based on sample inventory” if applicable)
1. Add a minimal “bundle details” view:
   - What’s included, why it’s recommended, and a clear next step to checkout.

6. **Checkout integration constraints (avoid dead-end flows)**
1. Confirm what `src/app/[locale]/checkout/` expects as input (route params, query string, state store).
1. Choose one integration path for this milestone:
   - “Flight only to checkout” plus “bundle add-ons as optional toggles”
   - Or “bundle selection goes to checkout pre-populated”
1. Ensure there is at least one complete happy path end-to-end:
   - Flights list → choose flight/bundle → checkout page renders coherent summary.

7. **Clean up repo hygiene just enough to ship**
1. Decide what to do with new top-level docs and sync logs:
   - `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`, `sync_log.md`
1. Confirm what belongs in git vs local tooling artifacts (avoid committing noisy sync logs if not required).
1. Ensure `PLAN.md` changes reflect actual shipped scope (not aspirational only).

8. **Verification checklist (fast + repeatable)**
1. Manual smoke checklist (desktop + mobile widths):
   - Flights page renders
   - Filters/sort work and do not crash
   - Flight details slug page works (if linked)
   - Checkout route works from at least one CTA
1. Basic build/test gates you typically run before merging (you decide the standard for this repo):
   - `lint`, `typecheck`, `build` (or equivalent)

---

**Next Ship Milestone (Recommended)**  
**Milestone: “Phase 11 v1: Bundled Trip Recommendation on Flights Page”**

Deliverables:
1. Flights list page shows flights with working filters/sort and compare (if already integrated).
1. A “Predictive Trip Bundler” panel that produces **3 recommended bundles** for a selected flight (or top flight) using deterministic heuristics.
1. Each bundle has:
   - Inclusions (hotel + add-ons)
   - Savings/price estimate (even if approximate)
   - Reasons (3 short bullets)
   - CTA to proceed to checkout (pre-populated or at least coherent)
1. One end-to-end happy path to checkout without broken navigation.

Non-goals for this milestone (explicitly defer):
1. Voice/AR/map/gamification extras unless already stable and essential.
1. Full AI planner orchestration across many widgets.
1. Real inventory/pricing integrations (unless they already exist and are safe).

---

**Blockers / Questions (Need Your Answers Before Implementation)**

1. **What is “ship” for you right now?**
   - Deploy to production, merge to main, or a demo build?
1. **Are the new directories (`components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`) intentional?**
   - This looks like mixed Next.js structures (app router + legacy pages). Is that expected in this repo?
1. **Which of these are real vs experimental?**
   - Many components are marked “ready”. Which ones must be included in the next milestone vs can remain unused?
1. **What’s the bundler’s data source today?**
   - Purely `src/data/flights.ts` mock data, or any API layer already exists?
1. **Checkout contract:**
   - How does checkout receive selected items today (URL params, global store, server action, etc.)?
1. **Locale requirements:**
   - Do you need currency/number/date localization correct for this ship, or is English-only acceptable for v1?
1. **Repo hygiene:**
   - Should `SYNC_LOG.md`, `sync_log.md`, and `WIKI_SYNC.md` be committed, or are these local artifacts you don’t want in main?
\n---\n## 2026-05-11 06:43 UTC\n
Branch: main (ahead 1)

GIT_STATUS
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

DIFF_STAT
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT_1_120
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

PLAN_REPORT
**Onceliklendirilmis TODO Plani**

1. Calisma agacini temizle ve kapsam belirle
1. Bu degisikliklerin hepsi ayni amac icin mi: flights sayfasi gelistirmeleri mi, yoksa wiki ve sync altyapisi da bu releasee girecek mi netlestir
1. Untracked dosyalarin amacini ayir: urun ozelligi mi (components, lib, pages, checkout, flights slug), yoksa dokumantasyon ve otomasyon mu (CHANGELOG, WIKI, SYNC_LOG, WIKI_SYNC, sync_log)
1. Branch main uzerinde ahead 1 gorunuyor, remote ile farkli commit var mi ve bu fark release riskini artiriyor mu kontrol et

2. Flights sayfasi degisikliklerini urun seviyesinde stabilize et
1. src/app/[locale]/flights/page.tsx icin kabul kriterlerini yaz: filtreleme, siralama, kartlar, karsilastirma paneli, fiyat grafigi, saved searches, price alert gibi hangi moduller sayfada aktif
1. Performans ve SSR CSR sinirlarini netlestir: sayfa server render mi, client components yogun mu, veri kaynagi mock mu (src/data/flights.ts)
1. UX dogrulama listesi: mobil kirilimlar, filtre paneli davranisi, empty state, loading state, hata durumlari

3. Ucus detay ve checkout rotalarini minimum ship icin uyumlu hale getir
1. Untracked src/app/[locale]/flights/[slug]/ ve src/app/[locale]/checkout/ icin rota haritasi cikar: listingten detaile, detailden checkouta gecis calisiyor mu
1. Kritik akislari test et: ucus sec, detay gor, fiyat takibi, sepete ekle, checkout adimlari, basarili ekran

4. Bilesen patlamasini kontrol altina al
1. Untracked src/components altindaki bilesenleri gruplandir: flights odakli olanlar, gamification, itinerary, ai planner, harita, sosyal proof
1. Ship icin zorunlu olmayanlari feature flag veya lazy load dusun
1. Tasarim sistemi ve stil tutarliligi: kart, filtre, buton, badge, toast

5. Dokumantasyon ve sync dosyalarini release disina ayir veya kurala bagla
1. PLAN.md degisiklikleri: roadmap ve durumlar guncel mi, gercek teslim edilenle uyusuyor mu
1. CHANGELOG.md ve wiki dosyalari: release notlari icin gerekli mi, yoksa internal mi
1. SYNC_LOG, WIKI_SYNC, sync_log gibi dosyalar: otomatik uretiliyorsa repoya girmemeli olabilir, gitignore politikasini belirle

6. Kalite kapilari
1. Typecheck ve lint hatalari var mi
1. Build aliniyor mu
1. Smoke test senaryolari: flights listing, flights detail, checkout

---

**Bir Sonraki Ship Milestone (Oneri)**

Milestone: Flights Modulu v1 Listing plus Detail plus Checkout happy path

Kapsam:
1. Flights listing sayfasi: filtre, siralama, flight card, basic karsilastirma ya da saved searchten en fazla biri
1. Flights detail slug sayfasi: sefer detaylari ve fiyat takibi
1. Checkout akisi: guest checkout dahil minimum odeme onayi UI ve siparis ozeti

Milestone disi:
1. AI planner, voice map, party plan, loyalty tiers, gamification gibi advanced moduller
1. Wiki sync ve otomasyon log dosyalari

Basari olcumu:
1. Listingten checkouta 3 adimda akisin bozulmamasi
1. Mobilde filtre ve kartlarin kullanilabilir olmasi
1. Build ve basic testlerin gecmesi

---

**Blockerlar ve Sorular**

1. Bu release icin hedef ne: flights deneyimi mi, yoksa tum yeni modulleri birden ship etmek mi
1. Untracked klasorler components, lib, pages, scripts, src pages bunlar gercekten yeni urun kodu mu yoksa daha once commitlenmemis gecici calisma mi
1. SYNC_LOG, WIKI_SYNC, sync_log dosyalari otomatik uretiliyor mu, repoya alinmasi isteniyor mu
1. main branch ahead 1 durumu var, o commit neydi ve bu degisikliklerle baglantili mi
1. Next shipte hangi 2 ozellik olmazsa olmaz: karsilastirma paneli mi, dynamic price chart mi, saved searches mi, price alert mi
1. Veri kaynagi: src/data/flights.ts mock mu, yoksa entegrasyona mi baglanacak

Bu sorulara yanit verirsen TODO listesini ship kapsamina gore daraltip daha net teslim listesine donusturebilirim.
## 2026-05-11 06:53 UTC

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

### plan report
**Prioritized TODO Plan (Ship-First)**

1. **Stabilize repo state and scope the change**
1. Decide what belongs in the next milestone vs what’s experimental/prototype.
1. Identify which of the many untracked paths are actually required for the current product direction (notably `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, `sync_log.md` duplicates, multiple wiki/changelog files).
1. Confirm whether `main...origin/main [ahead 1]` is intentional (there’s already one local commit not on origin).

1. **Define “Flights v1” acceptance criteria (minimal shippable)**
1. Flights listing page must load reliably with: search input, results list, filters, sort, and navigation to detail.
1. Data source must be explicit: mock (`src/data/flights.ts`) vs API (server route) vs third-party integration; define what “real” means for this milestone.
1. i18n/locale correctness: verify `[locale]/flights` respects locale routing and strings.

1. **Triage `src/app/[locale]/flights/page.tsx` (large diff risk)**
1. Review what changed in the +290 lines: ensure no hardcoded assumptions, duplicated components, or client-only logic accidentally placed in a server component.
1. Ensure performance constraints: avoid rendering huge lists without pagination/virtualization (even if mock data grows).
1. Confirm URL/search param handling is deterministic (deep-linkable filters/sort).

1. **Information architecture cleanup (avoid Next.js routing conflicts)**
1. Decide: are you App Router-only (`src/app/...`) or also keeping `pages/` + `src/pages/`? Mixing often causes confusion, duplicate routes, and build-time conflicts.
1. If `pages/`/`src/pages/` are experiments, explicitly quarantine (docs + ignore) or delete later; if they’re real, define routing ownership.

1. **Checkout linkage sanity**
1. Confirm the new `src/app/[locale]/checkout/` route aligns with the flights funnel (CTA from flight card/detail leads to checkout with correct payload).
1. Define what is persisted (localStorage vs server) and how it behaves for guest checkout.

1. **Documentation and release hygiene**
1. Consolidate `CHANGELOG.md`, `SYNC_LOG.md`, `sync_log.md`, `WIKI*.md` into one coherent source of truth (or clearly separate purpose).
1. Update `PLAN.md` to reflect what is actually implemented vs “component hazırlandı ✅” (right now the repo status suggests many components exist but may not be wired).

---

**Quality/Verification TODOs (Before Shipping)**
1. **Build + route verification**
1. Confirm Next build passes with the current mixture of routes/components.
1. Manually smoke test: `/[locale]/flights` -> detail `/[locale]/flights/[slug]` -> checkout.

1. **Data correctness + edge cases**
1. Empty results state.
1. Invalid query params (bad dates, reversed ranges, unknown airports).
1. Locale-specific formatting for currency/date/time.

1. **UX essentials**
1. Loading states for results and filters.
1. Mobile layout: filters usability (drawer) and compare panel if enabled.

---

**Next Ship Milestone (Proposed): “Flights v1: Usable Funnel”**
Scope for the next shippable milestone (tight, realistic):

1. Flights listing page (`/[locale]/flights`) loads fast and is deep-linkable (filters/sort via URL).
1. Flight detail page (`/[locale]/flights/[slug]`) works for at least the mock dataset and supports price tracking UI if already implemented.
1. “Book/Continue” CTA takes the user into `/[locale]/checkout` with a stable summary of the selected itinerary.
1. No routing ambiguity (pick App Router as canonical; anything else is clearly non-shipping).
1. Docs: single changelog entry + brief “how to run + what’s included in v1”.

If you want a smaller milestone: **“Flights Listing v1”** only (listing + filters/sort + detail navigation), defer checkout wiring.

---

**Blockers / Questions (Need Answers to Proceed Safely)**
1. Are the many untracked folders (`components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`) intended to ship, or are they generated/experimental?
1. Should this repo be **App Router-only**? If yes, should `pages/` and `src/pages/` be removed/ignored going forward?
1. What is the target for flights data in this milestone: mock-only (`src/data/flights.ts`) or a real API integration (and if real, which provider/back end)?
1. Do you want the upcoming ship milestone to include **checkout completion** (payment flow), or just the pre-checkout funnel?
1. There’s already `main` ahead of origin by 1 commit. Is that commit part of this work, and should the next work build on it or be separated?

---


---
## 2026-05-11 07:04 UTC

### Git status
```
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
```

### Git diff --stat
```
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
```

### PLAN.md (1-120)
```
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
```

### Plan report (opencode plan agent)
```
**Next Ship Milestone (MVP “Flights v1 + Checkout Hook”)**
Ship a coherent end-to-end user flow that is stable, buildable, and reviewable:

1. Flights listing page renders for all locales and supports search/filter/sort using `src/data/flights.ts` as the data source.
2. Flight detail page works via `src/app/[locale]/flights/[slug]/` route and links correctly from listing cards.
3. Checkout entry exists via `src/app/[locale]/checkout/` and can accept a selected flight (even if only as a “review your selection” stub).
4. Documentation hygiene: `PLAN.md` reflects reality; only one canonical sync log/wiki file set exists; untracked content is either intentionally included or removed.

This milestone is primarily about integrating and de-risking what’s already been added (many new components/routes exist but are currently unverified from this context).

---

**P0 TODOs (Must Do Before Shipping)**
1. **Stabilize repo state and decide what’s in this release**
   - Confirm which of the many untracked directories are intended deliverables: `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/` (note both root-level and `src/` duplicates).
   - Decide canonical docs/log files:
     - You have both `SYNC_LOG.md` and `sync_log.md` (case-different duplicates, a common cross-platform trap).
     - You also have `WIKI.md` and `WIKI_SYNC.md`.
   - Output of this step: an explicit include/exclude list for commit/PR so the milestone doesn’t accidentally ship experimental modules.

2. **Route integrity: confirm Next.js routing isn’t split-brain**
   - You now have `src/app/...` (App Router) plus `pages/` and `src/pages/` (Pages Router patterns).
   - Decide which router is authoritative for this project right now.
   - Blocker risk: accidental route shadowing, unexpected build behavior, or confusing navigation in production.

3. **Flights listing page review for correctness and performance**
   - `src/app/[locale]/flights/page.tsx` changed heavily (+290 lines). Verify:
     - It is not accidentally importing from both `pages/` and `app/` worlds.
     - Filter/sort logic is deterministic and doesn’t depend on client-only APIs unless declared as client component.
     - Any new UI components referenced in this page exist in the expected path (`src/components/...` vs `components/...`).
   - Blocker risk: runtime errors from missing imports/paths due to duplicated `components/` roots.

4. **Flight detail + slug linkage**
   - Confirm listing cards link to `src/app/[locale]/flights/[slug]/` and the slug matches `src/data/flights.ts`.
   - Confirm the detail page can render for a direct navigation (not just client-side transitions).
   - Blocker risk: broken deep links and SEO/unshareable pages.

5. **Checkout entry point**
   - Confirm `src/app/[locale]/checkout/` exists and is reachable from flight selection.
   - Decide minimal contract: pass `flightId`/`slug` in URL vs store (localStorage) vs server state.
   - Blocker risk: user can’t complete flow; flights module feels “dead-end”.

---

**P1 TODOs (Should Ship With Milestone If Time Allows)**
1. **Remove/avoid feature-creep components from the critical path**
   - Many “trend” components are present (AITravelPlanner, VoiceInteractiveMap, AR sizer, gamification, etc.).
   - Decide whether they are:
     - Hidden behind feature flags / not rendered anywhere yet, or
     - Actually included in flights page (which could destabilize core flow).
   - Goal: keep listing/detail/checkout lean and reliable.

2. **Documentation alignment**
   - `PLAN.md` claims many phases are “Tamamlandi”. Make sure this is accurate relative to what’s actually wired into routes.
   - Create a short “What’s actually live in UI” section for the milestone.

3. **Changelog discipline**
   - You have `CHANGELOG.md` untracked. Decide if you want to start formal version notes now; otherwise it becomes noise.
   - If included, record only the shipped milestone scope (Flights v1 + detail + checkout hook).

---

**P2 TODOs (After Shipping / Next Milestone Candidates)**
1. **Predictive Trip Bundler (Faz 11)**
   - Only after core flight selection → checkout is stable.
2. **Notifications / price alerts**
   - LocalStorage tracking is mentioned; true notifications need backend integration (Supabase + email).
3. **Map view / split view comparison**
   - Useful UX, but not worth destabilizing core routing/build during MVP.

---

**Blockers / Questions (Need Your Decisions)**
1. Which routing system is authoritative right now: App Router only (`src/app`) or mixed with `pages/`? If mixed, what are the rules?
2. Are the root-level `components/`, `lib/`, `pages/`, `scripts/` meant to exist alongside `src/...`, or are they accidental duplicates/new structure migration?
3. Which “sync log” is canonical: `SYNC_LOG.md` or `sync_log.md`? (I strongly recommend picking one to avoid case-sensitive vs case-insensitive filesystem issues.)
4. Is the current goal to ship only Flights + Checkout, or also ship Hotels/Gamification/AI modules in the same release?
5. The branch is `ahead 1`: is that existing commit already intended to be part of this milestone, or should the milestone be a new clean commit series?

If you answer the 5 questions, I can turn this into a concrete “commit/PR checklist” with an inclusion list (exact directories/files), acceptance criteria, and a minimal smoke-test matrix for the milestone.
```

## 2026-05-11 07:13 UTC

### Git status
```
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
```

### Git diff --stat
```
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
```

### PLAN.md excerpt (1-120)
```md
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (Component hazırlandı ✅) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- (excerpt truncated; see PLAN.md)
```

### Plan report (opencode)
- Next ship milestone (recommended): Flights Module Hardening v1 (Flights Search -> Listing -> Detail -> Checkout, filters/sort/compare + price tracking)
- Top risks: very large flight listing delta (+290 LOC) + many untracked paths (possible prototypes/route-system mix)

**Top 3 TODO**
1) Stabilize flights listing change set (params parsing, filter/sort composability, empty/loading/error states, mobile)
2) Resolve untracked files: define ship set, exclude prototypes, avoid pages vs app router confusion
3) Verify end-to-end flow: listing -> detail -> checkout + localStorage SSR/locale safety

**Blockers / questions**
- Routing strategy: are pages/ and src/pages/ intentional?
- What is in the ahead 1 commit; should it ship?
- Should CHANGELOG/WIKI/SYNC_LOG/sync_log be versioned or gitignored?
- Milestone focus: flights hardening vs bundler preview vs checkout UX vs repo hygiene first?
- Data plan: keep flights mocked or integrate API next?
\n---\n# izgetour plan report\nTime: 2026-05-11 07:25:04 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

## PLAN.md excerpt (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

## opencode plan
**Prioritized TODO Plan (Ship-Focused, No Code Changes Yet)**

1. **Stabilize repo state + decide what is in-scope for the next ship**
   1. Decide whether the next milestone is “Flights listing UX complete” or “End-to-end booking path (Flights → Detail → Checkout)”.
   2. Identify which of the many untracked folders/files are real product work vs. experiments/scaffolding:
      1. `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/` (possible duplication with `src/app/…`)
      2. `sync_log.md` vs `SYNC_LOG.md` (case-duplication risk on macOS/CI)
      3. `WIKI*.md`, `CHANGELOG.md` (docs vs runtime)
   3. Define a strict “ship set” of files to include; everything else stays out of the milestone until validated.

2. **Confirm Next.js routing model consistency (biggest systemic risk)**
   1. You have both `src/app/...` and `src/pages/` / `pages/` present (and new). Decide if this project is intentionally hybrid (App Router + Pages Router) or if `pages/` is accidental drift.
   2. If hybrid is intended:
      1. Confirm route precedence and avoid duplicated routes (same pathname in both systems).
      2. Define where shared UI lives (`src/components` vs top-level `components`).
   3. If hybrid is not intended:
      1. Next ship should exclude the “other router” content until a deliberate migration plan exists.

3. **Flights listing page quality gate (since `src/app/[locale]/flights/page.tsx` changed heavily)**
   1. Establish the acceptance criteria for the flights listing page:
      1. Loads with zero runtime errors.
      2. Filters/sort do not break URL locale routing.
      3. Responsive layout works on mobile.
      4. Empty state and loading state are defined.
   2. Validate the data contract:
      1. `src/data/flights.ts` exists (untracked) and likely feeds the UI; confirm it matches the UI fields and edge cases (missing baggage, cancellation policy, multi-leg).
   3. Confirm performance guardrails:
      1. Avoid heavy client-side work in the listing page if it’s server-rendered.
      2. Ensure any dynamic widgets are lazy/conditional if needed.

4. **Detail + checkout path coherence (avoid dead-end UX)**
   1. You have untracked:
      1. `src/app/[locale]/flights/[slug]/` (flight detail)
      2. `src/app/[locale]/checkout/` (checkout flow)
   2. Define a minimal “happy path”:
      1. User selects a flight card.
      2. Lands on detail page for the selected item.
      3. Proceeds to checkout with a persisted selection (query params, state, or storage).
   3. Decide what persistence method is acceptable for the next ship (URL-only vs localStorage vs server session). For MVP, URL-only is usually safest and debuggable.

5. **“Module explosion” containment (many new feature components)**
   1. The repo has a large set of new components (AI planner, gamification, AR sizer, voice map, etc.). For the next ship, pick *one* optional “delight” feature at most, and gate the rest behind:
      1. Feature flags, or
      2. Not routed/linked from primary user flows.
   2. For each non-core component, answer:
      1. Is it used in any route today?
      2. Does it add dependencies (APIs, client-only libs, permissions like mic/camera)?
      3. Does it impact performance or bundle size?

6. **Docs and process hygiene (pre-ship, but lightweight)**
   1. `PLAN.md` says “cron checks every 10 minutes”; confirm this is aspirational or implemented. If not implemented, clarify in docs to avoid misleading.
   2. Decide what `CHANGELOG.md` should track (user-facing releases vs internal dev log).
   3. Resolve naming conventions: `SYNC_LOG.md` vs `sync_log.md` (pick one).

---

**Next Ship Milestone (Recommended)**

**Milestone: “Flights MVP: Search/Listing → Detail → Checkout (locale-aware)”**

**Scope**
1. `Flights listing` is stable and usable (filters + sort + responsive).
2. `Flight detail` renders for a selected flight (`[slug]` path) and shows core info (price, legs, baggage/cancellation if present).
3. `Checkout` can accept a selected flight and complete a “success” confirmation (even if payment is mocked).

**Explicitly out of scope for this ship**
1. AI concierge / planner, voice map, AR luggage sizing, sustainability scoring, social proof toasts, party planning, etc. (unless already integrated and stable).
2. Predictive bundling (Faz 11) unless it’s purely UI with no new backend coupling.

---

**Blockers / Questions (Need Your Answers Before Executing Work)**

1. Router intent: App Router only, or hybrid Pages Router too?
2. Ship target: Flights-only MVP end-to-end, or broader release?
3. File inclusion: include all untracked components, or keep minimal ship set?
4. Case-duplicate logs: SYNC_LOG.md vs sync_log.md which is canonical?
5. Data source direction: src/data/flights.ts mock only, or real API soon?
6. i18n expectations: query params localized or stable keys?
\n---\n# Izgetour Plan Report - 2026-05-11 07:33 UTC\n
## Git status (-sb)\n\nmain...origin/main [ahead 1]\n M PLAN.md\n M src/app/[locale]/flights/page.tsx\n?? CHANGELOG.md\n?? SYNC_LOG.md\n?? WIKI.md\n?? WIKI_SYNC.md\n?? components/\n?? lib/\n?? pages/\n?? scripts/\n?? src/app/[locale]/checkout/\n?? src/app/[locale]/flights/[slug]/\n?? src/components/* (many)\n?? src/data/flights.ts\n?? src/pages/\n?? sync_log.md\n
## Git diff --stat\n\nPLAN.md | 15 +-'\nsrc/app/[locale]/flights/page.tsx | 290 +++\n2 files changed, 293 insertions(+), 12 deletions(-)\n
## PLAN.md (lines 1-120 excerpt)\n\n# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)\n
## Opencode Plan Output\n\n**Prioritized TODO Plan (Ship-Focused, Based on Your Status/Diff Summary)**

1. **Stabilize the current flight listing page change (`src/app/[locale]/flights/page.tsx`, +290 lines)**
1. Define the intended behavior contract for the listing page:
   1. URL params: sort, filters, pagination, locale.
   1. Data source: static (`src/data/flights.ts`) vs API vs hybrid.
   1. Rendering mode: server vs client, and where filtering happens.
1. Audit for common regression risks introduced by a large diff:
   1. Hydration mismatches (if mixing server/client logic).
   1. Non-deterministic rendering (dates, random IDs, locale formatting).
   1. Loading/error/empty states.
   1. Accessibility basics (focus order, form labels, keyboard nav).
1. Ensure routing consistency:
   1. Listing links correctly target detail route (`src/app/[locale]/flights/[slug]/...`).
   1. Slug generation and lookup are consistent with `src/data/flights.ts`.

2. **Verify and normalize the new route surface area you’ve introduced (large untracked tree)**
1. Inventory new pages/routes quickly:
   1. `src/app/[locale]/checkout/` and `src/app/[locale]/flights/[slug]/` for App Router.
   1. `src/pages/` and `pages/` presence implies possible mixed routing (App Router + Pages Router).
1. Decide “one router path” per feature:
   1. Flights listing/detail/checkout should live either entirely in `src/app/...` or you intentionally support both (which is extra complexity).
1. Confirm shared components live in one place:
   1. If you now have both `components/` and `src/components/`, pick one as canonical and treat the other as legacy or delete later.

3. **Close the documentation/ops loop for all the new untracked docs/logs**
1. Decide which docs are product-facing vs internal:
   1. `CHANGELOG.md`: release notes (ship-facing).
   1. `PLAN.md`: internal roadmap (fine to keep, but don’t let it drift).
   1. `WIKI*.md`: decide if these replace `PLAN.md` or complement it.
   1. `SYNC_LOG.md` vs `sync_log.md`: pick one filename to avoid cross-platform pain and duplication.
1. Put a single source of truth for “what is shippable now”:
   1. A short milestone section in either `PLAN.md` or `CHANGELOG.md` (not both).

4. **Make “Predictive Trip Bundler (Phase 11)” an additive milestone, not a blocker**
1. Identify the minimal “bundler” deliverable:
   1. Basic recommendation list (static heuristics OK).
   1. Explicitly non-ML first version if needed.
1. Keep it behind a feature flag or a soft entry point:
   1. Don’t block checkout flow completion on bundling.

5. **Testing/verification pass (before any merge/ship)**
1. Decide what “done” means for this milestone:
   1. Listing page loads for at least one locale.
   1. Filters and navigation work.
   1. Detail page reachable.
   1. Checkout route reachable and returns a deterministic UI.
1. Add lightweight smoke checks (manual + minimal automated):
   1. A single happy-path navigation through landing → listing → detail → checkout.

---

## Next Ship Milestone (Smallest Valuable Release)

**Milestone: “Flights Browse v1”**
- Users can:
  1. Open the flights listing page in any supported locale.
  1. See a list of flights from `src/data/flights.ts` (or your current source).
  1. Click a flight to open the detail page (`/flights/[slug]`).
  1. Continue to checkout route (`/checkout`) and see a stable confirmation/entry UI (even if payment is stubbed).

**Success criteria**
- No routing ambiguity (App Router vs Pages Router) for these flows.
- No fatal runtime errors, no hydration warnings in core pages.
- Basic empty/error states exist (even placeholder messaging).

---

## Blockers / Questions (Need Your Answers to Reduce Rework)

1. **Routing architecture decision**
   1. Are you intentionally supporting both `src/app` (App Router) and `src/pages`/`pages` (Pages Router), or should we consolidate to one?
   1. If consolidating: which is the intended standard in this repo right now?

2. **Canonical components directory**
   1. Which is canonical: `components/` or `src/components/`?
   1. Same question for `lib/` vs `src/lib` (if both exist or will).

3. **Data source contract for flights**
   1. Is `src/data/flights.ts` the current truth for flights, or a seed/mock?
   1. Do slugs come from that dataset, or are they generated at runtime?

4. **Checkout scope**
   1. Is checkout meant to be:
      1. A form-only capture (traveler info) for now, or
      1. Full payment integration in this milestone?
   1. What is the minimal acceptable “checkout done” for the next ship?

5. **Docs/log files**
   1. Should `SYNC_LOG.md`/`sync_log.md` be committed, or is it local-only?
   1. Do you want `WIKI.md` to replace `PLAN.md`, or keep both?\n
\n## 2026-05-11 07:45 UTC

### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

### Plan report (opencode plan agent)
**Prioritized TODO Plan (From Current Repo State)**

1. **Stabilize repo hygiene for a shippable branch**
   1. Decide what is intended to ship vs. experimental: you have a large surface area of new, untracked folders (`components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, multiple `src/components/*`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, plus multiple wiki/changelog/log files).
   1. Align naming/ownership for duplicate-looking artifacts: both `SYNC_LOG.md` and `sync_log.md` exist, plus `WIKI.md` and `WIKI_SYNC.md`. This is a future merge/conflict risk on case-insensitive filesystems and tends to cause CI noise.
   1. Define a “ship set” list of paths that belong in the next release and explicitly exclude the rest (either via `.gitignore` or moving them to a sandbox area). Right now, the worktree implies a lot more than “flights page update”.

2. **Make the Flights listing page production-ready**
   1. Confirm `src/app/[locale]/flights/page.tsx` changes are coherent with the app-router and locale routing conventions you’re using. 290 lines added suggests major UI composition; validate it is not accidentally embedding demo components or placeholder data flows.
   1. Confirm data dependencies: you added `src/data/flights.ts` (untracked). Decide if this is temporary fixture data or the intended data layer for MVP. If fixture, gate it behind a clear “mock mode” so it doesn’t become accidental production behavior.
   1. Validate performance & UX constraints for listing pages:
      1. Filtering/sorting should be deterministic and not re-sort on every render unexpectedly.
      1. Ensure mobile layout and scroll performance with potentially large result sets.
      1. Ensure empty states, loading states, and “no results” behavior exist.

3. **Scope and integrate “ready components” without exploding the milestone**
   1. You’ve introduced many new UI modules (AI planner, compare panel, dynamic price chart, badges, loyalty tiers, AR sizer, etc.). Treat these as a backlog unless they are already wired into one cohesive user flow.
   1. Pick at most 1-2 “differentiator” widgets for the next ship milestone on Flights:
      1. Candidate: `DynamicPriceChart` (fits Flights naturally).
      1. Candidate: `ComparePanel` (also fits listings).
      1. Defer others unless they are already required by the route.

4. **Checkout route readiness**
   1. `src/app/[locale]/checkout/` is untracked: confirm whether checkout is already “✅ completed” as per PLAN, or whether this is a new rework.
   1. Ensure checkout entry points exist from Flights detail/listing, and the basket/summary logic is consistent.

5. **Documentation synchronization**
   1. `PLAN.md` was edited and seems to contain claims like “cron checked every 10 min”. Decide whether that’s real or aspirational.
   1. Decide whether `CHANGELOG.md` is meant to track real releases. If yes: define format and start with the upcoming milestone only (avoid dumping a full feature catalog).

6. **Pre-ship verification checklist (define now, execute after scoping)**
   1. Lint/typecheck/build passes.
   1. Manual smoke test paths:
      1. `/[locale]/flights` listing
      1. `/[locale]/flights/[slug]` detail (since folder exists untracked)
      1. `/[locale]/checkout` end-to-end navigation
   1. Basic i18n sanity: at least 2 locales render without hardcoded strings breaking layout.

---

**Next Ship Milestone (Recommended)**  
**Milestone: “Flights MVP v1: Browse → Filter/Sort → Detail → Checkout entry”**

Definition of done (tight, shippable):
1. Flights listing route is stable and responsive: filter + sort + flight cards.
2. Flight detail route works for at least one flight and exposes key info (baggage, cancellation policy, aircraft type, etc. per your plan).
3. A single clear CTA from detail to checkout (even if payment is stubbed, the checkout page must load and summarize selection).
4. Optional (pick one): include either `DynamicPriceChart` on detail/listing or `ComparePanel` on listing.

Non-goals for this milestone:
- AI concierge, trip boards, voice map, AR sizing, loyalty tiers, gamification system-wide. These look “component-ready” but are not required to ship a coherent Flights funnel.

---

**Blockers / Questions (Need Your Answers Before Implementation/Shipping Decisions)**

1. **What is the intended ship scope for the untracked flood of files?**  
   Do you want the next release to include all these new modules, or should we constrain the milestone to the Flights funnel only and park the rest?

2. **Fixture data vs real integration:**  
   Is `src/data/flights.ts` meant to be permanent (static catalog) or temporary mock data pending an API/Supabase integration?

3. **App router vs pages router policy:**  
   You have untracked `pages/` and `src/pages/` alongside `src/app/…`. Is that intentional (hybrid) or accidental? Next.js projects can support both in limited ways, but it increases routing ambiguity and maintenance cost.

4. **File duplication/casing:**  
   Why both `SYNC_LOG.md` and `sync_log.md`? Which one is canonical? Same question for wiki artifacts.

5. **Release discipline:**  
   You’re ahead of `origin/main` by 1 commit already, but with many untracked changes. Do you want:
   1. One PR/commit for “Flights MVP”, and keep the experimental components out, or
   2. A big-bang commit that adds everything at once?
\n## 2026-05-11 07:54:42 UTC
\n### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### plan report
**Prioritized TODO Plan (Ship-Oriented)**

1. **Stabilize the flights listing page change (src/app/[locale]/flights/page.tsx)**
1. Define “done” for the page: expected query params, filter/sort behavior, empty-state, loading-state, error-state.
1. Verify it still matches the Phase 3 checklist in `PLAN.md` (Filters, SortSelect, FlightCard) and didn’t regress routing/i18n expectations for `[locale]`.
1. Confirm data source boundaries: is it still using mock `src/data/flights.ts`, or did it introduce new server/client behavior that needs hardening.

2. **Triage and classify the large set of untracked additions**
1. Decide what is product code vs. experiments/scaffolding vs. docs generated by cron/sync:
- `src/components/*` (many new UI modules)
- `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`
- `components/`, `pages/`, `src/pages/`, `lib/`, `scripts/` (potential duplication or legacy Next.js structures)
- `CHANGELOG.md`, `SYNC_LOG.md`, `sync_log.md`, `WIKI*.md`
1. Identify the minimum subset required for the next milestone (below) and explicitly defer the rest.

3. **Resolve architecture consistency (Next.js app router vs pages router)**
1. Make a call: stick to `src/app/...` as primary, and treat `pages/` / `src/pages/` / top-level `components/` as legacy or remove/migrate later.
1. If both routers are being used intentionally, document the rule of engagement (what lives where, routing precedence, i18n behavior).

4. **Reduce risk before shipping**
1. Ensure any “AI/interactive” components are not blocking core flows (flights search → detail → checkout). Gate them behind feature flags or keep them unused until validated.
1. Confirm localStorage usage (price tracking, saved searches) won’t break SSR or server components assumptions. Ensure client-only boundaries are clear.

5. **Documentation hygiene for the repo**
1. Decide canonical filenames and purpose:
- `SYNC_LOG.md` vs `sync_log.md` (case/duplication risk on different OSes)
- `WIKI.md`, `WIKI_SYNC.md` and how they’re updated (cron mention in plan)
1. Ensure `PLAN.md` reflects reality: many items marked ✅; validate they exist, are wired, and not just “component created”.

6. **Release packaging**
1. Decide what goes into the next commit(s): one cohesive milestone commit vs. split into (a) flights page change (b) new components (c) docs.
1. Add/confirm changelog strategy: whether `CHANGELOG.md` is manual, generated, or sync-produced.

---

**Next Ship Milestone (Recommended): “Flights Flow v1 End-to-End”**
Goal: a user can reliably go from flight search results to flight detail and into checkout, with i18n routing intact.

**Acceptance criteria**
1. `/[locale]/flights` renders results deterministically (even if from mock data) with filters + sorting working and no console/runtime errors.
1. `/[locale]/flights/[slug]` detail page exists and matches the “Fiyat Takibi + Sidebar” expectation already marked ✅ in the plan.
1. Checkout route under `/[locale]/checkout` works from the flight detail CTA (guest checkout allowed as stated in plan).
1. Empty / no-match state is handled gracefully (not a broken UI).
1. No dependency on “extra modules” (AI planner, AR sizer, voice map, gamification) for the core flow to function.

---

**Blockers / Questions (Need Your Decision)**
1. **Router strategy:** Are `pages/` and/or `src/pages/` intentional, or accidental leftovers? Which router is authoritative for shipping: `src/app` only?
1. **Untracked bulk components:** Do you want to ship all the new “trend modules” now, or keep them staged but not shipped until wired into UX? (Shipping them unreferenced increases maintenance surface and review cost.)
1. **Sync/cron artifacts:** You mention “cron checks every 10 minutes.” Are `SYNC_LOG.md`, `WIKI_SYNC.md` generated files that should be gitignored, or are they meant to be versioned?
1. **Case-duplicate logs:** Why both `SYNC_LOG.md` and `sync_log.md`? Which one is canonical? (This will cause cross-platform pain.)
1. **Data source:** For flights, is the expectation still mock/static (`src/data/flights.ts`) until an API integration, or do we need to align to a real backend contract now?
1. **Scope control:** `PredictiveTripBundler` is marked “Devam Ediyor” but you said the component is ready. Is the remaining work integration logic, backend, or just UI wiring?
\n---\n# izgetour plan report - 2026-05-11 08:04 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## plan output
**Onceliklendirilmis TODO Plani (ship odakli)**

1. **Repo hijyeni ve commit kapsamini netlestir**
   - Amac: Tek bir ship milestone icin gereksiz dosyalari ayiklamak.
   - TODO:
     - `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI*.md`, `sync_log.md` gibi log/wiki/senkron dosyalarinin bu release icin gerekli olup olmadigini karara bagla.
     - `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/` gibi cok sayida yeni klasorun neden eklendigini (migrasyon mu, kopya mi) netlestir.
     - Git status: `main` origin/main ahead 1. Bu 1 commitin ne oldugunu ve PR/merge stratejisini belirle.

2. **Flights listing sayfasi risk analizi ve kalite kapilari**
   - Girdi: `src/app/[locale]/flights/page.tsx` 290+ satir degismis. Bu buyuk bir blast radius.
   - TODO:
     - Sayfanin sorumluluklarini listele: data kaynagi, filtreleme, siralama, kart render, localStorage price tracking, compare panel vb.
     - Client/Server boundary: Next App Router icinde bu sayfa server component mi, client mi? (Yanlis boundary performans ve hydration sorunlari dogurur.)
     - Performans: Buyuk liste renderi, filtre/sort state guncellemeleri, gereksiz re-render riskleri.
     - URL state: Filtrelerin query param ile mi tutuldugu, geri/ileri navigasyonda davranis.
     - Empty/loading/error state: bos sonuc, invalid param, data yok, exception.

3. **Yeni eklenen moduller: "var ama entegre mi" denetimi**
   - PLAN.md, bircok komponentin "hazirlandi" dedigini soyluyor; git status ise bunlarin bircogunun untracked oldugunu gosteriyor.
   - TODO:
     - "Ship edilecek minimum set" belirle: Flights core deneyimi icin gercekten gereken komponentler hangileri?
     - Geri kalanlarini feature flag / deneysel klasor / daha sonraki milestone icin ayir (aksi halde release karmasiklasir).

4. **Checkout ve flights detail (slug) ile entegrasyon tamamlama kontrolu**
   - Untracked: `src/app/[locale]/checkout/` ve `src/app/[locale]/flights/[slug]/`
   - TODO:
     - Flights listing -> detail -> checkout user journey uctan uca calisiyor mu?
     - Paylasilan data modeli: flight item id/slug tutarliligi, fiyat ve bagaj politikasi gibi alanlarin tipi.

5. **Docs/Plan guncelleme ve dogrulama**
   - PLAN.md degismis (15 satir). Bunun gercek durumla uyumlu kalmasi gerekiyor.
   - TODO:
     - PLAN.md "tamamlandi" dedigi seylerin repo icinde gercekten varligi ve kullanimi (dead code degil).
     - CHANGELOG (eger release notu tutulacaksa) ship milestone ile hizala.

6. **Test/QA kapisi (minimum)**
   - TODO:
     - Manual smoke test senaryolari: flights search/listing, filter/sort, detail sayfasi, price tracking, compare, checkout girisi.
     - Build ve lint ciktilari (ileride calistirilacak): TypeScript errors, Next build warnings, route conflicts (pages/ vs app/).

---

**Bir Sonraki Ship Milestone (onerim)**

**Milestone: "Flights MVP Release Candidate"**
- Kapsam:
  - `src/app/[locale]/flights/page.tsx` stabil, performansli, URL/state tutarli flights listing.
  - En az 1 detail route: `src/app/[locale]/flights/[slug]/` calisir durumda.
  - Checkout entry: secilen flight ile checkout akisi baslayabiliyor (`src/app/[locale]/checkout/`).
  - Minimum UI: FlightCard + FlightFilters + FlightSortSelect (ve gerekiyorsa data `src/data/flights.ts`).
- Kapsam disi (bu milestone icin):
  - AITravelPlanner, VoiceInteractiveMap, AR sizer, gamification gibi "wow" komponentler. Bunlar entegre edilmediyse shipi geciktirmesin.

Basari kriterleri:
- 1. Flights listingte filtre/sort tutarli, sayfa yenilemede bozulmuyor.
- 2. Listing -> detail -> checkout akisi kopmuyor.
- 3. Build/lint temiz (en azindan error yok).

---

**Blokajlar / Sorular (cevaplar ship scope u belirler)**

1. Bu releasein hedefi ne: sadece flights mi, yoksa "platform demo" mu?
2. `main...origin/main [ahead 1]`: Bu ahead commit nedir ve remote ile nasil paylasilacak (PR mi, direkt push mu)?
3. Untracked dosyalarin tamami gercekten ship edilecek mi?
   - Ozellikle `components/`, `pages/`, `src/pages/` ayni anda varsa: Bu bilincli bir migrasyon mu, yanlislikla kopya mi?
4. Next yapisi: App Router kullaniyorsunuz (src/app var), ama pages/ da eklenmis. Bu iki routerin birlikte yasamasini istiyor musunuz?
5. Flights datasi su an statik mi (`src/data/flights.ts`) yoksa API entegrasyonu bekleniyor mu? MVP icin hangisi hedef?
6. PRICE tracking (localStorage) ve compare panel gibi ozellikler MVP icinde "must" mi, yoksa nice-to-have mi?
7. Dokumanlar (WIKI*.md, SYNC_LOG.md) shipte repo icinde kalacak mi, yoksa internal gelistirme dosyalari mi?

Bu sorulari yanitlarsan, milestone kapsamindan tasan dosyalari net bir "include/exclude" listesine indirgerim ve bir sonraki adim olarak da uygulama/commit stratejisini (tek commit mi, feature branch + PR mi) onerebilirim.
\n---\n## 2026-05-11T08:13:00Z\n
### git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n### git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n### PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n### Plan raporu (opencode)
**Onceliklendirilmis TODO Plani (Ship odakli)**

1. Calisan minimum urun dilimini netlestir
   - Ucus listeleme sayfasi icin hedef: arama parametreleri, filtre, siralama, kart, temel navigasyon
   - Checkout icin hedef: secimden checkout a gecis, ozet, odeme baslatma (mock olsa bile)
   - Kabul kriterleri: hata vermeden acilsin, mobile ve desktop temel akis tamam olsun

2. Repo hijyen ve kapsam kontrolu yap
   - Su an cok sayida untracked (components, lib, pages, scripts, yeni app rotalari) var
   - Bunlarin hangisi gercekten bu milestone icin gerekli: ayir
   - Gerekli olmayanlari milestone disi bir dala veya ayri PR a bol (ileride)

3. Ucus listeleme sayfasi kalite ve performans
   - `src/app/[locale]/flights/page.tsx` icindeki buyuk degisiklikleri parcala: veri, UI, state yonetimi, filtre-siralama mantigi
   - Server vs client sinirini netlestir: arama parametreleri, URL state, hydration riskleri
   - Bos durumlar: sonuc yok, loading, hata, eksik parametre

4. UI tutarliligi ve tasarim sistemi
   - FlightCard, FlightFilters, FlightSortSelect gibi bilesenlerin prop ve veri modelini standartlastir
   - Aynı pattern: tours, hotels, flights listeleme sayfalari arasinda benzer grid, spacing, responsive davranis
   - Eriilebilirlik: klavye ile filtre, aria etiketleri, renk kontrasti

5. Veri modeli ve fake data siniri
   - `src/data/flights.ts` gibi kaynaklar icin: hangi alanlar zorunlu, hangileri opsiyonel
   - Fiyat, bagaj, iptal politikasi, durak sayisi, kalkis varis saatleri gibi alanlarin tipleri net olsun
   - Gercek API entegrasyonuna gecis icin adapter katmani planla

6. Checkout entegrasyon noktasi
   - Ucus secimi -> checkout route: parametre tasima (id, fare, baggage, passengers)
   - Checkout icinde state kaybi olmamasi: refresh durumunda davranis
   - Guven ve yasal ekranlar: kvkk, iptal kosullari, odeme bilgilendirme (placeholder yeter)

7. Test ve dogrulama
   - En azindan duman testi senaryolari:
     - flights acilir
     - filtre degisir, sonuc degisir
     - siralama degisir
     - karttan detay veya checkout a gidilir
   - Lint typecheck build calisir (milestone icin kirmizi olmamali)

8. Dokumantasyon ve changelog
   - PLAN.md guncellemeleri: ne gercekten tamam, ne demo
   - CHANGELOG ve SYNC loglari: bu milestone kapsaminda anlamli ve kisa tut

---

**Next Ship Milestone (onerilen)**

Milestone adi: **Flights Listing v1 + Secimden Checkout a Akis**

Teslim icerigi:
1. Flights listing sayfasi: filtre + siralama + kartlar stabil
2. En az 1 secim aksiyonu: ucusu sec ve checkout a gec
3. Checkout icinde ozet gorunur (mock data ile bile kabul)
4. Mobile responsive temel kalite (layout kirilmasin)
5. Build ve typecheck temiz

Milestone disi (simdilik):
- AI moduller (planner, concierge, bundler)
- AR luggage, voice map gibi ileri UX
- Gercek bildirim, supabase email, price alert backend

---

**Blockerlar ve Sorular (cevaplarin plana kilit etkisi var)**

1. Bu kadar untracked dosya: hepsi bilincli mi, yoksa generator veya sync sonucu mu
2. Milestone hedefi ne: demo mu yoksa uretime yakin release mi
3. Flights verisi su an tamamen mock mu, yoksa yakinda bir API baglanacak mi
4. Checkout odeme entegrasyonu: hangi saglayici (iyzico, stripe, paytr vb) ve hedef kapsam (sadece UI mi, sandbox mi)
5. Routing yapisi: `pages/` ve `src/pages/` ile `src/app/` ayni anda mi kullaniliyor, yoksa migrate surecinde mi
6. i18n locale yapisinda flights ve checkout icin URL kurali: query param mi path param mi tercih ediyorsun
7. Kabul kriteri: filtre ve siralama URL de kalici olsun mu (shareable link) yoksa sadece client state yeter mi

Bu sorulara yanit verince milestone planini daha keskinlestirip, scope u daraltarak 1-2 gunluk net bir ship listesine indirebilirim.

---
## 2026-05-11 08:23 UTC

Repo: /home/turk/projects/izgetour

Git status -sb

## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

Git diff --stat

 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

PLAN.md excerpt (1-120)

# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

Opencode plan output



**Prioritized TODO Plan (Ship-Focused, No-Code)**

1. **Stabilize repo state for review/merge**
1. Decide what the “ahead 1” commit contains and whether it belongs with this batch.
1. Confirm which of the many untracked files are intentional deliverables vs experiments (right now it reads like a large feature drop plus scaffolding).
1. Decide naming/duplication cleanup policy before shipping:
   - `SYNC_LOG.md` vs `sync_log.md` (case-sensitive duplication risk on Linux vs macOS/Windows).
   - `pages/` at repo root vs `src/pages/` vs `src/app/` (Next routing split risk).
   - Untracked top-level `components/` and `lib/` vs `src/components/…` (import/path confusion).

2. **Define the actual “release surface area”**
1. Pick the single user-visible milestone to ship next (suggested below).
1. For that milestone, explicitly include/exclude:
   - Flights listing page changes in `src/app/[locale]/flights/page.tsx` (big diff: +290 lines).
   - Newly added UI components (many untracked `src/components/*.tsx`).
   - New routes under `src/app/[locale]/checkout/` and `src/app/[locale]/flights/[slug]/` (untracked).
1. Freeze scope: anything not in that milestone gets parked behind a flag or deferred (even if “component hazırlandı”).

3. **Routing and architecture sanity check (highest risk)**
1. Verify the app uses **one** routing paradigm for shipped paths:
   - If App Router (`src/app/...`) is primary, confirm `pages/` and `src/pages/` are either unused or intentionally legacy.
1. Identify any conflicting routes (example: `/flights` defined in both routers would produce surprising behavior).
1. Ensure locale routing (`[locale]`) is consistent across listing, detail, checkout.

4. **Quality gates for flights module (minimum shippable)**
1. Flights listing page:
   - Confirm data source behavior (`src/data/flights.ts` is untracked) and whether it’s mock-only.
   - Ensure filters/sorts are deterministic and don’t break on empty results.
1. Flights detail page (`src/app/[locale]/flights/[slug]/` untracked):
   - Define required fields (baggage, cancellation, times, airline) and fallback UX when missing.
1. Price tracking:
   - Confirm localStorage keys/versioning and behavior across locales.
   - Define what “tracking” means without backend (purely local) vs with Supabase notifications.

5. **Checkout integrity (even if already “✅”)**
1. Confirm checkout route exists only once and is reachable from flights/tours.
1. Define payment status handling and success page routing.
1. Ensure guest checkout vs auth is coherent (no dead ends).

6. **Documentation + changelog hygiene**
1. Decide if `CHANGELOG.md`, `WIKI.md`, `WIKI_SYNC.md`, and sync logs are part of the product repo or internal tooling.
1. Standardize on one sync log file name and location.
1. Update `PLAN.md` statuses so “✅” reflects shipped, not merely “component exists”.

7. **Release packaging**
1. Create a release checklist:
   - build passes
   - lint/typecheck passes
   - basic navigation smoke test: home → flights listing → flight detail → checkout → success
   - i18n smoke test for 2 locales
1. Prepare a “what changed” summary aligned to the chosen milestone.

---

**Next Ship Milestone (Recommended)**  
**Milestone: “Flights v1: Search/Listing + Detail + Local Price Watch + Checkout entry”**

Deliverables:
- A working `/[locale]/flights` listing experience with filters + sorting.
- A working `/[locale]/flights/[slug]` detail page that matches the PLAN promise (baggage, plane type, refund rules).
- Local-only price watch (localStorage) with clear UX (tracked/untracked).
- A single, reliable CTA path into checkout (even if payment is stubbed).

Non-goals for this milestone:
- Predictive bundling, AI concierge, collaborative boards, AR sizer, voice map, sustainability scoring (these are big-scope multipliers; ship later behind flags).

---

**Top Blockers / Risks**

1. **Routing split-brain risk**
- Presence of `pages/`, `src/pages/`, and `src/app/` suggests mixed Next routing.

2. **Untracked file explosion**
- Many untracked components and directories indicate the repo may not be in a curated “ship-ready” shape.

3. **Case-sensitive duplicate logs**
- `SYNC_LOG.md` and `sync_log.md` is a real cross-platform footgun.

4. **Done vs shipped mismatch**
- Plan marks many modules as complete, but repo state suggests ongoing integration.

5. **Data realism**
- If flights rely on mock data, label it and add guardrails.

---

**Questions (scope lock)**
1. Which milestone to ship next: Flights v1 or other?
1. App Router only? If yes, what to do with pages/src/pages?
1. Should everything live under src (components/lib)?
1. Are CHANGELOG/WIKI/sync logs shipped artifacts or internal notes?
1. Price tracking: local-only ok, or include Supabase notifications?
\n---\nTIMESTAMP: 2026-05-11T08:33:00Z
\nGIT_STATUS
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\nGIT_DIFF_STAT
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\nPLAN_MD_EXCERPT_FIRST_120
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\nPLAN_REPORT
**Oncelikli TODO Plani (Prioritized)**

1. Calisan durumu stabilize et (ship edilebilir baseline)
1. `src/app/[locale]/flights/page.tsx` icin build/compile risklerini kontrol et: import yollar, client/server boundary, hook kullanimi, undefined degiskenler, tip hatalari.
1. Yeni eklenen `src/components/*` ve `src/data/flights.ts` ile `flights/page.tsx` entegrasyonunun "minimum calisir" seviyde oldugunu dogrula.
1. Routing butunlugu: `src/app/[locale]/flights/[slug]/` ve `src/app/[locale]/checkout/` akisi (liste -> detay -> checkout) basic navigasyonla tamamlanabiliyor mu.
1. i18n uyumu: `[locale]` altinda kullanilan metinler ve URL parametreleri (query/slug) locale degisince bozuluyor mu.

2. Flights listing MVP (kullanici degeri en yuksek parca)
1. Listing sayfasinda temel senaryo: arama kriterleri (nereden/nereye/tarih) + sonuc listesi render.
1. Filtreler: price range, stops, airline (en azindan 2-3 temel filtre) calisiyor mu.
1. Sort: en ucuz / en kisa / en iyi (varsa) calisiyor mu.
1. FlightCard: fiyat, saat, sure, aktarma, airline bilgileri tutarli ve bos veri durumunda graceful fallback.
1. Bos sonuc / hata / loading state: UI kilitlenmeden tutarli gorunuyor mu.

3. Detay sayfasi ve fiyat takibi (Phase 3 vaadiyle uyum)
1. `[slug]` detay sayfasinda secilen flight datasi dogru cekiliyor mu (slug->data map).
1. Price tracking: localStorage kayit/okuma, UI toggle (Bell/BellOff) ve SSR uyumlulugu (window erisimi sadece client).
1. Sidebar ve checkout CTA: secilen flight ile checkout’a gecis data tasimasi net mi (query param vs state vs storage).

4. Checkout akisi MVP
1. Checkout sayfasinda secilen flight/urun ozeti (fiyat, tarih, yolcu) gorunuyor mu.
1. Guest checkout senaryosu: login zorunlulugu olmadan ilerliyor mu.
1. Basarili odeme/confirmation ekrani: en azindan mock confirmation ve redirectler.

5. Dokumantasyon ve repo hijyeni (ship etmeyi kolaylastirir)
1. `CHANGELOG.md` ilk entry: bu buyuk feature drop’un kapsamini yaz.
1. `SYNC_LOG.md`, `WIKI*.md` ve `sync_log.md` cakisik/tekrarlayan dosya isimleri var gibi: tek standard belirle (ornegin sadece `SYNC_LOG.md`) ve kalanlarini karara bagla.
1. Untracked top-level `components/`, `lib/`, `pages/` ile `src/components`, `src/pages` birlikteligi: hangi kok kullaniliyor netlestir. Next app router kullaniyorsan `src/app` + `src/components` tercih edilir; duplicate yapilar teknik borc yaratir.

---

**Sonraki Ship Milestone (Next Ship Milestone)**

Milestone: Flights Search MVP - Listing + Detay + Checkout Basic Flow

Kapsam:
1. /[locale]/flights listing sayfasi: filtre + sort + kartlar calisir
1. /[locale]/flights/[slug] detay sayfasi: secilen flight detaylari ve fiyat takibi (localStorage) calisir
1. /[locale]/checkout basic checkout: secilen flight ozeti + guest checkout ile tamamlanabilir
1. Minimum kalite bariyeri: bos state/hata state, mobil gorunum bozulmuyor, build aliyor

Cikis kriterleri (DoD):
1. Prod build alinir (TypeScript/ESLint kritik hata yok)
1. Core navigation: listing -> detay -> checkout -> success tamam
1. En az 1-2 kritik e2e senaryo manuel smoke testten gecmis

---

**Blockerlar / Sorular**

1. Next.js yapi karari: hem root pages hem src/pages hem src/app gorunuyor. Hedef sadece App Router mi?
1. Untracked root components/lib ile src/components duplication var mi? Hangisi canonical?
1. Data kaynagi: src/data/flights.ts mock mu, yakinda API mi?
1. i18n: translation layer var mi, yoksa hardcoded mi?
1. Checkout state tasima: URL query vs storage vs store standardi ne olacak?
1. Auth: guest checkout var; login opsiyonel mi?
1. Dosya isim standardi: SYNC_LOG.md ve sync_log.md bir arada. Hangisi kalacak?
\n---\n# Izgetour Plan Report - 2026-05-11 08:43 UTC\n
## Git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## Git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## Opencode plan output
**Prioritized TODO Plan (Ship-first, risk-reducing)**

1. **Stabilize repo shape and routing (highest priority)**
1. Decide on routing model: `src/app` (App Router) vs `pages/` (Pages Router). Right now you have both `src/app/...` and untracked `pages/` plus `src/pages/`, which is a classic source of route conflicts, double bundles, and “why is this page rendering instead of that one?” bugs.
1. Choose a single canonical location for new work (strong default: stay in `src/app` since you already have locale segment there) and explicitly mark the other as legacy or remove/relocate.
1. Confirm Next.js version constraints (you have a warning that this Next.js differs; breaking conventions are possible). This impacts file placement, routing, and i18n handling.

2. **Make the flights listing page shippable (scope cut + correctness)**
1. `src/app/[locale]/flights/page.tsx` has a large delta (+290/-). Do a pass to ensure:
1. Data source is deterministic (mock vs real) and doesn’t ship with broken/placeholder calls.
1. Filters/sort have a single source of truth and don’t fight each other (URL params vs local state vs derived state).
1. Rendering is robust on empty states: no-results, loading, error, and “invalid param” cases.
1. Avoid unbounded client-side work (large arrays + expensive filtering) without virtualization or pagination.
1. Verify accessibility basics: keyboard focus order, filter controls labels, and mobile layout.

3. **Integrate only the minimum “wow” components for this milestone**
1. You have many untracked components (AI planner, compare panel, dynamic charts, gamification, etc.). For a ship milestone, pick **1-2** that directly increase flights conversion:
1. Recommend: `FlightFilters`, `FlightSortSelect`, `FlightCard` (core), plus optionally `DynamicPriceChart` (secondary).
1. Defer “platform-wide” modules (loyalty tiers, badges, party planning, voice map) unless they’re already wired and proven not to destabilize.

4. **Triage untracked directory explosion (prevent shipping a junk drawer)**
1. The git status shows many untracked top-level directories: `components/`, `lib/`, `pages/`, `scripts/`, plus `src/components/*` and `src/pages/`.
1. Decide which of these are real, needed artifacts vs accidental copies/mirrors.
1. Establish a clear convention:
1. Either everything lives under `src/` (`src/components`, `src/lib`, `src/scripts`), or you intentionally use root-level folders. Mixing both will hurt maintainability and imports.

5. **Documentation + release hygiene (fast wins)**
1. `CHANGELOG.md`, `SYNC_LOG.md`, `WIKI.md`, `WIKI_SYNC.md`, `sync_log.md` exist untracked; likely duplicates/automation artifacts.
1. Define what’s actually shipped:
1. Keep `CHANGELOG.md` if you want release notes.
1. Keep one sync log format (and one filename casing) or ignore via `.gitignore`.
1. Update `PLAN.md` to reflect what’s truly implemented vs “component exists”. Your plan currently marks a lot as “✅” but git shows many are just untracked files, not necessarily integrated.

6. **Test pass + build pass criteria (gate before ship)**
1. Define “ship gate” explicitly:
1. `next build` passes.
1. Core routes load: homepage, flights listing, flight detail, checkout.
1. No console errors, no hydration warnings, no broken locale routing.
1. Minimal smoke tests: filter/sort works, selecting flight leads to detail/checkout (even if mock).

---

**Next Ship Milestone (recommendation)**  
**Milestone: “Flights v1 MVP: Search/List/Detail/Checkout happy path”**

Scope (tight):
1. Flights listing page is stable and fast.
1. Filters + sort work and persist (either URL-driven or local, but consistent).
1. Flight detail page exists and is reachable from listing (your status shows `src/app/[locale]/flights/[slug]/` untracked; likely intended).
1. Checkout flow reachable from selected flight (you have `src/app/[locale]/checkout/` untracked).
1. i18n locale segment doesn’t break navigation between these pages.

Explicitly out-of-scope for this milestone:
1. AI bundler, loyalty tiers, party plan, voice map, social proof toasts, AR luggage sizer, etc. Keep them behind flags or as follow-on milestones.

Success criteria:
1. A user can go from flights page → pick a flight → see details → proceed to checkout without dead ends.
1. Build passes and routes are deterministic (no Pages/App router ambiguity).

---

**Blockers / Questions (need answers to avoid wrong direction)**

1. **Routing decision:** Are you committing to App Router (`src/app/...`) only, or do you intentionally want to support `pages/` / `src/pages/` too?
1. **Next.js version & constraints:** What Next.js version is installed, and do you have any repo-specific routing/i18n rules beyond `[locale]`?
1. **Data source for flights:** Are flights currently mocked (`src/data/flights.ts` exists untracked) or do you plan an API integration now? If mocked, should we treat it as stable fixture data for MVP?
1. **Locale strategy:** Should filters/sort be reflected in URL query params (shareable) or kept purely client-side for MVP?
1. **Untracked modules intent:** The many untracked components: are these meant to be committed now, or are they generated/experimental and should stay out until integrated?
1. **Sync log files:** Are `SYNC_LOG.md` / `WIKI_SYNC.md` / `sync_log.md` produced by automation? If yes, should they be ignored or tracked?

If you answer just #1 (routing) and #3 (data source), the rest of the plan can be executed with minimal rework.
\n---\n# Izgetour plan report - 2026-05-11 08:54 UTC\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (1-120)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## opencode plan output
**Prioritized TODO Plan (from current worktree state)**

1. **Stabilize the flights listing page change (highest risk)**
1. Define “done” for `src/app/[locale]/flights/page.tsx` (it’s the only large diff: +290 LOC).
1. Confirm it still matches the intended Kayak-style UX you describe in `PLAN.md`: left filters, sort, card tags, compare panel, saved searches, price chart, etc.
1. Add acceptance checks (manual QA checklist, since you asked for no code/tools):
   1. Empty state (no results).
   1. Filter combinations (airline + stops + price + time).
   1. Sort interactions (best/cheapest/fastest, etc.).
   1. Locale routing and URL params behavior (shareable links).
   1. Mobile layout (filters as drawer, cards readable, no overflow).

2. **Triage the massive untracked surface area (ship blocker if not curated)**
1. Decide what is intentionally new vs accidental/temporary:
1. Big buckets present: `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/`, and many new `src/components/*.tsx`.
1. Decide ownership/placement:
   1. Next.js App Router code should generally live under `src/app` + `src/components` (having both `pages/` and `src/pages/` suggests potential routing conflicts or legacy leftovers).
1. Identify “should never ship” files:
   1. `SYNC_LOG.md`, `sync_log.md`, `WIKI_SYNC.md` look like generated sync artifacts.
   1. Duplicate-case logs (`SYNC_LOG.md` vs `sync_log.md`) can cause cross-OS pain (Linux vs macOS case sensitivity).

3. **Rationalize documentation and release notes**
1. `PLAN.md` changed: confirm the roadmap statuses reflect reality (it currently marks a lot as ✅, but the repo state suggests many components are newly added/unintegrated).
1. `CHANGELOG.md` is untracked: decide if it’s part of release discipline or a local scratchpad. If it’s real, add a first entry describing what the ahead commit contains and what remains experimental.

4. **Define integration status for all “component hazırlandı ✅” items**
1. For each newly added component under `src/components/…`, mark it as one of:
   1. Integrated and reachable in UI
   1. Wired but hidden behind feature flag
   1. Not used yet (prototype)
1. Anything “not used yet” should not be treated as “done” in the plan, and should not block the next ship milestone.

5. **Checkout and flight detail verification**
1. There are untracked directories: `src/app/[locale]/checkout/` and `src/app/[locale]/flights/[slug]/`.
1. Confirm they’re consistent with the PLAN’s flow:
   1. Guest checkout supported
   1. Order summary correctness
   1. Navigation between listing → detail → checkout doesn’t break locale.

6. **Repository hygiene before shipping**
1. Decide final folder structure (avoid `pages/` + `src/pages/` duplication unless you truly run both routers).
1. Add/confirm `.gitignore` entries for sync logs/wiki sync outputs if they’re generated.
1. Normalize naming (only one of `SYNC_LOG.md`/`sync_log.md`).

---

**Next Ship Milestone (recommendation)**  
**Milestone: “Flights MVP usable end-to-end (Listing → Detail → Checkout) + repo hygiene”**

**Scope (ship-worthy, minimal, user-visible)**
1. Flights listing page is stable and responsive, with filters + sorting working and no obvious broken states.
1. Flight detail route (`/flights/[slug]`) renders reliably and supports the “price tracking” localStorage behavior you claim is ✅.
1. Checkout route works for guest checkout and shows a correct, consistent summary for a selected flight.
1. Repo does not include accidental/generated sync artifacts; documentation reflects what’s actually integrated.

**Explicitly out of scope for this milestone**
1. Predictive Trip Bundler and other “trend modules” unless they are already integrated and proven non-breaking.
1. AI concierge / collaborative boards unless already shipped behind a controlled entry point.

---

**Blockers / Questions (need your decisions before a clean ship)**

1. **Routing architecture decision**
1. Are you intentionally using both App Router (`src/app/...`) and Pages Router (`pages/` or `src/pages/`)?  
If not, which one is authoritative so we can avoid conflicts and dead code?

2. **What is the “ahead 1” commit supposed to represent?**
1. Is that commit meant to be a small doc update, or does it already include functional flights changes?  
This affects whether we batch these untracked additions into the same release or stage them.

3. **Are the sync/wiki/log files meant to be versioned?**
1. Should `SYNC_LOG.md`, `sync_log.md`, `WIKI.md`, `WIKI_SYNC.md` be committed, or should they be ignored/generated?  
If they’re generated, committing them will create constant churn.

4. **Component integration reality check**
1. The plan marks many components as ✅ “completed”. Are they actually wired into user flows, or just present in `src/components/`?  
If they’re just present, I’d reclassify them as “built, not integrated” to avoid overstating progress.

5. **Target release behavior**
1. What is the immediate user-facing target: flights-first (Kayak-like) or tours-first with flights as secondary?  
This determines what we consider “must pass” in manual QA.

If you answer the 5 questions above, I can tighten this into a concrete “cut list” (exactly what to include/exclude from the next ship) and a short, testable acceptance checklist per route.
\n## 2026-05-11 09:04:49 UTC
Branch: main (ahead 1)

GIT_STATUS
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

GIT_DIFF_STAT
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)

PLAN_MD_EXCERPT_FIRST_120
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)

OPENCODE_PLAN_REPORT
**Onceliklendirilmis TODO Plani (Ship odakli)**

1. **Repo hijyeni ve kapsam sabitleme**
1. Calismayi iki parcaya ayir: (A) flights listing sayfasi degisiklikleri, (B) yeni eklenen component/lib/pages klasorleri.
1. Untracked dosyalar icin karar ver: bu PR/ship icinde mi, yoksa ayri bir “feature drop” mi.
1. Duplicate/karisik dosya adlarini netlestir: `SYNC_LOG.md` ve `sync_log.md` ayni amaca mi hizmet ediyor? Case-sensitive ortamlarda sorun cikartir.

2. **Flights listing sayfasi (src/app/[locale]/flights/page.tsx) stabilizasyonu**
1. Sayfanin tek sorumlulugu: arama parametrelerini al, filtrele/sirala, listele.
1. Yeni eklenen UI modullerinin (ComparePanel, filters, sort, price chart vb) render sirasi ve responsive davranisi: mobilde “soldaki filtre” yerine drawer/panel davranisi var mi.
1. State yonetimi: filtre/sort/compare secimleri URL query ile mi, local state ile mi? Tutarlilik sagla (yenilemede kaybolmasin isteniyorsa URL).
1. Performans: liste buyukse render costu (virtualization yoksa en azindan pagination ya da “load more”).
1. Erişilebilirlik: filtre kontrolleri label/aria, keyboard navigation, focus trap (drawer varsa).

3. **Bilesenlerin entegrasyon siniri**
1. “Yeni componentler hazirlandi” gorunuyor ama hepsi flights page icine gomulu ise risk buyur.
1. MVP icin sec: sadece en cok deger veren 2-3 modulu ac (or: FlightFilters, FlightSortSelect, FlightCard + PriceChart).
1. Digerlerini feature-flag ya da kapali placeholder mantigina al (ship sonrasina).

4. **Checkout akisi ve routing dogrulamasi**
1. `src/app/[locale]/checkout/` yeni route var: locale routing ile uyumlu mu, navigation linkleri dogru mu.
1. Flights detail route: `src/app/[locale]/flights/[slug]/` ile listing’den linkleme dogru mu.
1. Eski `pages/` klasoru da var gorunuyor: App Router ile Pages Router ayni projede ise cakisma riskini kontrol et (hangi kisimlar gercekten kullaniliyor).

5. **Data ve tipler**
1. `src/data/flights.ts` kaynagi: mock mu, production API placeholder mi.
1. Flight modeli: stops, airline, time windows, cancellation policy gibi filtre alanlari gercekten datada var mi. Yoksa filtreler “UI only” kalir.
1. Para birimi/i18n: locale bazli formatlama, TL/EUR vs.

6. **Test ve smoke senaryolari (min set)**
1. `/[locale]/flights` aciliyor mu.
1. Filtre degisince liste degisiyor mu.
1. Sort degisince sira degisiyor mu.
1. Flight card’dan detail’e gidis calisiyor mu.
1. Checkout’a giden happy path var mi (en azindan UI seviyesinde).

---

**Next Ship Milestone (onerilen)**  
**Milestone: Flights Listing v1 (stabil + kullanilabilir)**
- Kapsam: `FlightCard` + `FlightFilters` + `FlightSortSelect` + temel mock data ile calisan listing.
- Opsiyonel (eger problemsizse): `DynamicPriceChart` (liste ustunde, tek modul).
- Kapsam disi (sonraya): AITravelPlanner, VoiceInteractiveMap, PartyPlan, GamificationBadges, SustainabilityScore gibi “nice-to-have” moduller.

Basari kriterleri:
- Mobil/desktop layout bozulmuyor.
- URL ile temel arama parametreleri tasinabiliyor (en azindan origin, destination, date).
- Filtre/sort dogru calisiyor, hata vermiyor.

---

**Blockerlar / Sorular (cevap verirsen plan netlesir)**

1. Bu ship icin hedefin ne: demo mu (mock data ok) yoksa production’a yakin mi (API entegrasyonu sart)?
1. Untracked cok sayida dosya var. Hepsini tek commit/PR’da mi toplamak istiyorsun, yoksa “flights listing” ile sinirlayip kalanini ayri drop mu yapalim?
1. `pages/` ve `src/pages/` klasorleri bilerek mi var. Hala Pages Router kullanan route var mi, yoksa artifakt mi?
1. `SYNC_LOG.md` ve `sync_log.md` ikisinden hangisi canonical? Biri silinecek mi yoksa ikisi farkli mi?
1. Flights sayfasinda filtre/sort secimlerinin URL’de kalmasini istiyor musun (shareable link), yoksa sadece session icinde yeterli mi?
\n---\n# izgetour plan report\nTimestamp: 2026-05-11T09:13:00Z\n
## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md
\n## git diff --stat
 PLAN.md                           |  15 +-
 src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
 2 files changed, 293 insertions(+), 12 deletions(-)
\n## PLAN.md (first 120 lines)
# İzgetour Proje ve Geliştirme Planı (Kayak.com Referanslı)

## 🎯 Vizyon
İzgetour platformu, Kayak.com gibi global, uçtan uca modern bir "Seyahat Arama ve Karşılaştırma" deneyimi sunarken, aynı zamanda İzge Tour'un özel turlarını ve butik deneyimlerini öne çıkaran bir mimari üzerine inşa edilmiştir.

## 🧭 User Flow (Kullanıcı Akışı)
1. **Ana Sayfa (Landing)**
   - Devasa, ilham verici Hero Banner (Türkiye odaklı)
   - *Kayak-style Smart Search:* Tur, Uçak, Otel (yakında Araç) sekmeleri arası pürüzsüz geçiş.
   - Öne Çıkanlar ve "Neden İzgetour" özellikleri.
2. **Arama ve İndeksleme Sonuçları (Listing Platform)**
   - Smart Search'ten gelen parametrelere (Tarih, Kişi, Lokasyon) göre anlık (Server-Side) render edilmiş sonuçlar.
   - Sol menü: Detaylı filtreleme (fiyat, süre, puan, iptal politikası).
   - Card tasarımı: "En İyi Eşleşme", "Fiyat Performans" gibi tag'ler.
3. **Detay Sayfası (Detail & Itinerary)**
   - Görsel ağırlıklı (gallery) sunum.
   - **Uçak:** Sefer detayları, bagaj hakları, uçak tipi, iade koşulları ✅
   - Tur: Gün gün güzergah (Itinerary) haritalı, dahil/hariç hizmetler, rehber bilgisi.
   - Otel: Oda tipleri, olanaklar.
   - **Fiyat Takibi:** Takip edilen uçuşları localStorage'da saklama + Bell/BellOff UI ✅
4. **Checkout & Rezervasyon**
   - Kayıt olmadan devam edebilme (Guest Checkout).
   - %100 güvenli (Shield) ödeme onaylama ekranı.
   - Dinamik özet alanı.
5. **Kullanıcı Paneli (Dashboard)**
   - Geçmiş ve gelecek seyahatler.
   - Fatura yönetimi, bilet indirme.
   - Favoriler.

## 📦 Modül Geliştirme Sırası & Roadmap

| Aşama | Modül | Durum |
| :--- | :--- | :--- |
| **Faz 1** | Homepage (Hero, SmartSearch, Features, Popular Tour Cards) | ✅ Tamamlandı |
| **Faz 1** | i18n & Navigation Routing Sistemi | ✅ Tamamlandı |
| **Faz 2** | Tours - Listeleme Sayfası & Filtreler | ✅ Tamamlandı |
| **Faz 2** | Tours - Detay Sayfası (slug) & Harita UI | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Modülü (Uçuş Arama & Listeleme UI) | ✅ Tamamlandı |
| **Faz 3** | Uçak Bileti Detay Sayfası (Fiyat Takibi + Sidebar) | ✅ Tamamlandı |
| **Faz 3** | FlightFilters (Airline/Stops/Price/Time/Cancellation) | ✅ Tamamlandı |
| **Faz 3** | FlightSortSelect + FlightCard Component'leri | ✅ Tamamlandı |
| **Faz 4** | Otel Modülü (Entegrasyona Hazır Tasarım) | ✅ Tamamlandı |
| **Faz 5** | Auth (Login/Signup - Supabase via İzgetour ID) | ✅ Tamamlandı |
| **Faz 6** | Sepet, Checkout ve Başarılı Ödeme Ekranları | ✅ Tamamlandı |
| **Faz 7** | Checkout UX Geliştirmeleri (Apple/Google Pay, Kupon, Order Summary componentleri) | ✅ Tamamlandı |
| **Faz 8** | Gamification/Badge Sistemi (GamificationBadges.tsx) | ✅ Tamamlandı |
| **Faz 8** | Smart Itinerary - Hava Durumu + Etkinlik Entegrasyonlu Seyahat Planı (SmartItinerary.tsx) | ✅ Tamamlandı |
| **Faz 8** | Görsel Karşılaştırma Paneli - Kayak-style Split View (ComparePanel.tsx) | ✅ Tamamlandı |
| **Faz 9** | Saved Searches & Notification Hub (SavedSearches.tsx) | ✅ Tamamlandı |
| **Faz 9** | Mood-Based Destination Picker (MoodDestinationPicker.tsx) | ✅ Tamamlandı |
| **Faz 9** | Loyalty Tier System - Bronze/Silver/Gold/Platinum (LoyaltyTierSystem.tsx) | ✅ Tamamlandı |
| **Faz 10** | Collaborative Trip Board - Sürükle-bırak paylaşımlı planlama panosu (CollaborativeTripBoard.tsx) | ✅ Tamamlandı |
| **Faz 10** | AI Chatbot Concierge - LLM tabanlı seyahat asistanı (AIChatbotConcierge.tsx) | ✅ Tamamlandı |
| **Faz 10** | Flexible Date Calendar Heatmap - Kayak-style en ucuz gün takvimi (FlexibleDateCalendar.tsx) | ✅ Tamamlandı |
| **Faz 11** | Predictive Trip Bundler - AI tabanlı otomatik paketleme (PredictiveTripBundler.tsx) | 🔄 Devam Ediyor |

## 🚀 Yeni Bulunan Modüller (Devamlı Eklenecek)
- **Predictive Trip Bundler (2026 Trendi):** Kullanıcı bir uçuş seçtiğinde, AI otomatik olarak ilişkili otel+transfer+tur önerileri oluşturur ve "Paket İndirim" ile sunar. Google Trips benzeri ama auto-bundle mantığıyla. (Component hazırlandı ✅)
- **Micro-Adventure Generator (2026 Trendi):** 1-2 günlük, yakın mesafe, düşük bütçeli "kaçamak" önerileri. Gen-Z ve remote worker segmentine yönelik, lokasyon bazlı hızlı arama.
- **Accessibility Score & Filters (2026 Trendi):** Engelli-dostu otel/tur/uçuş filtresi. Tekerlekli sandalye uyumluluğu, duyusal hassasiyet derecesi, yardımcı hayvan politikası gibi detaylı erişilebilirlik skoru.
- **Luggage AR Sizer:** Telefon kamerasıyla valizin boyutunu ölçüp Uçak bagaj kurallarına (Cabin/Checked) uyup uymadığını anlık doğrulayan AR modülü. (Component hazırlandı ✅)
- **Dynamic Local Cuisine Recommender:** Seçilen uçuş/otel varış noktasına göre restoran ve lokal lezzet önerilerini Itinerary listesine serpiştiren akıllı öneri. (Component hazırlandı ✅)
- **Smart Itinerary (Akıllı Seyahat Planı):** Seçilen tatil tarihlerine hava durumu tahminleri (Weather API) ve yerel etkinlik/festival bildirimleri entegre ederek gösterim. (Component hazırlandı ✅)
- **Dinamik Fiyatlandırma Gösterimi:** Kullanıcılara belirli tarih aralıklarındaki fiyat dalgalanmalarını gösteren grafik (Kayak uçuş fiyat grafiği benzeri). (Component hazırlandı ✅)
- **Gamification/Badge Sistemi:** Kullanıcıların belirli turları (ör. İlk Asya Uçuşu, Tarih Meraklısı) tamamladıkça rozet kazandığı mini bir UX gamification özelliği. (Component hazırlandı ✅)
- **AI-powered Hotel Recommendation Engine:** Kişiye özel otel önerileri, kullanıcı tercihleri ve bütçeye göre dinamik öneri sistemi.
- **Vize Destek Modülü:** Check-list ekranı (Kayak modeline ek olarak)
- **Paket Seyahat Planlayıcı (AI Travel Planner):** Kullanıcı bütçe ve ilgi alanı girer, platform tüm uçak+otel+tur sepetini hazırlar. (Component hazırlandı ✅)
- **Görsel Karşılaştırma Paneli (Kayak-style Split View):** Listeleme sayfasında 2-3 turu yan yana karşılaştırmalı görüntüleme (fiyat/süre/içerik tablosu) (Component hazırlandı ✅)
- **Akıllı Filtre Önerileri:** Kullanıcı aramasına göre otomatik filtre önerme (örn: "denizvar" yazınca plaj turlarını otomatik seçme)
- **Harita Katmanı (Map View):** Tur listesinde harita üzerinde lokasyon bazlı görüntüleme (Kayak Otel haritası gibi)
- **Uçuş Fiyat Takibi (Price Alert):** Takip edilen uçuşlar localStorage'da saklanır. Gerçek bildirim için Supabase + e-posta entegrasyonu. (Component hazırlandı ✅)
- **Uçuş Karşılaştırma (Split View):** 2-3 uçuşu yan yana karşılaştırmalı görüntüleme
- **Hızlı Rota Seçimi:** Popüler rotalara tek tıkla arama, emoji ile görselleştirme
- **Kabin Sınıfı Filtresi:** Economy/Business/Premium seçimi
- **Passwordless Magic Link Auth:** Kullanıcı e-posta ile tek tıkta oturum açabilir, OTP yerine güvenli link gönderilir
- **Sosyal Seyahat Grupları (Yeni UX):** Kullanıcıların sepetini veya planladıkları seyahatleri ortak bir link üzerinden arkadaşlarıyla grupça oylayabileceği bir mini "Party Plan" modülü. (Component hazırlandı ✅)
- **Trip Countdown Widget:** Rezervasyon sonrası ana sayfada anlık olarak "Seyahate 14 Gün Kaldı" şeklinde gösteren kişisel animasyonlu sayaç. (Component hazırlandı ✅)
- **Social Proof Toasts:** "Şu an 5 kişi bu tura bakıyor", "Son 2 koltuk" gibi canlı motivasyon bildirimleri. (Component hazırlandı ✅)
- **Multi-City Complex Router:** A'dan B'ye uç, arayı trenle/turla geç, C'den dön mantığında gelişmiş Kayak tarzı çoklu rota oluşturucu. (Component hazırlandı ✅)
- **Sustainability Score:** Yeşil Seyahat Skoru ve karbon ayak izi hesaplama/dengeleme modülü. (Component hazırlandı ✅)
- **Voice Guided Interactive Map:** Haritada sesli rehber ile turları/lokasyonları interaktif gezme UX'i. (Component hazırlandı ✅)

*Not: Bu plan proje geliştikçe sürekli revize edilerek güncellenecektir (Her 10 dk'da cron tarafından denetlenir).*
- **Collaborative Trip Board (Yeni Trend — 2026):** Arkadaşlarla gerçek zamanlı paylaşımlı planlama panosu. Kayak, Wanderlog ve Notion benzeri sürükle-bırak itinerary özelliği. (Component hazırlandı ✅)
- **AI Chatbot Concierge (Yeni Trend):** LLM tabanlı doğal dil seyahat asistanı — "Ailemle hafta sonu Ege'de ne yapabiliriz?" tarzı sorulara cevap + otomatik arama. (Component hazırlandı ✅)
- **Flexible Date Calendar Heatmap:** Kayak'ın esnek tarih özelliği gibi, ay boyunca en ucuz günleri renk haritasıyla gösteren takvim view'i. (Component hazırlandı ✅)
- **Saved Searches & Notification Hub:** Kullanıcının son aramalarını kayıt altına alıp, fiyat düştüğünde Dashboard üzerinden bildirim gönderecek merkezi bildirim paneli. (Component hazırlandı ✅)
- **Mood-Based Destination Picker:** "Macera", "Romantik", "Huzur", "Kültür" gibi mod seçimi ile kullanıcıya özelleştirilmiş destinasyon önerisi sunan interaktif picker widget'i. (Component hazırlandı ✅)
- **Loyalty Tier System (Bronze/Silver/Gold/Platinum):** Gamification badge'leriyle entegre, toplam harcama ve seyahat sayısına göre özel ürgü tier sistemi. Üst tier'lerde öncelikli servis, indirim, lounge erişimi gibi avantajlar. (Component hazırlandı ✅)
\n## plan output
Onceliklendirilmis TODO Plani (Ship odakli)

1. Repo hijyeni ve kapsam kontrolu (hemen)
1. Hangi dosyalar bu degisiklik dalgasinin parcasi: `components/`, `lib/`, `pages/`, `scripts/`, `src/pages/`, `src/app/[locale]/checkout/`, `src/app/[locale]/flights/[slug]/` bir kerede buyuk bir scope. Bunlari ship hedeflerine gore parcalara ayir.
1. Duplicate / case farki riskleri: `SYNC_LOG.md` ve `sync_log.md` ikisi birden var; Linux'ta farkli dosya, diger ortamlarda karisiklik yaratabilir. Tek isme indirgeme karari alinmali.
1. `CHANGELOG.md`, `WIKI*.md` gibi dokumanlar: ship commitine girecek mi, yoksa ayri dokuman PR/commiti mi olacak netlestir.

2. Flights liste sayfasi (src/app/[locale]/flights/page.tsx) stabilizasyonu
1. 290 satirlik eklemeler var: buyuk olasilikla yeni UI/filtre/siralama/kart entegrasyonlari. Bu sayfanin "minimum calisir" kriterlerini netlestir:
1. Data kaynagi: mock (`src/data/flights.ts`) mi, API mi? (Simdilik mock ise fallback davranisi tanimla.)
1. Filtreler: fiyat, kalkis/varis saati, havayolu, aktarma, bagaj vb. hangileri MVP?
1. Siralama: fiyat, sure, kalkis saati MVP?
1. Pagination / infinite scroll var mi, yoksa liste tamamini mi basiyor?
1. Empty state / loading / error state kesin olmali.
1. Locale parametresi: `[locale]` route'u var; locale switch ve metinler i18n ile uyumlu mu kontrol listesi cikar.

3. Bilesen envanteri ve entegrasyon stratejisi (src/components + components/)
1. `src/components/*.tsx` altinda cok sayida yeni bilesen gorunuyor (FlightCard, FlightFilters, FlightSortSelect, ComparePanel, DynamicPriceChart vb).
1. MVP icin sadece flights akisini ship edeceksek: sadece flights ile direkt ilgili bilesenleri aktif et, digerlerini park et (flag, route baglantisi yoksa commite girmeyebilir).
1. UI tutarliligi: tasarim sistemi/tailwind/shadcn vb kullanim standardi var mi? (Varsa bilesenler ona gore hizalanmali.)

4. Flights detay sayfasi ve checkout yolu
1. `src/app/[locale]/flights/[slug]/` var: slug semasi nedir (id mi, SEO slug mi)?
1. Liste -> detay -> checkout akisi calisiyor mu? Minimum:
1. Liste kartindan detay sayfasina navigasyon
1. Detaydan "Rezervasyona devam" ile checkout
1. Checkout route'u: `src/app/[locale]/checkout/` var. Flights checkout mu, genel checkout mu? Data contract netlestir.

5. Test / kalite kapilari
1. Typecheck: TS hatalari yok.
1. Lint/format: repo standardina uyum.
1. Minimal e2e/route smoke: flights liste sayfasi render, filtre degisince crash yok, detay route 404 degil.
1. Build: Next build basarili.

6. Dokumantasyon ve roadmap guncellemesi (PLAN.md + CHANGELOG)
1. PLAN.md degisikligi: Faz 11 "Predictive Trip Bundler" devam ediyor denmis. Bu release icin hangi faz ship ediliyor net yaz.
1. CHANGELOG: "Flights search/list MVP" gibi tek bir milestone altinda ozet.

Sonraki Ship Milestone (onerilen)

Milestone: "Flights Browse MVP"
- `/[locale]/flights` sayfasi uzerinde:
- Mock data ile (veya mevcut data kaynagi ile) listeleme
- Temel filtreler (en az 2-3 kritik filtre)
- Temel siralama (fiyat + sure)
- FlightCard ile detay linki
- Empty/loading state
- Kirmayan locale davranisi

Opsiyonel (MVP+1, milestone disi):
- ComparePanel
- DynamicPriceChart
- SavedSearches
- Gamification / SocialProof / AITravelPlanner gibi growth bilesenleri

Blockerlar / Riskler (su an gorunenler)

1. Scope patlamasi riski: Bir committe/degisiklik setinde cok fazla yeni klasor ve bilesen var. Hangi subset ship edilecek belli degilse entegrasyon uzar.
1. Dosya isim cakismasi riski: `SYNC_LOG.md` vs `sync_log.md` (ayni isim farkli case). CI, zip, macOS checkout gibi ortamlarda problem cikarma riski var.
1. Iki farkli "pages" alani: `pages/` ve `src/pages/` ve ayrica `src/app/` var. Next.js app router vs pages router birlikteyse net kurallar lazim; yoksa route cakismalari ve build surprizleri olabilir.
1. Data contract belirsizligi: flights datasi `src/data/flights.ts` ile mi gelecek, yoksa API planlandi mi? UI bilesenleri API semasina bagimliysa sonradan refactor buyur.
1. Locale/i18n belirsizligi: `[locale]` var ama metinler/hardcode strings kontrol edilmezse TR/EN karisabilir.

Netlestirmem Gereken Sorular (kisa, karar odakli)

1. Bu release icin hedef: sadece flights liste + detay mi, yoksa checkout da calisir olacak mi?
1. Flights verisi su an mock mu kalsin (src/data/flights.ts), yoksa backend/API entegrasyonu bekleniyor mu?
1. `pages/` ve `src/pages/` klasorleri bilerek mi eklendi? Projede app router ile pages router birlikte kullanilacak mi, yoksa bunlar gecici mi?
1. `SYNC_LOG.md` ve `sync_log.md` ikisinden hangisi kanonik olacak (tek dosyaya dusurelim mi)?
1. Yeni eklenen `components/` ile `src/components/` ikisi birden kullanilacak mi? (Tek kok hedefi belirleyelim mi?)

---
# izgetour plan report @ 2026-05-11T09:23:00Z

## git status -sb
## main...origin/main [ahead 1]
 M PLAN.md
 M src/app/[locale]/flights/page.tsx
?? CHANGELOG.md
?? SYNC_LOG.md
?? WIKI.md
?? WIKI_SYNC.md
?? components/
?? lib/
?? pages/
?? scripts/
?? src/app/[locale]/checkout/
?? src/app/[locale]/flights/[slug]/
?? src/components/AITravelPlanner.tsx
?? src/components/ComparePanel.tsx
?? src/components/DynamicCuisineRecommender.tsx
?? src/components/DynamicPriceChart.tsx
?? src/components/FlightCard.tsx
?? src/components/FlightFilters.tsx
?? src/components/FlightSortSelect.tsx
?? src/components/GamificationBadges.tsx
?? src/components/HotelCard.tsx
?? src/components/HotelFilters.tsx
?? src/components/LoyaltyTierSystem.tsx
?? src/components/LuggageArSizer.tsx
?? src/components/MoodDestinationPicker.tsx
?? src/components/MultiCityRouter.tsx
?? src/components/PartyPlan.tsx
?? src/components/SavedSearches.tsx
?? src/components/SmartItinerary.tsx
?? src/components/SocialProofToast.tsx
?? src/components/SustainabilityScore.tsx
?? src/components/TripCountdownWidget.tsx
?? src/components/VoiceInteractiveMap.tsx
?? src/components/checkout/
?? src/data/flights.ts
?? src/pages/
?? sync_log.md

## git diff --stat
PLAN.md                           |  15 +-
src/app/[locale]/flights/page.tsx | 290 +++++++++++++++++++++++++++++++++++++-
2 files changed, 293 insertions(+), 12 deletions(-)

## PLAN.md excerpt (1-120)
(unchanged; see earlier sections)

## plan (opencode)
Next ship milestone: Flights MVP v0.1
- /[locale]/flights listing stable + fast
- filters + sort with clear defaults
- flight card to detail works or gracefully disabled
- detail to checkout works (stub ok)
- no obvious routing or hydration errors
- repo structure not confusing (at least documented)

Prioritized TODO
1) Stabilize flights listing page (src/app/[locale]/flights/page.tsx)
2) Confirm end to end flow: landing -> listing -> detail -> checkout
3) Lock minimal Flights MVP scope (inputs, filters, sorting, data source)
4) Decide data/loading strategy (client vs server, URL as source of truth, caching)
5) Minimal QA gate (smoke, locale, types)
6) Repo hygiene: untracked dirs, duplicate routing (app vs pages), SYNC_LOG.md vs sync_log.md
7) Docs/release discipline (PLAN truth, CHANGELOG policy, WIKI ownership)

Blockers / questions
- flights demo only (local seed) or production connected
- search state URL driven or client state
- keep both src/app and pages or not
- which untracked dirs are real product code vs experiments
- expected [locale] set
- commit/PR boundary: include new components now or reduce scope
