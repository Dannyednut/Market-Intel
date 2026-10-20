# DAO Formation Intelligence — Sweep (Cycle 004)

**Program:** Market Intel, Cycle 004 Wave 1 — Task C4-1c (DAO-WATCH support, Pillar 2)
**Sweep performed:** 2026-10-20 (UTC). Report dated for cycle day 2026-10-21.
**Method:** ~14 web search queries + direct primary-source fetches (SEC PDF, ESMA PDF, EC consultation PDF, GitHub repos, governance forums, vendor docs). SEC.gov HTML was rate-limit-blocked; SEC content captured via search-result metadata + static PDF fetch + secondary legal press.
**Confidence grades:** A = primary/official · B = 2+ independent outlets · C = single outlet · D = unverified/uncorroborated.

---

## 1. Executive snapshot (≤10 bullets)

- **US "verified-governance" runway is real but legislative clarity stalled.** The CLARITY Act passed the House 294–134 on 2025-07-17, cleared Senate Banking 2026-05-14, then **failed a Senate procedural vote 49–50 on 2026-09-15** — regulatory weight has shifted to SEC/CFTC rulemaking (B).
- **SEC pivoted from enforcement to rulemaking:** Chairman Atkins unveiled a token **safe harbor / "Regulation Crypto Assets"** framework 2026-03-17 and a follow-on **exemptions proposal (Part 228: $5M startup exemption, $20M/$75M tiers, Form TR safe harbor) on 2026-08-18**; SEC+CFTC issued a **joint 5-category token taxonomy interpretive release in March 2026** (A for existence, B for detail).
- **DUNA adoption remains tiny but headline-making:** ~**3 notable DUNAs** after 18 months — Syndicate Network Collective, Uniswap "DUNI" (adopted by governance vote 2025-09-09/10), and "WYDE" (B for the count; A for DUNI and Syndicate individually; WYDE uncorroborated → C/D).
- **Offshore foundations are the real volume story:** Cayman foundation-company registrations **+70% YoY, 1,300+ by end-2024, 400+ new in 2025**, ahead of **CARF reporting starting 2026** (B).
- **MiCA's "sufficiently decentralized" carve-out is under formal review:** EC targeted consultation ran 2026-05-20 → 2026-09-30; **ESMA (2026-09) says "full decentralisation" (Recital 22) is divergently interpreted, flags "decentralisation washing," and wants a narrow statutory DeFi definition + a new regulated CASP "DeFi gatekeeper" service** (A).
- **Governance attacks are now the top treasury threat:** **BonkDAO lost ~$20M on 2026-07-06** (attacker bought ~$4.4M of BONK for voting power; only 7 wallets voted); Binance security intercepted another malicious proposal (~$1.2M, detected 2026-08-18). CSO quote: attacks are shifting to human/governance vectors (B).
- **Treasury AUM:** DAO treasuries ≈ **$26–28B across 13,000+ DAOs in early 2026**; ~**220 DAOs hold >$1M; fewer than 80 are "truly active."** Top: Uniswap ~$4.8B (mostly UNI), Sky/MakerDAO ~$3.9–5B+ ($8B+ collateral, diversified), Arbitrum ~$3B, Optimism ~$2.1B (B/C).
- **Professional treasury management is institutionalized:** Karpatkey/KPK (Balancer non-custodial mandate since BIP-103, H1-2026 review published 2026-08-14), Steakhouse (dYdX treasury SubDAO contender; Cayman Foundation entity), **Aera (policy-enforced, non-custodial treasury vaults with hooks/guardians)** (A for forum/vendor docs).
- **Formal verification of governance *components* exists (Aave Governance V3 is Certora-verified, with invariants over the proposal lifecycle); formal verification + runtime enforcement of a DAO's *operating rules as a package* (constitution → governor → treasury mandates) does not appear to exist as a product or practice.** Whitespace verdict: **YES — credible, unoccupied niche** (see §6).
- **For a trading DAO:** wrapper choice converges on Wyoming DAO LLC/DUNA (US) vs Cayman Foundation/Marshall Islands DAO LLC (offshore); Peirce's 2026-07-22 vault statement means **vault-share trading structures remain squarely inside the securities perimeter when there is managerial discretion** (B).

---

## 2. Legal wrapper map (jurisdiction / vehicle / adoption / fit for a trading DAO)

