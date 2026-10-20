# Cycle 004 [P2-FEED] Deliverable — Tokenized-Equity Arability Map (v1, compact)

**Purpose:** direct pipeline artifact for Edge-Engine's TokenizedEquity / EquityPerpCrossVenue strategies. Defines which tokenized-equity symbols are arable (tradeable off-hours / on crypto venues) under the issuer-objection regime, and the data-integrity conditions for trusting cross-venue prices.

**Built from:** Cycle 003 verified objection map (as of 2026-10-20) + Cycle 004 Wave 1 findings [Q1]-[Q6].

---

## 1. Arability rule

A symbol is arable ONLY if all of the following hold:

1. **No issuer objection filed** on that symbol in the OKXICE operating notice process (and no SIFMA-driven opt-in amendment in force — if the SEC adopts opt-in, EVERY symbol requires affirmative consent before trading).
2. The symbol survived the pre-launch removals (17 of the original 63 symbols were removed before venue launch).
3. The venue's market for it is live (not delisted/frozen — beware Hyperliquid zombie prints).
4. Unit conventions are normalized across venues before any spread computation.

## 2. Known NON-arable set (objection-confirmed, 16 as of Oct 20; any >20 triggers the Card 6 kill threshold)

Objection-verified nine (Oct 4–15 wave): Cerebras, AppLovin, Applied Digital, Rocket Lab, CoreWeave, Verizon, Applied Optoelectronics, Broadcom, UnitedHealth.
Wave-2 additions (Oct 15–19): Microsoft, Alphabet, Goldman Sachs, Qualcomm, Caterpillar, McDonald's, Western Digital.
Plus: **Nasdaq opted out its own shares** (self-exclusion).

## 3. Confirmed-live core (crypto-native issuers — notably silent in the objection process)

Coinbase (COIN), Robinhood (HOOD), Circle (CRCL), Securitize (SECZ) — un-objected as of Oct 20 and structurally motivated to stay in (they are the tokenization stack). Four mega-cap holdouts remain un-objected but likely still processing: JPM, WMT, COST, LLY — **their ~Nov 3–8 window expiries are the next verdict dates** (calendar.md).

## 4. Data-integrity conditions (from [Q2], Grade A — non-negotiable before go-live)

1. **Unit normalization table per venue:** assumed share counts and quanto multipliers differ wildly (live example, 2026-10-21: Gate lists the same company as KIMI $7.78 and MOONSHOT $65.45 — an 8.4× unit gap; MEXC KIMISTOCK $65.72 matches the MOONSHOT scale). Naive ticker matching fabricates spreads.
2. **Exclude delisted-but-frozen markets** (Hyperliquid vntl, io:MOONSHOT still print zombie marks).
3. **Re-derive the spread series with normalized units** before trusting any persistence statistic (the internal "10.95% MEXC→Gate" is not reproducible; "MEXC→Robinhood ≈4.7%" is confirmed at ~2.5–5.0% depending on name).
4. **OI figures from the internal baseline are off by ~3 orders of magnitude** ($34B/$18B claimed vs $6.0M/$8.1M actual on Robinhood). Sizing on internal OI = sizing on fiction.
5. **"Shared margin pool" holds only within Hyperliquid HIP-3 legs** — never assume cross-venue margin netting.

## 5. Forcing-event overlay (Weeks away)

**Anthropic S-1 filed 2026-06-01; Nasdaq target November 2026.** Expect conversion mechanics per venue (SpaceX precedent: Binance 30-day-notice index conversion; Gate delist; Kraken xStocks conversion; HL continuation). MEXC's ANTHROPICUSDT settlement terms are undocumented — treat all ANTHROPIC perp positions as event-risk positions until terms are verified. Issuer-nullification precedent (Anthropic/OpenAI May 2026 warnings; Forge/Hiive callouts) means pre-IPO "underlyings" can be legally impaired independent of price.

## 6. Open items (→ Wave 1b / C005)

- Pull the full current 63-symbol OKXICE notice table + live objection status (this map carries the named-objector subset only).
- Objection-window expiry verdicts ~Nov 3–8 (JPM/WMT/COST/LLY).
- SIFMA opt-in amendment outcome (would hard-reset arability to opt-in-consent-only).
- Build the full venue × symbol unit-normalization table (MEXC/Gate/HL/Lighter/Robinhood).
