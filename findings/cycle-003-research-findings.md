# Market Intel — Cycle 003 Research Findings Bank

Date: 2026-10-20 | Wave 1: 4 parallel research agents (C3-1a watchlist sweep + verifications, C3-1b payout-leg deep-dive, C3-1c tokenized-equities deep-dive, C3-1d fresh scan). All findings graded HIGH/MEDIUM/LOW. De-duped against cycle-001/002 banks. Prior: [cycle-002-research-findings.md](cycle-002-research-findings.md)

---

## PART A — C3-1a: Watchlist sweep (10 markers) + carry-forward verifications

Method: ~48 news queries + 12 primary-source pulls (DefiLlama API ×4, CMC live, rwa.xyz live, Federal Register API ×3). De-duped against cycle-002 and siblings.

### A.1 Watchlist sweep

**W#1 GENIUS final-rule distribution scope | NO MOVEMENT (rule), NEW DATA (context) | MED-HIGH**
No final rule text exists. Federal Register API (queried Oct 20): only final-rule item remains Treasury's Sept 30 interim final rule (FR 2026-19966 — state-certification review committee procedures; not distribution scope). OCC final issuer rule NOT published as of Oct 20; Comptroller Gould's target moved UP to **Oct 31** (reported Oct 15). Comment window closed Oct 19 with **87 open NPRM questions**; Blockchain Association filed comments urging narrowed DASP liability and DeFi/foreign-issuer clarity (Oct 19–20). Structural change: **CLARITY Act failed Senate cloture 49–50 on Sept 15** — markup pushed toward May 2027 — killing the legislative path to extend the yield ban to distributors; White House (Sept 15) publicly undercut bank claims (yield ban lifts bank lending only ~0.02%). Distribution-scope extension now hangs solely on Treasury/OCC interpretation (cycle-002 prior: 40–50%). Also new: **Fed proposed its two GENIUS rules Sept 24–29** (reserve/capital/redemption for bank issuers); **ECB/EU central banks pushing to widen the MiCA yield ban to lending/staking** (Sept 22–Oct 2) — yield-ban perimeter widening abroad while the US legislative path dies.

**W#2 OKX USDG 10% APY | NO MOVEMENT | HIGH**
Zero regulator response as of Oct 20; program live. Adjacent touch only: **Texas Banking Commissioner fined OKX + Triple-A $115,000 (Oct 6)** for unlicensed stablecoin transmission (transmission, not yield). USDG expanding (native Arbitrum launch Oct 6). Cross-ref [N-scan]: Gate launched a competing all-in-one money app (Oct 7) — subsidy competition spreading.

**W#3 Two-speed split | MOVED ↓ (float) / ↑ (flow) | HIGH (primary-source live pulls)**
DefiLlama (live Oct 20): total **$304.1B, rolled over from the $308.05B Oct 6 peak (−1.3%)**; USDT **$183.0B** (−$1.2B from Oct 8 peak); USDC **$72.3B** (−$1.9B in 2 weeks). Float is inside the marker's **<$310B confirm zone** (deadline Jan 31, 2027); Tether redemption drift ~0.65% off peak — far from the >5%/quarter trigger. Flow accelerating: rwa.xyz **monthly transfer volume $10.42T, +36.11% 30d**. EBA/USDC: **USDC designated first "significant EMT" Oct 14; joint EBA–ACPR supervision from Nov 12, 2026** (The Block Oct 15, CoinDesk Oct 19); Circle fighting 60% bank-deposit reserve treatment. Trigger fires on schedule in 23 days.

**W#4 OKXICE SEC decision + objections | MOVED ↑ | HIGH**
No SEC "decision" exists to wait for — the TSV exemption has been live since Sept 17; the venue gate is objection mechanics. **Objection count: 1 (Oct 4) → 4 (Oct 8) → 9 (Oct 15) → 16 (Oct 19/20)** — wave 2 added Microsoft, Alphabet, Goldman Sachs, Qualcomm, Caterpillar, McDonald's, Western Digital (filed Oct 15–19) plus Applied Digital (Oct 19); **17 of the original 63 symbols removed before launch**. **Nasdaq opted its own shares out** (CoinDesk Oct 18). No withdrawals; crypto-native names (Coinbase, Robinhood, Circle, Securitize) notably silent; JPMorgan/Walmart/Costco/Eli Lilly un-objected (possibly processing time). Count at **80% of the >20 kill threshold** for Card 6.

**W#5 Binance terminal state | NO MOVEMENT | HIGH**
DOJ compliance probe (Iran sanctions; 2023 $4.3B settlement review) stands (Bloomberg Oct 9; nothing new Oct 10–20); EU halt since Jul 1 stands, regulators scrutinizing "reverse solicitation" loophole (FT, Oct 1). Non-regulatory color: Binance shutting mining pool/cloud mining Nov 10 (infra retreat); Binance.US raising $100M at ~$1B (valuation reset from $4.5B). No CASP licence, no curtailment, no settlement.