| Jurisdiction | Vehicle | Adoption (dated) | Fit for a trading DAO (assessed) |
|---|---|---|---|
| Wyoming, US | **DAO LLC** (W.S. 17-31, since 2021-07-01) | First DAO LLC: American CryptoFed (2021). No reliable public count of active DAO LLCs found in this sweep — Wyoming SOS entity database not crawlable here (**data gap**; see §9). Filing $100; annual $60 (C: terms.law guide, upd. Dec 2024). Structural issues: 1-year inactivity auto-dissolution trigger, mandatory public smart-contract disclosure (C: StateBay 2026-04-24) | **Good** — pass-through tax, purpose-built statute; but CFTC/SEC/IRS apply federal frameworks regardless; inactivity clause is a real risk for a slow-moving DAO |
| Wyoming, US | **DUNA** (SF0050, effective 2024-07-01) | ~**3 organizations in 18 months**: Syndicate (SNC — publishes DUNA financials, 2026-01-22, A), Uniswap **DUNI** (governance vote passed 2025-09-09/10, A), "WYDE" (C/D — single outlet). Requires 100 members minimum for DUNA status (C: daotimes; C: frblaw: UNA→DUNA conversion at 100+) | **Moderate** — nonprofit-only; suits protocol governance DAOs; a for-profit trading DAO would use DAO LLC instead, or DUNA for the governance layer + LLC for ops |
| Marshall Islands | **DAO LLC** (DAO Act 2022-12, amended 2023) | Established practice; 3 members min; >10% governance rights require KYC (C: StateBay). No fresh 2025-26 adoption counts found (**unverified**) | **Good for offshore/privacy** — English-common-law blend; banking historically challenging (C: terms.law) |
| Cayman Islands | **Foundation Company** | **1,300+ registered by end-2024 (+70% YoY); 400+ new registrations in 2025**; cited as most-deployed DAO treasury wrapper for top-100 DeFi; CARF reporting from 2026 (B: Cointelegraph + Cayman News Service/Cayman Finance + multiple) | **Best for treasury/holdco** — separate legal personality, established precedent, banking OK; CFC/PFIC complexity for US persons (C: terms.law) |
| Switzerland | **Association (Verein) / Foundation** | No dedicated DAO law; DLT Act 2021 backdrop; "Zug Crypto Foundations 60+" per one tracker (C: zugdao, 2026-03-05). Widely used for foundations of major protocols (C) | **Moderate** — good reputation/banking; not purpose-built; Swiss tax nuance (C) |
| UAE (RAK) | **RAK DAO / DARe** (launched 2024-10) | Legal personality for DAOs in free zone; 0% corporate tax on qualifying income (C: StateBay 2026-04-24). No independent adoption counts found | **Interesting** — most commercially practical purpose-built framework per StateBay; venue/counterparty comfort TBD |
| EU | None (MiCA governs services, not DAO entities) | MiCA review consultation 2026-05-20→09-30; ESMA push to define DeFi narrowly & regulate "gatekeeper" access (A: ESMA response 2026-09) | **Poor as wrapper; relevant as market** — a "fully decentralized" Recital-22 exemption is uncertain and being tightened, not loosened |
| BVI / Liechtenstein / Panama | Foundation/association variants | Listed as "usual options"; no 2025-26 adoption data found in sweep (**unverified**, D) | Secondary options |

**Key legal-risk precedent:** unwrapped DAO = general partnership risk — *Samuels v. Lido DAO* (N.D. Cal., Judge Chhabria) held Lido DAO plausibly a general partnership; active-participant liability claims allowed to proceed (B: Duane Morris alert + astraea.law). CFTC v. Ooki DAO (2022) remains the cautionary case for token-governed trading venues (B: StateBay + terms.law).

**US state-layer note:** Utah DAO LLC Act (2023) is the other purpose-built US state statute (C: lexyomlaw). An academic "Harmony Framework" (jurisdiction-neutral modular DAO law, published 2025-02) and a UK DAOLLP model exist on paper only; neither adopted (C: StateBay).

---

## 3. Regulatory posture (dated actions & statements)

**SEC (under Chair Paul Atkins; "Project Crypto" launched 2025):**
- 2025-04-30 — Crypto Task Force solicited written input "Navigating DAO Legality" (Opolis memo on file, arguing Limited Cooperative Associations) — evidence the Task Force formally studied DAO personality/securities treatment (A: sec.gov/files PDF).
- 2025-11-12 — Atkins outlines priorities under "Project Crypto" (B: MoFo client memo).
- 2026-03-17 — Atkins, DC Blockchain Summit: **"Regulation Crypto Assets: A Token Safe Harbor"** — previews startup exemption (≤4 yrs, ≤$5M), non-exclusive of Reg D/S; same week **SEC+CFTC joint interpretive release: 5-category crypto-asset taxonomy + Howey/investment-contract clarification** (A: SEC speech page exists; detail via B: Ledger Insights 2026-03-18).
- 2026-08-18 — Atkins statement "Fit-for-Purpose Exemptions": **Regulation Crypto Assets proposal — Part 228 rule text, $5M startup exemption, $20M/$75M tiers, Form TR safe harbor, blue-sky preemption** (A: SEC statement page; detail via C: astraea.law guide — **rule-text detail unverified against release**, grade for detail C).
- **FY2025 enforcement results** announced (press release 2026-34; content not fetchable in this sweep — the CFTC/SEC posture summaries below indicate the substance of the shift) (A: existence; content unverified).
- **DAO-specific enforcement in 2025-26: none found in this sweep.** The last landmark DAO settlements predate the window (Mango DAO/Mango Labs/Blockworks Foundation — MNGO offering + unregistered broker, settled 2024; recap article undated in capture → treat date as 2024, unverified, D on exact date). Status: "no new DAO enforcement actions located Oct 2025–Oct 2026" — **absence of evidence, not evidence of absence**.
- Commissioner Peirce, 2026-07-22 — **"Headstands and Summervaults: A Statement on Crypto Vaults and Lending Strategies":** vault *interests* can be investment contracts even when deposited assets are not; managerial discretion (strategy selection, curator choice, LTV params) is the trigger; investment-company/note/adviser regimes can stack; explicitly **not** a safe harbor (B: Practus analysis 2026-08-04; statement itself primary on sec.gov).

