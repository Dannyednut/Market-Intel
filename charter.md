# Market Intel — Program Charter

**Status:** Amended 2026-10-20 (Charter Amendment 001 — first user directive of record). Supersedes the informal charter in README §"How the program runs" where they conflict; all other program mechanics unchanged.

---

## 1. Identity & position in the Org

Market Intel is the **third pillar of an envisioned Org** (owner's framing, 2026-10-20). It is not a standalone research hobby and not a software product: it is the organization's standing intelligence function.

- ~~Pillars 1 and 2 of the Org are not yet defined by the owner.~~ **Superseded by Charter Amendment 002 (§6, 2026-10-20): the Org architecture is now defined.**
- The findings bank (`findings/`) is the **Org's institutional brain** — accumulated, verified, confidence-graded memory that outlives any single cycle or session. Every cycle must treat prior findings as assets to be maintained (verified, revised, killed) rather than re-derived.

## 2. Mandate (owner-confirmed, 2026-10-20)

> To provide strategic intel, discovery, actionable edges and opportunities across different market landscapes.

Scope remains multi-market — fintech, exchanges, and the cross-market infrastructure between them (stablecoins, RWAs, custody, macro-capital flows), with emerging-market (Africa-first) coverage as a standing focus.

The principal is **all three consumers at once**: decision-maker/investor, builder/founder, and strategic observer. This is now a hard design constraint on output, not a preference.

## 3. Tri-focal lens mandate (Amendment 001)

Every cycle brief from **Cycle 004 onward** must carry three explicit lenses over the same evidence base:

| Lens | Question it answers | Primary inputs |
|---|---|---|
| **Decision** | What should the Org watch, back, or avoid — and on what dated trigger? | Watchlist markers, kill triggers, valuation/exit datapoints |
| **Builder** | What could the Org actually build, position, or structure — entry sequence and timing? | Strategy cards, whitespace map, exclusivity/contract windows |
| **Map** | What is actually true about the landscape right now, independent of what we do? | Verified findings, problem registry (P#), implication chains |

Rules:

1. Lenses are **layers, not silos** — one evidence base, three projections. A claim appearing in only one lens must be traceable to the shared findings bank.
2. The **Map lens is authoritative**: if a Decision or Builder statement contradicts a verified finding, the finding wins and the statement gets revised or killed.
3. Every Decision-lens item carries a **dated trigger or explicit "no trigger" status**. Undated "watch this" items are forbidden.
4. Every Builder-lens item names its **capital posture** (deploy / stage-gate / zero-capital wedge) and its expiry condition.

## 4. Initial lens re-projection — Portfolio v3 (worked example, 2026-10-20)

First cut of the current portfolio through the three lenses. Cycle 004 re-renders this on fresh evidence.

### Decision lens (allocate / watch-to-decide / avoid)

- **Back:** Card 4 (Warehouse-to-IPO credit platform) remains the anchor — clock-free, exit leg broadened beyond Africa (OPay ~$4B target, Mynt ~$7B PSE listing = EM exit window widening). Float add-on economics (~44bps/10-day, decaying) are price-the-entry, not count-on-forever (P12).
- **Watch-to-decide (dated):** Oct 27 IST Coalition NYSE event → read-through on Card 6; Oct 31 OCC final-rule target (kill trigger #1); Nov 3–8 OKXICE objection-window expiries (16/20 threshold — Card 2/6 gate cluster); Nov 12 EBA/USDC; mid-Nov OPay NYSE pricing (marks Card 4's exit model); Dec 6 Nasdaq 23×5 launch (Card 2 decay gate).
- **Avoid:** distributor-yield products inside the widening ban perimeter (CLARITY dead 49–50, Kenya ban live Nov, ECB pushing MiCA widening — P11); second-source tokenized-credit platforms (category still single-issuer >$2B); head-on competition with the $4.2B Bullish–Equiniti consent stack.

### Builder lens (entry structures & sequencing)

- **Build order #1 — Card 7 (Payout-Leg Holdco):** exclusivity-first, floor-priced tolls (10–60bps vs Mavapay's 10–50bps wholesale floor), 2-quarter front-load against the 12–15mo Circle–Tazapay close clock. Governing logic of the cycle: *durable edges are contracts signed before windows close, not spreads owned.*
- **Build order #2 — Card 6 (Consent-Administration Substrate):** zero-capital wedge; do not compete with coalitions, administer what they make mandatory (SIFMA opt-in would convert consent administration into a compliance utility). Oct 27 event is a free look — no capital before it.
- **Stage-gated:** Card 2 (session-bridge) — capital only after the three-gate cluster clears; residual edge = weekend/holiday bridge + non-objected tokenized names.
- **Rider-only:** Card 3 (yield routing) — never standalone; perimeter monitored under P11. Card 1 revised: wholesale floor-priced rails + float rider, Ghana weighted on the 4.8–5.1% wedge.

### Map lens (landscape truth, October 2026)

- **Compression is the cycle's governing thesis:** every Cycle-002-era moat compressed within one week — three heavyweights bid for the payout leg (Thunes×Coinbase, Visa Direct production, JPMorgan Nigeria onshore entry).
- **Float and flow have diverged in both directions:** aggregate float rolled over to $304.1B (inside the <$310B confirm zone) while monthly transfer volume grew +36% m/m; the buyer of last resort for float economics — banks — went multipolar (Japan megabank trio PoC, Cross River/RLUSD).
- **Issuer consent institutionalized:** 1→16 objectors in 16 days, 17/63 symbols removed pre-launch, Nasdaq self-opt-out, SIFMA pushing opt-in + universal opt-out. There is **no pending SEC decision** — the gates are objection mechanics, possible amendment, and venue go/no-go.
- **Yield-ban perimeter is globalizing** (P11) and **float yield is decaying** (P12: NGN anchor 15.90% vs stale 16.84%, MPR −350bps) — two rented moats expiring on observable clocks.
- **EM exits bifurcating wider:** the window is no longer Africa-only (Mynt/GCash PSE ~$7B oversubscribed); JPM's onshore Nigeria entry validates whitespace #1's home market.

## 5. Governance

- **Steering:** owner directives (like this amendment) enter the next wave as top-priority inputs and are recorded in the worklog. Directives may add scope, kill scope, or re-rank the portfolio.
- **Cycle protocol unchanged:** ping-triggered long sessions; Research → Discovery → Analysis → Engineering waves; synthesis into PDF + markdown brief; archive to this repository; worklog = program memory.
- **Cycle 004 queue (armed):** OCC rule-text reading (Oct 31 target); Oct 27 IST event read-through; objection-window expiries Nov 3–8 vs ≥30-name gate; EBA/USDC Nov 12; OPay pricing mark; Nasdaq Dec 6 session-share baseline; Ghana Dec regime text; JPM licence grant; live exclusivity term-sheet pricing vs Mavapay floor; **first brief rendered under the tri-focal mandate**. Amended by §6.5.

---

## 6. Charter Amendment 002 — Org architecture defined; brain-led expansion (2026-10-20)

### 6.1 The three pillars

| Pillar | Project | Status | Role |
|---|---|---|---|
| **1 — Foundation** | [SRW3](https://github.com/Dannyednut/SRW3) (`Dannyednut/SRW3`) | In research | Formal-verification research: abstract K/KEVM model with commitment gates (`<committed>`/`<prospective>`), invariants, effect-completeness (`wfCheck`), lineage, authority/policy cells; three-app binding scope **Oracle / Lending / Liquidator**. The correctness foundation on which Pillar 2's DAO governance will be modeled. |
| **2 — Engine** | [Edge-Engine](https://github.com/Dannyednut/Edge-Engine) (`Dannyednut/Edge-Engine`) | Narrow project, in development (paper-trading only, not live, not audited) | Arbitrage engine: 33 strategies / 19 running across Hyperliquid, Ethereum, Solana, HyperEVM, 8+ CEX/DEX venues. Current unique edge: **VOOI price-spread arb on private-AI-company perps** (alias markets sharing Hyperliquid's USDC margin pool; MEXC→venue legs; ~90% 2.5-min persistence claimed, paper). Tier-2 VOOI funding arb; Tier-3 HyperEVM kHYPE carry + Euler lending. `AgentVault.sol` exists; go-live awaits principal approval. Trajectory: expand into a **DAO following the model of its foundation (SRW3)**. |
| **3 — The Brain** | Market Intel (this program) | Operational — 3 cycles complete | Strategy and business operations of the envisioned org flow from here. |

### 6.2 Governing principle — brain-led expansion

Owner directive (2026-10-20): *"The strategy and business operations of the envisioned organizations will mostly come from its third pillar — Market Intel: The Brain. The brain is not limited to the scope of the organization at any point, but the expansion of the org is dependent on the capacity of the brain's intelligence and discovery."*

Operational translation:

1. **Research scope remains unbounded by org scope.** The org follows the evidence; the brain does not follow the org.
2. **New standing Discovery output — expansion theses:** each cycle's Discovery wave must produce evidence-backed, falsifiable cases for where the Org should move next (new market, capability, or structure), each carrying a capital posture and a kill condition. This is the mechanism by which brain capacity converts into org expansion.
3. **Strategy cards are org business-ops drafts.** The Brain's Engineering outputs are first-class organizational artifacts, not internal analysis.

### 6.3 Pillar-support duties (new standing workloads, tagged in all future outputs)

- **[P2-FEED] Edge-Engine pipeline:** intel products relevant to live/latent strategies are tagged and routed. Initial crosswalk: issuer-objection map ↔ TokenizedEquity arable-symbol set; stablecoin float/flow ↔ StablecoinDepeg + margin-pool monitors; Hyperliquid/HYPE ecosystem risk ↔ kHYPE carry; venue-risk watch (VOOI, MEXC, Backpack, Hyperliquid) ↔ counterparty exposure; funding-rate regimes ↔ funding arb.
- **[P1-WATCH] SRW3 domain:** formal-verification landscape (K ecosystem, KEVM, audit market, competing verification stacks) monitored for positioning as SRW3 matures.
- **New standing landscape — private-AI-company equity perps:** Pillar 2's current unique edge lives in alias/perp markets on private AI companies. The Brain opens this as a standing landscape: market structure, oracle/settlement mechanics, counterparty and venue risk, regulatory posture, and above all the **durability of the spread** (structural vs transient). Cycle 004 carries the first scan.
- **[DAO-WATCH] Pillar 2 trajectory:** regulatory and governance-model intel for the future DAO (legal wrappers, DUNA/MiCA posture, treasury-management practice, governance-framework market).

### 6.4 Portfolio v3 pillar crosswalk (initial)

- **C2 session-bridge** ↔ [P2-FEED] TokenizedEquity / EquityPerpCrossVenue: the objection map *is* the engine's arable-symbol set; the Dec 6 clock is shared.
- **C6 consent-administration** ↔ [P2-FEED] + standalone construct: consent data is a raw input the engine needs.
- **C7 payout-leg Holdco** ↔ [P2-FEED]: stablecoin-rail health underwrites margin-movement legs.
- **C4 warehouse-to-IPO** ↔ Org capital formation / future DAO treasury trajectory.
- **C1 / C3** ↔ EM rails + yield-perimeter (P11) for org operating footprint.

### 6.5 Cycle 004 queue — amended (adds, all carried triggers unchanged)

1. **First private-AI-equity-perps landscape scan** (market structure, oracle/settlement, venue/counterparty risk, spread durability) — [P2-FEED], highest added value.
2. **Formal-verification market scan** — [P1-WATCH].
3. **DAO-formation intel sweep** — [DAO-WATCH].
4. **Venue-risk baseline** on VOOI / MEXC / Backpack / Hyperliquid — [P2-FEED].
5. **Objection-list → Edge-Engine arable-symbol deliverable** — [P2-FEED], direct pipeline artifact.
