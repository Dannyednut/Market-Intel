# Private-AI Equity Perps — Landscape Scan (Cycle 004)

**Task ID:** C4-1a (retry) · **Date of research:** 2026-10-21 · **Researcher:** Market Intel agent (C4-1a)
**Method:** Combined effort of the original C4-1a run (~17 queries + live-API pulls: Hyperliquid, Gate, VOOI; page fetches: Kraken blog, Gibson Dunn, VOOI, Robinhood, Galaxy) and this retry (~12 additional queries + a second same-day live pull of VOOI/Hyperliquid/Gate APIs + fetches of crypto.news, Crypto Briefing, Bing News). CoinDesk / CoinGecko / MEXC / The Block bodies block datacenter fetches — where a primary fetch failed, headline+date via Google News/Bing index is cited and graded down. All internal Edge-Engine claims treated as hypotheses. Retry additions are marked **[NEW]** where they change a conclusion.

---

## 1. Executive snapshot

- **This is now a real, large, multi-venue market — not a niche.** As of 2026-10-21, perps on private companies (OPENAI, ANTHROPIC) trade on at least **5 live venues simultaneously** (MEXC, Gate, Hyperliquid HIP-3 "io" deployer, Lighter, Robinhood), plus pre-IPO perps at OKX, Coinbase, Binance, Kraken, **BloFin [NEW]**, and dated pre-IPO futures on MNX; more than a dozen other private names trade across the same venues. [A/B — venue APIs + multiple outlets]
- **Hyperliquid's "alias markets" decoded:** the internal term maps to (a) **HIP-3 builder-deployed perps** (HyperCore order book, shared USDC margin; HIP-3 live since **Oct 2025**) and (b) VOOI's **"alias:" asset keys** (`alias:openai`) that map one underlying across venues. [A — Hyperliquid API + Galaxy Research]
- **Verified live spread, twice on 2026-10-21 (VOOI + venue APIs):** OPENAI: Lighter $1,571.5→$1,572.8 / Robinhood $1,554.7→$1,556.8 / Hyperliquid io:OAI ~$1,511.5 / MEXC $1,481.3→$1,482.6 / Gate $1,480.3→$1,481.2 → **Lighter−Gate ≈ +6.2%, Robinhood−MEXC ≈ +5.0%**. ANTHROPIC: Lighter $1,935.4→$1,932.6 / Robinhood $1,926.4→$1,924.4 / Gate $1,926.0→$1,921.5 / HL io:ANTH $1,921.7 / MEXC $1,878.8→$1,877.1 → **Lighter−MEXC ≈ +3.0%**. Internal claim "MEXC→Gate ≈ 10.95%" is **not visible (0.06–0.09%)**; "MEXC→Robinhood 4.7%" ≈ confirmed. [A]
- **The internal OI claims are wrong by ~3 orders of magnitude:** actual pre-IPO OI is **$1.3M–$42M per venue** (HL io:ANTH $42.5M deepest; Robinhood OPENAI $6.0M, ANTHROPIC $8.1M). No "$34B/$18B deep OI on Robinhood" exists. [A — VOOI/HL APIs]
- **Spreads are structural, not transient:** no shared underlying exists — every venue runs its **own synthetic oracle** (Kraken: self-referential smoothed index ±0.25% clamp; OKX: cites Forge Global data; Gate: internal index; HL HIP-3: deployer-defined oracle). Funding is ~0 to ±0.3%/day — **too weak to force convergence**. CoinGecko (2026-09-02) documented perps trading **42–106% above** secondary-market implied valuations. [A/C]
- **[NEW] The Robinhood leg is now identified: Robinhood's perps stack is Lighter.** Robinhood launched EU "tradFi" perpetual futures 2026-07-01 (official scope: crypto, commodities, ETFs, FX — **private names not in official scope**) on the same day Robinhood Chain (Arbitrum L2) mainnet went live "alongside … Lighter perps" (The Block); crypto.trade press explicitly calls Lighter "**Robinhood's perps DEX**" (2026-07-17). VOOI's "robinhood" venue prices sit within ~1% of "lighter" venue prices on every shared name. **[NEW] The Robinhood↔Lighter intra-family gap is itself a persistent ~1% spread** (OPENAI: $1,556.8 vs $1,572.8), so arb legs inside one corporate family remain possible but carry correlated counterparty risk. [B]
- **[NEW] Issuers have fired back — settlement-legitimacy risk is explicit:** Anthropic publicly warned (2026-05-12/15) that unauthorized pre-IPO share sales **are void** and "may be worth exactly nothing," specifically calling out **Forge Global and Hiive** channels; OpenAI issued parallel warnings. **Anthropic confidentially filed its S-1 2026-06-01 with a Nasdaq target of November 2026 — i.e., the conversion event for every ANTHROPIC perp is weeks away.** [B]
- **[NEW] Enforcement is arriving via the private-markets side:** Linqto (pre-IPO share platform) went bankrupt 2025-07-19; two former CEOs charged over a **$450M pre-IPO fraud** 2026-09-02 (one pleaded guilty); SEC charged the founder 2026-10-11; a law firm is investigating **Forge Securities** (2026-03-12). Offshore perps remain uncharged as a class so far. [B]
- **Venue risk is real:** VOOI self-describes as **non-custodial and "not regulated or licensed by any financial regulatory authority"**; MEXC publicly apologized (2025-10/11) for freezing ~$3M of a user's funds; a single anomalous TradFi print (one SK Hynix share, Seoul, 2026-07-28) liquidated **~$57–80M** on a Hyperliquid HIP-3 equity perp. [A/B]
- **Bottom line for the Edge-Engine:** the MEXC-discount / premium-cluster (Robinhood+Lighter+Gate+HL) dislocation is **reproducible and currently live**, but the baseline's OI numbers, the 10.95% MEXC→Gate spread, and any "same margin pool ⇒ safe arb" assumption need correction before capital is sized. Unit conventions differ across venues (e.g., Gate's KIMI $7.78 vs MOONSHOT $65.45 vs MEXC KIMISTOCK $65.72 — same company, different assumed share counts) — naive cross-venue price comparison can manufacture fake spreads. [A]

---

## 2. Name × venue map

### 2a. Name-centric view (live 2026-10-21, VOOI aggregator + venue APIs) **[NEW table]**

OI = USD notional as reported by VOOI (venue unit conventions not fully reconciled; approximate). "SPACEX" went public 2026-06 (Nasdaq: SPCX) — legacy contracts now track the public share.

