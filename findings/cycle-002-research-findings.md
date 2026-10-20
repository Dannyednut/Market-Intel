# Market Intel — Cycle 002 Research Findings (Wave 1)

Date: 2026-10-20 | Method: 4 parallel research agents (verification+watchlist, EM off-ramp deep-dive, yield-routing deep-dive [pending], fresh 7-day scan) | Evidence base: builds on [cycle-001-research-findings.md](cycle-001-research-findings.md) (42 findings).

Tag conventions this cycle: verifications ref [E7]/[C8]/[F14]; fresh findings [D1]-[D12]; missed-in-001 candidates [M1]-[M5]; watchlist markers W1-W6 (from cycle-001-analysis.md).

---

# AGENT 2-a — Verification & Watchlist Report

Method: 35+ web searches, 25+ page fetches, primary-source pulls (DefiLlama API, rwa.xyz, GlobeNewswire/Figure, CoinMarketCap Research, Citi briefing coverage).

## Part 1 — Verifications

### [E7] Binance TradFi perps — $433B Aug notional, ~15x Jan → **VERDICT: CONFIRMED** (HIGH on figure as Binance-reported; MED on economic substance)
- Binance self-reported **~$433.4B TradFi perpetual volume in August, ≈15x the $29.5B in January** — carried verbatim by The Crypto Basic (Sep 1) and TechStock² (Sep 1), sourced to Binance alongside the US stock-options launch.
- **Notional DOES include FX/commodity perps**: equity-linked = $342.9B in Aug (79%; up from $410.9M in Jan) — ~21% (~$90B/mo) is FX + commodities.
- Independent cross-checks: WuBlockchain — **all-CEX stock perps $665.42B in Aug, 56x January's $11.58B** (SNDK $193.6B + SK Hynix $75.9B + SPCX $65.9B = 50.4% concentration); Bloomberg-reported $778B stock+commodity Aug = **23.48% of all perp volume vs 0.5% in Nov 2025**; CoinMarketCap Research (19 venues): **August record $799.5B**, $3.16T cumulative, Binance = 50.4% of window, CEX share 87%.
- **Stickiness test**: Sept RWA perps posted **first monthly decline since April** (CoinDesk Sept review; spot +27.3% to $1.13T); but **open interest hit $5.78B** (CryptoRank, Oct 2); DEX RWA perps weekly volume +75% since August (KuCoin, Oct 16); Binance kept expanding (5 new TradFi contracts Sep 29; 24/7 USD/BRL FX perps at 100x).
- Caveats: self-reported notional is leverage-inflated; extreme single-theme concentration (memory chips); Aug 18 equity-oracle failure caused $57M liquidations/960 accounts; trackers disagree (CryptoRank narrower series: Aug −13.5% to $122B).
- **Impact**: I3's flashpoint is real — the book is verified at category scale ($3T+/8mo, 23% of all perp volume) and sticky-then-cooling; the "regulatory action vs offshore single-stock perps within 6-12 months" clock keeps running; P5 unchanged.

### [C8] Citi "Custody+" → **VERDICT: CONFIRMED** (HIGH; go-live still pending)
- Primary: **Citi press release, Business Wire, Aug 18, 2026** — "Citi Unveils Custody+: A Suite of Near- and Real-time Custody Solutions to Meet Always-On Industry Demand."
- Markets Media (Aug 18) on-record briefing: **digital asset custody goes live "this year, starting with bitcoin"**; one platform for traditional + crypto custody; ~5 yrs build; execs Chris Cox & Amit Agarwal named. Corroborated by The Block and CoinDesk (Aug 18).
- Q3 earnings (Oct 12-13): Fraser pushing **tokenized deposits over stablecoins** for enterprises (PYMNTS Oct 13) + Citi-Coinbase stablecoin checkout for merchants (Stock Titan Sep 28; The Defiant Oct 12).
- **BNY comparator**: BNY Belgian entity on ESMA MiCA register since July 2026; **expanded EU digital-asset custody platform Oct 8-13** (Ledger Insights).
- Residual: Custody+ is a modular post-trade suite; crypto module announced, not yet live; fees undisclosed.
- **Impact**: U3 resolved; G-SIB custody commoditization scheduled 2026 → P5/P6 pace-setter intact.