**CFTC:**
- 2025-04-08 — Acting Chairman Pham, Release 9063-25: enforcement realignment with DOJ digital-asset memo; "back-to-basics" (fraud/manipulation focus) (B: Hunton + Paul Weiss year-in-review).
- 2025-08-01 — **CFTC "Crypto Sprint"** announced to implement CLARITY-Act-style regime and the Presidential WG report (A: cftc.gov 9104-25).
- 2025 — Withdrawal of outdated "actual delivery" virtual-currency guidance (A: cftc.gov 9152-25). December 2025 "Digital Assets Directive" reported (C: gate.com wiki — **unverified**, D).
- Leadership flux: Quintenz nomination stalled (B: mvalaw/Law360); later references to "Pham and Michael Selig" statements (C/D — **chairmanship as of Oct 2026 unverified**).
- Historical anchor for DAOs: **CFTC v. Ooki DAO (2022)** — governance-token structure ≠ liability shield (B).

**Congress / EU:**
- 2025-07-17 — CLARITY Act (H.R. 3633) passes House 294–134 (B: eco.com + multiple).
- 2026-05-14 — Senate Banking Committee advances market-structure package (B: hodder.law).
- 2026-07-22 — Senate Republicans release updated CLARITY text (B: DWT).
- **2026-09-15 — CLARITY Act fails Senate cloture 49–50**; near-term locus shifts to SEC/CFTC rulemaking (B: DLA Piper 2026-09 + Orrick 2026-10).
- GENIUS Act (stablecoins) already enacted (2025) (B: eco.com).
- **EU:** EC MiCA review targeted consultation published 2026-05-20, closed 2026-09-30 (A: EC site + PDF); **ESMA response (2026-09)**: Recital-22 "full decentralisation" divergently applied; "decentralisation washing" risk; asks for narrow statutory DeFi definition or ESMA guidelines; proposes **new regulated CASP service = "access to DeFi"** (gatekeeper) (A). EBA and ECB/ESCB responses also filed 2026-09 (A: EBA/ECB PDFs exist).

**Treasury-token classification risk (synthesis):** even with the Atkins safe-harbor framework, governance tokens held *by the DAO treasury* remain double-exposed: (i) the token itself may be an investment contract where the DAO continues managerial efforts (LBRY precedent logic, C: chainscorelabs — careful, content-farm grade), and (ii) treasury diversification programs (selling native token) can be re-framed as unregistered distribution by an issuer-adjacent entity. DUNI's structure (governance layer as nonprofit DUNA + foundation ops) is the emerging template. No safe harbor yet covers a *trading* DAO's vault shares (Peirce statement, B).

---

## 4. Governance practice & failure catalog (last 12 months)

**Dominant patterns (2025-26 practice):**
- Stack mix (per ZUG DAO tracker table, 2026-03-05, covering 2024-25, drawing on Tally/Snapshot/DeepDAO): **Tally + Snapshot** (Uniswap, ENS, Gitcoin), **Aave** uses Snapshot + BGD Labs-executed Governor, **Aragon** (Lido), **Agora** (Optimism), **Compound Governor**, **Commonwealth** (dYdX) (C).
- **Optimistic/multisig councils + security councils:** Aave Governance V3 formalizes "guardian" emergency powers and cross-chain execution; Optimism's bicameral + security-council model continues (C: zugdao; B: Aave repo docs).
- **Delegated voting is the load-bearing wall:** academic work in the window — arXiv 2503.11940 (2025-03) on vote delegation using Uniswap as laboratory; arXiv 2510.05830 (2025-10) "Fairness in Token Delegation" (B: two independent arXiv preprints).
- **Turnout (2024-25 averages, % of delegated/circulating supply):** MakerDAO/Sky 15–25%, Uniswap 5–15%, Arbitrum 10–18%, Aave 8–18%, Optimism 20–35%, Compound 8–15%, ENS 15–25%, Lido 12–20%, Curve 25–40%, dYdX 10–15%, Synthetix 15–25% (C: ZUG DAO 2026-03-01/05). **Bimodal pattern:** routine proposals 3–8%; existential/fee-switch proposals 50%+ (Uniswap fee-switch vote 2024 >50%). Conflicting single-outlet aggregates: "17% average" (C: bullmonitor 2026) vs "below 5% average across major DAOs" (C: coincraft 2026) — **treat point-estimates with low confidence; per-DAO table is the better anchor**.
- Academic survey of voting-power concentration & participation apathy published in ACM (dl.acm.org/doi/full/10.1145/3777416, 2025/26) (B for existence).

