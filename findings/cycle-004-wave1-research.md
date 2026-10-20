# Market Intel — Cycle 004 · Wave 1 Research Findings (Pillar-Support Landscapes)

**Wave:** C4 Wave 1, executed 2026-10-21 (4 parallel research agents; full reports archived in `findings/cycle-004-wave1/`).
**Charter basis:** Amendment 002 §6.3 standing duties ([P2-FEED], [P1-WATCH], [DAO-WATCH]) under the scope guard — additive to, never narrowing, the generalist mandate.
**Confidence grades:** A = primary/official · B = 2+ independent outlets · C = single outlet · D = unverified.
**Finding IDs:** `Q#` keyed to agent (4a/4b/4c/4d) per Part below.

---

## Part A — Private-AI Equity Perps (C4-1a) · [P2-FEED] · NEW STANDING LANDSCAPE

**[Q1] The market is real, large, and multi-venue — not a niche.** | Grade B/A
OPENAI and ANTHROPIC perps trade live on at least 5 venues simultaneously (MEXC, Gate, Hyperliquid HIP-3 "io" deployer, Lighter, Robinhood-EU), plus pre-IPO products at OKX, Coinbase, Binance, Kraken, BloFin, Bitget and dated 2027-expiry futures on MNX (MegaETH). A dozen more private names trade: Moonshot/Kimi, Oura, Unitree, Cerebras, MiniMax, Zhipu, Shein, Neuralink, Anduril, Kalshi, YMTC. SpaceX went public (SPCX, ~2026-06-12 at ~$1.75T); legacy pre-IPO contracts now track the public share. Live OI 2026-10-21: HL io:ANTH $42.5M (deepest), xyz:SPCX ~$132M, xyz:CBRS $34.7M, Gate OPENAI $7.3M, Robinhood OPENAI $6.0M / ANTHROPIC $8.1M.

**[Q2] BASELINE CORRECTIONS — engine-critical (live API pulls ×2, 2026-10-21).** | Grade A
1. "$34B/$18B deep OI on Robinhood" — **FALSE by ~3 orders of magnitude.** Actual: $6.0M (OPENAI) / $8.1M (ANTHROPIC). Suspected units bug in the engine's data pipeline.
2. "MEXC→Gate 10.95% spread" — **NOT REPRODUCIBLE.** Live: 0.06–0.09% (Gate $1,481.2 vs MEXC $1,482.6 on OPENAI). Stale or mis-derived.
3. "MEXC→Robinhood 4.73%" — **≈ CONFIRMED** (OPENAI: Robinhood $1,556.8 vs MEXC $1,482.6 = +5.0%; ANTHROPIC ≈ +2.5%).
4. "Alias markets share Hyperliquid's USDC margin pool" — **TRUE ONLY FOR HL HIP-3 legs.** Not across MEXC/Gate/Lighter (separate margin engines everywhere else).
5. **Unit-convention traps are live:** Gate lists the same company (Moonshot AI) as KIMI $7.78 AND MOONSHOT $65.45 (8.4× unit difference) while MEXC KIMISTOCK = $65.72. Naive ticker matching fabricates spreads. Legacy delisted-but-frozen HL markets (vntl, io:MOONSHOT) still print zombie prices.
6. Live dislocation confirmed on second pull: premium cluster (Lighter/Robinhood/Gate/HL ~$1,921–1,933 ANTHROPIC) vs MEXC discount ($1,877–1,879), ≈3.0% Lighter−MEXC.

