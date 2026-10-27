# Market Intel — Decision Calendar

**Purpose:** the program's persistent dated-marker register. Every session (wave or full cycle) **reads this file at boot and sweeps every marker whose date has passed** before running new scans. Markers only change status via cycle outputs, recorded in the worklog — never silently.

**Session trigger:** owner pings. The calendar does not fire sessions; it guarantees no dated trigger is missed and orders the sweep when a session opens.

**Last committed:** 2026-10-27 (Cycle 004 Wave 2b multi-agent read-through sweep).

---

## Near-dated markers

| Date | Marker | Gates / fires | Status |
|---|---|---|---|
| **Tue Oct 27, 2026** | IST Coalition (Bullish–Equiniti) NYSE issuer event | Card 6 free look; first consolidation checkpoint of issuer-consent administration | **Event day; in progress at sweep time (12:10 ET)** — no day-of coverage, no issuer commitments/pricing disclosed. **Eve-of-event: QRT + Vertalo + zerohash joined (8 members, PR Oct 26); coalition formally OPEN/non-exclusive; Vertalo launched SecondParty consent-administration product Oct 27 → Card 6 whitespace CONTESTED-WITH-INCUMBENT.** Post-event readout leads next ping |
| **Wed Oct 28, 2026** | FOMC decision (2:00 PM ET) | Hold priced 93–95% (Polymarket 94.6¢ / Kalshi 93% / CNBC survey 93%, Oct 27); **December = 74.5% HIKE priced** (Polymarket Dec +25bp 74.5¢; Kalshi 76%) — float discriminator (U8) tilts to pre-hike de-risking; dissents expected (Hammack, Logan) | pending (statement due Oct 28 2PM ET; next decision Dec 8–9 SEP) |
| **Sat Oct 31, 2026** | OCC final-rule publication target (Gould's stated date) | **Kill trigger #1**; GENIUS distribution-scope decision; distributor-yield interpretive path | **DISCHARGED — rule finalized Oct 21, FR-published Oct 23 (Vol. 91), effective Jan 18, 2027; trigger never fired.** Distribution scope decided: yield ban retained (no grandfathering/de minimis), third-party reward presumption DROPPED (distributor-yield path open for non-affiliates); daily liquidity 10%→5%; $5M floor kept; applications gated on OMB (forms comments due Nov 23, 2026) |
| **Nov 3–8, 2026** | OKXICE objection-window expiries (JPM, WMT, COST, LLY et al.) | ≥20-objection kill threshold (at 16 as of Oct 20) → Card 2/6 three-gate cluster | **26/63 = 41% objected** (notice Oct 26: +IBM, IonQ, Oracle, Intel; no withdrawals) — threshold crossed, C6 licensable core dead; **C2 gate-1 margin = 7 names** (37 non-objected vs ≥30 line; burn ~4/wk); post-Nov 8 objection-map re-run booked |
| **Nov 12, 2026** | EBA/USDC milestone; kill-trigger #9 clock (strategy-cards Part 4) | Watchlist v3 #3 sub-marker | pending |
| **~Nov 9–20, 2026** | **NEW: Anthropic ANT IPO window** (S-1 public Oct 26; Nasdaq; marketing ~week of Nov 9; Polymarket modal dates Nov 19–20; Kalshi 93% by Jan-1) | Private-AI perps forcing event: implied-valuation → public-index conversion mechanics (Wave 1 report 4a) enter watch window | pending (H1-26 revenue $16.3B; leads MS/GS/JPM/Citi) |
| **Mon Nov 23, 2026** | OMB comment deadline — OCC GENIUS application forms | Gate that opens issuer-application acceptance (OCC announces by press release after OMB approval) | pending — application form itself NOT released; OMB 1557-NEW approval undated (clock ~Oct 30); Bulletin 2026-51 + reporting forms already out |
| **Mid-Nov 2026** | OPay NYSE pricing window (~$4B target, Standard Bank cornerstone) | Card 4 exit-model mark; EM exit-bifurcation verdict | **Accelerated: pricing expected WEEK OF OCT 26** (IPOScoop, single source) — no print yet as of Oct 27; bookrunners Citi/DB/Standard Bank/CICC (JPM absent, CICC added — conflict to reconcile); $336M vs $366M raise discrepancy; ~$270M demand lined up; Standard Bank $200M = IPO-conditional PP not closed cash |
| **Sat Dec 6, 2026** | Nasdaq 23×5 extended-hours launch (1-hour daily close) | Session-bridge decay gate #1; off-hours liquidity baseline reset | pending |
| **Dec 2026** | Ghana FX-regime text (five-agency committee → regime); JPM Nigeria licence decision | Watchlist #6 / #7; whitespace #1 home-market | pending |
| **Dec 2026** | FOMC December decision (Oct 27–28 hold expected first) | Float-rollover discriminator: structural vs pre-hike de-risking (U8) | pending |

## 2027 markers

| Date | Marker | Gates / fires | Status |
|---|---|---|---|
| **Jan 18, 2027** | GENIUS Act effective-date horizon | Kill-trigger #1 fallback deadline | **CONFIRMED — now also the OCC final rule's effective date** (finalized Oct 21, 2026) |
| **Jan 2027** | Bullish–Equiniti ($4.2B) deal close target | Consent-administration consolidation state | pending |
| **Jan 31, 2027** | Stablecoin float <$310B confirm-zone deadline ($304.1B Oct 20; $302.9B Oct 16; **$299.2–301.6B band Oct 27 DefiLlama — first sub-$300B print**; USDC −5.51%/30d; USD1 −10.85%/30d collapse; USDS rotation decelerating; PYUSD/RLUSD now the share-takers) | Watchlist #3 verdict window | pending (deepening inside zone; Dec-hike pricing tilts discriminator to pre-hike de-risking) |
| **Q1 2027** | Robinhood 24/7 weekend trading via Bruce ATS (announced Sep 29) | Session-bridge decay gate #2 | pending |
| **Q1 2027** | Nigerian seed-round counts (Q4 aggregate data) | Watchlist #10 (seed-to-growth gap) | pending |
| **Mar 31, 2027** | Kenya yield-ban compliance horizon; Card 2 API-only expiry | P11 perimeter; C2 stage-gate | pending |
| **Apr 30, 2027** | Credit second-source / Figure stress check | Watchlist #9 (single-issuer category) | pending |
| **May 2027** | Senate CLARITY markup window (pushed) | P11 legislative path (currently dead) | pending |
| **Jun 30, 2027** | FX-disclosure (#6); payout-leg consolidation (#7); Binance terminal state (#10) | Triple verdict date | pending |

## Standing scans (no date; run when fresh value exists)

> **Amendment 004 (2026-10-21):** standing pillar-support scans are retired. Entries below retained as the completed record of Wave 1; no pillar scan is queued again unless market evidence independently warrants it.

- Private-AI-company equity perps landscape — [P2-FEED] — **COMPLETE 2026-10-21** (findings/cycle-004-wave1-research.md Part A; full report findings/cycle-004-wave1/4a)
- Formal-verification market — [P1-WATCH] — **COMPLETE 2026-10-21** (Part B; full report 4b)
- DAO-formation intel — [DAO-WATCH] — **COMPLETE 2026-10-21** (Part C; full report 4c)
- Venue-risk baseline (VOOI / MEXC / Hyperliquid / Backpack) — [P2-FEED] — **COMPLETE 2026-10-21** (Part D; full report 4d)
- Objection-list → Edge-Engine arable-symbol deliverable — [P2-FEED] — **COMPLETE 2026-10-21 (compact v1)** (findings/cycle-004-arable-symbol-map.md; full 63-symbol table pull → Wave 1b)

## Staging

- **Cycle 004 Wave 1** (this session, 2026-10-21): the four standing landscape scans above. Marker sweep not yet due (nearest marker Oct 27). **COMPLETE.**
- **Cycle 004 Wave 1b + Wave 2** (2026-10-27, owner ping "Next cycle"): **COMPLETE** — marker sweep run ([`findings/cycle-004-wave1b-sweep.md`](findings/cycle-004-wave1b-sweep.md)): kill trigger #1 DISCHARGED (OCC rule landed Oct 21/23), ≥20 kill threshold CROSSED (22 objectors Oct 24), OPay terms filed (Oct 23), FOMC decision Oct 28 (hold ~92% priced), float $299.2B (first sub-$300B print). Wave 2 rendered the **first tri-focal brief** ([`briefs/cycle-004-brief.md`](briefs/cycle-004-brief.md); Decision / Builder / Map + 3 expansion theses).
- **Cycle 004 Wave 2b** (2026-10-27, owner ping "Continue the next cycle; deploying multiple agent into research"): **COMPLETE — 4 parallel research agents deployed** (records: worklog Task IDs C4-W2b-A/B/C/D; consolidated in [`findings/cycle-004-wave2b-readthrough.md`](findings/cycle-004-wave2b-readthrough.md)). Four decision-set moves: **(1) Card 6 whitespace CONTESTED** — coalition expanded to 8 members eve-of-event (QRT/Vertalo/zerohash, PR Oct 26), formally OPEN/non-exclusive, and Vertalo launched SecondParty (Oct 27) productizing consent administration from inside; **(2) Card 2 gate-1 margin = 7 names** (objections 26/63 = 41%, notice Oct 26: +IBM/IonQ/Oracle/Intel); **(3) Card 4 mark accelerated** — OPay pricing expected week of Oct 26 (IPOScoop), no print yet, roster + raise discrepancies flagged; **(4) December flipped to 74.5% HIKE** (Polymarket; Kalshi 76%) — float discriminator tilts; hold 93–95% for Oct 28. Plus: **tokenized-stock SCALE CORRECTION** (≈$3.3B mcap not ~$25B; $37B quarterly volume; 10.7% issuer-sponsored); **Anthropic S-1 public Oct 26** (ANT, Nasdaq, modal debut Nov 19–20 — new dated marker); EM exits widened (MNT-Halan +18% EGX, Airtel Money $7B LSE, Mynt flat debut, Dangote $1.6B closed); OCC reporting forms + Bulletin 2026-51 out, application form NOT released, OMB gate undated.
- **Next ping bookings:** IST post-event readout (Card 6 revised-posture verdict) → FOMC statement outcome + December language → **OPay pricing print** (window open NOW) → objection count into Nov 3–8 expiries + post-Nov 8 map re-run vs 7-name margin → Anthropic marketing week (~Nov 9) → OMB 1557-NEW gate (~Oct 30 clock).
