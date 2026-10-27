# Market Intel — Decision Calendar

**Purpose:** the program's persistent dated-marker register. Every session (wave or full cycle) **reads this file at boot and sweeps every marker whose date has passed** before running new scans. Markers only change status via cycle outputs, recorded in the worklog — never silently.

**Session trigger:** owner pings. The calendar does not fire sessions; it guarantees no dated trigger is missed and orders the sweep when a session opens.

**Last committed:** 2026-10-27 (Cycle 004 Wave 1b sweep + Wave 2 first tri-focal brief).

---

## Near-dated markers

| Date | Marker | Gates / fires | Status |
|---|---|---|---|
| **Tue Oct 27, 2026** | IST Coalition (Bullish–Equiniti) NYSE issuer event | Card 6 free look; first consolidation checkpoint of issuer-consent administration | **Event day arrived**; sweep pre-dated the event — post-event read-through booked for next ping |
| **Wed Oct 28, 2026** | FOMC decision (2:00 PM ET) | Hold priced ~92% (Polymarket, Oct 23); December-hike chatter — outcome read next ping; float discriminator keys off the **Dec 9** decision | pending (statement due Oct 28) |
| **Sat Oct 31, 2026** | OCC final-rule publication target (Gould's stated date) | **Kill trigger #1**; GENIUS distribution-scope decision; distributor-yield interpretive path | **DISCHARGED — rule finalized Oct 21, FR-published Oct 23 (Vol. 91), effective Jan 18, 2027; trigger never fired.** Distribution scope decided: yield ban retained (no grandfathering/de minimis), third-party reward presumption DROPPED (distributor-yield path open for non-affiliates); daily liquidity 10%→5%; $5M floor kept; applications gated on OMB (forms comments due Nov 23, 2026) |
| **Nov 3–8, 2026** | OKXICE objection-window expiries (JPM, WMT, COST, LLY et al.) | ≥20-objection kill threshold (at 16 as of Oct 20) → Card 2/6 three-gate cluster | **22/20 — kill threshold CROSSED Oct 24** (CoinDesk via TechFlow; MSFT/GOOGL/GS/MCD/WFB/CSCO among objectors; Securitize + BitGo non-objectors; Nasdaq self-opted) → C6 licensable core dead, administration core appreciates; post-Nov 8 objection-map re-run vs C2's ≥30-name gate booked |
| **Nov 12, 2026** | EBA/USDC milestone; kill-trigger #9 clock (strategy-cards Part 4) | Watchlist v3 #3 sub-marker | pending |
| **Mon Nov 23, 2026** | OMB comment deadline — OCC GENIUS application forms | Gate that opens issuer-application acceptance (OCC announces by press release after OMB approval) | pending |
| **Mid-Nov 2026** | OPay NYSE pricing window (~$4B target, Standard Bank cornerstone) | Card 4 exit-model mark; EM exit-bifurcation verdict | **Formal terms filed Oct 23** (Reuters): 16M ADS at $19–21, ≤$366M raise, ≤$4.42B valuation; ~$200M private placement layered on; NGX dual listing approved — window on track |
| **Sat Dec 6, 2026** | Nasdaq 23×5 extended-hours launch (1-hour daily close) | Session-bridge decay gate #1; off-hours liquidity baseline reset | pending |
| **Dec 2026** | Ghana FX-regime text (five-agency committee → regime); JPM Nigeria licence decision | Watchlist #6 / #7; whitespace #1 home-market | pending |
| **Dec 2026** | FOMC December decision (Oct 27–28 hold expected first) | Float-rollover discriminator: structural vs pre-hike de-risking (U8) | pending |

## 2027 markers

| Date | Marker | Gates / fires | Status |
|---|---|---|---|
| **Jan 18, 2027** | GENIUS Act effective-date horizon | Kill-trigger #1 fallback deadline | **CONFIRMED — now also the OCC final rule's effective date** (finalized Oct 21, 2026) |
| **Jan 2027** | Bullish–Equiniti ($4.2B) deal close target | Consent-administration consolidation state | pending |
| **Jan 31, 2027** | Stablecoin float <$310B confirm-zone deadline ($304.1B Oct 20; $302.9B Oct 16; **$299.2B Oct 27 DefiLlama — first sub-$300B print**, USDC −5.55%/30d) | Watchlist #3 verdict window | pending (deepening inside zone) |
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
- **Cycle 004 Wave 1b + Wave 2** (2026-10-27, owner ping "Next cycle"): **COMPLETE** — marker sweep run ([`findings/cycle-004-wave1b-sweep.md`](findings/cycle-004-wave1b-sweep.md)): kill trigger #1 DISCHARGED (OCC rule landed Oct 21/23), ≥20 kill threshold CROSSED (22 objectors Oct 24), OPay terms filed (Oct 23), FOMC decision Oct 28 (hold ~92% priced), float $299.2B (first sub-$300B print). Wave 2 rendered the **first tri-focal brief** ([`briefs/cycle-004-brief.md`](briefs/cycle-004-brief.md); Decision / Builder / Map + 3 expansion theses). Oct 27 IST event read-through carried to next ping (sweep pre-dated the event).
- **Next ping bookings:** Oct 27 IST post-event read-through (Card 6 v2 checkpoint verdict) → FOMC Oct 28 outcome → objection-count watch into Nov 3–8 expiries → post-Nov 8 objection-map re-run vs ≥30-name gate (arable-symbol full pull rides this re-run if evidence warrants) → OPay pricing flow → Nov 23 OMB gate.