**[Q3] Spread durability: STRUCTURAL, with an abrupt end-date approaching.** | Grade A/B
Structural because: (a) **no shared underlying exists** — every venue runs its own synthetic oracle (Kraken: self-referential smoothed index, mark clamped ±0.25%; Gate: internal index with `funding_rate_limit 0.000001` — funding is institutionally prevented from policing the basis; OKX cites Forge Global prints; HL HIP-3: deployer-defined oracle); (b) access segmentation is codified (Kraken excludes US/EEA/CA/AU/NZ; leverage 50x offshore vs 5x retail venues); (c) premia persisted for months (CoinGecko 2026-09-02: perps 42–106% above secondary-market implieds); (d) even Robinhood↔Lighter — same corporate family — holds a persistent ~1.0% gap. **But the convergence forcing-event is weeks away: Anthropic confidentially filed its S-1 on 2026-06-01 with a Nasdaq target of November 2026.** SpaceX precedent: Binance converted to public-stock index on 30-day notice, Gate delisted, Kraken converted to xStocks. Conversion can rebase marks and strand premium with either side; MEXC's ANTHROPICUSDT settlement terms are **undocumented — highest-priority unknown**.

**[Q4] Issuer nullification risk — the underlying's legitimacy is impaired at the root.** | Grade B
Anthropic publicly warned (2026-05-12/15) that unauthorized pre-IPO share sales **are void** and "may be worth exactly nothing," specifically calling out **Forge Global and Hiive**; OpenAI issued parallel warnings. Several venues' oracles cite exactly those secondary-platform prints. The chain perp → secondary print → possibly-void transfer is legally fragile; further issuer shocks are possible pre/at IPO.

**[Q5] Oracle transmission shock has a live precedent.** | Grade A
One anomalous SK Hynix print (one share, Seoul, 2026-07-28) drove a Hyperliquid HIP-3 equity perp −18.7% instantaneously and liquidated $57–80M across ~960 accounts via shared ADL — crypto-style auto-deleveraging hit equity-perp positions. Single-print → cascade transmission is proven in this asset class.

**[Q6] Regulatory arc: onshore unapproved by default; enforcement via fraud, not product.** | Grade A/B
CFTC's Kalshi Order (2026-05-29) puts equity/private-valuation perps under case-by-case Reg 40.3 review; CME sued CFTC (2026-06-18) arguing perps are swaps; Hyperliquid pitched the SEC (2026-08); Citadel urged SEC oversight (2026-09). Pre-IPO enforcement is arriving through the private-markets side (Linqto bankruptcy 2025-07-19; ex-CEOs charged over $450M fraud 2026-09-02; SEC founder charge 2026-10-11; Forge Securities under investigation 2026-03-12). Offshore perps uncharged as a class so far. Onshore legitimization forming fast: OKX SEC filing for 63 tokenized stocks (2026-10-02), SEC five-year tokenized-stock sandbox (2026-10-09), Perpetuals.com filing (2026-10-14).

**Watch (→ Wave 1b / C005):** Anthropic IPO conversion mechanics per venue (MEXC terms undocumented); Robinhood in-app private-name verification; funding/mark history for the persistence claim; HIP-3 deployer health (TradeXYZ >90% of HIP-3 OI); venue unit-normalization table build-out.

---

## Part B — Formal Verification Market (C4-1b) · [P1-WATCH]

**[Q7] Demand has shifted to exactly SRW3's layer.** | Grade A/B
2025 DeFi losses $680.3M (+27% y/y; median $1.5M/incident); **89% of 2025 DeFi protocol losses were protocol-logic exploits** (private-key compromise down to 8.1%). H1 2026: $1.315B across 344 incidents (record count). The market is moving from "find my bug" to "prove my rules" — specification-level problems (invariants, effect completeness, authority/policy), not code typos.

**[Q8] The whitespace is CONFIRMED: nobody sells runtime-enforced verified gates.** | Grade B (negative result, 16-query sweep)
Closest analogues are proof-optional: Hypernative Guardian (heuristic pre-transaction policy enforcement) and Certora's continuous re-verification (CI-style). An Oct 2026 academic preprint (arXiv 2610.22913) proposes runtime compliance evidence — conceptual validation, zero commercialization. **Authority/policy cells, lineage binding (proof ↔ deployed artifact), and effect-completeness checks have no vendor language anywhere.** These are SRW3's exact mechanisms.

