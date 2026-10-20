# Venue-Risk Baseline — VOOI / MEXC / Hyperliquid / HyperEVM / Backpack (Cycle 004)

**Task:** C4-1d — Market Intel research program, Cycle 004 Wave 1 (RESEARCH ONLY)
**Compiled:** 2026-10-20/21 UTC. All API pulls and page fetches executed 2026-10-20 ~17:00–18:30 UTC.
**Method:** Live queries — Google News RSS (8 topic searches), DefiLlama API (protocols, protocol histories, yields), CoinGecko API, direct fetches of vooi.io, docs.vooi.io (full corpus incl. llms-full.txt, 226,887 bytes), vooi.io Terms & Conditions. ~12 query/executions total. No fabrication: every claim is tagged with a retrieval date and, where third-party, the publication + date. Google News RSS links are redirect URLs (publication, date, headline given for traceability).

---

## 1. Executive snapshot (≤10 bullets)

- **VOOI is a non-custodial perp aggregator, not a venue** — it routes to Hyperliquid, Kinetiq/trade.xyz, Lighter, Robinhood, Aster, Extended, Ondo, plus CEX perps (Binance, MEXC, Bybit, Gate) via API keys (docs.vooi.io, retrieved 2026-10-20). Its own footer admits: "VOOI.io is not regulated or licensed by any financial regulatory authority" (vooi.io, retrieved 2026-10-20).
- **VOOI transparency is grade D:** Terms (updated 2026-06-24) name no legal entity ("binding agreement… with vooi.io"), claim non-custodial venue-native execution, and the full docs corpus contains **zero** mentions of "audit" or "security review" (llms-full.txt scan, 2026-10-20). On-chain TVL registered by DefiLlama is de minimis ($14.7k, "Vooi V1" on Linea).
- **Hyperliquid platform itself shows no solvency events in 2026** — 2026 incidents were market-structure events (SK Hynix oracle anomaly → $57M liquidations, 2026-07-28; user account drain $738,600, 2026-09-09; JELLY meme-coin $6.2M exploit + delisting, 2026-10-11).
- **HYPE verified at $80.08 / $17.81B mcap** (CoinGecko, 2026-10-20); 130-day window max $96.63 (2026-09-22), Oct 7 print $87.78, 30d change −14.2% — i.e., HYPE is pulling back from September highs, not pumping.
- **HLP is shrinking, not failing:** TVL $178.2M on 2026-10-20, −28.4% over 90 days ($248.8M on 2026-07-20) (DefiLlama). The "~−50% 30d APR in early Oct 2026" claim is **not independently verifiable** (HLP absent from public yield feeds) — logged as unresolved.
- **MEXC publishes monthly proof-of-reserves** (Oct 2026 PoR released 2026-10-16; BTC reserve coverage 294%; Sept 2026: 297%) **but has a documented wrongful-freeze pattern** — the $3M "White Whale" case (apology 2025-11-01), dispute reignited 2026-01-07, and a $340k account-hack complaint (2026-09-28).
- **MEXC now lists private-company pre-IPO perps** — ANTHROPICUSDT perpetual (2026-04-14), MOONSHOTUSDT/Kimi (2026-08-12), OURA (2026-09-22), POLYMARKET (2026-09-22) — a high-risk-appetite listing signal.
- **HyperEVM had a network outage in early April 2026** (Binance Square 2026-04-01; PeckShield via CryptoRank 2026-04-02) plus a $1.5M Purrlend exploit (2026-04-25); Hyperliquid Bridge TVL stands at $6.75B (2026-10-20).
- **HyperEVM DeFi legs are thin:** Kinetiq/kHYPE healthy at $841M TVL (kHYPE APY ~1.99%, 30d mean 2.02%), but Euler V2 on Hyperliquid L1 holds only **$1.77M**, HyperSwap V3 $10.4M, Ramses CL V2 $10.98M (DefiLlama, 2026-10-20) — position sizing must respect that.
- **Backpack is scaling fast with a US regulatory push:** $1B daily volume 5 days into "Pre-Season" (CoinMarketCap, 2026-10-09); former SEC Acting Chairman Piwowar joined Backpack US board (2026-06-09); BP token launched 2026-03-23. No incidents found. Still a young venue.

---

## 2. Venue-by-venue baseline

### 2.1 VOOI (vooi.io / ultra.vooi.io) — Grade: **D** (solvency-transparency grade; not a custody venue)