| Private company | Venues live (ticker) | Price range seen 2026-10-21 | OI (largest venue) | Notes |
|---|---|---|---|---|
| **OpenAI** | MEXC (OPENAIUSDT), Gate (OPENAI_USDT), Robinhood (openai), Lighter (openai), Hyperliquid HIP-3 (io:OAI), Aster, Ondo (closed, OI≈0) | $1,481–$1,573 | HL io:OAI $7.1M; Gate $7.3M; Robinhood $6.0M; MEXC $4.2M; Lighter $1.4M | Deepest multi-venue listing; OKX/Coinbase/Kraken/Binance also run OpenAI pre-IPO products (§2b) |
| **Anthropic** | MEXC (ANTHROPICUSDT, since 2026-04-14), Gate (ANTHROPIC_USDT), Robinhood, Lighter, HL (io:ANTH), Aster; OKX/Coinbase/Kraken/Binance products; **21Shares ETP (Europe) 2026-10-13** | $1,877–$1,933 | HL io:ANTH **$42.5M** (deepest anywhere); Robinhood $8.1M; MEXC $6.3M; Gate $1.3M; Lighter $2.3M | **S-1 filed 2026-06-01; Nasdaq target Nov 2026** — conversion event imminent |
| **Moonshot AI / Kimi** | MEXC (MOONSHOTUSDT since 2026-08-12, KIMISTOCK), Gate (**both** KIMI $7.78 **and** MOONSHOT $65.45), HL (io:MOONSHOT — **delisted**, frozen $67.24) | $7.78 vs $65–67 (units differ!) | MEXC KIMISTOCK $1.2M | Gate's KIMI/MOONSHOT dual listing at a 8.4× price ratio is a live unit-convention trap |
| **Oura** | MEXC (OURASTOCK since 2026-09-22), Gate (OURA), Lighter, HL (xyz:OURA) | $48.6–$51.4 | Gate $1.1M; MEXC $1.2M | |
| **Polymarket** | MEXC (POLYMARKETSTOCK since 2026-09-22), Gate (POLYMARKET) | $23.6–$24.0 | Gate $0.13M | Prediction-market company as perp underlying — self-referential stack |
| **Cerebras (CBRS)** | HL (xyz:CBRS), MEXC (CBRSSTOCK), Gate, Bybit, Lighter, Polymarket, Ondo | $121.3–$121.5 | HL $34.7M; Bybit $2.9M | "Backpack tokenized Cerebras" reports not confirmed this cycle; CBRS perps are everywhere — Cerebras is effectively a public-grade synthetic |
| **SpaceX → public (SPCX)** | HL xyz:SPCX, Bybit ($40M OI), Gate (pre-market contract **delisted** at IPO), Ondo, Polymarket, Lighter (legacy unit, closed), MEXC (SPCXSTOCK) | $147.7–$148.1 (share units) | HL ~$132M | IPO ~2026-06-12 at ~$1.75T; Binance converted to public-stock index on 30-day notice |
| **Unitree (robotics)** | MEXC (since 2026-08-12 per Yellow.com PR), Gate, Bybit, Lighter, Polymarket, Ondo, HL (xyz:UNITREE) | $76.7–$76.9 | MEXC $4.6M; Gate $2.6M; HL $19.4M | First MEXC "pre-IPO futures" PR'd by Yellow.com |
| **MiniMax** | MEXC, Gate (+ MINIMAXHKD), Bybit, Lighter, Ondo, HL (xyz:MINIMAX) | $22.19–$22.26 | Gate $1.2M; HL $2.9M | Hong Kong-listed (public) + perp on HKD unit at Gate |
| **Zhipu AI** | MEXC, Gate (+ ZHIPUHKD), Bybit, Lighter, Ondo, HL (xyz:ZHIPU) | $62.5–$62.6 | Gate $2.3M; HL $11.0M | Same dual-unit pattern as MiniMax |
| **YMTC (Yamaha?/Yangtze Memory)** | MEXC (YMTCSTOCK), HL (xyz:YMTC — closed, OI 0) | $10–$12.2 | MEXC $0.7M | Identity unconfirmed |
| **Shein** | MEXC, Gate, Bybit, Lighter, Robinhood, Ondo, HL (xyz:SHEIN) | $4.68–$4.75 | Bybit $0.5M; HL $0.7M | |
| **Neuralink** | Gate (NEURALINK) | $449.06 | $9k | Single-venue, thin |
| **Anduril** | Gate (ANDURIL) | $118.48 | $47k | Single-venue, thin |
| **Kalshi** | Gate (KALSHI) | $28.50 | $94k | Private prediction-market co. on a perp |
| **xAI** | — | — | — | **Caution: ticker "XAI" on MEXC/Gate/Bybit/Binance is the unrelated XAI gaming token** (crypto category), NOT Elon Musk's xAI. No xAI-corp perp found on any venue. |
| OpenAI/Anthropic-adjacent dated | MNX (MegaETH): 2027-expiry futures on OpenAI, Anthropic, DeepSeek (2026-10-13) | — | — | Dated, not perpetual |

No perp found for: Stripe, Databricks, Canva, Figure, Ripple, Epic (none of the venues checked list them; absence itself is a liquidity signal, not proof of non-existence).

### 2b. Venue-centric view

Live snapshot 2026-10-21 unless noted. **[NEW] rows: BloFin, Bitget.**