**[Q9] Certora is converging on SRW3's territory from the pre-deployment side.** | Grade A (vendor claims)
$196.5B TVL protected, 14 of top-20 DeFi protocols, ~150 audits in 2025, ~40 researchers (25 PhDs); continuous engagements (Aave 5+ yrs, Compound 5+ yrs, Sky 4+ yrs); its own 2025 trend list: "increased focus on protocol-level invariants," "expanded scope to deployment configuration, governance, and operational security." **Race risk: 12–18 months** if Certora adds a runtime component.

**[Q10] K/KEVM stack health: application layer alive, core core-watching.** | Grade A (GitHub, 2026-10-20)
KEVM master commits 2026-10-05; Kontrol (K+KEVM+Foundry FV, free/open-source) commits 2026-10-15 and is edging toward hybrid static/runtime reasoning ("external computation" — loading execution transcripts). **K core master dormant since 2026-06-18** (was weekly through H1) — branch strategy, staffing, or center-of-gravity shift to Pi Squared (K→ZK, $12.5M Polychain seed); watch item. Lean 4 is rising fast (SP1 zkVM chip proofs by Nethermind+Succinct; first Lean 4 proof of OZ reentrancy-guard vs production Solidity, Jun 2026) — K's moat vs Lean is gas-level EVM conformance.

**[Q11] The canonical case study is on record.** | Grade B/C
Aave CAPO oracle misconfiguration (snapshot misalignment) forced **$21.7M wrongful liquidations on 2026-03-10** through an automated risk pipeline — a textbook Oracle/Lending/Liquidator failure of exactly the class SRW3's binding scope targets. Post-mortem = collect.

**[Q12] Economics: $50k–200k FV engagements; capacity constraints at the incumbents.** | Grade C
Top-tier audit band $80k–300k+; RV "premium-priced" with 8–20 week lead times (room for a new entrant); Kontrol free/open-source; Certora monetizes SaaS + services; spec-writing = 30–50% of effort (automatable). Who pays: L1 foundations, blue-chip DAO treasuries, insurers as gatekeepers.

**Watch (→ C005):** K core repo pulse; Certora runtime moves; Hypernative spec-ingestion; Aave CAPO post-mortem; EF grant rounds (FV track); ERC-8319 progression; Pi Squared launches; Lean-vs-K protocol-modeling contest.

---

## Part C — DAO Formation (C4-1c) · [DAO-WATCH]

**[Q13] "Verified-gates DAO" whitespace CONFIRMED — moderate-to-high conviction.** | Grade B (negative result)
Component pieces all exist and are respected: Aave Governance V3 is Certora-verified (lifecycle invariants); Aera ships policy-governed, runtime-constrained treasury vaults ("DAO-approved policy" — no formal specification claim). But an integrated **"formally specified constitution → verified governor → runtime-enforced treasury mandate"** does not exist as a product or named practice anywhere in the sweep. The differentiator for Pillar 2's DAO is the **specification layer** — the machine-readable constitution whose compiled gates are provably equivalent to the spec.

**[Q14] Governance attacks are now the top treasury threat — the demand catastrophe is on record.** | Grade B
**BonkDAO lost ~$20M on 2026-07-06** — attacker bought ~$4.4M of BONK for voting power; only 7 wallets voted. Binance security intercepted another malicious proposal (~$1.2M, detected 2026-08-18). These are pure token-vote treasury drains through legitimate rails — exactly the failure class verified commitment gates + quorum invariants + runtime treasury mandates neutralize. (Cross-ref Part B: same conclusion from the verification side.)