**Failure catalog (Oct 2025 → Oct 2026):**
| Date | Incident | Mechanism | Loss | Source/grade |
|---|---|---|---|---|
| **2026-07-06/07** | **BonkDAO treasury drain** (Solana) | Attacker bought ~$4.4M BONK → voting power → passed malicious proposal → drained ~$20M in BONK; **only 7 wallets voted** | ~$20M | B (CryptoTimes 2026-07-07 + CryptoBriefing + multiple) |
| **2026-08-18 (detected), reported 2026-08-20** | Unnamed DAO malicious proposal (~$1.2M target) | Binance security flagged mid-flight (<48h to execution), froze deposits cross-platform; community voted it down; no loss | $0 (prevented) | B/C (CryptoBriefing 2026-08-20, named CSO quote) |
| **2025-12-14** | **FutureSwapX** governance exploit | Flash-loan vote manipulation | ~$500K | C (Verichains postmortem) |
| 2025-11 (context) | Balancer "incident" (referenced by KPK) | Referenced as cause of 2026 restructuring; details not swept here | n/a | A for reference existence (KPK forum post 2026-08-14); incident details **not verified in this sweep** |
| Aggregate | "Seven documented governance exploits 2020–2026 extracted >$325M" | Flash-loan votes, quorum acquisition, storage-collision bypass, oracle-gamed governance | >$325M cumulative | C (smartcontractaudit.com guide) |

**Read-through:** the two 2026 incidents were *pure token-vote treasury drains*, not smart-contract exploits — exactly the class a "verified commitment gate + runtime treasury mandate" would neutralize. BonkDAO's 7-wallet vote is the poster child for quorum/turnout gates.

---

## 5. Treasury management truth (AUM data, practice, service providers)

**AUM (dated):**
- Early 2026 total: **~$26–28B across 13,000+ DAOs**; ~220 DAOs >$1M; **<80 "truly active"** (B/C: Streamflow report 2026-05-28 citing Eco/DefiLlama).
- Q1 2026: DAOs crossed **$26B total treasury assets**; 6.5M+ token holders across largest networks (C: daotimes).
- 2025 estimates: ~$21.4B liquid / $24.5B total (C: CoinLaw). DeepDAO's "top $25B first" milestone reported (C: checkcryptonews citing DeepDAO; **DeepDAO site/API not directly reachable in this sweep** — grade C, date of milestone ambiguous).
- Top treasuries Q1 2026: **Uniswap ~$4–4.8B (predominantly UNI)**; **Sky/MakerDAO ~$3.9–5B+ (diversified; $8B+ collateral)**; **Arbitrum ~$3B (ARB + RWAs)**; **Optimism ~$2.1B (OP + stablecoin reserves)** (B/C: Streamflow citing Eco). Uniswap Foundation runs ~$45M/yr operating budget + ~$40M/yr grants (C via Streamflow citing Eco).
- Concentration: ~67% of DAO treasuries held in own governance token (C: theledgermind citing DeepDAO — **unverified**).

**What $100M+ treasuries actually do (observable practice):**
- **Two-track structure:** native token (long-term) + stablecoin reserves for runway; >80% of contributor payments in large DAOs executed by smart contracts (vesting/streaming rails) (B/C: Streamflow 2026-05-28).
- **Diversification policy:** Sky/MakerDAO is the flagship diversified balance sheet (RWA-heavy, $8B+ collateral); Arbitrum holding RWAs; OTC desks used for native-token diversification to avoid slippage (C: mintarex 2026; C: Streamflow).
- **Yield policy:** delegated non-custodial mandates into stablecoin/DeFi vaults — Steakhouse stablecoin vaults; Morpho curators; Enzyme; Aera policy vaults (B: dYdX forum comparison + vendor docs; C: markaicode tool-stack guide).
- **Spending mandates & runway targets:** Balancer/KPK: two-year gross stablecoin runway target, monthly performance reporting on governance forum (A: KPK post 2026-08-14).
- **Governance wrapper for the treasury:** dYdX "Treasury SubDAO" competition between Steakhouse and Karpatkey explicitly included **Cayman Foundation entity formation** and coverage model (A: dYdX forum, dated proposal).

**Service providers serving DAO treasuries:**
- **Karpatkey/KPK** — non-custodial strategic treasury management; Balancer (since BIP-103, late 2022); H1-2026: managed treasury closed June at **$7.7M (from $12.4M)** during post-incident restructuring; removed mgmt/performance fees (A: forum).
- **Steakhouse Financial** — treasury SubDAO proposals (dYdX), stablecoin vault curation (B/C).
- **Aera** — non-custodial, policy-governed treasury vaults: strategies submit via `submit()` against **DAO-approved policies**, configurable **hooks**, **guardians**, fee vaults, cross-chain (A: docs.aera.finance, live docs 2026).
- **Safe + Zodiac Roles** — custody/permissioning standard (C: markaicode; A: Safe ubiquity implied in all forum reports).
- **Streamflow, Superfluid-class streaming rails** — payroll/vesting automation (B/C: Streamflow 2026-05-28).
- Context: stablecoin market cap >$300B in 2026, the substrate for treasury yield programs (C: onchaintreasury.org 2026-03-09).

---

## 6. Verified-gates whitespace verdict

**Question:** does anyone formal-verify *governance itself* — verified governor models, runtime enforcement of treasury mandates, formal spec of DAO constitutions — as a package?