| Venue | Product | Since (first private-name evidence) | Names listed (private/pre-IPO relevant) | OI / volume (reported) | Confidence |
|---|---|---|---|---|---|
| **MEXC** | USDT-margined perps, "pre-ipo" category, **50x** | ≥ 2026-04-14 (Google-indexed contract page: ANTHROPICUSDT $1,912.85); MOONSHOTUSDT 2026-08-12; OURA/POLYMARKET 2026-09-22 | OPENAI, ANTHROPIC, KIMISTOCK, MOONSHOT, OURASTOCK, POLYMARKETSTOCK, YMTCSTOCK, UNITREE, CBRSSTOCK, MINIMAXSTOCK, ZHIPUSTOCK, SHEINSTOCK + ~295 stock perps | OPENAI OI $4.2M, ANTHROPIC OI $6.3M, UNITREE $4.6M; funding 8h | B (Google-indexed MEXC pages + VOOI feed; MEXC blocks direct fetch) |
| **Gate** | USDT-margined perps, "pre-ipo"/stock categories, 50x (10x ANDURIL/OURA) | ≥ 2026-04-08 (Gate API `create_time` 1775733209 for SPACEX_USDT pre-market) | OPENAI, ANTHROPIC, ANDURIL, KALSHI, **KIMI + MOONSHOT (dual listing)**, NEURALINK, OURA, POLYMARKET, UNITREE, CBRS, MINIMAX(+HKD), ZHIPU(+HKD), SHEIN + 249 US-stock + 92 Asia-stock perps | OPENAI OI $7.3M, ANTHROPIC $1.3M, CBRS $2.0M; funding ~0 | **A** (live Gate API pull 2026-10-21) |
| **Hyperliquid (HIP-3 builders)** | Builder-deployed perps on HyperCore, USDC-margined, shared margin | HIP-3 mainnet since 2025-10; private names: vntl dex (delisted), io & xyz live | Live: io:OAI, io:ANTH, xyz:OURA/CBRS/UNITREE/MINIMAX/ZHIPU/SHEIN, xyz:SPCX (public-tracking). Delisted: **io:MOONSHOT [NEW]**, vntl:OPENAI/ANTHROPIC/SPACEX, para:ANTH, xyz:YMTC | io:ANTH OI **$42.5M**; io:OAI $7.1M; xyz:SPCX ~$132M; xyz:CBRS $34.7M; HIP-3 total OI ~$3.6B (Galaxy, Jul 2026) | **A** (live HL API + Galaxy Research) |
| **Lighter** | zk-rollup perp DEX — **Robinhood's perps DEX [NEW]**; "pre-ipo" category, 5x | Live by 2026-10-21 (VOOI feed); has own LIT token (CoinMarketCap 2026-08-18) | OPENAI, ANTHROPIC, OURA, CBRS, UNITREE, MINIMAX, ZHIPU, SHEIN + 49 US-stock + 18 Asia-stock perps | OPENAI OI $1.4M, ANTHROPIC $2.3M; 1h funding; prices consistently **highest of the cluster** | B (VOOI feed; Lighter API blocked 403) |
| **Robinhood** | EU perps (official scope: crypto, commodities, ETFs, FX, up to 10x — launched 2026-07-01); **perps infrastructure = Lighter**; private names confirmed only via VOOI feed | EU perps 2026-07-01 (crypto.news/Bloomberg); private names via VOOI 2026-10-21; Robinhood Chain mainnet + stock tokens 2026-07-01 (120+ countries, not US) | Per VOOI: OPENAI (5x, OI $6.0M), ANTHROPIC (5x, OI $8.1M), SHEIN + 32 US-stock perps. **No official Robinhood page/PR lists private names** | OPENAI OI $6.0M, ANTHROPIC $8.1M (VOOI). "$34B/$18B" claim **rejected** | B for product/infra existence; **C** for private-name provenance (aggregator-only) |
| **VOOI (ultra.vooi.io)** | **Aggregator / arbitrage desk, not a venue** — non-custodial routing to 11 venues (hyperliquid incl. HIP-3 dexs, lighter, robinhood, aster, extended, binance, mexc, bybit, ondo, gate, polymarket) | "Ultra" arbitrage desk live 2026-10-21; claims $30B+ cumulative volume | Indexes 5,039 markets; `alias:` identity keys; surfaces live cross-venue spreads | 763 strategies shown; self-reported $30B+ | **A** (own site/API; volume self-reported) |
| **OKX** | "X-Perps" pre-IPO perps, 10x (EU) | 2026-05-06 (CoinDesk) global; 2026-09-10 Europe; 2026-10-13 Australia | OpenAI, SpaceX, Anthropic (TradingView symbol OKX:ANTHROPICUSD.UMU2031 suggests far-dated synthetic) | Not independently verified | B (2+ outlets) |
| **Coinbase** | Pre-IPO perps (SpaceX, then OpenAI/Anthropic) | 2026-06-04 / 2026-06-22 | SpaceX, OpenAI, Anthropic | Not verified | B (Seeking Alpha + Yahoo + Stocktwits 2026-06/10) |
| **Binance** | Stock & pre-IPO perps, USDT-settled | 2026-05-28 | SpaceX (converted to public-stock index on 30-day notice), Anthropic | ANTHROPIC $643M 24h volume (2026-09-09, via OneBullEx) | B |
| **Kraken** | Pre-IPO perps `PF_ANTHROPICXUSD`, `PF_OPENAIXUSD`, 5x, USD multi-collateral | 2026-06-15 (Kraken blog) | Anthropic, OpenAI. Not available US/EEA/CA/AU/NZ; UK professional-only | 20% IM / 10% MM; hourly funding clamp ±0.25% | **A** (Kraken official blog) |
| **BloFin [NEW]** | OPENAI-USDT & ANTHROPIC-USDT pre-IPO perpetual contracts, with launch fee discounts | 2026-07-06 (Traders Union) | OpenAI, Anthropic | n/a | C (single outlet) |
| **Bitget [NEW]** | "IPO Prime" — tokenized SpaceX pre-IPO exposure (not confirmed as perp) | 2026-04-12 (TradingView) | SpaceX | n/a | C (single outlet) |
| **MNX (MegaETH-powered)** | Pre-IPO **dated** futures (2027-expiry), "no shares required" | 2026-10-13 (CoinDesk) | OpenAI, Anthropic, DeepSeek | n/a | B |
| **Kalshi** | CFTC-regulated DCM: IPO-timing event contracts (not perps) + first US crypto perp (BTCPERP, 2026-05-29) | IPO markets live by 2026-05/06 | "OpenAI or Anthropic IPO first?", IPO-date markets | n/a | B |
| **Polymarket** | Private-company event bets (2026-05-19, CBS) + stock perps (CBRS/SPCX/UNITREE, 10x) | 2026-05 (bets); perps live by 2026-10 | Private-company events; perps on SPCX, CBRS, UNITREE | SPCX OI $0.6M (VOOI) | C |
| **Ondo Global Markets** | Perp-style venues on tokenized stocks (VOOI "ondo" venue) | Live 2026-10-21 | SPCX, CBRS, UNITREE, MINIMAX, ZHIPU, SHEIN, SKHYNIX; OPENAI listed but closed (OI≈0) | SPCX OI $3.9M | B (VOOI feed) |
| **FTX (historical)** | Pre-IPO futures era; **listed Coinbase pre-IPO futures 2020-12-22** (The Block) — first crypto-venue pre-IPO derivative on record | 2020-12 | Coinbase, (later Robinhood-era names) | n/a | C (single outlet headline; era known from regulatory literature) |

**Legacy "frozen pre-IPO tokens" (2021-22 era):** the FTX Coinbase pre-IPO futures (2020-12-22) is now anchored; the full 2021-22 catalog (FMV/Equity-token attempts) remains thin — Gibson Dunn (2026-08-11) frames pre-IPO perps primarily as a **2025-26 offshore phenomenon**. Flagged again as a minor follow-up.

---

## 3. Oracle & settlement mechanics — verified vs speculation

**Verified (primary/official):**