**What it is.** A "Unified Perp Trading Layer": aggregator + execution layer across perp venues, with three interfaces — Ultra v3 (trading desk), Pro v1 (terminal), Light v2 — plus Arbitrage Desk, Arbitrage Bots, a unified Perps API and an MCP server for AI agents (docs.vooi.io "VOOI Introduction" + "Ultra Overview", retrieved 2026-10-20). Homepage claims: 500+ crypto & RWA perp markets, "$30B+" cumulative volume, 5 DEXs aggregated, 99.91% uptime, 100ms median latency (vooi.io, retrieved 2026-10-20). Supported venues per Ultra Operational Guidelines: **Hyperliquid, trade.xyz/Kinetiq, Lighter, Robinhood, Aster, Extended, Ondo** (venue-native deposits) and **Binance, MEXC, Bybit, Gate** futures via user-created API keys (docs.vooi.io llms.txt + llms-full.txt, retrieved 2026-10-20). Token: $VOOI ERC-20 on Ethereum (`0xb31561F0e2aaC72406103b1926356D756F07A481`), bridged to BNB Chain and Mantle, 1B fixed supply (docs.vooi.io "VOOI Token", retrieved 2026-10-20). Listed on Kraken 2025-12-18 (Kraken Blog) and tracked by CoinMarketCap since 2025-10-31.

**Registration/licensing.** First-party admission, homepage footer: *"Regulatory Status: VOOI.io is not regulated or licensed by any financial regulatory authority. The Services offered are not subject to any regulatory oversight."* (vooi.io, retrieved 2026-10-20). Terms & Conditions (last updated 2026-06-24): agreement is made "between you… and vooi.io ('VOOI')" — **no operating legal entity, jurisdiction, or registration disclosed**; not licensed/registered/approved by MAS, US SEC, US CFTC "or any other financial regulatory authority"; services unavailable to US and Singapore persons (vooi.io/terms&conditions, retrieved 2026-10-20).

**Team.** Not identified in any public page pulled (no team page linked from homepage or docs index; no funding announcement found in news searches beyond 2024 ICO-era coverage by ICO Drops 2024-03-05 and CryptoRank 2024-08-23). Thin public info = finding (per brief).

**Audits/security.** Zero occurrences of "audit" or "security review" across the entire docs corpus (llms-full.txt, 226,887 bytes, retrieved 2026-10-20). No audit report linked from homepage. Docs repeatedly state non-custodial, venue-native execution ("keeping execution venue-native and non-custodial", Ultra Overview) and T&Cs state VOOI "does not take possession, custody, or control of user assets, private keys, accounts, collateral, margin, orders, or positions" — but this is self-attested, unaudited.

**TVL/volume.** DefiLlama "Vooi V1": **$14,652** (Linea, 2026-10-20); main "Vooi" derivatives slug: no TVL (consistent with non-custodial venue-native margin — funds live on venues, not VOOI). The "$30B+ cumulative volume" claim is self-reported and **unverified**; docs point to Dune (dune.com/vooi/vooidash) as the operational-metrics source — flagged for next-cycle verification. Proof-of-reserves: **N/A by design** (non-custodial); risk instead concentrates in API-key handling and front-end trust.

**Red flags.** (1) No named legal entity; (2) no license; (3) no audits; (4) self-reported volume with no independent TVL footprint; (5) docs note risk of API keys with withdrawal permission enabled (llms-full.txt: "VOOI if the Withdrawal permission is enabled for the API key" — cautionary context, 2026-10-20). No security incidents found in news searches (2024–2026) — silence, not proof of safety.

**Verdict: D.** Usable as an orchestration/UI layer over venues the engine already trusts, but it should never be a custody point, and its own regulatory disclaimer plus absent audit trail caps it at D until an audit, entity disclosure, or Dune-verified usage appears.

### 2.2 MEXC — Grade: **C+**

**What it is.** Large CEX (spot + USDT-M perps), country: Seychelles (historical registration; not re-verified this cycle). The venue for the engine's spread legs.

**Regulatory state.** No CFTC/SEC enforcement action against MEXC surfaced in 2025-26 news searches (queries run 2026-10-20). Maintains a self-published "Restricted Countries" list (MEXC blog, 2025-09-02). No new jurisdiction bans found in this cycle's queries; do not overstate either way.