**[Q15] Regulatory posture: US détente on DAO entities, rulemaking era, vault shares inside the securities perimeter.** | Grade A/B
CLARITY failed Senate cloture 49–50 (2026-09-15) — same datapoint as the C003 P11 record; locus shifted to SEC/CFTC rulemaking. Atkins token safe harbor (2026-03-17) + exemptions proposal (2026-08-18: Part 228, $5M startup tier, Form TR). **Peirce vault statement (2026-07-22): vault interests can be investment contracts — managerial discretion is the trigger.** A trading DAO's vault shares sit squarely in the securities perimeter when strategy is discretionary; structure matters. ESMA (2026-09) proposes a narrow statutory DeFi definition + a regulated "DeFi gatekeeper" CASP service; MiCA Recital-22 divergence flagged as "decentralisation washing."

**[Q16] Wrapper and treasury truth for the DAO trajectory.** | Grade A/B/C
Wyoming DUNA adoption is tiny (~3 orgs in 18 months: Syndicate SNC, Uniswap DUNI, "WYDE" uncorroborated) but productization is appearing (OtoCo auto-upgrades UNA→DUNA at 100+ holders). Real volume is offshore: Cayman foundation companies 1,300+ by end-2024 (+70% y/y), 400+ new in 2025, CARF reporting from 2026. For a US-origin trading DAO: DUNA (governance) + LLC (ops) pair, or Cayman foundation for treasury/holdco. DAO treasuries ≈ $26–28B across 13,000+ DAOs; ~220 DAOs hold >$1M; fewer than 80 "truly active." Professional mandates are institutionalized (Karpatkey/KPK for Balancer — H1-2026 closed $7.7M vs $12.4M, fees waived, 2-yr runway policy; Steakhouse; Aera). Precedent risk: unwrapped DAO = general-partnership exposure (Samuels v. Lido DAO).

**Watch (→ C005):** SEC Reg Crypto-Assets proposed rule text (does the safe harbor cover treasury diversification?); Wyoming SOS DAO-LLC count (data gap); MiCA review outcome; BonkDAO post-mortem/enforcement follow-on; Aera adoption footprint (nearest-neighbor competitor); CLARITY re-file timing.

---

## Part D — Venue-Risk Baseline (C4-1d) · [P2-FEED]

**[Q17] VOOI — Grade D transparency; orchestration layer only, never custody.** | Grade A (self-attestations verified)
Non-custodial aggregator routing to venue-native accounts (Hyperliquid, Kinetiq/trade.xyz, Lighter, Robinhood, Aster, Extended, Ondo + CEX futures via user API keys). First-party admissions: "not regulated or licensed by any financial regulatory authority"; T&Cs name **no legal entity**; full docs corpus (226,887 bytes) contains **zero** mentions of "audit" or "security review"; self-reported "$30B+ volume" unverified; DefiLlama on-chain TVL $14.7k. **Go-live rule: verify the planned $25k "VOOI deposit" lands in venue-native accounts with VOOI holding nothing but trade-scoped API keys — otherwise route venue-direct.**

**[Q18] MEXC — Grade C+: functioning and liquid, with a confirmed wrongful-freeze pattern.** | Grade B
Monthly self-published PoR (Oct 2026: BTC coverage 294%; Sep: 297% — hygiene signal, not proof). **Confirmed pattern:** $3M "White Whale" wrongful freeze (apology 2025-11-01), dispute reignited 2026-01-07, $340k account-hack complaint 2026-09-28, API-key/freeze interaction 2026-09-29. Exotic-listing risk appetite: pre-IPO perps incl. ANTHROPICUSDT. **Go-live rule: spread-leg balances = working-capital only, automated same-day sweeps, API keys without withdrawal permission.**