1. **Hyperliquid HIP-3 (io/xyz/vntl deployers):** deployer defines **oracle, leverage, margin mode, contract spec** by staking 500k HYPE; Hyperliquid supplies execution/settlement and "does not pick the price" (Galaxy, 2026-07-31). TradeXYZ's mark = **median of three inputs** (oracle price; oracle + 150s EMA of book deviation; median of bid/ask/last). Markets are **USDC-margined on HyperCore** — same margin engine as crypto perps (confirmed by the 2026-07-28 SK Hynix event: crypto-style ADL hit profitable shorts). Internal claim "shared USDC margin pool" = **TRUE for HL HIP-3**, with the contagion caveat in §6.
2. **Kraken (official, 2026-06-15):** pre-IPO marks come from a **"Kraken PreMarket Synthetic index" derived from the contract's own market** (self-referential), exponentially smoothed, with mark **clamped to ±0.25%** of the index; hourly funding "structurally minimal" because of the clamp. At IPO: convert to **xStocks tokenized-equity index** (Backed Assets JE Ltd). If no IPO / index unavailable: Kraken may **delist and settle at a value determined by Kraken**.
3. **Gate (API):** `mark_type: "index"` — internal index price; 8h funding (currently 0 for OPENAI/ANTHROPIC); pre-market contracts flagged `is_pre_market: true` and **delisted** (not converted) at SpaceX IPO. **[NEW]** Gate's OPENAI_USDT contract: `quanto_multiplier 0.01`, `mark_type index`, `funding_rate_limit 0.000001`, `is_pre_market true` — an in-house index with effectively zero funding-rate cap, i.e., funding cannot police the basis.
4. **Binance (via OneBullEx citing Binance Square/H1-2026 report):** pre-IPO contracts use a **synthetic "implied valuation" convention** (ANTHROPIC at $2,120 with **assumed 1.0B share count** ⇒ ~$2.12T); transition to a **public-stock index** on ≥30 days' notice once listing approaches (SpaceX precedent). Clearest documented settlement/conversion term for the class.
5. **OKX:** trading materials **"citing Forge Global company data"** for X-Perps (OneBullEx, 2026-09-30) — secondary-market platform prints feed the reference. Single-outlet citation (C).
6. **VOOI:** pure aggregator — no order book, no custody, no venue-side oracle. VOOI's `alias:` keys are identity mappings, not price sources.
7. **[NEW] Issuer position (decisive for settlement legitimacy):** Anthropic publicly warned investors (2026-05-12, Yahoo Finance: "Anthropic Slams Tokenized Equity Instruments, Tanks Onchain Pre-IPO Share Prices"; 2026-05-15: "Anthropic warns unauthorized stock sales are void") and — per Crypto Briefing — **invalidated transfers made outside officially sanctioned sales, specifically calling out Forge Global and Hiive**; OpenAI issued parallel warnings ("Anthropic and OpenAI Warn Buyers: Unauthorized AI Startup Shares May Be Worthless," 2026-05-12). **Implication: the secondary-market prints (409A-adjacent, Forge/Hiive) that several venues cite as oracle anchors are precisely the channels the issuer declares void.** The mark chain "perp → secondary print → possibly-void transfer" is legally fragile at its root.

**Speculation / unverified:**