**Evidence FOR component-level verification (exists):**
- **Aave Governance V3 is formally verified by Certora** — CVL rules/invariants over the proposal lifecycle and cross-chain voting; Certora also reviewed the VotingMachine MerklePatriciaTrieVerifier fix (a minor voting-DOS was found and fixed, then verified; onboarded via on-chain Proposal 273) (A: aave-dao/aave-governance-v3 README + security/certora; B: DeepWiki mirrors).
- Invariant-testing culture around **OpenZeppelin Governor** (quorum edge cases, timelock, veto, upgrade paths) is documented as guidance (C: chainscorelabs guide).
- **Runtime enforcement of treasury policy exists in vault form:** Aera's policy-governed vaults (DAO-approved policies, hooks, guardians) are exactly "treasury mandate as runtime constraint" (A: docs).
- **Optimistic-verification modules exist:** Zodiac Reality/E reality modules (optimistic oracle-verified proposals) and Aragon OSx permissioned plugin systems are the runtime-gate lineage (D for current 2026 usage — not directly verified in this sweep; well-known prior art).
- **Academic layer exists:** Springer chapter "Formal Verification of Decentralized Autonomous Organizations" (LNCS 978-3-032-26752-8, 2026) — specification/verification challenges of DAO governance (A: Springer landing page).

**Evidence AGAINST an occupied niche (the package does not exist):**
- No vendor, DAO, or standard was found that offers **"formally verified DAO constitution → verified governor → runtime-enforced treasury mandate"** as an integrated product or as a named practice (negative result across all searches this sweep).
- The failures catalog (§4) shows treasuries dying through *legitimate* governance rails (7-wallet votes), i.e., verification of code correctness (Aave-style) does not address **specification of the rules themselves** — no one is shipping that specification layer.
- The verified-component practice (Certora) is marketed per-protocol, not as DAO operating-system governance; Aera enforces *a* policy but does not verify the *governor/constitution* above it.

**Verdict:** **Whitespace confirmed — moderate-to-high conviction.** The niche "a DAO whose operating rules are formally specified, whose governor is formally verified, and whose treasury executes only through runtime-enforced mandate gates" is unoccupied as of 2026-10. Adjacent pieces all exist and are respected (Certora on Aave Governance V3; Aera policy vaults; Zodiac/Aragon plugins; academic FV-of-DAO literature), which both validates feasibility and supplies the integration surface. For DAO-WATCH (Pillar 2): the differentiator to prototype is the **specification layer** (machine-readable DAO constitution whose compiled gates are provably equivalent to the spec), not another vault.

**Honest caveats:** (1) sweep depth was ~14 queries; a stealth project could exist (paper-trading world ↔ stealth is plausible); (2) "Formal verification" claims by content-farm sites (chainscorelabs et al.) were not independently validated; (3) K-Framework governance specs were **not found** — absence of evidence, not evidence of absence.

---

## 7. Hard data points (each with date + source URL + grade)