**Proof-of-reserves.** Monthly cadence, self-published: **October 2026 PoR released 2026-10-16**, BTC reserve coverage **294%** (GlobeNewswire release; TOKENPOST 2026-10-16); **September 2026 PoR**, BTC ratio **297%** (markets.businessinsider.com, 2026-09-15). MEXC "Guardian Fund" claims +1,000 BTC addition (Yellow.com, 2026-10-19 — MEXC press echo). Caveat: CEX PoR without third-party attestation of liabilities is weak evidence of solvency; treat as a hygiene signal, not proof.

**Withdrawal/freezing incidents (the pattern that matters).**
- 2025-08-25: trader launches $2M public campaign after MEXC freezes $3M ("White Whale") (TradingView).
- 2025-11-01: MEXC **apologizes** for wrongfully freezing the $3M (Cryptonews); same day MEXC warned against "speculation on rumors of the exchange's financial problems" (Binance Square) — a solvency rumor that was denied, and no failure followed.
- 2026-01-07: White Whale vs MEXC dispute back in focus (CryptoRank) — unresolved tail.
- 2026-09-28: "MEXC account hack: How did a user lose $340K?" (Crypto News); 2026-09-29: "API Key Outlived the Freeze and Drained an Account" (CryptoTicker) — account-control complaints continue into Sep 2026.
- "Internal accounts" controversy: no article using that exact term surfaced in this cycle's searches; the White Whale case embodies the underlying allegation (exchange absorbing/controlling user funds). Logged as **unresolved** — do not assert.

**Delisting waves.** No specific delisting-wave article found (search run 2026-10-20). MEXC's listing machinery is instead visibly hyperactive: **private-company pre-IPO perps** — ANTHROPICUSDT USDT-M perpetual (MEXC page headline, 2026-04-14), MOONSHOTUSDT "Pre-IPO Futures" for Kimi/Moonshot AI (2026-08-12), OURA Pre-IPO Futures ahead of Nasdaq listing (2026-09-22), POLYMARKET Pre-IPO Futures (2026-09-22), plus an Anthropic-IPO SEO content push (Sept 2026). Marketing pre-IPO equity exposure via perps is a jurisdiction-sensitive, counterparty-unfriendly product class — treat MEXC's exotic listings as a risk-appetite signal.

**Verdict: C+.** Functioning, liquid, monthly PoR claims; offset by a two-year pattern of freeze complaints and exotic product risk. Operational rule for go-live: spread-leg balances at MEXC must be working-capital-only with automated same-day sweeps.

### 2.3 Hyperliquid (HyperCore) — Grade: **B**

**What it is.** On-chain perp DEX L1 (HyperCore) + HyperEVM chain + spot orderbook; the engine's USDC margin pool lives here.

**HYPE state (verified).** Price **$80.08**, market cap **$17.81B**, 24h volume $689.6M (CoinGecko API, retrieved 2026-10-20). Daily closes (DefiLlama coins chart, confidence 0.99, retrieved 2026-10-20): 2026-06-15 $68.21 → low **$52.10 (2026-08-02)** → **$96.63 peak (2026-09-22)** → $87.98 (2026-10-01) → **$87.78 (2026-10-07)** → $81.59 (2026-10-15) → $78.15 (2026-10-19). 30d change **−14.2%**. The orchestrator claim "3.5x'd to ~$89 around Oct 7": the ~$89 print is verified; a **3.5x move does not occur inside the last 130 days** (max multiple low→peak = 1.9x) — the 3.5x must refer to an earlier-2026 base (~$25–28), unverified this cycle.

