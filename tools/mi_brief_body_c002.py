#!/usr/bin/env python3
"""Market Intel - Cycle 002 Brief (body) + cover merge.
Pipeline: ReportLab body -> pypdf merge with Playwright cover -> final PDF.
Adapted from validated Cycle 001 pipeline (Template 07 Crystal Blue, pdf_qa PASS).
"""
import os, sys

PDF_SKILL = '/home/z/my-project/skills/pdf'
sys.path.insert(0, os.path.join(PDF_SKILL, 'scripts'))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, CondPageBreak, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

FONT_DIR = '/usr/share/fonts'
pdfmetrics.registerFont(TTFont('FreeSerif', f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold', f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic', f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC-Bold', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf'))
registerFontFamily('FreeSerif', normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')
registerFontFamily('NotoSerifSC', normal='NotoSerifSC', bold='NotoSerifSC-Bold')

from pdf import install_font_fallback
install_font_fallback()

# -- Template 07 Crystal Blue body palette (fixed; from typesetting/cover.md) --
PAGE_BG      = colors.HexColor('#f5f8fc')   # XL
CARD_BG      = colors.HexColor('#e4ecf5')   # L
TABLE_STRIPE = colors.HexColor('#eef3fa')   # L
HEADER_FILL  = colors.HexColor('#1a4a7a')   # M
BORDER       = colors.HexColor('#c0d0e2')   # S
ACCENT       = colors.HexColor('#2d7ab3')   # XS
TEXT_PRIMARY = colors.HexColor('#142840')
TEXT_MUTED   = colors.HexColor('#5a7a96')

MARGIN = 0.9 * inch
PAGE_W, PAGE_H = A4
AVAIL = PAGE_W - 2 * MARGIN
BODY_PDF = '/home/z/my-project/scripts/mi_body_002.pdf'
COVER_PDF = '/home/z/my-project/scripts/mi_cover_002.pdf'
FINAL_PDF = '/home/z/my-project/download/market-intel/briefs/cycle-002-brief.pdf'

# -- styles --
h1 = ParagraphStyle('H1', fontName='FreeSerif', fontSize=15, leading=19,
                    textColor=HEADER_FILL, spaceBefore=16, spaceAfter=4)
h2 = ParagraphStyle('H2', fontName='FreeSerif', fontSize=12, leading=15.5,
                    textColor=TEXT_PRIMARY, spaceBefore=12, spaceAfter=4)
body = ParagraphStyle('Body', fontName='FreeSerif', fontSize=10.5, leading=16.2,
                      textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY, spaceAfter=8)
bullet = ParagraphStyle('Bullet', fontName='FreeSerif', fontSize=10.5, leading=15.5,
                        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                        leftIndent=14, spaceAfter=5)
muted = ParagraphStyle('Muted', fontName='FreeSerif', fontSize=8.5, leading=12,
                       textColor=TEXT_MUTED, spaceBefore=6)
cell = ParagraphStyle('Cell', fontName='FreeSerif', fontSize=9, leading=12.5,
                      textColor=TEXT_PRIMARY)
cell_b = ParagraphStyle('CellB', fontName='FreeSerif', fontSize=9, leading=12.5,
                        textColor=colors.white)
stat_num = ParagraphStyle('StatNum', fontName='FreeSerif', fontSize=16, leading=19,
                          textColor=ACCENT, alignment=TA_CENTER)
stat_lab = ParagraphStyle('StatLab', fontName='FreeSerif', fontSize=7.5, leading=10,
                          textColor=TEXT_MUTED, alignment=TA_CENTER)

H1_ORPHAN = (PAGE_H - 2 * MARGIN) * 0.22

def heading(text):
    return KeepTogether([
        CondPageBreak(H1_ORPHAN),
        Paragraph('<b>%s</b>' % text, h1),
        HRFlowable(width='100%', thickness=1.1, color=ACCENT, spaceBefore=2, spaceAfter=9),
    ])

def make_table(header, rows, fracs, fs=9):
    assert abs(sum(fracs) - 1.0) < 1e-6
    widths = [f * AVAIL for f in fracs]
    assert sum(widths) <= AVAIL + 0.5
    cs = ParagraphStyle('c%d' % fs, parent=cell, fontSize=fs, leading=fs + 3.5)
    hs = ParagraphStyle('h%d' % fs, parent=cell_b, fontSize=fs, leading=fs + 3.5)
    data = [[Paragraph('<b>%s</b>' % htxt, hs) for htxt in header]]
    for r in rows:
        data.append([Paragraph(c, cs) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='CENTER')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
        ('GRID', (0, 0), (-1, -1), 0.6, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t

def stat_row(stats):
    n = len(stats)
    w = AVAIL / n
    cells = [[Paragraph('<b>%s</b>' % num, stat_num), Paragraph(lab, stat_lab)]
             for num, lab in stats]
    t = Table([cells], colWidths=[w] * n, hAlign='CENTER')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.75, BORDER),
        ('BOX', (0, 0), (-1, -1), 1.0, ACCENT),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('FreeSerif', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, PAGE_H - 0.55 * inch, 'MARKET INTEL  |  CYCLE 002 VERIFICATION & DEEP-DIVE BRIEF')
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(1.2)
    canvas.line(MARGIN, PAGE_H - 0.62 * inch, PAGE_W - MARGIN, PAGE_H - 0.62 * inch)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 0.6 * inch, PAGE_W - MARGIN, 0.6 * inch)
    canvas.setFont('FreeSerif', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, 0.44 * inch, 'Market Intel Research Program  |  Multi-agent continuous intelligence')
    canvas.drawRightString(PAGE_W - MARGIN, 0.44 * inch, 'Page %d' % (canvas.getPageNumber() + 1))
    canvas.restoreState()

story = []

# ============ 1. EXECUTIVE SUMMARY ============
story.append(heading('1. Executive Summary'))
story.append(Paragraph(
    'Cycle 002 was designed as an adversarial test of the Cycle 001 baseline rather than a fresh scan. Four '
    'research agents re-verified the single-source findings that carried the most analytical weight, swept the '
    'six falsifiable watchlist markers, and produced corridor-level unit economics for the two highest-conviction '
    'whitespace positions; three reasoning agents then re-ranked the whitespace map, audited every structural '
    'problem, and rebuilt the strategy portfolio on observed prices instead of assumptions. The result is a '
    'materially sharper picture: the baseline survived contact with the evidence, but two of its pillars have '
    'been re-engineered, and two new structural problems entered the ledger.', body))
story.append(Paragraph(
    'The verification wave passed in full. The offshore TradFi perp complex is confirmed at category scale - '
    '23.5 percent of all perpetual volume in August against 0.5 percent ten months earlier - though it cooled '
    'for the first time in September while open interest kept building. Citi\'s Custody+ custody suite is '
    'confirmed by primary press release with a stated 2026 go-live. The vendor remittance-cost claim is the one '
    'casualty of precision: the honest benchmark is the World Bank digital-only index of 3.5 to 4.6 percent, not '
    'the 6.36 percent cash-inclusive average, which still leaves a 55 to 70 percent cost gap but nearly halves '
    'the headline disruption arithmetic.', body))
story.append(Paragraph(
    'The single most consequential update is a mechanism revision, not a contradiction: regulators are onshoring '
    'offshore activity through approval rather than enforcement. Kalshi received CFTC approval for US '
    'single-stock perpetuals on October 6 while no action landed against the offshore book, and Korea simply '
    'blocked 27 unregistered exchanges. Meanwhile nine issuers - Microsoft, Alphabet, Goldman Sachs among them - '
    'filed formal objections to tokenized listings on the OKX-ICE venue, flipping the tokenized-equity moat from '
    'venue technology to signed issuer content. Both facts redirect the exchange-structure thesis from a '
    'regulatory flashpoint narrative to a market-structure narrative.', body))
story.append(Spacer(1, 4))
story.append(stat_row([
    ('$306.8B', 'Stablecoin float Oct 20 - +2.0% from Oct 1 despite a hawkish Fed hold'),
    ('$482B', 'Stablecoin payment volume Q1-Q3 2026 - +45% y/y while float stagnates'),
    ('$24.8B', 'Tokenized private credit - +30% since Cycle 001, still one issuer'),
    ('91 days', 'To GENIUS effective date Jan 18, 2027 - comment window closed Oct 19'),
]))
story.append(Spacer(1, 8))
story.append(Paragraph('<b>Key judgments</b>', h2))
for k in [
    'The stablecoin category is two-speed: float stagnates near $307B while payment volume compounds at 45 '
    'percent growth. Issuers are being redefined from float holders to flow networks - Circle closed Tazapay '
    'and immediately announced a 40-market emerging-market push.',
    'The EM off-ramp spread is real but it is a policy artifact: gross 80-150bps B2B is confirmed by live '
    'quotes, yet the premium is the official-parallel FX wedge in disguise. The durable moat is naira float '
    'yield at 16.84 percent, an owned payout leg, and premium-duration corridor selection.',
    'Yield routing is demoted to a rider: the assumed 25-50bps placement fee is unpriced at every issuer, '
    'break-even sits at $150-250M of AUM, and the economics only clear as an FX-and-turnover business.',
    'Issuer consent is the scarce input of the tokenized-equity market, not venue technology - a new structural '
    'problem (P8) and a new whitespace position in the same fact.',
]:
    story.append(Paragraph('\u2022 ' + k, bullet))

# ============ 2. WATCHLIST SWEEP ============
story.append(heading('2. Watchlist Sweep: What Moved'))
story.append(Paragraph(
    'Cycle 001 closed with six falsifiable markers so that this cycle would update on evidence rather than '
    'narrative. Three markers moved, two produced new datasets, and one stayed deliberately silent exactly where '
    'the falsifiers look - the absence of enforcement against exchange-paid APY and offshore single-stock perps '
    'is itself informative, because the Kalshi approval shows the regulators\' preferred instrument is market '
    'structure, not action. The sweep also surfaced a euro-side surprise: the 37-bank Qivalis consortium '
    'licensed ahead of the American 21-bank venture, pulling the bank-consortium thesis forward on the European '
    'leg.', body))
story.append(make_table(
    ['Marker', 'Status', 'What moved'],
    [
        ['W1 Stablecoin supply / Fed / consortium', 'MOVED up',
         'Float +2.0% to $306.8B despite a hawkish hold (hike odds 14-17%); USDT stabilized; Qivalis (37 EU banks) won DNB EMI licence Oct 14.'],
        ['W2 Regulator touch on APY / offshore perps', 'NO MOVEMENT',
         'Zero enforcement; instead Kalshi won CFTC approval for US equities perps Oct 6 - onshoring via approval, not enforcement.'],
        ['W3 EM operator filings', 'MOVED',
         'OPay NYSE pricing expected mid-November (revenue +137%, income +300%, lending top line); MNT-Halan order book closed Oct 14, biggest EGX book in years.'],
        ['W4 Tokenized credit second source', 'NEW DATA',
         'Category +30% to $24.8B; concentration worsened - no non-Figure issuer above $2B; Figure Q3 volume +20% q/q, no stress disclosed.'],
        ['W5 African seed funding', 'NEW DATA (mixed)',
         'Q3: $583M across 58 deals, a four-year equity high - but mega-deal-led; seed counts have not rebounded.'],
        ['W6 Exchange structure events', 'MOVED',
         'OKXICE filed with SEC Oct 5; nine-plus issuers filed objections Oct 15-19; Binance EU halt and DOJ probe stand; Nasdaq-Kraken issuer-first gateway live Oct 15.'],
    ],
    [0.24, 0.13, 0.63]))
story.append(Paragraph(
    'Beyond the watchlist, the fresh-event scan added twelve new items to the evidence base, three of which '
    'warrant standing attention: the GENIUS Act compliance stack is now date-certain with the comment window '
    'closed and the effective date 91 days out; JPMorgan put its deposit token on a public blockchain the same '
    'week a Kansas City Fed research note flagged deposit-flight risk, meaning banks can now legally pay yield '
    'in the channel where stablecoins cannot; and the Philippines regulator moved from capping instant-transfer '
    'fees to making them free outright, extending the fee-decommissioning template from transfers to cash '
    'infrastructure through the South African Reserve Bank\'s shared-ATM plan.', body))

# ============ 3. STRUCTURAL PROBLEMS ============
story.append(heading('3. Structural Problems: Verdicts'))
story.append(Paragraph(
    'Every Cycle 001 problem was re-audited against the new evidence. None died; one was substantially '
    'reframed; two were strengthened; and the cycle formalized two entirely new problems. The reframing of P1 '
    'matters most: the supply-contraction symptom that motivated it is dead - float recovered 2 percent despite '
    'a hawkish central bank - but the bank-reallocation mechanism strengthened on every leg, from the GENIUS '
    'clock to public-chain deposit tokens. The correct description of the category is no longer contraction but '
    'divergence: float stagnates while payment flow compounds, and the P&L migrates from reserve income to '
    'network income.', body))
story.append(make_table(
    ['Problem', 'Verdict', 'What changed this cycle'],
    [
        ['P1 Float-yield reallocation to banks', 'REFRAMED',
         'Supply-contraction symptom dead (+2% recovery); mechanism strengthened (GENIUS clock date-certain, JPM deposit token on Ethereum, Qivalis licensed). New signature: two-speed category - payments +45% vs stagnant float.'],
        ['P2 Free-A2A fee decommissioning', 'CONFIRMED + REFRAMED',
         'Escalated from caps to zero (BSP made InstaPay P2P free Aug 15); extends to cash/ATM (SARB utility) and corridor FX (Ethiopia joins PAPSS). Binding constraint migrated to FX-spread transparency regulation (IMF on Nigeria; Ghana advertising notice).'],
        ['P3 Exit-market bifurcation', 'STRENGTHENED',
         'Q3 African rebound is mega-deal-led; Airtel Money cleared the LSE at ~$7B; seed counts stay at 2020 lows; OPay pricing is the live test.'],
        ['P4 Tokenized credit one-issuer category', 'STRENGTHENED',
         'Category grew 30% to $24.8B on a single name; the defusal condition (second issuer above $2B) remains unmet; Figure growing faster than rivals.'],
        ['P5 Licence moat strands offshore leaders', 'CONFIRMED (mechanism revised)',
         'Onshoring runs through approval (Kalshi) and globalized lockouts (Korea blocks 27 venues); zero US enforcement no longer falsifies the thesis.'],
        ['P6 Venue take-rate squeeze', 'CONFIRMED crypto / DELAYED equities',
         'Issuer veto thins OKXICE\'s 63 symbols; Nasdaq launches issuer-first gateway; fee compression reroutes into issuer-consent moats.'],
        ['P7 EM credit concentration at rate peak', 'ON TRACK',
         'OPay F-1 confirms the credit-led model going public; untested until the first post-IPO filing.'],
        ['P8 (NEW) Issuer-content veto', 'FORMALIZED',
         'Issuers gatekeep the 24/7 equity market; consent is the scarce input; favors incumbent exchange groups that own issuer relationships; delays P6\'s equities leg.'],
        ['P9 (NEW) Last-mile rail capture', 'FORMALIZED',
         'Off-ramp spreads are revocable licences granted by the disintermediated; the Partna-M-Pesa eviction (corridor dead since May, no alternative route) is the precedent; beneficiaries are MNOs, payout-monopoly banks, and card rails.'],
    ],
    [0.22, 0.15, 0.63]))

# ============ 4. WHITESPACE MAP V2 ============
story.append(heading('4. Whitespace Map v2'))
story.append(Paragraph(
    'The whitespace map was re-ranked on unit economics rather than narrative strength, which produced real '
    'movement: yield routing fell from second to seventh when the deep-dive showed its placement fee is an '
    'engineering assumption rather than an observed market price, while merchant acquiring rose from sixth to '
    'third on the Philippines\' escalation to zero fees and the hardened South African opening. Two new '
    'positions entered - issuer-content licensing and compliance infrastructure - both direct children of this '
    'cycle\'s strongest facts. Two candidates were killed: neutral cost attestation, because the Bank of Italy '
    'produced the disintermediation data as a public good, and the cheap agent-network acquisition arm, because '
    'Baxi\'s agents were transitioned to a principal bank for free, which simultaneously proves there is no '
    'distress market and that agent relationships are portable.', body))
story.append(make_table(
    ['Position', 'Change', 'Evidence anchor', 'Horizon', 'Primary risk'],
    [
        ['1. EM off-ramp (reframed)', 'Hold #1',
         'Spread confirmed 80-150bps B2B; moat = naira float yield (16.84%) + owned payout leg + premium duration; Circle attacking 40 markets.',
         '12-24 mo', 'FX-spread disclosure rule; premium compression as FX windows converge.'],
        ['2. EU licensed-capacity redistribution', '#3 to #2',
         'USDC becomes first significant EMT Nov 12; Qivalis 37-bank licence; Binance still locked out.',
         '6-12 mo', 'Window shuts before a third party buys in.'],
        ['3. Merchant acquiring in free-A2A markets', '#6 to #3',
         'BSP went beyond cap to free; SA opening hardened incl. cash utility; +50% volume elasticity underwrites the credit-data play.',
         '12-30 mo', 'Visa-Mesh stablecoin spend at 175M merchants pressures the FX rider.'],
        ['4. Issuer-content licensing (NEW)', 'New',
         'Nine objections vs OKXICE; Nasdaq gateway is issuer-first; content bps unpriced.',
         '6-18 mo', 'Issuers go venue-direct; blanket refusals.'],
        ['5. Compliance infrastructure (NEW)', 'New',
         'Mastercard screening launch; OCC-Metrika supervisory tech; CBN data-localisation Jan 2027; EBA supervision date-certain.',
         '6-24 mo', 'Card networks bundle screening free into existing contracts.'],
        ['6. Tokenized private credit second source', 'Hold',
         '$24.8B category on one name; Figure Q3 +20% q/q; no second source above $2B.',
         '12-24 mo', 'A Figure stress event taints the category; entry cost rising.'],
        ['7. Yield routing (DEMOTED)', '#2 to #7',
         'Placement fee unpriced (OUSG at 0%, BENJI at 15bps); break-even $150-250M; clears only as FX-and-turnover.',
         '6-18 mo', 'GENIUS final rule extends yield ban to distribution (est. 40-50%).'],
        ['8. EM dollar-savings front end', 'Wait-state',
         'OKX 10% APY subsidy unmatchable (~640bps over underlying); Ghana advertising-ban precedent.',
         'None', 'Re-enter on first enforcement or a licensed local wrapper.'],
    ],
    [0.19, 0.09, 0.36, 0.09, 0.27]))

# ============ 5. STRATEGY CONSTRUCTS V2 ============
story.append(heading('5. Strategy Constructs v2'))
story.append(Paragraph(
    'The engineering cell audited all five Cycle 001 constructs against observed prices, killed one, revised '
    'two, validated one, stress-tested one, and added two new cards. The highest-conviction revision is the '
    'reframe of the Yield Router: it was the only card where observed market prices could replace engineering '
    'assumptions, and the replacement showed the placement fee does not exist as a listed price anywhere. The '
    'construct survives folded into the rail business as an FX-and-float machine - turnover, not idle AUM, is '
    'the unit driver, at six times annual velocity worth six to twelve times the placement fee. The portfolio '
    'now has a clear center of gravity: the payout leg.', body))
story.append(make_table(
    ['Construct', 'Verdict', 'Core mechanic / revision', 'Kill trigger'],
    [
        ['C1 Dual-Rail Merchant Network', 'REVISED',
         'Spread stronger than assumed (80-150bps B2B realized); add an exclusive payout leg as a required component, corridor weighting to premium duration (Ghana in, Kenya out), naira float-yield pool (~46bps per 10-day prefunding cycle), Mastercard screening layer.',
         'NGN premium below 1.0% for two consecutive months; a de-platforming event on a live corridor.'],
        ['C2 Session-Bridge market-making', 'STRESSED',
         'Decay clock accelerated (NYSE extended options hours; Ripple Prime 24/7 with Virtu; Kalshi onshore) but issuer objections extend the dislocation window for non-objected names; capital stage-gated at $25-50M pending the SEC decision.',
         'Closed-session dislocation nets under 5bps; blanket issuer approvals arrive.'],
        ['C3 Yield Router', 'REFRAMED',
         'Now an FX-and-float machine with a yield rider, folded into the C1/C7 rails; placement fees unpriced; break-even $150-250M AUM; turnover at 6x per year times 40-80bps is the real engine.',
         'Treasury final rule extends the yield ban to distribution before Jan 18, 2027.'],
        ['C4 Warehouse-to-IPO credit platform', 'VALIDATED',
         'IPO leg is live (OPay mid-Nov, Airtel $7B, MNT-Halan); Figure concentration strengthens the second-source pitch; bank-LP evidence updated with Standard Bank in the consortium.',
         'No second or third bank LP signs within 12 months; an OPay credit-loss spike.'],
        ['C5 Agent-Network Reversal', 'KILLED',
         'Baxi agents transitioned to a principal bank for free - clearing price zero, buyers are banks, relationships portable; salvage economics folded into C7.',
         'n/a - construct retired this cycle.'],
        ['C6 Issuer-Consent Gateway (NEW)', 'FORMALIZED',
         'Issuer-side licensing desk for tokenized-listing consent before affiliated venues lock content; roughly $3-10M per year per venue set in licensing revenue; near-zero capital; 12-18 month time-box.',
         'Blanket issuer refusals; exclusive venue-direct deals lock the market.'],
        ['C7 Payout-Leg Holdco (NEW)', 'FORMALIZED',
         'Exclusive MNO/bank payout capacity wholesaled as payout-as-a-service at 20-60bps tolls (dLocal-anchored precedent at 2.68% blended take); $5-30M per year potential per corridor.',
         'FX-disclosure toll caps; MNO verticalization; issuer-level direct integration by Circle.'],
    ],
    [0.17, 0.11, 0.45, 0.27]))
story.append(Paragraph(
    'Portfolio view: Cards 1, 3, and 7 now form one correlated vertical sharing the FX-disclosure and '
    'emerging-market regime clocks, and should be funded contract-first as a single unit in the $15-40M range. '
    'Cards 2 and 6 form a cheap correlated option pair on the SEC\'s OKXICE decision. Card 4 anchors the '
    'portfolio as the only counter-cyclical, clock-independent construct. The consolidation is deliberate: this '
    'cycle\'s evidence collapsed three would-be separate businesses into one because they all monetize the same '
    'scarce asset - the owned or exclusive last mile.', body))

# ============ 6. WATCHLIST V2 ============
story.append(heading('6. Watchlist v2: Markers for Cycle 003'))
story.append(Paragraph(
    'The watchlist was rebuilt to ten dated, falsifiable markers replacing the original six, with sharper '
    'thresholds and the enforcement-versus-approval distinction written into the triggers. Carry-forward '
    'verification items for Cycle 003: reconcile the CoinMarketCap $315B supply print against the rwa.xyz '
    '$300.9B scope; pull Tether weekly redemption flows; confirm the $250M Coinme consideration; verify the '
    'Ghana cost stack and e-levy status; watch for a Partna or M-Pesa corridor restart; and read the GENIUS '
    'final-rule text the week it lands, since it is the portfolio\'s single largest kill-trigger.', body))
story.append(make_table(
    ['#', 'Marker', 'Confirms if', 'Kills if', 'Deadline'],
    [
        ['1', 'GENIUS final-rule distribution scope',
         'Ban extends to distributors and affiliates.', 'Silent on distribution by effective date.', 'Jan 18, 2027'],
        ['2', 'OKX USDG 10% APY regulator response',
         'Any guidance or enforcement lands.', 'Still live untouched - jurisdictional gap durable.', 'Mar 31, 2027'],
        ['3', 'Two-speed split composition',
         'Float below $310B or Tether redemptions above 5% in a quarter; EBA supervision lands Nov 12.',
         'Float above $321B with USDT above $190B.', 'Jan 31, 2027'],
        ['4', 'OKXICE SEC decision + objection fallout',
         'Approval with objections intact; onshore perps take 20%+ of US-relevant flow in two quarters.',
         'Rejection, or objections withdrawn and onshore capture under 5%.', 'Q2 2027'],
        ['5', 'Binance terminal state',
         'DOJ curtailment or EU halt persists past June.', 'CASP licence plus a clean DOJ settlement.', 'Jun 30, 2027'],
        ['6', 'OPay pricing + first post-IPO filing',
         'Credit-loss spike or transfer revenue down 20% y/y.', 'Revenue at range with stable NPLs.', 'Q2 2027'],
        ['7', 'FX-spread disclosure rule (Nigeria/Ghana)',
         'A disclosure or benchmark-rate proposal is tabled.', 'No proposal by June.', 'Jun 30, 2027'],
        ['8', 'Rail-capture events',
         'One more eviction or a competing MNO corridor launches.', 'Neutral-access SLAs become standard.', 'Jun 30, 2027'],
        ['9', 'Tokenized-credit second source',
         'A non-Figure issuer crosses $2B (defuses) - or Figure stress (confirms).', 'n/a - two-sided marker.', 'Apr 30, 2027'],
        ['10', 'African seed counts',
         'Persist at 2020 lows; banks keep replacing venture LPs.', 'Rebound above 30%.', 'Q1 2027'],
    ],
    [0.05, 0.21, 0.31, 0.28, 0.15]))
story.append(Paragraph(
    'Archive note: the complete Cycle 002 evidence base - verifications, watchlist sweep, twelve fresh findings, '
    'five missed-in-Cycle-001 candidates, both unit-economics deep-dives, the discovery update, the analysis '
    'chains, and the full seven-card strategy document - is versioned alongside this brief in the Market Intel '
    'repository under findings/, together with the program worklog recording each agent\'s assignment and '
    'output.', muted))

# ---- build body ----
doc = SimpleDocTemplate(BODY_PDF, pagesize=A4,
                        leftMargin=MARGIN, rightMargin=MARGIN,
                        topMargin=MARGIN, bottomMargin=0.85 * inch,
                        title='Market Intel - Cycle 002 Verification & Deep-Dive Brief',
                        author='Z.ai', creator='Z.ai',
                        subject='Market intelligence brief: fintech, exchanges, cross-market infrastructure')
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print('body built:', BODY_PDF)

# ---- merge cover + body ----
from pypdf import PdfReader, PdfWriter
writer = PdfWriter()
body_reader = PdfReader(BODY_PDF)
bw = float(body_reader.pages[0].mediabox.width)
bh = float(body_reader.pages[0].mediabox.height)
for p in PdfReader(COVER_PDF).pages:
    p.scale_to(bw, bh)  # normalize cover to exact body page size (A4)
    writer.add_page(p)
for p in body_reader.pages:
    writer.add_page(p)
os.makedirs(os.path.dirname(FINAL_PDF), exist_ok=True)
with open(FINAL_PDF, 'wb') as f:
    writer.write(f)
print('final merged:', FINAL_PDF, 'pages:', len(writer.pages))