1. **Uniswap Governance adopted "DUNI," a Wyoming DUNA, as of 2025-09-09 (vote approved 2025-09-10)** — https://vote.uniswapfoundation.org/info (A)
2. **Syndicate Network Collective (a DUNA) published Q4/YE-2025 DUNA financials, 2026-01-22** — https://syndicate.io/blog (A, first-party)
3. **Wyoming DUNA: ~3 adopting organizations in first 18 months (Syndicate, Uniswap/DUNI, WYDE); DAO LLC Act effective 2021-07-01; DUNA effective 2024-07-01** — https://statebay.com/blog/dao-legal-wrappers-2026-jurisdictions-licensed (2026-04-24) (B for count corroborated by #1/#2; WYDE = C/D)
4. **Cayman foundation companies: +70% YoY, 1,300+ entities by end-2024; 400+ registered in 2025; CARF rules arrive 2026** — https://cointelegraph.com/news/cayman-islands-web3-foundation-companies + https://caymannewsservice.com/2025/12/daos-and-web3-business-booming-in-cayman/ (2025-12) (B)
5. **ESMA response to EC MiCA review (2026-09): "full decentralisation" (Recital 22) divergently interpreted; "decentralisation washing"; proposes narrow statutory DeFi definition + new CASP "DeFi gatekeeper" service** — https://www.esma.europa.eu/sites/default/files/2026-09/ESMA75-113276571-1721_Response_to_the_EC_consultation_MiCA_regulation_review.pdf (A)
6. **EC MiCA review targeted consultation: published 2026-05-20, comments closed 2026-09-30** — https://finance.ec.europa.eu/regulation-and-supervision/consultations-0/targeted-consultation-review-mica-regulation_en (A)
7. **SEC Chair Atkins "Regulation Crypto Assets: A Token Safe Harbor," DC Blockchain Summit, 2026-03-17; follow-up exemptions statement 2026-08-18** — https://www.sec.gov/newsroom/speeches-statements/atkins-remarks-regulation-crypto-assets-031726 and https://www.sec.gov/newsroom/speeches-statements/atkins-statement-regulation-crypto-assets-081826 (A for existence; detail via https://www.ledgerinsights.com/sec-chair-atkins-outlines-crypto-funding-exemptions-token-safe-harbor/ 2026-03-18, B)
8. **SEC+CFTC joint interpretive release: 5-category crypto taxonomy + Howey clarification, March 2026** — reported at https://www.ledgerinsights.com/sec-chair-atkins-outlines-crypto-funding-exemptions-token-safe-harbor/ (B; primary release not fetched — SEC.gov rate-limit)
9. **CLARITY Act: House 294–134 on 2025-07-17; Senate Banking 2026-05-14; Senate cloture FAILED 49–50 on 2026-09-15** — https://www.dlapiper.com/en/insights/publications/2026/09/senate-fails-to-advance-the-clarity-act + https://www.fintechweekly.com/news/what-is-the-clarity-act-digital-asset-market-structure-explained-2026 (B)
10. **CFTC "Crypto Sprint" announced 2025-08-01 (Release 9104-25); enforcement realignment 2025-04-08 (Release 9063-25)** — https://www.cftc.gov/PressRoom/PressReleases/9104-25 and https://www.hunton.com/blockchain-legal-resource/cftc-shifts-crypto-enforcement-priorities (A/B)
11. **Peirce vault statement "Headstands and Summervaults," 2026-07-22: vault interests can be investment contracts; managerial discretion is the trigger; not a safe harbor** — analysis: https://practus.com/crypto-vaults-and-onchain-lending-sec-securities-law-analysis/ (2026-08-04) (B; statement primary on sec.gov)
12. **BonkDAO: ~$20M treasury drain 2026-07-06; attacker spent ~$4.4M on BONK; 7 wallets voted** — https://www.cryptotimes.io/2026/07/07/bonkdao-hit-by-20m-treasury-drain-in-governance-attack-bonk-slides/ + https://cryptobriefing.com/bonkdao-treasury-governance-attack/ (B)
13. **Binance security intercepted malicious DAO proposal (~$1.2M) detected 2026-08-18; voted down; no loss** — https://cryptobriefing.com/binance-stops-malicious-dao-proposal-treasury/ (2026-08-20) (C→B edge, single outlet + named CSO)
14. **DAO treasuries ≈ $26–28B early 2026; 13,000+ DAOs; ~220 >$1M; <80 active; top-4 treasuries as listed in §5** — https://streamflow.finance/blog/dao-treasury-distribution-report (2026-05-28) (B/C)
15. **Aave Governance V3 formally verified by Certora (CVL invariants incl. proposal lifecycle, cross-chain voting; VotingMachine DOS fix verified)** — https://github.com/aave-dao/aave-governance-v3 (README, "Extensive properties checking (formal verification) procedure by Certora") (A)
16. **KPK (Karpatkey) H1-2026 Balancer treasury review: $7.7M at June-close vs $12.4M start-of-year; fees removed; 2-yr stablecoin runway policy** — https://forum.balancer.fi/t/kpk-h1-2026-review-for-balancer-dao/7094 (2026-08-14) (A, first-party forum)
17. **Turnout averages 2024-25 by DAO (e.g., Uniswap 5–15%, MakerDAO/Sky 15–25%, Curve 25–40%; routine proposals 3–8%)** — https://zugdao.com/tracker/dao-governance-activity-tracker/ (2026-03-01/05) (C)
18. **FutureSwapX flash-loan governance exploit, 2025-12-14, ~$500K** — https://blog.verichains.io/p/governance-attack-flashloan-vote (C)

---

## 8. Weak signals & anomalies