**[Q19] Hyperliquid — Grade B: platform solvency intact; risk is market-structure, not solvency.** | Grade A (APIs)
HYPE $80.08 / $17.81B mcap (2026-10-20), 30d −14.2% (correcting from Sep 22 peak $96.63 — correction to the engine's "3.5x'd overnight" note: max 1.9x inside the 130-day window; the 3.5x must reference an earlier-2026 base, unverified). HLP TVL $178.2M, −28.4%/90d — shrinking, not failing; the "−50% 30d APR" claim is unresolved (no public APR feed). 2026 incidents are market-structure (SK Hynix oracle anomaly → $57M liquidations Jul 28; user drain $738.6k Sep 9; JELLY meme $6.2M exploit Oct 11) — no platform-level solvency event. Constructive CFTC path (Aug 2026); bridge TVL $6.75B intact.

**[Q20] HyperEVM legs are thin — cap positions.** | Grade A/C−
Kinetiq/kHYPE healthy: $841M TVL, APY ~1.99% (30d mean 2.02%). **Euler V2 on Hyperliquid L1 holds only $1.77M** (peak $4.28M Mar 2026) — exclude from go-live paths if still <$2M at execution. HyperSwap V3 $10.4M; Ramses CL $11.0M — 5-figure-notional caps. April 2026 HyperEVM outage precedent (Binance Square 2026-04-01) + Purrlend $1.5M exploit (2026-04-25).

**[Q21] Backpack — Grade B−: growth + US regulatory signaling, young-venue discount.** | Grade B/C
$1B daily volume 5 days into incentive "Pre-Season" (2026-10-09 — sustainability unproven); former SEC Acting Chairman Piwowar + Multicoin's Samani on Backpack US board; no incidents found; custody/insurance unverified this cycle.

**Go-live risk ranking for a ~$35k allocation:** 1) Hyperliquid Core (margin home), 2) HyperEVM (capped), 3) Backpack (medium), 4) MEXC (working-capital-only + sweeps), 5) VOOI (signed-instruction layer only, custody path must be verified).

**Watch (→ C005):** MEXC Nov PoR + freeze complaints; HLP APR ground truth via Dune; HL insurance-fund size (gap); HyperEVM outage recurrence; Euler TVL check; VOOI Dune volume + any audit/entity disclosure; Backpack unlock/volume decay; CFTC-SEC perps harmonization (affects Backpack US push + MEXC product-removal risk on hedge legs).

---

## Cross-Wave Synthesis Notes (for Wave 2 analysis)

1. **One weak chain runs through everything:** private-market prints (Forge/Hiive — issuer-declared-void channels [Q4]) feed synthetic oracles ([Q3]) which back perps liquidatable by single prints ([Q5]). The private-markets data chain is the stack's weakest link and a candidate structural problem (provisional **P13: synthetic-exposure settlement legitimacy**).
2. **Unit fragmentation is a second candidate problem (provisional P14: venue unit-convention fragmentation)** — fake spreads from unit mismatch are a data-integrity risk to any cross-venue strategy ([Q2.5], Gate KIMI/MOONSHOT 8.4×).
3. **Parts B and C independently confirm the same whitespace:** runtime-enforced verified gates ([Q8] zero vendors; [Q13] zero DAOs) — with two live demand catastrophes on record (Aave $21.7M oracle misconfiguration [Q11]; BonkDAO $20M governance drain [Q14]). SRW3's positioning has never been clearer.
4. **Engine go-live conditions converge from all four reports:** unit normalization before any cross-venue spread trust ([Q2]); MEXC working-capital-only ([Q18]); VOOI custody-path verification ([Q17]); Euler exclusion check ([Q20]); an IPO-forcing-event plan for ANTHROPIC conversions weeks away ([Q3]).
5. **Cycle 003 landscape feeds this wave:** the onshore legitimization track (SEC tokenized-stock sandbox, OKX/Perpetuals filings) is the same P8 consent-institutionalization force seen from the offshore side — one regulatory perimeter hardening, two products converging.

**Candidate new problems for full formalization in Wave 2:** P13, P14 (above). **Candidate expansion thesis (§6.2 duty):** "runtime-enforcement layer for synthetic-markets oracles and DAO treasuries" — evidence in [Q8]+[Q13]+[Q11]+[Q14]; capital posture zero-to-low (research/prototype); kill condition: Certora ships a runtime-enforcement product first.