### [F14] Stablecoin remittances ~1% vs 6.36% traditional → **VERDICT: PARTIAL** (HIGH that claim exists as vendor-reported; MED that comparison is economically valid)
- Borderless.xyz Q3 2026 report (Oct 16-19, multi-covered): median 1% ($2 per $200) vs World Bank global average 6.36%; **SSA 2.9% vs 8.46%; LatAm 1.25% vs 5.64%**; $10k business transfer $26-52 vs $135-150 bank wire.
- **Methodological flaw (key)**: 6.36% is WB average for Q3 2025; Borderless 1% is median for Q3 2026 — different stats, periods. WB's own **digital-only MTO index was 3.54%**, digital remittance index 4.59% — the honest benchmark. Banks average 14.99%.
- **Bank of Italy rebuttal confirmed multi-source**: 200 USDC transfers across 10 corridors; stablecoins "aren't necessarily cheaper" end-to-end (ramps/cash-out dominate).
- No new World Bank RPW release found (latest cited remains Q3'25 = 6.36%). No dLocal×WU unit economics disclosed; WU×dLocal Cameroon payouts went live Oct 15.
- **Impact**: U1 unresolved but sharpened — size MTO-margin erosion off ~1% vs ~3.5-4.6% (55-70% gap), not vs 6.36% → thesis stands, magnitudes tempered.

## Part 2 — Watchlist status

| Marker | Status | Evidence + date | Implication |
|---|---|---|---|
| **W1 Stablecoin supply / Tether / Fed / consortium** | **MOVED↑** (partly) | Aggregate **$306.8B** (Oct 20) vs $300.9B Oct 1 (+2.0%); USDT $183.0B stabilized; USDC $72.3B (+$1.6B); RLUSD $2.40B; USDG $3.07B (DefiLlama). Fed: hold ~83-86% for Oct 27-28; **hike odds 14-17%**; minutes signal another hike eventually. **Qivalis (37 European banks, 15 countries) won DNB EMI licence Oct 14** for euro stablecoin. SC pushed $2T forecast to 2030. | Supply recovering **despite** hawkish hold — P1 contraction symptom not worsening; falsifier (reclaim $321B within 2 qtrs of a *pause*) untriggered (no pause). EUR-side bank consortium ahead of US one. |
| **W2 Regulator touch on APY / offshore perps** | **NO MOVEMENT** (enforcement) / NEW DATA (product) | OKX Money app launched Oct 6 with **10% APY USDG** for EM (yield sourced off-app); **Kalshi got CFTC approval for US equities perps Oct 6** (onshoring route); Coinbase filed SEC (Sep 3) + CFTC (Sep 18) for single-stock perps. Oct 12: brand yield called "next regulatory flashpoint". **Zero enforcement/guidance found.** | I1/I3 falsifier windows intact; onshore approvals (Kalshi) may *displace* enforcement as the weapon. |
| **W3 EM operator filings** | **MOVED** (IPO timeline) | OPay F-1: revenue +137% to $467M H1'26, NI +300% to $91M, lending top income; **NYSE pricing expected mid-November**; Stanbic up to $200M. MNT-Halan: EGP 7.84bn IPO, **order book closed Oct 14 = biggest EGX order book in years**. CBN digital-asset sandbox open. Egypt FRA freeze persists. | P7/I2 on track: credit-led growth goes public at cycle peak in ~4 weeks; H1'27 filings remain the checkpoint. |
| **W4 Tokenized private credit** | **NEW DATA** (category up, concentration intact) | **Tokenized Private Credit $24.82B** (Oct 16-17) vs ~$18-19B baseline → +~30%. Figure: Q3 prelim marketplace volume **$5.119B (+20% q/q)**, ~$30B cumulative home equity, AAA securitizations (S&P+Moody's); no delinquency/warehouse stress disclosed. Second source: **still no non-Figure issuer >$2B** (Tradable→Stellar "up to $1B"; Animoca NUVA Oct 8). rwa.xyz credit class $8.16B distributed / $37.79B represented (taxonomy change). | P4 defusal condition NOT met; no stress event → I4 clock paused but concentration worsened. |
| **W5 African seed funding H2'26** | **NEW DATA** (mixed) | Q3 2026: **58 startups raised $583M** (Disrupt Africa, Oct 5); equity funding **$797M = 4-year high**; 9M total $2.49B "Q3 rebounds" (TechCabal). Mega-deal-led. | Dollar recovery is mega-deal-led; 58 deals/quarter ≠ seed rebound — I5 falsifier (+30% seed counts) not triggered; P3 intact. |
| **W6 Exchange structure events** | **MOVED** (2+ resolving toward regulated venues) | ① **OKXICE filed with SEC Oct 5**; then **9+ issuers (Microsoft, Alphabet, Goldman, Qualcomm, Caterpillar, McDonald's, Western Digital, Broadcom, CoreWeave…) filed objections Oct 15-19**. ② Binance: EU service halt since Jul 1; DOJ compliance probe (Bloomberg Oct 9). ③ Kraken–Saldo advancing ("first crypto firm to buy a European bank", FT/Fortune Oct 14). ④ Coinbase single-stock perps: CFTC "standstill" — Kalshi approved first. ⑤ Nasdaq-Kraken: **"issuer-first tokenized equity gateway" launched Oct 15**. | P5 confirmed direction; NEW friction = issuer objections slowing tokenized-equity venue launch (caps how fast P6 fee compression propagates into equities). |

## Part 3 — New events not in Cycle 001
1. **Oct 14 — Qivalis (37 European banks) granted DNB EMI licence** for MiCA-compliant euro stablecoin. EUR-side bank-consortium rails materializing faster than US 21-bank USD venture. (HIGH)
2. **Oct 15-19 — Nine+ issuers object to tokenized listings on OKXICE** under SEC TSV issuer-objection rights. First real test of E1's issuer-objection mechanism; launch friction + moat for licensed listings. (HIGH)
3. **Oct 6 — Kalshi receives CFTC approval for US equities perpetual futures.** Onshore single-stock perps beat Coinbase to market; SEC/CFTC answer is approval, not (yet) enforcement → partially de-fuses I3. (HIGH)
4. **Oct 6-7 — OKX launches OKX Money app with 10% APY USDG** in EM. Escalates exchange-paid-APY loophole to scaled retail product; W2 trigger now live. (MED)
5. **Oct 5 — OKXICE files with SEC** for 24/7 tokenized US stock venue (63 symbols, permissioned AMMs). SEC decision = highest-leverage watch item in W6. (HIGH)
6. **Oct 13-15 — Philippines BSP moves on Coins.ph** (inbound rails restricted over offshore-gambling ties; licence reportedly at risk). BSP policing crypto rails. (MED)
7. **Oct 16 — Circle to push USDC into 40 new (mostly developing) markets** (Reuters). Confirms off-ramp race — flow-monetization pivot F2 foreshadowed. (MED)
8. **Oct 15 — Western Union × dLocal Cameroon wallet payouts live** (Nigeria next). F12 moved from announcement to production. (MED)
9. **Oct 13 — CoinDesk Sept Exchange Review: RWA perps first monthly decline since April; spot +27.3% to $1.13T.** First quantitative check on E7 stickiness. (HIGH)
10. **Oct 16-19 — Borderless Q3'26 stablecoin-remittance report resurfaces multi-outlet.** U1's "next release" arrived; median-vs-average caveat now explicit. (MED)
11. **Oct 19-20 — Perp-venue stress flash: $33M "AI perps" flash crash; BTC ~$83k after KOSPI −5.5%.** Second stress test of equity-linked perp plumbing within a quarter. (MED)
12. **Oct 13 — Sberbank added to Bank of Russia crypto-exchange register**, planning Dec 1 trading launch. State-bank entry in a G20 economy. (MED)
13. **Oct 15 — Standard Chartered pushes $2T stablecoin forecast to 2030**; SEC GENIUS comment window closes Oct 20. (MED)

---

# AGENT 2-b — EM Off-Ramp Unit Economics (Deep-Dive)

Method: ~48 web searches + direct fetches of live rate pages (Monierate, CBN/NIBSS, BSP fee schedule, Tazapay pricing, World Bank RPW), captured Oct 19-20, 2026. Confidence: H = 2+ quality sources/primary; M = strong single source; L = estimate.

Reference rates (Oct 19-20): NGN official NFEM ≈ ₦1,333.5/USD (CBN); parallel ≈ ₦1,380-1,390; GHS interbank 11.6650-11.6708 (BoG); KES mid ~129.9. Live USDT: Quidax USDT/NGN 1,362.86, Bitnob 1,369.32, Monierate aggregate 1,361.34; Quidax USDT/GHS 12.09; USDT/KES 129.6-132.1.

## Unit economics table

| Corridor / segment | Gross spread (bps) | Direct costs (bps) | Net take (bps) | Volume potential | Evidence |
|---|---|---|---|---|---|
| **Stablecoin — Nigeria B2B/API off-ramp** ($1k+) | **80-150** | 20-35: NIP payout ₦2 wholesale/₦10-50 retail cap; TRC20 ~$1; screening 2-5bps; mule/fraud provision 5-15bps | **45-115** | Nigeria ≈ $92B onchain inflows Jul'24-Jun'25; formal B2B slice 10-20% | M-H |
| **Stablecoin — Nigeria retail/OTC** ($200) | **200-270** (Quidax/Bitnob +2.2-2.7% over official) | 55-80 | **120-215** | Nigeria $59B crypto inflows Jul'23-Jun'24 (IMF) | M-H |
| **Stablecoin — Ghana (GHS)** | **150-350** (USDT/GHS 12.09 = **+3.55%** over BoG interbank — widest premium) | 30-100 (MoMo payout + cash-out) | **100-280** | Ghana remittances ~$6.5B+/yr; mobile-money receive cheapest globally (5.29%) | M |
| **Stablecoin — Kenya (KES)** | **30-120** (premium only 0-1.7%) | 15-45 (M-Pesa B2B KES 10-40/txn) | **10-90** | Constrained: **Partna KES M-Pesa corridor paused since 2026-05-07, "no other live KES M-Pesa route"** | M |
| **Traditional MTO — US→Nigeria** | total cost ~2.5-3.5%; corridor FX margin **−0.22%** (fee-driven) | embedded | MTO net ≈ 150-300bps embedded | Nigeria remittances ~$20B/yr formal | M-H |
| **Traditional MTO — US→Ghana** | total ~5-8% (SSA $200 avg 7.9-8.78%); **WU retail FX margin alone = 7.62%** (Oct 20 live quote) | — | MTO take far above stablecoin net | — | H on WU quote |
| **Traditional MTO — US→Kenya** | total ~3-6%; WU FX margin 1.10% | — | — | — | M-H |

**Arbitrage read:** stablecoin net 10-280bps vs MTO gross 250-800bps → **150-600bps of disintermediation margin per unit**, part kept, part passed to sender. LemFi's zero-fee + FX-spread model is the incumbent-adjustment case.

## The 60-100bps verdict

**CONFIRMED (gross) — PARTIAL (net & durability).**
1. **"Collect on free national rails, zero MDR" — HOLDS.** NIP wholesale ₦2/txn; 2026 framework: ≤₦5,000 free, caps ₦10/₦50 above; NIBSS CEO explicitly pushing zero fees in PSV 2028. **Exception:** Kenya M-Pesa merchant till collect costs up to 0.55% (capped KES 200) — free-rail assumption fails for Kenyan till collect.
2. **"Earn 60-100bps FX spread" — market clears HIGHER.** Retail platforms quote +2.2-2.7% over official; wholesale/retail ladder leaves **80-150bps gross at B2B**, 200-270bps at retail. Tazapay publicly charges **0.8-2.5% FX**; dLocal clears **2.68%** blended take on $40.8B TPV. 60-100bps is a conservative defensible wholesale price point, not a ceiling.
3. **But the spread is a policy artifact.** USDT/NGN premium is the official-parallel wedge in disguise (USDT ₦1,361 sits between official ₦1,333 and parallel ₦1,375-1,390). As FX windows converge, the pool compresses; premiums thinnest where FX most liberalized (Kenya 0-1.7%).
4. **Net verdict:** gross 60-100bps ✅ (realized 80-150bps B2B); net after 25-80bps costs = **40-220bps**; durability ⚠️ — premium compression + payout-rail de-platforming are the two ways it goes to zero.

## Margin pool map

| Pool | Size/mechanics | Evidence |
|---|---|---|
| **1. Retail FX spread (biggest)** | 150-350bps; Ghana widest (+3.55%), Nigeria +2.2-2.7%, Kenya thinnest | Live quotes, H |
| **2. Naira float yield (most under-modeled)** | NGN idle float earns **16.84%** (364-day T-bill stop, Oct 14) → ~4.6bps/day of prefunding; 10-day collection cycle adds ~46bps on top of FX | H |
| **3. Compliance/licence rents** | CBN sandbox Cohort 2.0 (apps Aug 12-31) with dedicated stablecoin track; IMTO ₦10M + $1M capital; PSSP ₦100M. Rents eroding: **Kenya-Rwanda PSP licence-passporting MoU** (Mar 13, 2026) spanning Rwanda, Ghana, Kenya | H |
| **4. Last-mile toll (dLocal×WU model)** | Selling payout rails to disruptors; Cameroon live Oct 15, Nigeria next; dLocal blended 2.68% proves owned-rail tolls clear >100bps | H |
| **5. Payout-leg fees** | Near-zero in Nigeria (₦2); real only in Kenya M-Pesa B2C | M-H |

## Risk updates

1. **Fee-cap risk — template escalated from caps to ZERO.** BSP made **P2P InstaPay transfers FREE effective Aug 15, 2026** (beyond the P1.50 cap Cycle 001 cited). EAC masterplan proposes interchange caps for cross-border mobile money; NIBSS lobbying zero NIP fees. **Reframed:** the binding risk is **FX-spread transparency regulation** — IMF publicly urged Nigeria to act on stablecoin cross-border flows (Jun 16, 2026). A mandated "official-rate + small fee" disclosure rule would legislate away pool #1.
2. **Capital-control risk — symmetric.** Nigeria official-parallel gap now ~3-4%; Ghana +3.55% premium signals residual friction. Controls → windfall spreads; liberalization → pool collapse. Nigeria posture sandbox-first, not prohibition.
3. **Structural risk Cycle 001 missed: the last mile can de-platform you.** Partna KES M-Pesa corridor paused since May 7, 2026, no alternative live route. Banks/MNOs building own corridors (Visa+M-PESA+Onafriq DRC stablecoin pilot Jul 6; Standard Bank only African bank in 21-bank consortium; Absa stablecoin treasury playbooks). **Without an owned or contractually exclusive payout leg, 60-100bps is a revocable license granted by an MNO/bank incentivized to internalize it.** Secondary miss: licence-passporting erodes the licence-rent layer.

## New facts (verified this cycle)
1. **BSP InstaPay P2P free effective Aug 15, 2026** — escalation beyond cap. (H)
2. **CBN Sandbox Cohort 2.0 (apps Aug 12-31, 2026) has a dedicated stablecoin track** (on/off-ramps, custody, wallets, token issuance). (H)
3. **NIP wholesale cost ₦2/txn; 2026 fee framework free ≤₦5k, ₦10/₦50 caps above.** (H)
4. **dLocal 2025: TPV $40.8B, revenue $1.09B, take rate 2.68%** (from 2.92% in 2024). (H)
5. **Tazapay public pricing 0.8-2.5% standard FX** — the real take of the network Circle bought for $400M (close expected 2027, pending MAS). (H)
6. **Live USDT premiums (Oct 19-20): Nigeria +2.2-2.7%, Ghana +3.55%, Kenya 0-1.7%.** (H)
7. **Kenya M-Pesa stablecoin corridor paused** (Partna, since 2026-05-07, no alternative). (M)
8. **Visa + M-PESA Africa + Onafriq stablecoin pilot in DR Congo** (Jul 6, 2026). (H)
9. **Nigeria 364-day T-bill stop rate 16.84%** (Oct 14) — the NGN float-yield pool. (H)
10. **SSA took $205B+ onchain Jul'24-Jun'25 (+52% y/y), Nigeria $92B; global cross-border stablecoin value +77.5% to ~$220B (Chainalysis); Africa cross-border payments $329B (2025) → $1T (2035F).** (M-H)
11. **Kenya-Rwanda PSP licence-passporting MoU** (Mar 13, 2026, spanning Rwanda/Ghana/Kenya). (H)
12. **Onafriq's Baxi wind-down confirmed; agents transitioned to another principal bank — distress assets being transitioned, not sold** (weakens the "cheap agent-network acquisition" arm). (H)

**Handoff:** (a) re-weight whitespace #1 from "licence rents + last-mile ownership" to "float yield + owned payout leg + premium-duration"; (b) watchlist fee-cap item should track FX-spread disclosure rules, not transfer fees; (c) Kenya = weakest corridor hypothesis; Ghana = premium-protection candidate; (d) verify Ghana cost stack + e-levy next pass (L-confidence).

---

# AGENT 2-c — Yield-Routing Unit Economics (Deep-Dive)

Method: 10-14 targeted searches (retry after timeout; efficient mode). Product data from eco.com, rwa.xyz, ondo.finance, superstate.com, wisdomtree.com, issuer PRs.

## Product economics table

| Product | AUM (latest) | Holder fee | Distributor fee | Yield source | EM access |
|---|---|---|---|---|---|
| **BlackRock BUIDL** | $2.25B (10/6/26) | 0.20% (0.20-0.50% range) | Embedded in Securitize platform fee — not separately published | T-bills/repo; 7-day APY 3.68% | QP only, $5M min — institutional, no EM retail |
| **Ondo USDY** | ~$2.1B (9/16/26) | ~0.35% (not surfaced) | None published; Ondo sells direct + via partners | Short Treasuries; ~3.4% APY | **Best**: Reg S, non-US retail eligible — the EM vehicle |
| **Ondo OUSG** | ~$396-650M (MED) | 0.15%, **waived to 0% until 1/1/2027** | None published | BUIDL-backed short Treasuries | $5K min instant mint; retail |
| **Franklin BENJI (FOBXX)** | Not surfaced | **0.15% — category floor** | None published; 5-yr Benji platform distribution | US Govt MMF, $1.00 NAV | Retail minimums; UCITS clone (Luxembourg) |
| **WisdomTree WTGXX** | Not surfaced | **0.25% expense ratio, $1 min** | None published | Govt MMF distributions | Retail, digital-first |
| **Superstate USTB → Invesco** | $824M, 3.60% 30-day yield (10/15/26) | **≤0.15%** | None published | Short-duration US Govt (Invesco-advised since 3/24/26) | QP only, $100K min — institutional |

**What bps exists for a router?** The observed fee pool is 15-50bps and it belongs to the issuer/manager; **no product surfaced a published distributor carve-out**. A router's 25-50bps must be (a) negotiated revenue-share from the issuer (Securitize-style, unpriced publicly), or (b) a self-charged access/redemption service fee. Fee compression is real: OUSG at 0%, BENJI/USTB ≤0.15%. Consumer distribution margins ~zero — OKX's baseline USDG rate (3.5-3.85% APY) ≈ the 3.60-3.68% underlying yield. **Conclusion: the 25-50bps placement fee is an engineering assumption, not an observed market price. Confidence: MED-LOW.**

## The 25-50bps verdict — **PARTIAL**

Revenue on $100M EM stablecoin float: 25bps = $250k/yr; 35bps = $350k; 50bps = $500k.
Realistic cost stack (2 jurisdictions, one market cluster): securities counsel/compliance $150-250k; qualified custody $50-100k; KYC/AML + redemption/liquidity ops $100-150k; engineering/infra $150-200k → **$400-700k/yr** (Card 3 assumed $400k — the low end).
Break-even AUM: **$80M** (50bps, lean stack) → **$157M** (35bps, $550k) → **$280M** (25bps, full stack). Cycle 001's "~$120M at 35bps" is **10-30% optimistic**; realistic break-even **$150-250M AUM**.
The model clears only with the FX leg: 40-80bps on local↔USD conversion. If $100M of exporter/freelancer float turns ~6x/yr, $600M turnover × 50bps ≈ **$3M/yr — 6-12x the placement fee**. **Turnover velocity, not AUM, is the actual unit driver; pure idle-treasury routing is sub-scale below ~$250M. Verdict: PARTIAL — economics clear only as an FX-and-turnover business with placement fees as a thin rider.**

## Regulatory clock

- **NPRM status CONFIRMED**: Treasury GENIUS NPRM published Federal Register **Aug 18, 2026; comments closed Oct 19, 2026** (FR 2026-16796). **Effective date: Jan 18, 2027** (or 120 days after final rules, whichever earlier).
- **Scope**: GENIUS §4(a)(11) bans **issuers** paying yield. Latham & Watkins: statute "does not explicitly prohibit" non-issuer distribution. But BPI/ABA actively lobbying to close the "loophole"; bank letters now in the NPRM record.
- **Probability ban extends to distributors/affiliates: MED (~40-50%)**. Path: Treasury interpretation of "offer and sale" in the final rule, or the stalled market-structure bill. Watch the final rule expected before 1/18/2027.
- **OKX USDG 10% APY: still live** (Cointelegraph 10/5, CoinDesk 10/6). No US regulator response surfaced; USDG is Paxos-issued under MAS oversight sold to non-US users — a jurisdictional gap; the 10% headline (vs ~3.6% underlying) is **subsidized acquisition spend**, i.e., the category's regulatory-tail poison and an unmatchable benchmark (a compliant router loses money matching it).

## EM demand evidence

- **Nigeria**: IMF (6/16/26) — ~$59B crypto inflows Jul'23-Jun'24, #2 globally on Chainalysis 2024; "savers prefer a dollar stablecoin wallet to a naira savings account" (IMF Jun '26); 62% of Nigerians spend stablecoins on everyday expenses; cNGN live with 1:1 naira reserves. Demand = store-of-value, not yield — fits the router thesis.
- **Ghana (headwind)**: cedi appreciated 40.7% in 2025, softening SoV demand; BoG FSR warns stablecoins "reduce demand for the Ghana Cedi"; BoG+SEC joint **Public Notice on Unauthorised Advertising of Virtual Asset and Stablecoin Products** — direct regulatory risk to advertised-yield distribution; cedi under renewed pressure in 2026 (demand episodic/FX-driven).
- Binance Research: three demand profiles — SoV vs instability/capital controls, yield-driven Earn, payments. Tokenized Treasuries ~$15.65B (9/16/26).

## Bank crowd-out

- **JPM Coin (JPMD) live on Ethereum public chain** (11/12/25), expansion reported **Oct 18, 2026** — first bank USD deposit token on a public blockchain. JPM AM launched GSIB-first tokenized MMF 12/15/25.
- **The Clearing House + 12+ owner banks** building a shared tokenized-deposit network targeting H1 2027; tokenized deposits **may legally pay yield** as bank liabilities.
- **Assessment**: crowd-out risk **MED-HIGH at the institutional tier** (JPMD + TCH network reach exactly the fintech-treasury segment) but **LOW-MED at the EM retail/exporter tier** near-term — bank rails won't reach unbanked Nigerian exporters. Router must anchor where banks can't serve.

## New facts

1. **GENIUS NPRM comment window closed Oct 19, 2026** — kill-trigger clock now runs to the final rule. (H)
2. **GENIUS effective Jan 18, 2027** or 120d post-final-rule. (H)
3. **OKX Money 10% APY USDG still live** in EM, no regulator response; 10% >> 3.6% underlying = subsidy. (H)
4. **Invesco absorbed Superstate's USTB** (~$900M, 3/24/26); now $824M at ≤0.15% — TradFi consolidating the wrapper layer. (MED-HIGH)
5. **OUSG fee waived to 0% until 1/1/2027** — issuer-side fee compression squeezes any distributor rev-share. (H)
6. **BUIDL $2.25B / 0.20% / 3.68% 7-day yield** (10/6/26). (H)
7. **JPM Coin on Ethereum expansion (Oct 18, 2026) + TCH 12+-bank tokenized-deposit network H1 2027** — banks can legally yield. (H/M)
8. **Ghana BoG+SEC notice vs unauthorised stablecoin-product advertising** — EM distribution-regulation precedent against advertised yield. (MED)

**Bottom line for Card 3**: keep the construct, re-anchor the model on FX/turnover economics (placement bps are unpriced and compressing), size break-even at $150-250M, treat the Treasury final rule (pre-1/18/2027) as the single monitored kill-trigger — with Ghana-style advertising bans as the EM-tier analog to watch.

---

# AGENT 2-d — Fresh Signal Scan (Oct 13-20, 2026)

Method: ~38 searches (Google News RSS + Bing News RSS + browser fetches) across 7 sweep segments; multi-outlet drills on ~18 candidates. All items below are NOT in the Cycle 001 findings bank.

## Fresh findings (12, ranked by signal strength)

**[D1] Nine issuers formally object to tokenized-share trading on OKXICE** | Oct 16-19 | Broadcom, Verizon, UnitedHealth, CoreWeave (plus Microsoft, Alphabet, Goldman per Ledger Insights) refused tokenized trading of their shares on the OKX-ICE venue via the SEC Innovation Exemption's issuer-objection right; WSJ: "Corporate America Is Balking at Tokenized Stocks." Of 63 filed symbols, the mega-cap core is thinning before launch. | Moat for tokenized equities is issuer **content licensing**, not venue tech; favors venues that sign issuers first (Nasdaq-Payward, LSE-Kraken). | theblock.co/news/markets/2026-10-17-coreweave-broadcom-verizon-among-nine-companies-objecting-to-tokenized-trading-of-their-shares-on-okxice-418859 · ledgerinsights.com/microsoft-alphabet-goldman-object-tokenized-stocks-okxice/ | **HIGH**

**[D2] GENIUS Act compliance stack locks in: comment window closed, 91 days to effective date** | Oct 15-20 | Treasury/OCC NPRM comment period closed Oct 19-20; effective ~mid-Jan 2027. OCC final stablecoin-issuer rule lands **before end-October**; OCC hired Metrika for GENIUS supervisory tech (Oct 14); Blockchain Association filed for DeFi/foreign-issuer clarity (Oct 20). | Confirms P1's hard clock — yield ban + bank-side compliance stack now date-certain. | forkast.news/tuesdays-sec-comment-deadline-closes-the-last-public-window-before-the-genius-act-compliance-stack-locks-in/ · ainvest.com "91 days" · globenewswire.com Metrika-occ | **HIGH**

**[D3] Stablecoin divergence: payments volume +45% to ~$482B while float stagnates** | Oct 14-19 | CoinDesk Research (Oct 18): Q1-Q3 2026 stablecoin payment volume +45% to ~$482B even as supply growth stalled; driver = Visa/Mastercard/Stripe connecting stablecoins to cards/cash. Standard Chartered pushed $2T supply forecast to 2030. Hot Sept CPI (Oct 13) revived October Fed **hike** bets; crypto IPO equities sold off. CoinMarketCap (Oct 19) claims supply "record ~$315B as USDC gains" — scope differs from rwa.xyz's $300.9B (Oct 1); needs reconciliation. | Float routed-not-abandoned (supports KJ1); card-rail spend is a new demand leg; a hike instead of pause would deepen rate-driven contraction. | newscord.org stablecoin-payments-jump-45 · coincentral.com standard-chartered | **HIGH** (MED on $315B record)

**[D4] EU double-move: USDC designated first "significant" EMT; 37-bank euro stablecoin licensed** | Oct 14-15 | EBA classified Circle's USDC as the EU's first "significant" e-money token — direct EBA supervision from **Nov 12**; Circle fighting 60% bank-deposit reserve treatment. Qivalis won Dutch DNB EMI licence (Oct 14) — 37-bank consortium euro stablecoin. | EU licensed-capacity redistribution consolidating around Circle + bank consortia as predicted; EUR leg of bank-consortium thesis now licensed while USDT stays outside. | crypto.news usdc-first-significant-emt · cointelegraph.com qivalis-authorization | **HIGH**

**[D5] Airtel Money begins full LSE trading at ~$7B after oversubscribed IPO** | Oct 9-14 | Airtel Mobile Commerce priced Oct 9 at £1.96 (~£5.3B), unconditional Main Market trading Oct 14 (~$7B). Africa's largest mobile-money listing; joins OPay (NYSE filed), MNT-Halan (EGX 11x), PalmPay (HKEX). | First hard public comparable for OPay's NYSE pricing; exits clearing at public marks while seed stays at 2020 lows. | kalkinemedia.com airtel-mobile-commerce · thebanker.com · techbooky.com | **HIGH**

**[D6] Circle to push into ~40 emerging markets** | Oct 16 | CEO tells Reuters: off-ramps, local banking partners, USDC distribution — days after closing the $400M Tazapay deal. | Largest incumbent issuer attacking whitespace #1 head-on; compresses runway for local rails (Kora, Yellow Card, dLocal×WU). | reuters.com circle-push-40-new-markets | **HIGH**

**[D7] Ethiopia's central bank joins PAPSS** | Oct 15-16 | National Bank of Ethiopia joined Pan-African Payment and Settlement System; Addis to host COWRY 2026; same week Wise cleared for SA remittances; Ecobank deepened China-Africa rails. | P2's free-A2A decommissioning dynamic extends to corridor FX — where stablecoin off-ramps currently earn their spread. | centralbanking.com ethiopia-joins-papss · ecofinagency.com | **MED-HIGH**

**[D8] SA payments opening hardens: cash utility, shared ATMs, free small withdrawals** | Oct 15-19 | Mid-2027 non-bank opening confirmed (Reuters); SARB cash-utility plan: 30,000 ATMs shared/white-labelled (pilot Jan 2027), free small withdrawals; Wise cleared to enter SA remittances. | Another fee pool (ATM/cash-handling) being decommissioned ahead of merchant acquiring; strengthens whitespace #6 timing + Card 5 logic. | techcentral.co.za reserve-bank-white-label-atms · techcentral.co.za banks-lose-grip | **HIGH**

**[D9] Tokenized deposits go public-chain — and the Fed notices the funding risk** | Oct 19 | JPMorgan extended JPM Coin deposit token to **Ethereum** for institutional clients (Bloomberg); VersaBank launched tokenized deposits in US; KC Fed piece flags bank-funding challenges from deposit tokenization. | P1 mechanism confirmed twice in one week — yield-bearing bank instruments on public chains while a Fed shop worries about deposit flight; raises probability the "yield ban extends to distribution" kill-trigger gets tested. | bloomberg.com jpmorgan-brings-deposit-token-jpm-coin-to-ethereum · pymnts.com kansas-city-fed | **HIGH**

**[D10] Card networks industrialize stablecoin spend rails + compliance layer** | Oct 19 | Visa×Mesh: crypto/stablecoin balances spendable at 175M+ merchant locations; Mastercard launched "Stablecoin Security" fraud/sanctions screening for banks/PSPs. | Merchant-side stablecoin acceptance no longer needs local acquiring deals — pressures Dual-Rail card's FX edge while validating its settlement leg. | forkast.news visa-mesh-175m · theblock.co mastercard-stablecoin-security | **MED-HIGH**

**[D11] Offshore-venue lockouts globalize: Korea blocks 27 exchanges; Australia tightens; Poland still lawless** | Oct 13-17 | Korea's FIU blocked 27 unregistered offshore exchanges (KuCoin, BitMart, MEXC…); ASIC seeks stiffer rules ahead of licensing deadline; Poland's president vetoed second MiCA-transposition bill. | Regulatory arbitrage now the dominant market-share variable outside US/EU core; blocked-venue flow must land somewhere (licensed locals, UAE staging). | financemagnates.com korea-blocks-27 · coindesk.com australia-crypto-exchange-rules | **MED-HIGH**

**[D12] Polygon completes $250M Coinme acquisition — Cycle 001's unverified item confirmed** | Oct 14 | Polygon Labs gains Coinme's US money-transmitter licences across 48 states. | Verifies "licences displace liquidity" at L2-infrastructure layer; removes a live uncertainty flag. | coingape.com polygon-coinme · bitcoinist.com | **MED-HIGH** ($250M single-source)

**Quiet segments:** funding >$50M (nothing new; largest fresh rounds sub-$15M — Synapse Analytics $13M Egypt, Archa A$61M, WalaPay $4.6M SA stablecoin); IPO filings (none new); venue hours (NYSE extended American options hours Oct 19; Ripple Prime launched 24/7 institutional RWA swaps with Virtu trading, Oct 15). **Anomaly file:** Ledger hardware implant ~$90M theft, German retail sales halted (FT); WSJ probing whether Trump's ex-crypto adviser's firm took millions from Tether while GENIUS was shaped.

## Missed-in-Cycle-001 candidates (5)

**[M1] SEC proposes conditional crypto-custody framework for advisers/funds** | ~Sep 30-Oct 1 | RIAs and registered funds may custody crypto (incl. conditional self-custody) with "qualified custodians" — clears biggest structural hurdle to adviser allocation. Extends C8 (custody demand) and C3 (who may hold tokenized MMF shares). | cointelegraph.com sec-moves-to-clear-custody-hurdle · crowdfundinsider.com | **HIGH**

**[M2] CBN: no extension of Jan 2027 payment-data localisation deadline** | Sep 29-Oct 8 | Banks/fintechs must host Nigerian payment data in-country; MTN flags cost pressure; phasing refused. Adds a compliance-cost floor to every Nigeria exposure (Cards 1/5, whitespace #1/#4). | guardian.ng cbn-commits-to-data-localisation · arise.tv | **HIGH**

**[M3] WisdomTree Onchain: tokenized funds >$1.2B; SEC already let an MMF trade 24/7** | Jul 31 / Sep 29 | SEC approval (July) lets WisdomTree's government MMF trade around the clock "like a stablecoin"; Onchain brand launched >$1.2B AUM with MoonPay retail distribution. A live, distributed yield-routing stack — direct precedent for the Yield Router card. | thestreet.com wisdomtree-sec-mmft · morningstar.com wisdomtree-onchain | **MED-HIGH**

**[M4] Treasury's first GENIUS rule draws a $10B federal/state line through the issuer market** | Oct 1 | NPRM thresholds route issuers ≥$10B to federal oversight, smaller issuers state-regulated — reshapes which issuers can scale and where the consortium must charter. | finance.yahoo.com treasury-first-genius-act-rule | **MED**

**[M5] SBI completed $289M Bitbank acquisition (Oct 1)** | Japan's largest crypto exchange via M&A of a licensed venue; consistent with licence-moat thesis. | finextra.com sbi-bitbank · crypto.news what-changes-for-bitbank | **MED**

**Carry-forward verification items:** reconcile CMC $315B vs rwa.xyz $300.9B supply scopes; check Tether weekly redemptions; confirm $250M Coinme consideration; re-test E7's $433B figure (did not resurface this week).