- **"WYDE"** appears exactly once (StateBay) as the third Wyoming DUNA adopter — no corroboration. Watch for it to surface or evaporate (D).
- **DUNA formation has gone productized:** OtoCo sells "(D)UNA" onchain — start as UNA, **auto-upgrade to DUNA at 100+ token holders** (https://www.otoco.io/duna, undated 2026 site). If UNA→DUNA auto-upgrade becomes standard tooling, the 100-member threshold stops being a barrier and DUNA adoption could inflect quietly (B/C).
- **A "second DAO wrapper" oddity:** Wyoming DAO LLC has a **1-year inactivity auto-dissolution trigger** — for a slow paper-trading org this is a real, unglamorous trap; DUNA/LLC hybrid structuring (DUNI-style) is the mitigation template (C).
- **Content farms are targeting this exact topic space** (tokenizationgovernance.com, confidentialdaos.com, chainscorelabs.com, markaicode.com — all claiming "SEC DAO guidance 2026" without citable primary docs). Noise signal: *someone* thinks "DAO compliance" is a high-value SEO vertical → demand-side signal, but zero evidentiary value (D).
- **SEC DAO-enforcement silence in the window:** 12+ months with no new DAO-named actions found, while the Task Force took written input on DAO legality (2025-04-30) and rulemaking replaced litigation. Either genuine détente or enforcement retargeting toward fraud-only cases (Paul Weiss: "back-to-basics") (B/A mix).
- **CFTC chairmanship ambiguity** in late 2026 sources (Pham vs Selig references) — unresolved in this sweep (D).
- **Turnout estimates conflict wildly** (17% avg vs <5% avg vs per-DAO 5–40%) — different denominators (delegated vs circulating vs eligible). Methodological caution for any DAO-WATCH KPI we adopt (C).
- **Governance-attack defense is being centralized by exchanges:** Binance freezing attacker deposits pre-execution (2026-08-18) worked — a de facto off-chain guardrail substituting for missing on-chain verified gates. Anomaly: CEXs becoming DAO emergency brakes (C).
- **Aera's docs read like the spec of our thesis** (policy-governed treasury vaults with hooks/guardians) but stop at "DAO-approved policy" — no formal specification or verification claim anywhere in the docs (A docs, negative finding).

---

## 9. Watch items for next cycle

1. **SEC "Regulation Crypto Assets" proposed-rule text** (Part 228 / Form TR) — pull the actual release from SEC.gov (rate-limited this sweep); confirm whether the safe harbor covers DAO treasury-diversification programs and vault shares. Trigger: Federal Register filing.
2. **CFTC chairmanship confirmation + any 2026 DAO/DeFi guidance** (incl. verifying the reported "December 2025 Digital Assets Directive" against cftc.gov).
3. **Wyoming SOS database crawl** for total active DAO LLCs + DUNA count (needs a scriptable approach or a FOIA/state data request; this sweep's gap).
4. **WYDE** and any 4th/5th DUNA adopter; OtoCo (D)UNA auto-upgrade volume if public.
5. **MiCA review outcome** (EC response to consultation, expected late 2026/2027): watch whether Recital-22 gets statutory definition and whether the "DeFi gatekeeper" CASP service becomes law — direct impact on any EU-facing DAO surface.
6. **BonkDAO post-mortem + litigation** and any SEC/CFTC follow-on — first test of whether 2026 governance drains trigger enforcement.
7. **DeepDAO AUM series** (site/API unreachable from here; retry via different network path or their data deals) to anchor a defensible treasury-AUM KPI; reconcile $24.5B vs $26–28B claims.
8. **Aera adoption footprint** (which DAOs run policy vaults in production) — nearest-neighbor competitor to Pillar 2's verified-gates concept.
9. **CLARITY Act S. companion re-file timing** after the 49–50 failure; any narrow decentralized-identity/decentralization-test amendments.
10. **Balancer incident (Nov 2025) full post-mortem** — KPK references imply treasury-impacting event; relevant to treasury-mandate design for our own engine.

---

## 10. Source list

**Primary/official (A):**
- Uniswap Foundation — DUNI: https://www.uniswapfoundation.org/duni ; https://vote.uniswapfoundation.org/info ; DUNI Q4-2025 financials: https://vote.uniswapfoundation.org/forum-article/7/duni-q4-and-year-end-2025-financial-statements-and-tax-update
- Syndicate blog (SNC DUNA financials): https://syndicate.io/blog
- Wyoming SOS — DAO FAQs: https://sos.wyo.gov/Business/Docs/DAOs_FAQs.pdf ; DAO LLC articles form: https://sos.wyo.gov/Forms/Business/LLC/DAOLLC-ArticlesOrganization.pdf
- SEC — Atkins speech 2026-03-17: https://www.sec.gov/newsroom/speeches-statements/atkins-remarks-regulation-crypto-assets-031726 ; Atkins statement 2026-08-18: https://www.sec.gov/newsroom/speeches-statements/atkins-statement-regulation-crypto-assets-081826 ; FY2025 enforcement results: https://www.sec.gov/newsroom/press-releases/2026-34 ; Opolis Task Force input 2025-04-30: https://www.sec.gov/files/ctf-written-input-navigating-dao-legality-opolis-043025.pdf
- CFTC — Releases 9104-25 (2025-08-01), 9152-25: https://www.cftc.gov/PressRoom/PressReleases/9104-25
- European Commission — MiCA review consultation: https://finance.ec.europa.eu/regulation-and-supervision/consultations-0/targeted-consultation-review-mica-regulation_en ; consultation document PDF: https://finance.ec.europa.eu/document/download/45eb6e7e-e45b-4bd5-aea5-7a0cf72dec5c_ga?filename=2026-mica-review-consultation-document_en.pdf
- ESMA — response to MiCA review (2026-09): https://www.esma.europa.eu/sites/default/files/2026-09/ESMA75-113276571-1721_Response_to_the_EC_consultation_MiCA_regulation_review.pdf ; EBA: https://www.eba.europa.eu/publications-and-media/press-releases/eba-identifies-priorities-review-mica ; ECB/ESCB: https://www.ecb.europa.eu/press/consultationresponse/pdf/ecb.conresp202609_micarreview.en.pdf
- Aave Governance V3 repo + Certora materials: https://github.com/aave-dao/aave-governance-v3
- Balancer forum — KPK H1 2026 review (2026-08-14): https://forum.balancer.fi/t/kpk-h1-2026-review-for-balancer-dao/7094
- dYdX forum — Treasury SubDAO Steakhouse vs Karpatkey: https://dydx.forum/t/treasury-subdao-proposal-comparison-steakhouse-vs-karpatkey/3009
- Aera docs (policy vaults, hooks, guardians): https://docs.aera.finance/aera-for-treasury-management.md ; https://docs.aera.finance/llms.txt
- Uniswap governance forum — DUNI proposal: https://gov.uniswap.org/t/governance-proposal-establish-uniswap-governance-as-duni-a-wyoming-duna/25770 ; UNIfication: https://gov.uniswap.org/t/unification-proposal/25881

**Secondary (B):**
- Ledger Insights (2026-03-18) — Atkins safe harbor + joint taxonomy: https://www.ledgerinsights.com/sec-chair-atkins-outlines-crypto-funding-exemptions-token-safe-harbor/
- DLA Piper (2026-09) — CLARITY Senate failure: https://www.dlapiper.com/en/insights/publications/2026/09/senate-fails-to-advance-the-clarity-act ; Orrick (2026-10): https://www.orrick.com/en/Insights/2026/10/The-CLARITY-Act-Stalls-in-the-Senate-Whats-Next-for-Digital-Asset-Regulation ; DWT (2026-07-22): https://www.dwt.com/blogs/financial-services-law-advisor/2026/07/senate-updates-crypto-market-bill
- Cointelegraph — Cayman foundations: https://cointelegraph.com/news/cayman-islands-web3-foundation-companies ; Cayman News Service (2025-12): https://caymannewsservice.com/2025/12/daos-and-web3-business-booming-in-cayman/
- Crypto Times (2026-07-07) — BonkDAO: https://www.cryptotimes.io/2026/07/07/bonkdao-hit-by-20m-treasury-drain-in-governance-attack-bonk-slides/ ; CryptoBriefing — BonkDAO: https://cryptobriefing.com/bonkdao-treasury-governance-attack/ ; CryptoBriefing (2026-08-20) — Binance interception: https://cryptobriefing.com/binance-stops-malicious-dao-proposal-treasury/
- Practus (2026-08-04) — Peirce vault statement analysis: https://practus.com/crypto-vaults-and-onchain-lending-sec-securities-law-analysis/
- Hunton — CFTC 9063-25: https://www.hunton.com/blockchain-legal-resource/cftc-shifts-crypto-enforcement-priorities ; Paul Weiss — CFTC 2025 year in review: https://www.paulweiss.com/insights/client-memos/cftc-enforcement-2025-year-in-review ; MoFo — Atkins Project Crypto (2025-11-12): https://www.mofo.com/resources/insights/251119-sec-chairman-atkins-speech-on-project-crypto
- Duane Morris — Samuels v. Lido DAO: https://www.duanemorris.com/alerts/the_dao_liability_court_finds_crypto_holding_community_partnership_under_california_law_1124.html
- DeepWiki (Aave Certora mirror): https://deepwiki.com/aave-dao/aave-governance-v3/5.1-certora-formal-verification
- arXiv — Vote delegation (2025-03): https://arxiv.org/pdf/2503.11940 ; Fairness in token delegation (2025-10): https://arxiv.org/html/2510.05830v2
- Springer — Formal Verification of DAOs (2026): https://link.springer.com/chapter/10.1007/978-3-032-26752-8_17

**Single-outlet / aggregator (C):**
- StateBay (2026-04-24) — DAO legal wrappers 2026: https://statebay.com/blog/dao-legal-wrappers-2026-jurisdictions-licensed
- ZUG DAO tracker (2026-03-01/05): https://zugdao.com/tracker/dao-governance-activity-tracker/
- Streamflow (2026-05-28): https://streamflow.finance/blog/dao-treasury-distribution-report
- terms.law — DAO legal structure for trading platforms (upd. 2024-12): https://www.terms.law/Trading-Legal/guides/dao-legal-structure.html
- Verichains — FutureSwapX (2025-12-14): https://blog.verichains.io/p/governance-attack-flashloan-vote
- daotimes — DUNA guide: https://daotimes.com/wyoming-becomes-first-state-to-provide-legal-framework-for-blockchain-based-nonprofit-organizations/ ; $26B Q1-2026: https://daotimes.com/ten-daos-now-control-a-quarter-of-a-trillion-in-combined-governance-power/
- frblaw — UNA→DUNA at 100 members: https://frblaw.com/the-wyoming-duna-and-the-future-of-dao-legal-frameworks/
- CoinLaw (2025 stats): https://coinlaw.io/dao-treasury-holdings-statistics/ ; checkcryptonews (DeepDAO $25B): https://checkcryptonews.com/dao-treasuries-top-25-billion-for-the-first-time-deepdao/
- OtoCo — (D)UNA onchain: https://www.otoco.io/duna
- onchaintreasury.org (2026-03-09): https://onchaintreasury.org/2026/03/09/stablecoin-vaults-for-dao-treasuries-steakhousefi-and-stone-vault-yields-in-2026
- higherground.io — Mango DAO settlement recap: https://higherground.io/insights/the-dao-settled-who-was-actually-in-charge

**Unverified (D):** "WYDE" as DUNA adopter; CFTC "December 2025 Digital Assets Directive" (gate.com); CFTC chairmanship identity Oct-2026; Marshall Islands/RAK/BVI adoption counts; "SEC issued DAO governance interpretive guidance in 2026" (tokenizationgovernance.com — no primary doc found); 67% native-token concentration figure; exact Mango-settlement date.

---
*End of report. Sweep executed 2026-10-20 UTC under Task C4-1c; no files modified other than this report; no worklog appended (orchestrator records entry).*