**W#6 OPay NYSE pricing | NO MOVEMENT (pricing), NEW DATA (terms) | MED-HIGH**
Still pre-pricing; no roadshow date. New color: Semafor frames **~$4B IPO/valuation target** (vs $2B in 2021) with **~$500M raise**, and Standard Bank confirmed for **up to $200M / 4.99% via linked private placement** (TechCentral Oct 10, The Paypers Oct 14, THISDAY Oct 19). F-1 economics unchanged (rev +137% to $467M H1'26).

**W#7 FX-spread disclosure rules | NO MOVEMENT | MEDIUM**
No disclosure proposal tabled in Nigeria or Ghana; IMF pressure (Jun 16) remains the only push. Ghana's clock sharpened instead: **five-agency implementation committee (Sept 3)**, formal regime targeted **December 2026**, licences "a year off" (Mariblock); IMF urging faster oversight (Sept 27–28). Disclosure-rule trigger (deadline Jun 30, 2027) quiet but the Ghana regulatory regime is now a dated event before it.

**W#8 Rail-capture events | NO MOVEMENT (eviction), NEW DATA (consolidation) | MED-HIGH**
No new MNO/bank eviction; Partna/M-Pesa unrestarted. What moved is **aggregator/bank consolidation of the payout leg**: **Thunes×Coinbase (Oct 19)** — 140-country fiat + mobile-wallet payout reach; **Kora "One Rail" launch (Sept 30–Oct 6)** — pan-African stablecoin collect+payout; **Stanbic Ghana×RD Technologies Ghana–Asia settlement exploration (Oct 20)**. Mauritius governor warned on stablecoins in African payments (Oct 13) — posture, not action.

**W#9 Tokenized private credit | NEW DATA | HIGH (primary-source live)**
rwa.xyz credit dashboard (live Oct 20): distributed **$8.13B (▼1.21% 30d)**, represented **$37.99B (▲4.07% 30d)**, 2,735 assets. **Figure FIGR_HELOC ≈ $24.02B represented** (vs $24.82B cycle-002 reading — flat-to-down); **still no second issuer >$2B** (largest non-Figure: STOKR $1.5B, Maple $1.0B distributed). No stress: Figure Q3 preliminary volume **$5.12B (+107% y/y)**, Kiavi merger closed Sept 1; no delinquency disclosures. Defusal condition unmet; concentration intact.

**W#10 African seed funding | SILENT**
No Q4 2026 aggregate data (quarter 3 weeks old; Disrupt Africa/TechCabal reports land January). Anecdotes only: FINCA $400K to 6 startups (Oct 16), Nigerian "seed-to-growth gap" commentary. Q3's $583M/58 deals remains baseline; I5 falsifier untriggered.

### A.2 Carry-forward verifications

**1. Supply-scope reconciliation — CONFIRMED (mechanism identified).** Live Oct 20: **CMC stablecoin category $313.78B** (broadest: yield tokens like Ondo USDY $2.35B at $1.15, non-USD pegs EURC $455M, USDGO $1.27B, self-reported). **DefiLlama $304.1B** (curated USD-pegged set incl. BUIDL $2.17B, bridged deduped; USDT $183.0B / USDC $72.3B ≈ CMC's core — the ~$10B delta is all tail + scope). **rwa.xyz $290.39B** (narrowest: native on-chain only, excludes RWA-classified tokens). Implication: use DefiLlama for watchlist triggers; treat CMC "records" as category-noise.

**2. Tether weekly redemptions — PARTIAL.** No Q3 attestation yet (Q2'26, Jul 31: $1.5B net operating profit, **excess-reserve buffer halved in a quarter to $4.11B = 2.2% of liabilities**; BDO Jun-30 buffer $4.11B −40% in six months; KPMG full audit for Dec 31, 2025: $6.81B). Supply drift not run: USDT −0.65% from Oct 8 peak. Counterparty watch: **EQIBank funds frozen after $89M US seizure** (Sept 24–Oct 5); Tether claims <0.034% exposure — unverified. $6.3M payment to Bo Hines-linked firm (Oct 15) keeps the GENIUS-shaping anomaly file open. Buffer erosion = watch item, not stress event.

**3. Coinme $250M — CONFIRMED.** Polygon completed the acquisition **Oct 14**; $250M multi-source (The Block Oct 14 + syndication Oct 18: **37 state MTLs + 11 exemptions, 48-state coverage**). Cycle-001 unverified item closes clean.

**4. Ghana cost stack + e-levy — CONFIRMED with UPDATE.** **E-levy formally repealed** (Repeal Bill passed Mar 26, 2025). But cost stack shifted: **MTN Ghana imposed 0.75% fee on MoMo→bank transfers from June 1, 2026** (still contested Sept 2026). BoG/SEC advertising notice stands, no enforcement yet; formal crypto regime due **December 2026** (five-agency committee; licences ~Sept 2027). Cards 1/7: Ghana payout leg now carries a 0.75% wallet-to-bank line item where e-levy sat.

**5. Partna/M-Pesa restart — UNRESOLVED (SILENT).** No restart/replacement/exit announcement; corridor dead since May 7, 2026. M-Pesa stablecoin energy going direct (ADI Foundation onchain deal Jan 2026; Visa×Onafriq DRC pilot Jul 6). Kenya stays weakest corridor; rail-capture risk expressing via MNO-direct deals.

**6. OCC final issuer rule — UNRESOLVED but dated.** Not published as of Oct 20 (FR API-verified; only Treasury Sept 30 IFR + Aug 18 NPRM FR 2026-16796 exist), Gould's target **Oct 31** (Oct 15). 120-day clock not started; if it starts in November, effective date ~March 2027 with Jan 18, 2027 statutory backstop. Trigger #1 live for 11 more days — highest-frequency item for the next sweep.

### A.3 Kill-trigger scoreboard (near-dated)

| # | Trigger | Status this sweep |
|---|---|---|
| 1 | OCC final rule (end-Oct 2026) | **PENDING — target moved up to Oct 31; not published Oct 20 (FR-verified)** |
| 2 | Treasury GENIUS final rule (pre-1/18/27) | **QUIET on rule; path changed** — CLARITY dead (9/15), White House pushback; interpretive path only |
| 3 | GENIUS effective 1/18/27 | On clock; possible slide to ~Mar 2027 if rule lands Nov |
| 7 | SEC decision on OKXICE | **MOVED** — no decision exists; exemption live; gate = objections + go/no-go |
| 8 | Issuer-objection expansion | **MOVED ↑ — 9→16 objects, 17/63 symbols removed; at 80% of >20 threshold** |
| 9 | EBA/USDC supervision 11/12/26 | **CONFIRMED on schedule** (designation Oct 14) |
| 15 | OKX 10% APY USDG | **QUIET** (adjacent Texas transmission fine only) |
| 18 | OPay pricing → filings | **QUIET** (pre-pricing; $4B/4.99% terms color) |
| 19 | Tokenized-credit second source | **QUIET** (single-issuer >$2B stands; Figure flat, no stress) |
| 22 | Fed path (Oct 27–28) | QUIET (hold expected ~83–86%; hike odds ~14%) |
| 23 | Stablecoin aggregate supply | **FIRED-INTO-CONFIRM-ZONE**: $304.1B <$310B |
| 11/12/16 | NGN/Ghana premium compression; de-platforming; ad-ban | QUIET (wedge intact ~4.8–5.1%) |
| 13/14/17/20/21/24 | Circle 40-market; card-rail spend; TCH/JPM; wind-downs; venue hours; PSV/sandbox | QUIET or covered by siblings |

### A.4 Sources (abridged)
Federal Register API (federalregister.gov/api/v1/documents.json); cryptonews.net OCC-rule analysis (Oct 19); AInvest OCC Oct-31 target (Oct 15); CNBC/FinTech Weekly/Orrick/Forkast CLARITY failure; American Banker White House 0.02% (Sept 15); Reuters/Arnold & Porter Fed GENIUS proposals (Sept 30/Oct 8); CoinDesk/The Block ECB MiCA yield-ban widening; DefiLlama stablecoins API (live); CMC stablecoin category (live); rwa.xyz stablecoins + credit dashboards (live); The Block/CoinDesk EBA significant-EMT (Oct 15/19); Ledger Insights OKXICE 16 objectors (Oct 19/20); CoinDesk Nasdaq opt-out (Oct 18); Bloomberg DOJ-Binance (Oct 9); Semafor/TechCentral/THISDAY OPay; Mariblock/BitKE Ghana regime; GhanaWeb e-levy repeal; MTN 0.75% MoMo fee (Tech Labari May 29 2026 + Modern Ghana Sept 24); Thunes/Coinbase PRs (Oct 19); Kora One Rail (Sept 30–Oct 6); Stanbic×RD (Oct 20); Figure Q3 prelim (Stock Titan Oct 6); Tether Q2 attestation coverage (CoinDesk Jul 31, CryptoRank Sept 3, BING Aug 13); EQIBank freeze (Sept 24–Oct 5); Polygon-Coinme (The Block Oct 14); Texas OKX fine (Oct 6); Disrupt Africa (Oct 5).

---

## PART B — C3-1b: Payout-leg deep-dive (Cards 1/3/7)

Method: 16 news queries + live primary-source fetches (Mavapay, Tazapay, Circle Mint, Monierate pricing pages). Cross-references siblings, not re-reported.

### B.1 Circle's EM offensive — partner-first, infrastructure-first, not rail-first

- **The "40 emerging markets" push remains a corporate statement, not a corridor map.** CEO Jeremy Allaire told Reuters (Oct 16): push USDC into ~40 mostly-developing markets via off-ramps and local banking partners; echoed by Decrypt/AMBCrypto/Finimize/International Finance (Oct 16–19). Some outlets say "50" — single downstream paraphrase. **No corridor list, no named MNOs, no pricing published as of Oct 20.** (HIGH on existence; LOW on operational detail.)
- **Concrete execution vehicle is the Tazapay acquisition: ~$400M, all-stock, agreed ~Sep 8, 2026** (CoinDesk, American Banker, Banking Dive, FinTech Futures). **⚠️ Status correction to cycle-002 [D6]: AGREED, NOT CLOSED** — close expected 2027 pending MAS approval. Tazapay's live rate card (below) is what Circle is buying.
- **Named partners verified:** Onafriq expanded regulated USDC settlement (circle.com, Aug 18); Circle Ventures invested in Flutterwave (Jul 7); Binance took $100M equity + renewed 5-year USDC commercial deal (Sept 22–30); Volante Technologies institutional settlement (Sept 29); Circle Stablecoin Payouts live in Europe (Jul 1).
- **Circle Mint supports 8 local-currency on/offramps — GBP, SGD, MXN, BRL, HKD, CNH (+2) — "FX handled inside Mint, no pre-funding required"** (circle.com, Aug 18, fetched primary Oct 20). **No African currency in the set.** No Circle Mint availability in Africa; no EM corridor pricing public.
- **Implication:** Circle attacks EM *distribution* through aggregators (Tazapay, Onafriq, Flutterwave), not exclusive payout legs. Card 7 kill-trigger #13 (Circle direct MNO integration ≥5 markets) NOT advanced; the 20–60bps toll faces a tougher competitor in ~2027 when Tazapay's 0.8–2.5% card is internalized. Window: ~12–15 months before Circle-owned EM off-ramp pricing exists.

### B.2 MNO payout-rail behavior — verticalization productized; no new evictions

- **Airtel Money:** LSE admission ~$7B (Oct 14) raised no new money for the business (Techish). Strategy = **product verticalization, not open APIs**: Mastercard-powered virtual card (VCN) launched/planned for Kenya to rival M-Pesa GlobalPay (Business Daily Oct 6, TechCabal Oct 14), 875k VCNs live in UG/ZM/TZ. No new open-API or exclusivity announcements. (HIGH)
- **Safaricom/M-Pesa:** flagship stablecoin activity remains the **Visa × M-PESA Africa × Onafriq DRC stablecoin pilot** (Jul 6–10) — the MNO owns the corridor; plus ADI Foundation onchain deal (Jan 2026). No API policy change; no new de-platforming. **Partna/M-Pesa restart silence persists** (cross-confirms C3-1a W8). (HIGH on silence)
- **MTN MoMo — new datapoint:** **MTN Group Fintech partnered Ant International (Jun 9, 2026)** to scale MoMo into a super-app (MTN PR, ITWeb, tech dot africa), on top of Ericsson cloud migration (Aug 21–24). Ant International is itself stablecoin infrastructure — an MNO + big-tech stack forming *inside* the rails. (HIGH)
- **Implication:** MNOs monetize cross-border/FX themselves (VCN, GlobalPay, Ant-powered super-app) rather than wholesale API capacity. The exclusivity window Card 7 depends on is **real but demonstrably closing**; eviction threat dormant, not resolved.

### B.3 Off-ramp pricing scan (observable, NGN-focused)

| Provider | Corridor | Observable price | Source | Date | Conf. |
|---|---|---|---|---|---|
| **Mavapay** | USD→NGN payouts (B2B API); KES & ZAR legs live | **0.75% <₦1M (min ₦200, cap ₦5,000); 0.5% >₦1M (cap ₦10k)** → effective **10–50bps at size** | mavapay.co/pricing (primary) | Oct 20 | **HIGH** |
| **Tazapay** (Circle, close pending) | Global FX incl. EM | **FX 0.8–2.5%**; cards 3.8%+; local payouts USD 2–5 flat; SWIFT USD 5–35 | tazapay.com/pricing (primary) | Oct 20 | **HIGH** |
| **Luno / Quidax / Gate / Textile / HyperFX / Bybit** | USD↔NGN retail/P2P | Buy/sell **₦1,361–1,365**; USDT/NGN ₦1,361.26; market USD/NGN ₦1,362.58 | monierate.com (primary) | Oct 20 | **HIGH** |
| **Nala / Vban (MTO send)** | USD→NGN | **₦1,349** per $1 | monierate.com | Oct 20 | HIGH |
| Official NGN reference | — | ~₦1,334 | monierate.com (prior capture) | Oct 20 | MEDIUM |
| **dLocal** | Blended global | Take-rate slide **2.9% → 0.9%** framed as "strategy, not commoditization"; Q2'26 revenue beat, EPS miss | earnings Aug 2/13 | Aug 2026 | MED-HIGH |
| Yellow Card, Busha | NGN retail | ~₦1,351 sell (prior capture) | monierate | Oct 20 | MEDIUM |
| Conduit, Blockradar, Fonbnk, Juicyway, Raenest, Grey | NGN/GHS/KES | **No public pricing found — absence confirmed** | multiple searches | Oct 20 | absence: HIGH |

**Structure read (HIGH):** platforms transcode AT the market/parallel rate (crypto-vs-market ≈ 0bps); the entire retail margin is the **official–parallel wedge (~2.1% NGN)** — the spread is a policy artifact, unchanged in structure from Cycle 002.

**Verdict: compression YES at the wholesale/API layer, NO at the retail wedge.** Mavapay's capped card is the first *public* sub-80bps wholesale pricing (10–50bps effective); Tazapay flat-fee local payouts + Circle Mint "FX inside Mint, no prefunding" show pricing toward per-transaction fees and internalized FX. dLocal's take-rate slide corroborates margin pressure. **Re-anchor the 80–150bps B2B band as "80–150bps today, with a demonstrated 10–50bps floor at the API high-value end."**

### B.4 Float-yield update

| Country | Instrument | Current yield | Direction |
|---|---|---|---|
| **Nigeria** | 364-day T-bill stop | **15.90%** (Oct 14 auction; DMO rejected higher-yield bids across ₦763bn, raised ₦269bn — Punch Oct 17, BusinessDay Oct 16) | **EASING** — ~95bps below the 16.84% Cycle-002 anchor (stale-vintage correction); Oct 7 blipped up on demand (15.85%) |
| Nigeria | MPR | **23.0%** — cut 350bps from 26.5% at Sep 21–22 MPC (NAN Sep 24); IMF endorses but warns against premature easing (Punch Oct 15) | **EASING**, further cuts expected → float pool shrinking |
| **Ghana** | 364-day / 182-day T-bill | **~9–10% / 6.12%** (Oct 5, MED); Oct 16 auction **missed target by Gh¢1.53bn, yields mixed** (Modern Ghana Oct 19) | FLAT-EASING (disinflation ~5%) — float-yield edge gone |
| **Kenya** | 364-day T-bill | **9.04%** (Oct 15, MED) | FLAT |

**No issuer-paid distribution yield to EM users anywhere (HIGH).** GENIUS prohibits issuer-paid yield; Circle retains ~95% of reserve interest; no new Circle/PayPal EM distribution-yield program. Off-issuer subsidies remain: OKX 10% APY USDG offshore-only, untouched; Kenya's VASP rulebook bans stablecoin interest from November.

### B.5 Portfolio implications (Cards 1/3/7)

1. **Circle = channel partner today, owned-infrastructure competitor in ~2027** (Tazapay agreed-not-closed). No African currency in Mint, no MNO deal, no EM pricing → kill-trigger #13 untriggered; sequencing urgency up, not thesis change.
2. **MNO verticalization moved from pilots to products** (Airtel×Mastercard VCN; MTN×Ant International) while **zero new evictions** — exclusivity contracts still available and still revocable; contract-first execution for Card 7 time-sensitive on both sides.
3. **Wholesale pricing floor discovered** (Mavapay 10–50bps effective): moat must lean harder on **exclusivity + float + premium duration**, not spread level. Retail wedge (~2.1% NGN) intact = policy artifact still funds the model.
4. **Float-yield engine downshifted:** NGN 15.90% (−95bps vs anchor) with MPR 23% easing bias — Card 1's ~46bps/10-day float add-on compresses toward ~40bps and shrinks on cuts; Ghana (~9%) and Kenya (~9%) no longer anchor. **Nigeria is the only high-yield float leg; Ghana weighting now rests on FX wedge (4.8–5.1%), not yield.**
5. **Brief synthesis correction to carry:** Tazapay = agreed-not-closed; NGN float-yield anchor = 15.90% not 16.84%.

### B.6 Sources
circle.com/blog Circle Mint 8 currencies (Aug 18, fetched Oct 20); Reuters via Decrypt/AMBCrypto Circle 40-EM (Oct 16–19); CoinDesk Circle-Tazapay $400M (Sep 8 + syndication); circle.com Onafriq USDC (Aug 18); Tech Labari Flutterwave-Circle Ventures (Jul 7); Bing/Yahoo Binance-$100M-Circle (Sep 22–30); mavapay.co/pricing (fetched Oct 20); tazapay.com/pricing (fetched Oct 20); monierate.com live tables (fetched Oct 20); Punch/BusinessDay NG T-bill auctions (Oct 16–17); NAN CBN MPR 23% (Sep 24); Punch IMF-CBN (Oct 15); Modern Ghana/CNBC Africa Ghana T-bill miss (Oct 16–19); Business Daily Airtel VCN (Oct 6); TechCabal (Oct 14); MTN×Ant International PR/ITWeb (Jun 9); TechAfrica News Visa×M-PESA×Onafriq DRC (Jul 6–10); BigGo/Investing.com dLocal take-rate (Aug 2026).

---

## PART C — C3-1c: Tokenized equities & issuer-content veto deep-dive (P8, Cards 2/6)

Method: ~32 news searches + 14 primary-source fetches. De-duped against [D1]/[W6]/Cards 2-6.

### C.1 OKXICE + issuer objection wave

**Status change: objections MOVED 9+ → 16 as of Oct 20** (Ledger Insights Oct 20, TokenPost Oct 20 — HIGH).

Notice-revision timeline (primary-source anchored via OKXICE's own public notice):

| Date | Event | Count |
|---|---|---|
| Oct 4 | OKXICE operating notice published — 63 proposed symbols; 1 objection (Cerebras) | 1 |
| Oct 8 | First notice revision — 3 more objectors | 4 |
| Oct 15 | Second revision — disclosed count nine: Cerebras, AppLovin, Applied Digital, Rocket Lab, CoreWeave, Verizon, Applied Optoelectronics, Broadcom, UnitedHealth | 9 |
| Oct 15–19 | Wave 2 (blue chips): Microsoft, Alphabet, Goldman Sachs, Qualcomm, Caterpillar, McDonald's, Western Digital | **16** |

- **Net effect: 17 of 63 symbols removed before launch** (Ledger Insights — MEDIUM; arithmetic caveat: crypto.news counts 8 of first 9 in the original 63, implying 15; 17-vs-15 gap unresolved, possibly share classes).
- **Wave structure:** wave 1 = AI-infrastructure names popular with crypto natives; wave 2 = blue chips. **Silent: Coinbase, Robinhood, Circle, Securitize.** Un-objected (windows open to ~Nov 3–8): JPMorgan, Walmart, Costco, Eli Lilly (MEDIUM, single source).
- **Nasdaq opted its OWN shares out** — grounds: won't allow its stock on a venue lacking real-time best-price display and consolidated-tape trade reporting (decrypt citing WSJ — HIGH).
- **Issuer grounds:** only Applied Optoelectronics publicly explained (price/liquidity uncertainty + implied-endorsement fear). Structural diagnosis (Four Pillars via Markets Media Oct 19 — HIGH): "revenue goes to the tokenizers and the risk goes to the companies, leaving companies with little reason to participate."
- **"SEC decision" framing — CORRECTED:** no pending SEC approval/decision exists. The Innovation Exemption (order of **Sept 17, 2026**) took effect **immediately upon publication**, runs **five years (~Sept 2031)**; OKXICE filed an operating *notice*, not an application. No launch date disclosed; no withdrawal. Venue must update its notice within 5 business days of each objection; trading cannot start until 30 days after issuer receipt; timely objection blocks that token on that venue only.
- **SIFMA comment letter (Oct 20 — HIGH):** asks SEC for FAQs/guidance and possible **amendment: affirmative issuer consent (opt-in instead of opt-out), longer objection period, universal issuer opt-out** (one letter blocking all venues); SIFMA supports delaying venue launches if needed. Atkins and Uyeda signal **formal notice-and-comment rulemaking**.
- **Venue mechanics (verified):** Uniswap v4 pools on OKX X Layer; USDC/USDG/USDT pairs; permissioned wallets; third-party tokenizer holds shares 1:1 via registered broker-dealer; same dividend/vote rights; trading halts when primary halts; **volume capped at a small slice of normal volume**; not subject to Reg NMS; fees = service + pool + network, amounts unpublished.

### C.2 Nasdaq–Kraken gateway traction

**No traction evidence since Oct 15 — no issuer signings, no volumes, no symbols, no economics disclosed.** Verifiable base: Nasdaq **$100M into Payward at $21B valuation** (announced Sept 10; "eyeing 2027 launch"); xStocks gateway concept dates to Mar 9, 2026; LSE–Kraken tokenized UK stocks prep (Sept 1); Deutsche Börse–Kraken institutional tie (Oct 13). **Data-hygiene correction: cycle-002's "Nasdaq–Kraken issuer-first gateway launched Oct 15" is better characterized as *announced/narrated* — downgrade to MEDIUM-LOW; pre-launch with 2027 target.**

### C.3 Kalshi perps + CFTC

- **Refinement of Oct 6 event:** CFTC approval + launch was for the **US 500 stock-INDEX perpetual** — cash-settled on MerQube US Large Cap Index (price-return, no dividends/votes), $1/point, 1/10,000 fractional, cleared at Kalshi Klear, **24/5 schedule (Sun 6pm–Fri 5pm ET)** identical to CME Globex (Finance Magnates/Reuters Oct 6 — HIGH).
- **Volume tiny: 24h $556K, OI $219.6K, leverage ~15.3x** (Finance Magnates Oct 6 — HIGH). Platform-wide Kalshi volume $18.37B Sept 28–Oct 4 (+17.3% w/w) dominated by prediction markets/crypto (MEDIUM).
- **Single-stock perps (58 names incl. TSLA/AAPL/NVDA) STILL PENDING** — filed Sept 11–22; no approval as of Oct 20; jurisdiction fight ongoing (Citadel alarms). **Coinbase single-stock perps blocked by CFTC standstill** (MEDIUM); CFTC approved converting 25-year index futures into never-expiring contracts for Coinbase (Oct 5 — MEDIUM). OG.com also filed (Sept 27 — MEDIUM).
- **Credibility overhang:** wash-trading allegations (~$5B under review; CFTC weighing probe — Sept 21–Oct 1); Kalshi ended liquidity incentive program Oct 1 (HIGH).

### C.4 Session-bridge decay indicators (Card 2 decay clock test)

| Event | Date | Impact | Conf. |
|---|---|---|---|
| **Nasdaq 23x5 SEC-approved; launch set Dec 6, 2026** — overnight session leaves US stocks closed just 1 hour/weekday | Approved Apr 2026; date confirmed Aug 18 | Exchanges' own 24/5 clock starts in **47 days** | HIGH |
| **Robinhood announces 24/7 weekend trading** for selected US stocks/ETFs via **Bruce ATS**; launch "early next year" pending review | Announced Sept 29–30 | First retail weekend bridge into regulated rails | HIGH |
| Robinhood US crypto perps live via Robinhood Derivatives (CFTC FCM) on Bitstamp — 8 assets, BTC/ETH 10x, 1bp promo | Sept 29–30 | Retail onshore perps | HIGH |
| **NYSE American options extended hours** — second exchange after Cboe (approved May 28) | Oct 19 | Options hedging extends toward 24/5 | HIGH |
| **Ripple Prime: Brevan Howard ($35B AUM) multi-asset prime-brokerage mandate** | Oct 6–8 | Institutional 24/7 PB legitimacy | HIGH |
| **Ripple Prime RWA perpetual swaps** — 100+ markets (stocks, metals, FX) via Trade.xyz referencing Hyperliquid perps; **Virtu already trading** | Oct 15–16 | Institutional 24/7 synthetic exposure, hidden-road | HIGH |
| **MEXC: ~half of tokenized-stock volume outside regular US hours** (earnings-season data) | Sept 29 | Direct off-hours demand datapoint | MEDIUM |
| MEXC July: tokenized equities = 62% of TradFi spot; stock futures +111% m/m | Aug 12 | Offshore venue demand scale | MEDIUM |
| Overnight (traditional) session share of total volume | — | **No exchange-grade share data found**; counsel view "evolution, not revolution" | LOW (absence) |

**Verdict: Card 2's decay clock is real and now date-certain — Nasdaq 23x5 goes live Dec 6, 2026, and Robinhood weekend trading targets early 2027. The perp leg of the threat is slower than Cycle 002 assumed (Kalshi index perp tiny; single-stock perps pending).**

### C.5 Issuer-content economics

- **Content bps remain UNPRICED.** No licensing fee, revenue-share, or venue-direct issuer deal at any venue (OKXICE, Nasdaq, Cboe, Bullish). Zero observed prices.
- **Structural reason documented** (Markets Media Oct 19 — HIGH): third-party model gives issuer **no capital, no fee, no data relationship** — tokenizers earn the fees, issuer carries price-divergence/brand/shareholder-comms risk.
- **The pricing pathway forming is issuer-sponsored, venue-direct infrastructure** — first "prices" will be embedded in platform economics, not posted rates:
  - **Issuer Sponsored Token (IST) Coalition — Bullish (NYSE: BLSH) + Equiniti, launched Sept 24, 2026**, joined by Alpaca, Apex Fintech Solutions, DriveWealth; issuer event at **NYSE on Oct 27**; grounded in **Bullish's $4.2B acquisition of Equiniti** (announced May 2026, closing Jan 2027) to build "the world's leading transfer agent for tokenized securities." A transfer-agent-anchored consent stack — **Card 6's slot, claimed by others.**
  - **Securitize**: issuer-sponsored model (security entitlements via registered transfer agent); tokenized its own NYSE stock (SECZ) on debut day Jul 2 (~$295M to Solana/Avalanche); launched 12 third-party stock tokens Oct 8, plans NYSE and OKXICE distribution (HIGH).
  - **Nasdaq "issuer-first"** design language + Nasdaq opting its own shares out = incumbent venue adopting the consent gate as product.
- **Regulatory nudge toward mandatory consent:** SIFMA's opt-in + universal opt-out ask would convert Card 6's construct from commercial option to compliance necessity (Oct 20 — HIGH).
- **Law-firm/advisory wave validating Card 6's premise:** Morgan Lewis (Sept 28 + Oct 7), Latham & Watkins (Oct 9), White & Case (Oct 7), Mayer Brown (Sept 22), WilmerHale (Oct 5), A&O Shearman (Sept 29), McDermott (Oct 8), Skadden (Oct 14), Gibson Dunn (Sept 29), McGuireWoods (Oct 19) — headline-level evidence (HIGH).
- Counterpoint on demand: unnamed investment-bank note "little demand for tokenized stocks" (Sept 21 — MED-LOW); Glider CEO expects "zero traction" on OKX×ICE citing AMM capital inefficiency (MEDIUM).

### C.6 Other venues + regulatory perimeter

- **Securitize Stocks (Oct 8):** 12 US stocks on Solana (Apple, Nvidia, Strategy, Amazon, Tesla), 1:1 security entitlements; plans **NYSE and OKXICE** distribution — a tokenizer positioned across both rails (HIGH).
- **Perpetuals.com** (perp DEX) moving to offer tokenized US stocks under the Innovation Exemption (Oct 14–15 — MEDIUM) → **new TSV applicant, second venue in queue**. Coinbase tokenized stocks live on Base (Aug 25 — MEDIUM). Backpack racing 24/7 equities (LOW).
- **xStocks/Backed (Kraken):** >$10B cumulative volume Nov 2025 → **$25B + 80K on-chain holders by Feb 2026**; SpaceX pre-IPO access (Jul 2026). "Oct 7" CMC item appears to be a republication.
- Sector sizing: tokenized-stock DEX volume $20.9B/30d (Sept 27 — MEDIUM); category market cap ~$2.3B (Jul 22 — MEDIUM).
- **SEC perimeter:** Innovation Exemption issued Sept 17, effective immediately, 5-year term; delayed twice in August; Atkins/Uyeda point to formal rulemaking; SEC 24-hour-trading roundtable Jul 24. No no-action letters affecting venues surfaced.
- **EU:** tokenized shares are financial instruments (MiFID II), outside MiCA CASP perimeter; EC MiCA review consultation (Jun 2026); DLT Pilot Regime upgrade floated; Lise prepping first tokenized IPO under Pilot Regime; Switzerland opening 24/7 stock trading via tokenization (Nov 2025); Spain calls EU rules too restrictive (Sept 2026) (MEDIUM).

### C.7 Implications (P8, Cards 2 & 6, whitespace #4)

1. **P8 STRENGTHENED, faster than modeled:** 9→16 objectors in 5 days; ~17/63 symbols (~27%) removed pre-launch; wave 2 hit blue chips. The veto is now the binding constraint on the US tokenized-equity venue set.
2. **Watchlist marker 4 must be REFRAMED:** no single "SEC/OKXICE decision" exists. The live gates: (a) receipt-based 30-day objection mechanics (more possible through ~Nov 3–8), (b) possible SEC **amendment** driven by SIFMA (opt-in consent, universal opt-out — hardens P8 structurally), (c) each venue's own go/no-go. Card 2's capital stage-gate should re-key onto these three, not a phantom approval date.
3. **Card 6 validated in premise, contested in position:** SIFMA's opt-in push makes consent administration mandatory (demand ↑); 10+ law-firm alerts confirm the advisory layer — but **Bullish–Equiniti's IST Coalition ($4.2B transfer agent at its core) plus Securitize compete for the same intermediary slot**. Card 6's 12–18mo time-box now has a named, better-capitalized rival; **Oct 27 NYSE issuer event is the first consolidation checkpoint.**
4. **Card 6 kill-trigger proximity:** objections at 16 of ~20 threshold — not yet triggered; four mega-cap holdouts (JPM, WMT, COST, LLY) plus silent crypto-natives (COIN, HOOD, CRCL, SECZ) keep the licensable core alive. The bifurcated symbol universe (crypto-native in, blue chips out) is exactly Card 2's "non-objected names only" tradeable set.
5. **Card 2 decay clock: DECAY CONFIRMED, date-certain.** Nasdaq 23x5 on Dec 6 shrinks the closed window to 1 hour/weekday; Robinhood weekend trading (early 2027) attacks the last unregulated gap; NYSE/Cboe 24/7 options extend the hedge stack. Cycle 002's terminal-decay kill criterion ("NYSE or Nasdaq files for 24h cash-equity sessions") is effectively reached Dec 6 — Card 2's residual edge narrows to weekend/holiday bridging, non-objected tokenized names, and the white-label routing API (the durable line).
6. **Synthetic-perp threat slower than assumed:** Kalshi's onshore index perp did $556K day-1 (rounding error vs offshore's $433B/mo Binance book), trades 24/5 not 24/7, single-stock perps unapproved. The bridge's real 2026 competitor is **regulated venue hours**, not onshore perps; offshore (Binance SPYUSDT, Trade[XYZ]/Hyperliquid) still owns true 24/7 short/leverage demand.
7. **Whitespace #4 economics: still unpriced; first prices will be structural** — embedded in issuer-sponsored platform deals (Equiniti/Bullish transfer-agent stack, Securitize entitlements, Nasdaq issuer-first), not posted licensing bps. Monetization window real but closing as coalitions form; watch the Oct 27 NYSE event and any Securitize/OKXICE tokenizer deal.
8. **Competitive-read update:** Nasdaq–Kraken gateway zero disclosed traction — near-term pressure on Cards 2/6 lower than Cycle 002 implied; but Nasdaq's $100M at $21B shows the incumbent buying optionality on the consent-gated end-state.
9. **Data hygiene:** correct cycle-002 objection list (mixed wave-1/wave-2 names); notice-verified nine are Cerebras/AppLovin/Applied Digital/Rocket Lab/CoreWeave/Verizon/Applied Optoelectronics/Broadcom/UnitedHealth; Microsoft/Alphabet/Goldman/Qualcomm/Caterpillar/McDonald's/Western Digital arrived Oct 15–19.
10. **New watch items:** SIFMA amendment outcome; IST Coalition's first issuer-signed deal; Nasdaq Dec 6 launch volumes + overnight-session share; Robinhood weekend-trading approval; Kalshi/Coinbase/OG.com single-stock perp rulings; objection count at ~Nov 3–8 window expiries (JPM/WMT/COST/LLY).

### C.8 Sources
crypto.news nine-companies objection (Oct 19); decrypt.co why-companies-object (Oct 19); Ledger Insights 16 objectors (Oct 20); TokenPost (Oct 20); Markets Media little-reason-to-permit (Oct 19); Markets Media SIFMA-TSV letter (Oct 20); GlobeNewswire IST Coalition (Sept 24); Finance Magnates Kalshi perps (Oct 6); Reuters Kalshi index perp (Oct 6); CryptoRank CFTC standstill (Sept 22); The Block Kalshi liquidity program (Oct 1); Seeking Alpha/Markets Media/Arnold & Porter/WilmerHale Nasdaq 23x5; ChainCatcher Robinhood HOOD Summit (Sept 30); Reuters Robinhood weekend (Oct 1); The Block/The TRADE/Hedgeweek Brevan×Ripple Prime (Oct 6–8); The Block/Markets Media/Finance Magnates Ripple Prime RWA swaps (Oct 15–16); GlobeNewswire MEXC off-hours (Sept 29); TechBullion MEXC July (Aug 12); PR Newswire/Reuters/CoinDesk Securitize Stocks (Oct 8); CNBC/Nasdaq PR Nasdaq-Payward $100M (Sept 10–11); Kraken blog xStocks gateway (Mar 9); BusinessWire xStocks $10B (Nov 2025); menafn xStocks $25B/80K (Feb 2026); TradingView Perpetuals.com filing (Oct 14); Yahoo Coinbase Base (Aug 25); Startup Fortune $20.9B/30d (Sept 27); WilmerHale/A&O Shearman/McDermott/Mayer Brown/Morgan Lewis/Latham/White & Case/Skadden/Gibson Dunn/JD Supra advisory wave; CoinDesk SEC delay (Aug 13); Better Markets (Sept 16); fintechanddigitalassets.com MiCA review (Jun 1); Ledger Insights DLT Pilot (Dec 2025), Lise tokenized IPO (Apr 2026).

---

## PART D — C3-1d: Fresh signal scan (window Oct 14–20 + missed items)

Method: ~49 news queries (~32 sweep + ~17 drills) + 2 DefiLlama API pulls + 10 URL-decode verifications. 15 findings, multi-outlet confirmed. Two stale-recycle traps caught and excluded (Deutsche Börse-$200M-Kraken = Aug 21 recycle; Visa-Bridge 100+ countries = Oct 5 recycle).

### D.1 Fresh findings [N1]–[N15]

**[N1] JPMorgan nears Nigeria launch — merchant bank by December, after deposit with CBN** | Oct 8–20 | Bloomberg (Oct 20); Businessday (Oct 20) confirms capital deposit; RioTimes: licence target merchant bank by December; ecofinagency frames with Absa as "breaking with foreign banks' retreat from Africa." First G-SIB building an onshore Nigerian payments/banking footprint since the retreat cycle — lands in the EM off-ramp's home market with balance-sheet and licence advantages no local challenger can match. | **HIGH** | Africa/Bank | Whitespace #1 + Cards 1/7 new competitive threat; Card 4 bank-LP evidence strengthens

**[N2] Coinbase×Thunes: stablecoin payouts to 140 countries — instant to bank accounts and mobile wallets** | Oct 19 | Joins Coinbase's stablecoin infrastructure with Thunes' global payout network (Thunes connected stablecoin payouts to 11,500 banks via Swift, Mar 2026). An incumbent exchange is buying the EM payout last mile rather than building it — the exact asset Card 7 assumed could be wholesaled. With Visa Direct production [N12] + Circle's 40-market push, the payout leg is being bid for by three heavyweights in one week. | **HIGH** | Payments/Africa | Card 7 + whitespace #1 — payout-leg scarcity stressed; P9 evidence

**[N3] Japan's three megabanks complete joint yen-stablecoin PoC; eyeing live corporate launch** | Oct 15–19 | MUFG, SMBC, Mizuho completed joint stablecoin co-issuance + cross-border trial (6-day test); "preparing real transactions" for corporate settlement. Bank-consortium issuer model validated in Europe (Qivalis) now has an Asia leg — a yen instrument with cross-border trade settlement as stated use case. | **HIGH** | Bank/Stablecoin | P1 bank crowd-out; whitespace #2 analog in Asia

**[N4] Ripple's RLUSD gets bank rails: Cross River links $2.4B RLUSD into core banking; DriveWealth adopts for settlement** | Oct 14–19 | Cross River (major BaaS provider) integrated RLUSD into core banking enabling fintech clients to move funds in/out; DriveWealth will use RLUSD for stablecoin settlement + cross-border. Commentary: banks earn the float yield on RLUSD reserves — bank-yield crowd-out extending to a non-Tether/Circle issuer's distribution. | **HIGH** | Stablecoin/Bank | P1; C3 rider — issuer fee pools intermediated by banks

**[N5] World Liberty's USD1 sheds ~$400M in two weeks; redemptions concentrated in one address ($200M)** | Oct 18–19 | USD1 supply fell $385M (−8.7–9.1%) in nine days; one address redeemed $200M. DefiLlama shows USD1 at $4.02B (Oct 20). First concrete issuer-side concentration/redemption event of the cycle — "float is rented, not owned" risk made visible in a politically connected issuer. | **HIGH** | Stablecoin | P1 two-speed; watchlist-3 issuer health; EM dollar-savings counterparty risk

**[N6] Perpetuals (PDC) files second SEC Innovation-Exemption tokenized-stock venue — ex-FTX Europe head, Nasdaq-listed** | Oct 14–16 | Filed to offer tokenized US stocks under the Innovation Exemption, days before OKXICE's objection wave made national print (WSJ Oct 16). The issuer-consent bottleneck now gates two applicants, not one — raising the value of signed content and odds the SEC framework gets its first stress test soon. | **HIGH** | Exchange | P8 + C6; C2 stage-gate input

**[N7] Binance bStocks: fastest tokenized-equity product to $1B AUM; $40B cumulative volume; 62% traded out-of-hours** | Oct 14–15 | PR Newswire/Finance Magnates: bStocks crossed $1B AUM fastest in category, $6B in share conversions, >$40B cumulative volume, 62% outside US market hours. Demand-side proof that off-hours access — not issuer blessing — is pulling flow, sharpening tension with P8's content veto. | **HIGH** | Exchange/RWA | P6/P8 tension; whitespace #4; C2 decay-clock data

**[N8] Ondo TVL hits $4B — surpasses BlackRock's BUIDL — on tokenized stocks/ETFs; share slipping to 26%** | Oct 14–18 | Ondo total TVL passed $4B, overtaking BUIDL ($2.25B, Oct 6); stocks passed $1B in Aug; market share slipping to ~26% as competitors scale. RWA growth now equities-led, not treasuries-led. | **HIGH** (MED on share) | RWA | Whitespace #6 context (credit NOT the growth engine); P6 venue-side demand compounding

**[N9] Gemini: judge refuses to vacate $5M CFTC settlement; stock −15% on 3 executive exits; 42% revenue growth disclosed** | Oct 15–16 | Federal judge rejected the joint Gemini–CFTC motion to undo the 2025 settlement + permanent injunction — rare enforcement-re-litigation loss. Same week: three top executives leaving sent GEMI down >15% (single source, LOW), against disclosed 42% revenue growth. | **MED-HIGH** | Exchange | P5 (enforcement permanence under friendly regulators); listed-venue comparable for OPay

**[N10] Taiwan blocks Coinbase and Kalshi over election-betting concerns** | Oct 14–16 | Taiwan blocked access ahead of its vote — Kalshi for election contracts, Coinbase by association with betable content. Lockouts now reach APAC's democratic perimeter; prediction-market regulation exported via content, not licence, failures. | **HIGH** | Exchange | P5 (lockouts globalize — APAC added)

**[N11] CME vs CFTC perp lawsuit escalates: CFTC moves to dismiss, challenges CME's standing** | Oct 19 | CFTC asked a federal court to dismiss CME's suit over crypto perpetual-futures jurisdiction and challenged standing. This is the jurisdictional fork deciding whether onshore perps run as futures (CME) or swaps (CFTC regime where Kalshi/Coinbase filed). | **MED-HIGH** | Exchange | P5/I3 revised criteria; watchlist-4 rider

**[N12] Card-rail industrialization: Visa Direct USDC prefunding to commercial production; Stripe×Plasma multi-currency stablecoin cards; Bridge OUSD multichain** | Oct 14–17 | Visa Direct moved stablecoin prefunding from pilot to **commercial production** with Inyo Global as first client; Stripe×Plasma launched multi-currency stablecoin cards; Bridge's OUSD live on Solana + 3 chains. The flow boom getting production-grade plumbing — including Visa closing the "banking-hours gap" stablecoins were supposed to expose. | **HIGH** | Payments | C1 settlement leg validated; Card 3 FX rider — networks internalizing the conversion moment

**[N13] Bank stack compounds: Deutsche Bank custody within weeks (Asia 2027); OCC debanking report confirms crypto throttling; BNY custody revenue double-digit** | Oct 14–16 | Deutsche Bank launches BTC/ETH custody "within weeks," Asia 2027 — a European G-SIB joining the Citi/BNY custody wave. OCC debanking report found bank restrictions tied to crypto activity under prior administration, flagged 9 top banks; fair-access rules proposed. BNY reported double-digit custody revenue growth. | **HIGH** | Bank | U3 fully resolved trajectory; whitespace #5 date-certain demand; P1

**[N14] Africa regulatory + float-yield bundle: Kenya VASP November deadline (stablecoin interest banned); Stanbic Ghana×RD Technologies explore stablecoin trade settlement; Cameroon MNOs earned CFA21.5B on customer float** | Oct 10–20 | Kenya's VASP regime entered compliance phase with November licensing deadline — rulebook **bans paying interest on stablecoins**; Kenya cleared 19 FATF items, targeting April grey-list exit. Stanbic Bank Ghana + Hong Kong's RD Technologies exploring stablecoin Ghana–Asia trade settlement — a bank-led corridor in the premium-duration market. Cameroon's Orange Money/MTN MoMo earned CFA21.5B interest on safeguarded customer funds — direct evidence the EM float-yield pool is harvested by MNOs (P9's incentivized de-platformer). | **MED-HIGH** | Africa | Card 1 (Ghana gets bank-led stablecoin challenger + yield-ban analog); P9 quantified; yield-ban perimeter widening beyond US

**[N15] Macro: Fed hold priced for Oct 27–28 (hike odds ~14%), December is the live hike; Ghana parallel wedge ~5%** | Oct 13–20 | Polymarket Fed hike probability ~14% for Oct 27–28 after Chair Warsh stayed silent; major brokerages expect next **hike in December** after hot PPI; El-Erian warns too many hikes priced. Ghana: interbank ~GHS11.67–11.78 vs forex-market ~GHS12.25–12.30 → official-parallel wedge ≈ +4.8–5.1%, consistent with +3.55% USDT premium. Deutsche Bank added Nigeria to frontier-FX watchlist, bullish naira. (NGN T-bill anchor correction in Part B: 15.90% not 16.84%.) | **MED** | Macro | P1 falsifier context (contraction pressure if Dec hike lands); Card 1 corridor weighting; NGN float-yield verified (revised level)

### D.2 Status changes to known items

1. **Aggregate stablecoin float ROLLED OVER: $304.1B (Oct 20) vs $306.4B seven days ago (−$2.3B w/w)** — DefiLlama API. Inside watchlist-v2 #3's <$310B confirm zone. Composition: USDT $183.01B (flat), USDC $72.26B (flat), USD1 $4.02B (−9%), USDG $3.07B, PYUSD $2.84B. CMC "$315B record" remains scope difference (reconciled in Part A).
2. **[D1]/OKXICE: objections hold at 9 firms** (AMBCrypto Oct 19 — superseded same-day by Ledger Insights' 16; see Part C).
3. **[D2]/GENIUS: OCC chief reconfirmed final rule "before end of October"** (Oct 15). Comment window closed Oct 19–20. No text yet.
4. **[W2]/marker-2: OKX 10% APY USDG still live and untouched**; Gate launched competing all-in-one money app (Oct 7) — yield-app playbook spreading venue-to-venue.
5. **[W3]/OPay & MNT-Halan: OPay raise sized ~$500M (IPO + private placement), Standard Bank cornerstone re-confirmed (Oct 14); MNT-Halan priced EGP 24.5/share (Oct 6), order book closed Oct 15 (biggest EGX book in years), debut imminent.** OPay NYSE pricing still expected mid-Nov.
6. **[P3] EM exit window widens beyond Africa: Mynt (GCash parent) listed on PSE at ~$7B valuation, oversubscribed** (priced ₱6.60 Oct 8, listed by Oct 19) — Asia joining the African IPO run.
7. **Listed-venue earnings: Bullish Q3 revenue +62% as trading cooled** (Oct 19); **Coinbase retail revenue −31%, leaning on institutions** (Oct 19) — flow-venue economics bifurcating pre-SEC decision.
8. **[F14] no new data** — Borderless 84% claim re-circulated Oct 16; [E7] Binance $433B Aug figure did not resurface (still Binance-reported).

### D.3 Handoff to Wave 2

(a) float now inside marker-3 confirm zone — feed analysis; (b) Coinbase×Thunes + Visa Direct production + JPM-Nigeria = three simultaneous attacks on the payout leg — feed discovery/engineering (Card 7 urgency); (c) Perpetuals PDC filing + bStocks/Ondo demand data = P8 stress test — feed analysis (watchlist-4); (d) Kenya stablecoin interest ban = yield-ban perimeter datapoint — feed engineering (whitespace #7/#8 risk register); (e) verify JPM merchant-bank licence grant (December target) next pass.

### D.4 Sources
Bloomberg JPM-Nigeria (Oct 20); Businessday/ecofinagency/RioTimes (Oct 9–20); Thunes/Coinbase PRs + CryptoBriefing (Oct 19); Finextra/PAWS/currencyanalytics Japan megabanks (Oct 15–19); CryptoSlate Cross River-RLUSD (Oct 16); The Block DriveWealth-RLUSD (Oct 14); AltcoinBuzz/Cointelegraph USD1 outflows (Oct 18–19); crypto.news Perpetuals filing (Oct 14); PR Newswire/Finance Magnates bStocks (Oct 14–15); MSN/KuCoin/CryptoTicker Ondo (Oct 14–17); Reuters/Coingape Gemini settlement (Oct 15–16); Straits Times/crypto.news/Bloomberg Taiwan (Oct 14–16); MSN/CoinDesk CME-CFTC (Oct 19); The Block/Forkast Visa Direct production (Oct 15–17); The Defiant Stripe×Plasma (Oct 14); Coingape/CrowdfundInsider/AMBCrypto Deutsche Bank + OCC debanking (Oct 14–16); Barron's BNY (Oct 15); ITWeb/StreetInsider Stanbic×RD (Oct 19–20); Vellum/FinanceFeeds Kenya VASP (Oct 10/Jul 27); TrendsNAfrica Cameroon float (Oct 16); cryptonews Polymarket odds (Oct 18); Reuters Factbox December hike (Oct 15); WSJ Warsh (Oct 16); BusinessDay DMO auction (Oct 15); ModernGhana BoG rates (Oct 13–19); Bloomberg DB NGN watchlist (Oct 19); DefiLlama API (Oct 20); The Paypers/Yahoo/fintechfutures/unbox.ph OPay/Mynt (Oct 8–19); Yahoo Bullish/Coinbase earnings (Oct 19).

---
*Findings bank complete. Wave 2 (discovery / analysis / engineering) reasons over Parts A–D.*