- **409A tender prints as direct oracle inputs:** plausible (Forge cited by OKX) but **no venue has published a 409A-based oracle spec**. The 42–106% premium over secondary-market implieds (CoinGecko, 2026-09-02) suggests 409A/secondary prints are at most a slow anchor, not the mark.
- **Who holds the other side:** on CEXs (MEXC/Gate/Binance) the house book takes flow (funding ~0 and Gate's `funding_rate_limit 0.000001` suggest heavy internalization with no funding enforcement); on HL HIP-3 it is trader-vs-trader with deployer backstop (TradeXYZ absorbed the SK Hynix loss "as a one-time discretionary decision" — not a standing policy). No venue discloses a designated counterparty.
- **What happens at the Anthropic IPO (November 2026 target) specifically:** no venue has published contract-by-contract terms. Evidence base is the SpaceX precedent (Binance 30-day notice to public-stock index; Gate delist; Kraken xStocks conversion; HL continues tracking the public name). Treat "premium auto-crystallizes at IPO" as **unproven** — conversion can rebase the contract and strand premium with either side; and if unauthorized-channel transfers are void, the "underlying" the perp references may have no enforceable value for its holders.
- **Unit conventions:** multiple coexisting conventions observed — post-IPO share price (xyz:SPCX $147.7), pre-IPO legacy units (Gate SPACEX_USDT index $2,743.82 vs HL SPCX $147.74), implied-valuation-per-assumed-share (Binance), and **[NEW] intra-company dual listings at Gate: KIMI $7.775 vs MOONSHOT $65.45 (8.4× ratio, same company, same day)** while MEXC KIMISTOCK quotes $65.72. **Any cross-venue spread model must normalize units per venue or it will fabricate spreads.**

---

## 4. Spread durability verdict

**Verdict: the cross-venue dislocation is STRUCTURAL (access + oracle segmentation), with a transient microstructure component on thin books. Expect it to persist for weeks-to-quarters — but the end will be abrupt: the Anthropic IPO (Nasdaq, November 2026 target) is the most likely convergence forcing-event, weeks away.**

Evidence for structural:

- **Access segmentation is codified:** Kraken excludes US/EEA/CA/AU/NZ; OKX split EU/AU launches; MEXC (50x) vs Robinhood 5x/HL 6x vs Gate 50x leverage tiers imply different client bases and margin regimes. MEXC persistently quotes the **lowest** ANTHROPIC price ($1,877.1 vs $1,921.5–$1,932.6 cluster on the second pull, 2026-10-21) and was also the low print in April 2026.
- **No common underlying ⇒ no convergence mechanism:** each venue's mark follows its own oracle (self-referential at Kraken; internal index at Gate; deployer-defined at HL; Forge-cited at OKX). Funding — the only enforcement arm of a perp — is **~0 to ±0.3%/day**, and Gate's funding cap (`0.000001`) plus Kraken's ±0.25% clamp *institutionalize* non-convergence.
- **Persistence across time:** premia documented 2026-09-02 ("42–106% higher" than secondary-market implieds — CoinGecko); still 3–6% across top venues today across two same-day pulls; SpaceX pre-IPO perp fell 27% over three weeks *without* collapsing to any external anchor (CoinDesk, 2026-06-10).
- **Arbitrage is gated:** offshore CEX vs EU retail app vs DEX wallet flow; USDT vs USDC vs multi-collateral. Capital cannot freely and instantly migrate.
- **[NEW] Even the same corporate family doesn't converge:** Robinhood (EU app) and Lighter (its perps DEX) quote OPENAI $1,556.8 vs $1,572.8 (~1.0%) — a persistent gap inside one stack. If intra-family books don't converge, cross-family convergence is even less enforceable.

Evidence for transient component:

- Top-5 venue ranking reshuffles intra-day; today's "MEXC→Gate" gap is ~0.06–0.09% (baseline claimed 10.95%).
- Lighter books are thin (OPENAI OI $1.4M) — part of the Lighter premium is illiquidity, not information.
- **[NEW] Copycat listings are accelerating:** BloFin (2026-07-06), Bitget IPO Prime (2026-04-12), 21Shares launched the first Anthropic ETP in Europe (2026-10-13) — synthetic supply is compounding, which should grind premia down between now and the IPO.
- **[NEW] The May-2026 Anthropic/OpenAI warnings caused an immediate price shock ("Tanks Onchain Pre-IPO Share Prices," 2026-05-12)** — narrative shocks DO compress these markets fast. A single issuer tweet can do what funding never will.

**Correction to internal baseline:** "10.95% MEXC→Gate (thin OI)" not reproducible; "4.7% MEXC→Robinhood" ≈ reproduced (5.0% OPENAI, ~2.5% ANTHROPIC); "$34B/$18B deep OI" **false** (actual $6–8M); "alias markets share Hyperliquid's USDC margin pool" **true for HL HIP-3 legs only**.

---

## 5. Precedent & enforcement catalog **[NEW — was the missing section]**

| Year | Precedent / action | What it establishes | Grade + source |
|---|---|---|---|
| 2020-12-22 | **FTX lists Coinbase pre-IPO futures** (The Block) | First crypto-venue derivative on a then-private company; ran through Coinbase's 2021-04 IPO; no US enforcement action against the product surfaced | C — The Block headline via Google News |
| 2021-22 | Pre-IPO token/FMV-era experiments | Thinly documented this cycle; Gibson Dunn (2026-08-11) frames the current wave as 2025-26 | D (gap) |
| 2025-07-19 | **Linqto (pre-IPO share platform) files bankruptcy** amid federal probes (FinTech Weekly); FINRA probes its BD arm 2025-08-18 (InvestmentNews) | Private pre-IPO retail rails can fail and attract federal scrutiny | B |
| 2026-03-12 | Law firm Meyer Wilson Werning investigates **Forge Securities** over alleged pre-IPO fraud scheme (Yahoo) | The secondary-print oracles themselves (Forge/Hiive) are under investor-fraud cloud | C |
| 2026-05-11/12/15 | **Anthropic + OpenAI issuer warnings**: "Anthropic Slams Tokenized Equity Instruments, Tanks Onchain Pre-IPO Share Prices" (2026-05-12); "Anthropic warns unauthorized stock sales are void" (2026-05-15); "Anthropic and OpenAI Warn Buyers: Unauthorized AI Startup Shares May Be Worthless" (2026-05-12); crypto lawyer warns crackdown risks litigation (2026-05-11) — all Yahoo | Issuers assert unauthorized-channel shares (incl. Forge/Hiive) may be **void/worthless**; caused an immediate on-chain pre-IPO price drop. Direct settlement-legitimacy precedent for every pre-IPO perp | B (multiple dated headlines) |
| 2026-06-18 | **CME sues CFTC** (D.D.C.) arguing perps are swaps; CFTC-SEC joint comment requests 2026-06-18/26 (incl. whether cash-settled equity perp = security futures product) | US classification fight over perps generally | A — Gibson Dunn 2026-08-11 |
| 2026-05-29 | CFTC "Kalshi Order": first US perp (BTCPERP) approved; same-day policy: perps on equity securities / private valuations need **case-by-case Reg 40.3 review** | Onshore equity/private-valuation perps = unapproved by default | A — Gibson Dunn |
| 2026-08-19/20 | **Hyperliquid pitches SEC** on pre-IPO derivatives (CryptoTicker/BigGo); 2026-09-09 Citadel Securities urges SEC oversight of KPI-linked wagers (Yahoo) | The venue itself seeks a US path; tradfi market-makers push back | B |
| 2026-09-02 / 10-11 | **US charges two former Linqto CEOs over $450M pre-IPO fraud**; one pleads guilty; SEC charges founder ("Wizard of Oz" deception) | Most significant US pre-IPO-markets enforcement to date (fraud theory, not product theory) | B |
| 2026-10-02 | **South Korea blocks 27 unregistered crypto exchanges** (CryptoRank) | Jurisdiction-ban pattern for offshore venues reachable by local retail | C |
| 2026-10-02 / 10-09 | **OKX files with SEC** to bring 63 US stocks to 24/7 blockchain trading under the SEC innovation exemption; SEC creates **five-year sandbox for tokenized stocks on public blockchains** (CryptoRank) | Onshore legitimization path forming — could absorb or marginalize offshore pre-IPO perps | C (single outlet each; cross-check next cycle) |
| 2026-10-14/16 | Nasdaq-listed "Perpetuals" company files to trade tokenized US stocks under SEC innovation exemption (The Defiant/StreetInsider/Crypto Briefing) | Same legitimization trend | B |

**Robinhood's own posture:** EU perps are offered on a self-described "**MiCA and MiFID II regulated platform**" (Robinhood EU tweet, 2026-07-01, via crypto.news) — but only for crypto/commodities/ETF/FX. No SEC/CFTC filing or PR covering private-name equity perps was found; if the "robinhood" venue's private names are real, they sit outside every published regulatory perimeter Robinhood describes.

---

## 6. Risk register

| # | Risk | Severity | Evidence (dated) |
|---|---|---|---|
| R1 | **Oracle staleness/manipulation on private names** — marks are self-referential or thinly anchored; no 409A feed | **High** | Kraken synthetic self-referential index (2026-06-15, official); CoinGecko 42–106% premium vs secondary implieds (2026-09-02); HL io:ANTH oracle ~$1,921 while Binance implies $2,120 (2026-10-21 vs 2026-09-30) |
| R2 | **TradFi-feed transmission shock** — one bad external print cascades into liquidations on leveraged equity perps | **High** | SK Hynix one-share print, Seoul 2026-07-28 → mark −18.7% instantly, $57–80M liquidated, ADL hit profitable shorts on Hyperliquid (Galaxy, 2026-07-31) |
| R3 | **Deployer concentration & mortality on HL** — TradeXYZ >90% of HIP-3 OI; vntl (first pre-IPO deployer) delisted all 3 private markets; **[NEW] io:MOONSHOT also delisted** (frozen $67.24, OI 0 — live API 2026-10-21) | **High** | Galaxy (2026-07-31); HL API (2026-10-21) |
| R4 | **Margin-pool contagion on Hyperliquid** — HIP-3 equity perps share HyperCore margin/ADL/insurance with crypto | **High** | Galaxy: HIP-3 ≈ half of HL perp volume, OI ~$3.6B (2026-07-31); SK Hynix used shared ADL; JELLY precedent 2025-03 |
| R5 | **MEXC counterparty risk** — freeze/withdrawal incidents; no top-tier license | **Medium-High** | MEXC froze ~$3M of "The White Whale," apologized (2025-10-31/11-01); site/API blocks institutional verification (Akamai 403 during both scans, 2026-10-21) |
| R6 | **VOOI layer risk** — unregulated, non-custodial aggregator; single point of failure for the Edge-Engine's view; self-reported volume | **Medium** | vooi.io legal footer (fetched 2026-10-21) |
| R7 | **Robinhood provenance — now largely resolved but re-scoped:** official EU perps scope (2026-07-01) covers crypto/commodities/ETF/FX only; private names visible only via VOOI; infra = Lighter (Robinhood's perps DEX). Residual risk: the private-name book's legal wrapper inside the Robinhood stack is undocumented | **Medium** | crypto.news 2026-07-02; The Block 2026-07-01; Crypto News 2026-07-17; VOOI API 2026-10-21 |
| R8 | **Regulatory reclassification/enforcement** — onshore equity/private-valuation perps unapproved; CME litigation; SEC/CFTC comment process | **Medium** | Gibson Dunn (2026-08-11); CME v. CFTC (2026-06-18); Hyperliquid SEC pitch (2026-08); Citadel (2026-09-09) |
| R9 | **Conversion/settlement event risk — imminent:** Anthropic S-1 filed 2026-06-01, **Nasdaq target November 2026**; at IPO, contracts convert to public-stock index on 30-day notice (Binance), delist (Gate), convert to xStocks index (Kraken), or keep trading (HL) | **High (new grade — timing is now weeks away)** | Crypto Briefing (Sept 2026); OneBullEx (2026-09-30); Gate API; Kraken blog (2026-06-15) |
| R10 | **Issuer-nullification risk [NEW]:** if unauthorized-channel shares are void (Anthropic/OpenAI warnings; Forge/Hiive callouts), the "underlying" several oracles cite has impaired legitimacy; issuers could repeat shocks before/at IPO | **Medium-High** | Yahoo 2026-05-11/12/15; Crypto Briefing (Forge/Hiive invalidation detail) |
| R11 | **Copycat listing compression** — OKX, Coinbase, BloFin, Bitget, MNX, 21Shares ETP all entered within 6 months; per-venue OI dilution and spread compression likely into the IPO | **Medium** | Venue map §2; BloFin 2026-07-06; 21Shares 2026-10-13 |
| R12 | **Funding-carry mirage** — funding ~0 and capped; "short premium, collect funding" does not exist on several venues | **Medium** | Gate `funding_rate_limit 0.000001` (API, 2026-10-21); Kraken ±0.25% clamp |
| R13 | **Data-integrity risk in the Edge-Engine itself** — OI inflated ~3-4 orders of magnitude; stale 10.95% spread; unit conventions unreconciled (KIMI/MOONSHOT 8.4× trap) | **Medium** | Baseline vs §2/§4 measurements (2026-10-21, two pulls) |

---

## 7. Hard data points

1. **2026-10-21 (live HL API, two pulls):** Hyperliquid HIP-3 private-name markets: io:ANTH mark ~$1,921–$1,923, OI $42.5M, 6x; io:OAI ~$1,510–$1,512, OI $7.1M; xyz:SPCX $147.7–$148.1, OI ~$132M; **io:MOONSHOT delisted (frozen $67.24, OI 0)**; vntl:OPENAI/ANTHROPIC/SPACEX delisted (frozen $1,336.2 / $1,619.3 / $2,109.5). — https://api.hyperliquid.xyz/info [A]
2. **2026-10-21 (live VOOI API, second pull):** 5,039 markets across 11 venues. OPENAI pre-IPO perps: Lighter $1,572.80 / Robinhood $1,556.76 / Aster $1,482.79 / MEXC $1,482.61 / Gate $1,481.23; OI $1.4M / $6.0M / $0.3M / $4.2M / $7.3M. ANTHROPIC: Lighter $1,932.60 / Robinhood $1,924.40 / Gate $1,921.47 / Aster $1,878.22 / MEXC $1,877.06; OI $2.3M / $8.1M / $0.07M / $6.3M / $1.3M. KIMI(Moonshot) at Gate: KIMI $7.775 vs MOONSHOT $65.45 vs MEXC KIMISTOCK $65.72. — https://ultra.vooi.io/api/perps/exchange/markets [A]
3. **2026-10-21 (live Gate API):** OPENAI_USDT index $1,481, mark=index, funding 0, `funding_rate_limit 0.000001`, quanto_multiplier 0.01, `is_pre_market: true`, 50x; ANTHROPIC_USDT index ~$1,927; SPACEX_USDT `status:"delisted"`, created 2026-04-08. — https://api.gateio.ws/api/v4/futures/usdt/contracts/OPENAI_USDT [A]
4. **2026-06-15 (Kraken official):** PF_ANTHROPICXUSD / PF_OPENAIXUSD live, 5x max, 20% IM / 10% MM, hourly funding clamped to ±0.25% of a self-referential smoothed "PreMarket Synthetic index"; conversion to xStocks at IPO; not available US/EEA/CA/AU/NZ. — https://blog.kraken.com/product/kraken-derivatives/trade-anthropic-and-open-ai-at-up-to-5x-leverage [A]
5. **2026-07-31 (Galaxy Research):** TradeXYZ/SK Hynix: one share printed −29.96% at Seoul open 2026-07-28; xyz:SKHYNIX mark −18.7% "effectively instantaneously"; ~$57–80M liquidated, ~960 accounts; one-time reimbursement. HIP-3 ≈ half of HL perp volume, OI ~$3.6B; TradeXYZ >90% of HIP-3 OI. — https://www.galaxy.com/insights/research/hyperliquid-tradexyz-oracle-liquidations [A]
6. **2026-08-11 (Gibson Dunn):** CFTC Kalshi Order 2026-05-29 (first US perp; equity/private-valuation perps need case-by-case review); CME v. CFTC filed 2026-06-18; "offshore venues listed Perpetuals referencing the implied valuations of … pre-IPO companies" in 2025-26. — https://www.gibsondunn.com/perpetual-contracts-product-structure-and-recent-us-regulatory-developments/ [A]
7. **2020-12-22 (The Block):** "FTX lists Coinbase pre-IPO futures contracts" — the direct 2021-era precedent for private-company derivatives on crypto venues. — via Google News index [C]
8. **2026-09-02± (Crypto Briefing, fetched):** Anthropic S-1 confidentially filed **2026-06-01**, target NASDAQ **November 2026**; Anthropic **invalidated unauthorized transfers, called out Forge Global and Hiive**; "shares may be worth exactly nothing"; OpenAI delayed listing by ≥1 year; SpaceX June-2026 IPO allocated up to 30% retail, largest US IPO on record. — https://cryptobriefing.com/retail-investors-anthropic-openai-ipo-frenzy/ [B]
9. **2026-05-12 / 2026-05-15 (Yahoo Finance headlines):** "Anthropic Slams Tokenized Equity Instruments, Tanks Onchain Pre-IPO Share Prices"; "Anthropic warns unauthorized stock sales are void"; "Anthropic and OpenAI Warn Buyers: Unauthorized AI Startup Shares May Be Worthless"; "Crypto Lawyer Warns Anthropic Stock Crackdown Risks Litigation" (2026-05-11). [B]
10. **2025-07-19 → 2026-10-12 (Linqto arc):** bankruptcy (FinTech Weekly); FINRA probe of BD arm (InvestmentNews 2025-08-18); two ex-CEOs charged over $450M pre-IPO fraud, one guilty plea (Yahoo 2026-09-02); SEC charges founder, "Wizard of Oz" deception (InvestmentNews 2026-10-12); SEC brings two pre-IPO fraud cases (SecondaryLink 2026-10-05); Forge Securities investigated by Meyer Wilson Werning (Yahoo 2026-03-12). [B]
11. **2026-07-01/02 (Robinhood stack):** Robinhood launches EU perpetual futures for crypto/commodities/ETFs/FX, ≤10x, on a "MiCA and MiFID II regulated platform"; Robinhood Chain (Arbitrum L2) mainnet live with 24/7 tokenized stocks in 120+ countries (not US); The Block: "Robinhood Chain goes live on mainnet alongside 24/7 tokenized stocks, **Lighter perps**…"; Crypto News 2026-07-17: "What is Lighter? **Robinhood's perps DEX**." — https://crypto.news/robinhood-launches-tradfi-perps-in-europe-unveils-blockchain-and-ai-trading-push/ [B]
12. **2026-07-06 (Traders Union):** BloFin announces OPENAI-USDT and ANTHROPIC-USDT pre-IPO perpetual contracts with fee discounts. — via Google News index [C]
13. **2026-07-13 (Reuters):** "Crypto exchanges cash in on SpaceX frenzy with pre-IPO derivatives" — mainstream-wire confirmation of the phenomenon and its demand base. — via Google News index [B]
14. **2026-10-13 (Yahoo Finance):** "21shares Launches First Anthropic ETP in Europe Ahead of Its IPO" — regulated synthetic supply arriving before the IPO. [C]
15. **2026-04-14 (Google-indexed MEXC contract page):** "1,912.85 [ANTHROPICUSDT] Futures, USDT-Margined Perpetual Contract | MEXC" — confirms the anchor listing date. [B]
16. **2026-09-02 (CoinGecko headline, fetch blocked):** "Crypto-enabled Pre-IPO Trading: Anthropic and OpenAI Perps Trade 42-106% Higher." — https://www.coingecko.com/learn/crypto-pre-ipo-trading-anthropic-openai-perps [C]
17. **2026-10-02/09 (CryptoRank headlines):** South Korea blocks 27 unregistered exchanges (10-02); OKX SEC filing for 63 tokenized US stocks (10-02); SEC five-year sandbox for tokenized stocks on public chains (10-09). [C each]

---

## 8. Weak signals & anomalies

- **[NEW] Gate's KIMI/MOONSHOT dual listing is a live unit trap:** same company, same day, $7.775 vs $65.45 (8.4×). MEXC's KIMISTOCK ($65.72) tracks the MOONSHOT scale. Any scanner matching "kimi" naively will fabricate a −88% "discount."
- **[NEW] The Robinhood↔Lighter intra-family gap (~1.0% on OPENAI)** persists despite common ownership/infra — evidence that even shared technology does not enforce convergence; also means the "Robinhood leg" and "Lighter leg" of any arb are **correlated counterparties**, not diversification.
- **[NEW] io:MOONSHOT delisted on Hyperliquid** while MEXC/Gate keep Moonshot alive — delisting churn on the newest private names is fast (weeks, not quarters).
- **Internal "$34B/$18B OI" looks like a units bug** (actual $6–8M). If the Edge-Engine sizes on OI, it is sizing on fiction.
- **The claimed 10.95% MEXC→Gate spread** is not present today (~0.06–0.09%); recommend re-deriving the spread series with unit normalization before trusting the "~90% persistence over 2.5 min" stat.
- **Funding is dead flat while a 3–6% gap persists** — economically strange; suggests mark/index governance (clamps, house books, `funding_rate_limit` ~0) rather than market clearing. Any funding-harvest variant is likely illusory.
- **Delisted-but-frozen markets linger on Hyperliquid** (vntl, io:MOONSHOT) — scanners pulling the HL universe wholesale will ingest zombie prices.
- **Gate still lists KALSHI and POLYMARKET as pre-IPO perps** — the private-markets stack is self-referential (prediction markets on IPOs; perps on the prediction-market companies).
- **Pre-IPO perp prices quoted in press as valuation truth** ("No Anthropic Stock Exists But Crypto Traders Just Priced It At $2T" — news.bitcoin.com, ~2026-09-30; CNBC 2026-10-16) — the tail wagging the dog; reflexivity/herding grows into the IPO.
- **OKX's TradingView symbol `ANTHROPICUSD.UMU2031`** implies a 2031-dated synthetic — verify whether OKX's "perp" is actually dated.
- **Ticker "XAI" on every CEX is the gaming token, not xAI corp** — a name-collision risk for the Edge-Engine's watchlist.
- **A Nasdaq-listed "Perpetuals" company filed (2026-10-14/16) to trade tokenized US stocks under an SEC innovation exemption; OKX filed similarly (2026-10-02); SEC opened a 5-year tokenized-stock sandbox (2026-10-09)** — onshore legitimization is fast; could either compress offshore spreads or absorb the demand.

---

## 9. Watch items for next cycle

1. **Anthropic IPO conversion mechanics (Nasdaq, November 2026 target) — top priority.** Build the event calendar: 30-day-notice windows at Binance (public-stock index conversion), Gate delist behavior, Kraken xStocks conversion, HL continuation, MEXC unknown. The Binance mechanism is the model to monitor; the MEXC contract's settlement terms remain **undocumented** — highest-priority unknown.
2. **Finish the Robinhood question with in-app evidence:** obtain Robinhood EU in-app perps market list (or official instrument list/API) to confirm/deny private-name perps in the EU app; establish which legal entity offers them and whether it is Lighter's book re-branded.
3. **Pull historical funding + mark series** (HL funding history; MEXC/Gate funding) for OPENAI/ANTHROPIC to test the "~90% persistence over 2.5 min" claim and measure MEXC→cluster mean-reversion half-lives within execution windows.
4. **Verify MEXC listing dates + specs** for OPENAI/ANTHROPIC/MOONSHOT (announcement pages; API via residential IP), incl. funding methodology and house-book disclosure.
5. **Map OKX X-Perps spec** (UMU2031 naming, Forge input weights) and Coinbase's wrapper (International Exchange vs Derivatives).
6. **Monitor HIP-3 deployer health:** TradeXYZ backstop posture post-SK-Hynix; whether the "io" deployer publishes oracle docs; watch for new private-name deployers (copycat listing = spread compression signal).
7. **Regulatory docket:** CME v. CFTC (D.D.C.); CFTC-SEC comment outcomes; any Reg 40.3 filing for an equity/private-valuation perp; SEC tokenized-stock sandbox rules (2026-10-09); South Korea-style bans propagating to other jurisdictions.
8. **Issuer-actions channel [NEW]:** watch Anthropic/OpenAI statements before/at IPO (the May-2026 warnings moved prices immediately); watch Forge/Hiive litigation fallout (Linqto trial, Forge investigation) since their prints feed several oracles.
9. **MEXC standing:** new freeze/withdrawal incidents; proof-of-reserves; jurisdictional actions.
10. **Close the 2021-22 precedent gap** (FTX-era pre-IPO product catalog, FMV/equity-token attempts, frozen products) with archive sources.
11. **Quantify venue-unit conventions** (contract multipliers, assumed share counts, KIMI/MOONSHOT-style dual units) into a normalization table for the Edge-Engine — prerequisite for trusting any cross-venue spread.

---

## 10. Source list

Primary / official (fetched or API, 2026-10-21 unless noted):
- Hyperliquid Info API — https://api.hyperliquid.xyz/info (POST `perpDexs`, `metaAndAssetCtxs` per dex: xyz, io, vntl, para)
- Gate Futures API — https://api.gateio.ws/api/v4/futures/usdt/contracts/{OPENAI_USDT,ANTHROPIC_USDT,SPACEX_USDT} and /tickers
- VOOI aggregator APIs — https://ultra.vooi.io/api/perps/exchange/markets ; https://ultra.vooi.io/api/perps/arbitrage-scanner ; UI https://ultra.vooi.io/arbitrage-desk ; site https://vooi.io
- Kraken Blog (2026-06-15) — https://blog.kraken.com/product/kraken-derivatives/trade-anthropic-and-open-ai-at-up-to-5x-leverage
- Galaxy Research (2026-07-31) — https://www.galaxy.com/insights/research/hyperliquid-tradexyz-oracle-liquidations
- Gibson Dunn Client Alert (2026-08-11) — https://www.gibsondunn.com/perpetual-contracts-product-structure-and-recent-us-regulatory-developments/
- Robinhood EU perps page — https://robinhood.com/eu/en/perpetual-futures/ (US: https://robinhood.com/us/en/perps/ → 404)
- OneBullEx (2026-09-30) — https://www.onebullex.com/news/articles/binance-anthropic-contract-faces-public-stock-index-shift-after-643m-volume
- Yellow.com press release (2026-08-12) — https://yellow.com/press-releases/mexc-first-to-list-unitree-pre-ipo-futures-as-daily-trading-volume-surges-1104
- **[NEW]** crypto.news (2026-07-02) — https://crypto.news/robinhood-launches-tradfi-perps-in-europe-unveils-blockchain-and-ai-trading-push/
- **[NEW]** Crypto Briefing (Sept 2026, fetched) — https://cryptobriefing.com/retail-investors-anthropic-openai-ipo-frenzy/

News (via Google News / Bing News index; dates as published):
- **[NEW]** The Block 2020-12-22 — "FTX lists Coinbase pre-IPO futures contracts"
- **[NEW]** Reuters 2026-07-13 — "Crypto exchanges cash in on SpaceX frenzy with pre-IPO derivatives"
- **[NEW]** The Block 2026-07-01 — "Robinhood Chain goes live on mainnet alongside 24/7 tokenized stocks, Lighter perps…"; Crypto News 2026-07-17 — "What is Lighter? Robinhood's perps DEX"; Cryptonomist 2026-09-30 — "Lighter Crypto Price Drop… After Robinhood Bitstamp Shift"; CoinMarketCap 2026-08-18 — "Lighter (LIT) Surges … on Robinhood Incentives"
- **[NEW]** Yahoo Finance 2026-05-11/12/15 — Anthropic/OpenAI unauthorized-shares warnings series; 2026-05-17 — "Anthropic's shadow IPO market is already flashing trillion-dollar prices"; 2026-08-04 — "Solana Investor Appetite Drives 78% Share of Pre-IPO Tokens"
- **[NEW]** Linqto arc: FinTech Weekly 2025-07-19; InvestmentNews 2025-08-18 & 2026-10-12; Yahoo 2026-09-02; Finance Magnates 2026-09-03; KuCoin 2026-10-11; SecondaryLink 2026-10-05; Yahoo 2026-03-12 (Forge Securities investigation)
- **[NEW]** Traders Union 2026-07-06 — BloFin OPENAI/ANTHROPIC-USDT pre-IPO perps; TradingView 2026-04-12 — Bitget "IPO Prime" SpaceX
- **[NEW]** Yahoo 2026-10-13 — 21Shares first Anthropic ETP in Europe; Stocktwits 2026-10-16 — Coinbase challenges Binance with OpenAI/Anthropic pre-IPO futures; news.bitcoin.com ~2026-09-30 — "No Anthropic Stock Exists But Crypto Traders Just Priced It At $2T"
- **[NEW]** CryptoRank 2026-10-02/09 — South Korea blocks 27 unregistered exchanges; OKX SEC filing (63 tokenized stocks); SEC five-year tokenized-stock sandbox
- CoinDesk 2026-05-06 — OKX joins pre-IPO frenzy; CoinDesk 2026-06-10 — SpaceX pre-IPO perp −27% in three weeks; CoinDesk 2026-10-13 — MNX pre-IPO futures (OpenAI/Anthropic/DeepSeek); CoinDesk 2026-09-10 — OKX Europe X-Perps
- Unchained 2026-05-18 — "SpaceX Pre-IPO Perpetuals Go Live on Hyperliquid"; CoinDesk 2026-05-18 — "$1.78 trillion valuation"
- Seeking Alpha 2026-06-22 / Yahoo 2026-06-23 / Crypto News 2026-06-23 — Coinbase pre-IPO perps SpaceX/OpenAI/Anthropic
- Binance (official) 2026-05-28 — futures ahead of SpaceX IPO settled in USDT
- CoinGecko 2026-09-02 — "Anthropic and OpenAI Perps Trade 42-106% Higher"
- CryptoPotato 2026-06-30 — tokenized pre-IPO volume +1,060%; BeInCrypto 2026-06-17 — pre-IPO perp volume 6,000× since March
- Forbes 2026-05-27 — "The Hyperliquid SpaceX Perp Is The Real Regulatory Blind Spot"; 디지털투데이 2026-05-27 — SPCX bets spread amid regulatory gap; TradingView 2026-05-27 — CMC Markets and Binance race on SpaceX retail access
- CryptoTicker 2026-08-20 — "Hyperliquid at the SEC: Pre-IPO Futures for the US"; BigGo 2026-08-19 — Hyperliquid pitches SEC
- CNBC 2026-08-21 — perps vs Wall Street; Yahoo/Cryptonews 2026-08-21 — Multicoin pitches CFTC; Yahoo 2026-09-09 — Citadel urges SEC oversight of KPI-linked wagers
- The Defiant / StreetInsider / Crypto Briefing 2026-10-14/16 — Nasdaq-listed Perpetuals files for tokenized US stocks
- Yahoo Finance / Binance Square 2025-10-31 & 2025-11-01 — MEXC froze $3M "White Whale"; "We Fucked Up" apology
- CBS News 2026-05-19 — Polymarket private-company bets; CNBC 2026-06-26 — Kalshi OpenAI-IPO odds; Time 2026-09-22; Action Network 2026-09-11
- CNBC 2026-10-16 — CoreWeave selloff affecting OpenAI vs Anthropic valuations; Pluang 2026-10-17 — pre-IPO futures diverge as CoreWeave hits one-year low
- MEXC blog 2026-06-08 — "SpaceX (SPCX) IPO on June 12: Inside the $1.75 Trillion Listing"; MEXC 2026-09-14 — "Is Anthropic Really Worth $965 Billion?" (content series)
- Google-indexed MEXC contract page (2026-04-14) — ANTHROPICUSDT $1,912.85

Blocked / unverified this session (explicit): CoinDesk article bodies (403/Fastly), CoinGecko research body (Cloudflare), MEXC site/API (Akamai 403), Lighter API (403), The Block (403), Traders Union body (fetch empty), Kraken price/API pages (Cloudflare), Seeking Alpha / Forbes / Capital Brief (not attempted/paywall), OKX product docs (not found), all Robinhood official confirmations of private-name perps (not found), crypto.news Lighter explainer (404 on direct URL; headline-only).

*Grades: A = primary/official; B = 2+ independent outlets; C = single outlet; D = unverified claim.*