**HLP (vault) state.** TVL **$178.2M** (2026-10-20), down from $248.8M on 2026-07-20 → **−28.4% / 90d** (DefiLlama protocol history, retrieved 2026-10-20): 2026-08-13 $199.4M → 2026-09-06 $189.4M → 2026-09-30 $182.9M → 2026-10-12 $180.2M. Claimed "~−50% 30d APR early Oct 2026": **no public APR feed found** (HLP is absent from yields.llama.fi pools; Hyperliquid's stats-data endpoint returned AccessDenied) → **unresolved**, directionally consistent with the TVL bleed.

**2025-26 incidents.** 2025 background: JELLYJELLY delisting after $12M manipulation (The Block/Yahoo, 2025-03-26); POPCAT crash → $5M bad debt, "third market manipulation attack in 2025" (Yahoo, 2025-11-13). 2026: SK Hynix perp **oracle anomaly** → $57M liquidations, Hyperliquid published explanation (BeInCrypto, 2026-07-28); user account drained $738,600 USDC (CryptoRank, 2026-09-09); JELLY meme coin $6.2M exploit + exchange delisting, whale retained 10% supply (CoinMarketCap, 2026-10-11); "Papertrade" (Hyperliquid-based app) $1.28M manipulation via 1000x leverage (BigGo Finance, 2026-10-11); ZachXBT: >87% of FreedomXMR inflows on Hyperliquid linked to illicit funds (Crypto News, 2026-10-20) — AML/reputational, not solvency. **No platform-level insolvency, exploit of the exchange itself, or extended outage found in 2026** (one HyperEVM outage — see 2.4).

**Regulatory contact points.** 2026-08-19: "HYPE Jumps 17% After Trump Backs CFTC Path for Hyperliquid in U.S." (Yahoo Finance); 2026-08-24: Hyperliquid Policy Center urges SEC/CFTC to harmonize perp rules (The Block); 2026-08-17: Wintermute CEO names US regulation as Hyperliquid's biggest long-term risk (CryptoRank); 2026-09-16: Payward (Kraken) plans permissioned Hyperliquid perps for US clients via Bitnomial (NewsCord). Net read: **constructive CFTC engagement, no enforcement action found**.

**Validator set.** No primary validator-count pull succeeded this cycle (info-API schema mismatch). Secondary: validators now deploy/settle real-world prediction markets (CoinMarketCap, 2026-05-26); "Who actually runs Hyperliquid? The governance audit" (Crypto News, 2026-07-27) — centralization debate alive. Watch item, not a graded finding.

**Verdict: B.** Deepest venue in the stack; risk is market-structure (oracle/liquidation incidents, HLP strategy losses), not platform solvency. Insurance fund size not independently pulled this cycle — gap noted.

### 2.4 HyperEVM ecosystem (Kinetiq / Euler / HyperSwap / Ramses / bridge) — Grade: **B−** cluster, **C−** for thin legs

**Bridge/network risk.** Hyperliquid Bridge TVL **$6.746B** (DefiLlama, 2026-10-20). **Incident:** HyperEVM **major service outage/disruption early April 2026** — "Hyperliquid's HyperEVM Faces Suspected Major Service Outage" (Binance Square, 2026-04-01) and "HyperEVM Outage Crisis: PeckShield Reports Major Service Disruption" (CryptoRank, 2026-04-02). No bridge exploit found. Ecosystem exploit: **Purrlend (HyperEVM lending) $1.5M exploit**, part of April 2026's "catastrophic DeFi security ledger" (Startup Fortune, 2026-04-25).

**Kinetiq (kHYPE) — healthy.** TVLs (DefiLlama, 2026-10-20): **kHYPE $841.0M**, kmHYPE $39.7M, Kinetiq Earn $36.3M, Kinetiq Launch $5.8M. **Rate state:** kHYPE staking APY **1.99%** current, 30d mean **2.02%** (DefiLlama yields, pool 9f25a954, retrieved 2026-10-20) — positive, low, stable. No incidents found. Trajectory: KNTQ token unveiled (The Defiant, 2025-10-22), traded at $130M valuation (The Defiant, 2025-11-28), Elysium L2 for Hyperliquid announced (Yahoo Finance, 2026-08-24).

**Euler V2 — thin on Hyperliquid.** Multichain TVL **$291.4M** across 16 chains, **but the Hyperliquid L1 deployment holds only ~$1.77M** (2026-10-20; history: $311k on 2026-02-04 → peak $4.28M on 2026-03-21) (DefiLlama protocol API). Utilization/rate data not publicly pulled — gap. Practical read: Euler-on-HyperEVM is a satellite, not a core venue.

**HyperSwap & Ramses V3 — DEX depth ~$10M scale.** HyperSwap V3 **$10.4M** + V2 $6.4M; Ramses CL V2 **$10.98M** (multi-chain) + Legacy V2 $1.07M; Ramses CL Arbitrum $129k (DefiLlama, 2026-10-20). Fine for kHYPE/WHYPE routing at small size; slippage risk scales quickly above ~5-figure notional.

**Verdict: B−** for the cluster (Kinetiq core solid, bridge enormous and intact), **C−** for Euler/HyperSwap/Ramses legs individually due to thin depth and the April 2026 outage history.

### 2.5 Backpack (Solana) — Grade: **B−**

**Standing/momentum.** BP token launched on Solana 2026-03-23 with 25% airdrop and "no insider allocation" (CoinDesk, 2026-03-23). On-chain IPO access launched (Yahoo Finance, 2026-03-04). Securities platform bridging traditional and tokenized stock trading (PR Newswire/The Block, 2026-06-02). **$1B daily trading volume 5 days after launching "Pre-Season"** (CoinMarketCap, 2026-10-09); NEAR listing (2026-10-06); tokenized-assets expansion incl. Brazil ETF, Cerebras, NEAR (Altcoin Buzz, 2026-10-07); BP at record high as Solana RWA market hit $33B (OneBullEx, 2026-09-26). CEO plans 10,000 tokenized stocks (Crypto News, 2026-09-26).

**Regulatory posture.** Former SEC Acting Chairman **Michael Piwowar** appointed to Backpack US board "amid push for crypto perps" (The Block, 2026-06-09); **Kyle Samani** (Multicoin Capital co-founder) to Backpack US board (GlobeNewswire, 2026-09-02). Clear US-market strategy.

**Incidents.** None found in news queries (2024–2026 window searched 2026-10-20). Custody model and insurance fund size not independently verified this cycle — gap. Volume spike is incentive-season-driven ("Pre-Season"); decay risk post-season.

**Verdict: B−.** Growth + credible US regulatory signaling + no adverse events; young-venue discount applies.

---

## 3. Risk ranking for a $35k go-live allocation (order + rationale)

| Rank | Venue | Implied role | Rationale |
|---|---|---|---|
| 1 | **Hyperliquid (HyperCore)** | USDC margin pool | Deepest, on-chain, no platform solvency events in 2025-26; constructive CFTC path (2026-08-19). Residual risks: oracle/liquidation incidents and HLP strategy drawdowns — do not route core margin through HLP. |
| 2 | **HyperEVM DeFi** | kHYPE staking yield, perp-adjacent legs | Kinetiq/kHYPE $841M + stable ~2% rate = lowest-risk DeFi leg. Euler ($1.77M on HL), HyperSwap ($10.4M), Ramses ($11.0M) are thin — cap any position at low 5-figures max, mind the April 2026 outage precedent. |
| 3 | **Backpack** | Optional secondary leg | Fast-growing, US regulatory push (Piwowar, Samani), no incidents found; but young venue, incentive-driven volume, custody/insurance unverified — medium size only. |
| 4 | **MEXC** | Spread legs (hedging side) | Liquidity is real and PoR is published monthly, but the wrongful-freeze pattern (2025-08 → 2026-09) is the single most probable way the engine loses money here. Working-capital-only balances, same-day sweeps, API keys without withdrawal permission. |
| 5 | **VOOI** | Orchestration/UI layer only | Grade D transparency (no entity, no license, no audit, unverified volume). Non-custodial per its own T&Cs, so capital should never rest "on VOOI" — the planned "~$25k VOOI deposit" must be confirmed to land in venue-native accounts (Hyperliquid/CEX), with VOOI holding nothing but keys-permissions. If that cannot be verified, route execution venue-direct. |

**Suggested framing:** treat the $35k as $25k margin + $10k spread-leg float; keep ≤$5k idle on MEXC at any moment; keep VOOI as a signed-instruction layer with API keys scoped to trade-only.

---

## 4. Hard data points (12, each with date + source)

1. **HYPE $80.08 / mcap $17.81B / 24h vol $689.6M** — CoinGecko API, retrieved 2026-10-20 — https://api.coingecko.com/api/v3/simple/price?ids=hyperliquid&vs_currencies=usd&include_market_cap=true
2. **HYPE daily closes: $52.10 low (2026-08-02), $96.63 max (2026-09-22), $87.78 (2026-10-07), 30d −14.2%** — DefiLlama coins chart, retrieved 2026-10-20 — https://coins.llama.fi/chart/coingecko:hyperliquid?start=1761500000&span=130&period=1d
3. **HLP TVL $178.2M, −28.4% over 90 days ($248.8M 2026-07-20 → $178.2M 2026-10-20)** — DefiLlama protocol history, retrieved 2026-10-20 — https://api.llama.fi/protocol/hyperliquid-hlp
4. **Hyperliquid Bridge TVL $6.746B** — DefiLlama, retrieved 2026-10-20 — https://api.llama.fi/protocols
5. **Kinetiq kHYPE TVL $841.0M; kHYPE APY 1.99% (30d mean 2.02%)** — DefiLlama protocol + yields API, retrieved 2026-10-20 — https://api.llama.fi/protocol/kinetiq-khype ; https://yields.llama.fi/pools
6. **Euler V2 total TVL $291.4M (16 chains) but Hyperliquid L1 deployment only $1.77M (peak $4.28M 2026-03-21)** — DefiLlama, retrieved 2026-10-20 — https://api.llama.fi/protocol/euler-v2
7. **HyperSwap V3 $10.4M / V2 $6.4M; Ramses CL V2 $10.98M** — DefiLlama, retrieved 2026-10-20 — https://api.llama.fi/protocols
8. **MEXC October 2026 PoR released; BTC reserve coverage 294%** — GlobeNewswire release 2026-10-16; TOKENPOST 2026-10-16 (via Google News RSS: https://news.google.com/rss/articles/CBMiWEFVX3lxTE9HNC02WlV1ZE1fV0pqblBPMDBJekwtbkRsa0EyaDVFYVBRNlBkYlhIWlVGZnRRNzFpRnRwWjZzbVB6Y1NweWhsX0ZwRzBacGtwVFBLTHRDMzM ) — September 2026 PoR BTC ratio 297%: markets.businessinsider.com, 2026-09-15 (RSS redirect: https://news.google.com/rss/articles/CBMigAJBVV95cUxOMmRPdFhDb19vNjVSSmllMlRoM25Yb0FuUE1OS3E0NFRCRXdPQzNaTWUwTGhGblpURU5ZSlRlVlIwLThwc2ZSNVhQaElNcllPcEVoa1I5YkxicVRoSHhDREE5Q0tMZlNHb0RYTnpaZWttQlFLXzQxWjFPM1R6ckh2RWJaRXFhOTlJcmtmUkxrZk9XdTJLdFA3NW1KTGFyc1l4dVVUNzR0NXZwOUNNb3RZWFc3QlczUklGb0VpUUpOck9zSTRHU09hTVA5N2FUazhvTmtTSnlSYjJtQlJpOG0zY0xjSF9JTGRWS0s1cl9sX3JwMFVuWXBKSTk1bDBo )
9. **MEXC apologizes for wrongfully freezing $3M ("White Whale")** — Cryptonews, 2025-11-01 (RSS redirect: https://news.google.com/rss/articles/CBMiqwFBVV95cUxPeVE2M0Raal9WN3hIZV9BXzNnRGpGSENMcXlaN0dRRC04MHdyNmFVRFNqWkZNV29CMDZqS1dBQW94OTRabEJtWkxXRk5NQi1kUXJsR0VUR1NPeTZQM0Nnc2hhaUxnMERnWGtYWU0taFY3Sk50T2NsbFdXLVp1OU1CYkU3MmhoNGJiT2paR2NYMGFqNTlrbVhkTGNXNTk3eEdVTDdzU25YTzNPeEE ) ; dispute revived 2026-01-07 (CryptoRank, RSS: https://news.google.com/rss/articles/CBMi… see rumour log)
10. **MEXC lists ANTHROPICUSDT USDT-M perpetual** — MEXC contract page headline, 2026-04-14 (RSS redirect: https://news.google.com/rss/articles/CBMi… see source list); OURA Pre-IPO Futures 2026-09-22 and POLYMARKET Pre-IPO Futures 2026-09-22 (MEXC blog via Google News RSS)
11. **Backpack reaches $1B daily volume 5 days after "Pre-Season" launch** — CoinMarketCap, 2026-10-09 (RSS redirect: https://news.google.com/rss/articles/CBMi… see source list); BP token launch 25% airdrop no-insider — CoinDesk, 2026-03-23
12. **VOOI self-declared unregulated + non-custodial T&Cs; zero audit mentions in full docs corpus** — vooi.io footer and https://vooi.io/terms&conditions (updated 2026-06-24); docs.vooi.io/llms-full.txt (226,887 bytes) scan, retrieved 2026-10-20

*(Note: items 9–11 carry Google News redirect IDs in the RSS payload; publication + date + headline are given so originals are one search away. API items 1–7 and 12 are primary URLs.)*

---

## 5. Rumor log (last ~90 days + carried context, with verdicts)

| # | Rumor / claim | First seen | Verdict |
|---|---|---|---|
| R1 | "MEXC has financial problems / solvency issues" | 2025-11-01 (Binance Square: "MEXC warned about speculation on rumors of the exchange's financial problems") | **Refuted-by-denial, no event since.** Exchange continued operating normally through Oct 2026; monthly PoR published. Substantively unverifiable — monitor. |
| R2 | "MEXC wrongfully freezes user funds (White Whale $3M)" | 2025-08-25 (TradingView), apology 2025-11-01 (Cryptonews), revived 2026-01-07 (CryptoRank) | **Confirmed** (MEXC publicly apologized for a wrongful freeze). Pattern extended by Sep 2026 account-drain complaints ($340k, 2026-09-28; API-key/freeze interaction, 2026-09-29). |
| R3 | "MEXC uses 'internal accounts' to absorb losses" | Context of R2 | **Unresolved.** No on-record article found in this cycle's searches using that term; treat as unverified allegation attached to the White Whale case. |
| R4 | "HLP running ~−50% 30d APR in early Oct 2026" | Orchestrator tracking, early Oct 2026 | **Unresolved.** No public APR feed for HLP found (absent from yields.llama.fi; Hyperliquid stats endpoint denied). Corroborating: HLP TVL −28.4%/90d (DefiLlama, 2026-10-20) and July 2026 oracle-anomaly losses. |
| R5 | "HYPE 3.5x'd to ~$89 around Oct 7" | Orchestrator tracking | **Partially confirmed.** $87.78 on 2026-10-07 verified (DefiLlama). No 3.5x within the last 130 days (max 1.9x from Aug low to Sep peak $96.63); the 3.5x must refer to an earlier 2026 run — unverified. |
| R6 | "Backpack $1B daily volume" | 2026-10-09 (CoinMarketCap) | **Confirmed as reported**; sustainability unproven (measured 5 days into an incentive "Pre-Season"). |
| R7 | "VOOI has $30B+ cumulative volume" | Self-reported (vooi.io homepage, retrieved 2026-10-20) | **Unverified.** No independent confirmation; DefiLlama shows $14.7k on-chain TVL for VOOI V1; Dune dashboard (dune.com/vooi/vooidash) is the designated verification path — next cycle. |
| R8 | "Hyperliquid ecosystem/bridge unsafe after incidents" | Various | **Refuted as stated, nuanced.** Platform solvency intact; incidents were user-level or market-structure (SK Hynix $57M liquidations 2026-07-28; $738.6k user drain 2026-09-09; JELLY meme $6.2M exploit 2026-10-11); bridge $6.75B TVL intact. HyperEVM had a genuine outage (2026-04-01/02). |

---

## 6. Watch items for next cycle (C005)

1. **MEXC November 2026 PoR** (cadence check ~mid-Nov) + any new freeze/withdrawal complaints; monitor whether the "internal accounts" allegation gets on-record coverage.
2. **HLP APR ground truth:** pull Hyperliquid's HLP stats via an authenticated source or Dune; reconcile against the −50% 30d APR claim; track whether HLP TVL stabilizes above $175M.
3. **Hyperliquid insurance fund size** — not obtained this cycle; pull from official docs/stats and log with date.
4. **HyperEVM stability:** any recurrence of the April 2026-style outage; bridge TVL trend vs $6.75B baseline.
5. **Kinetiq:** kHYPE APY trend (2% zone), Elysium L2 launch progress (announced 2026-08-24), any kHYPE redemption-queue friction.
6. **Euler-on-Hyperliquid utilization** — direct on-chain query of the $1.77M deployment; if still <$2M TVL, exclude Euler from go-live paths.
7. **HyperSwap/Ramses depth** post HYPE-volume cooldown (HYPE −14.2%/30d may thin LP incentives further).
8. **VOOI verification:** Dune (dune.com/vooi/vooidash) for real volume/OI; watch for any audit announcement or legal-entity disclosure; verify the exact custody path of the planned $25k deposit (which venue account actually holds it).
9. **Backpack:** BP token unlock schedule, volume decay post Pre-Season, custody/PoR disclosure.
10. **Regulatory:** SEC/CFTC harmonization progress for perps (The Block 2026-08-24 thread) — affects Backpack US perps push and any Hyperliquid US onboarding (Payward/Bitnomial, 2026-09-16); also MEXC pre-IPO perp products (ANTHROPICUSDT etc.) for sudden regulatory removal risk on the hedge leg.

---

## 7. Source list

**Primary / API (retrieved 2026-10-20 UTC):**
- https://api.coingecko.com/api/v3/simple/price?ids=hyperliquid&vs_currencies=usd&include_market_cap=true
- https://coins.llama.fi/chart/coingecko:hyperliquid?start=…&span=130&period=1d
- https://api.llama.fi/protocols ; https://api.llama.fi/protocol/hyperliquid-hlp ; https://api.llama.fi/protocol/euler-v2 ; https://api.llama.fi/protocol/kinetiq-khype
- https://yields.llama.fi/pools
- https://vooi.io/ (homepage incl. regulatory-status footer)
- https://vooi.io/terms&conditions (last updated 2026-06-24)
- https://docs.vooi.io/llms.txt ; https://docs.vooi.io/llms-full.txt (226,887 bytes) ; /vooi-introduction.md ; /vooi-ultra-v3/vooi_ultra-introduction.md ; /vooi-ultra-v3/ultra-operational-guidelines.md ; /vooi-tokenoverview.md

**Press / secondary (via Google News RSS, retrieved 2026-10-20; publication + date as listed):**
- MEXC October 2026 PoR — GlobeNewswire, 2026-10-16; BTC coverage 294% — TOKENPOST, 2026-10-16
- MEXC September 2026 PoR BTC 297% — markets.businessinsider.com, 2026-09-15; Guardian Fund +1,000 BTC — Yellow.com, 2026-10-19
- MEXC $2M campaign after $3M freeze — TradingView, 2025-08-25; MEXC apology — Cryptonews, 2025-11-01; solvency-rumor warning — Binance Square, 2025-11-01; exec speaks out — 99Bitcoins, 2025-11-02; dispute revival — CryptoRank, 2026-01-07; $340k account hack — Crypto News, 2026-09-28; API-key/freeze drain — CryptoTicker, 2026-09-29
- MEXC ANTHROPICUSDT futures — MEXC, 2026-04-14; MOONSHOTUSDT Pre-IPO futures — MEXC, 2026-08-12; OURA Pre-IPO — MEXC, 2026-09-22; POLYMARKET Pre-IPO — MEXC, 2026-09-22; Anthropic IPO content series — MEXC, 2026-09-14/15/16
- Hyperliquid: Trump backs CFTC path, HYPE +17% — Yahoo Finance, 2026-08-19; Policy Center SEC/CFTC letter — The Block, 2026-08-24; Wintermute CEO risk comment — CryptoRank, 2026-08-17; SK Hynix $57M oracle anomaly — BeInCrypto, 2026-07-28; $738,600 USDC drain — CryptoRank, 2026-09-09; JELLY meme $6.2M exploit + delisting — CoinMarketCap, 2026-10-11; Papertrade $1.28M manipulation — BigGo Finance, 2026-10-11; FreedomXMR/ZachXBT — Crypto News, 2026-10-20; Robinhood engineers charged — CoinDesk, 2026-09-16; governance audit — Crypto News, 2026-07-27; validators & prediction markets — CoinMarketCap, 2026-05-26; Payward/Bitnomial US perps — NewsCord, 2026-09-16
- Hyperliquid 2025 background: JELLYJELLY delisting — The Block/Yahoo Finance, 2025-03-26; POPCAT $5M bad debt — Yahoo Finance, 2025-11-13
- HyperEVM: suspected major outage — Binance Square, 2026-04-01; PeckShield disruption report — CryptoRank, 2026-04-02; Purrlend $1.5M exploit — Startup Fortune, 2026-04-25
- Kinetiq: KNTQ unveiled — The Defiant, 2025-10-22; $130M valuation — The Defiant, 2025-11-28; Elysium L2 — Yahoo Finance, 2026-08-24
- Backpack: BP token launch — CoinDesk, 2026-03-23; on-chain IPO access — Yahoo Finance, 2026-03-04; securities platform — PR Newswire/The Block, 2026-06-02; Piwowar to board — The Block, 2026-06-09; Samani to board — GlobeNewswire, 2026-09-02; $1B daily volume — CoinMarketCap, 2026-10-09; tokenized assets expansion — Altcoin Buzz, 2026-10-07; 10,000 tokenized stocks plan — Crypto News, 2026-09-26
- VOOI: Kraken listing — Kraken Blog, 2025-12-18; CMC price page — CoinMarketCap, 2025-10-31; ICO-era coverage — ICO Drops, 2024-03-05; CryptoRank, 2024-08-23

**Methodological notes:** (1) Sandbox clock read 2026-10-20 ~17:22 UTC during pulls vs task date 2026-10-21 — all retrieval dates given as pulled. (2) CoinGecko exchange-stat endpoints for MEXC/Backpack were rate-limited during the session; exchange rank/volume left as gaps rather than guessed. (3) Hyperliquid validator count could not be pulled from the info API this cycle (schema mismatch) — left as a watch item, not a finding.
