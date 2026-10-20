#!/usr/bin/env python3
"""Market Intel - Cycle 003 Brief (body) + cover merge.
Pipeline: ReportLab body -> pypdf merge with Playwright cover -> final PDF.
Adapted from validated Cycle 001/002 pipeline (Template 07 Crystal Blue, pdf_qa PASS).
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
PAGE_BG      = colors.HexColor('#f5f8fc')
CARD_BG      = colors.HexColor('#e4ecf5')
TABLE_STRIPE = colors.HexColor('#eef3fa')
HEADER_FILL  = colors.HexColor('#1a4a7a')
BORDER       = colors.HexColor('#c0d0e2')
ACCENT       = colors.HexColor('#2d7ab3')
TEXT_PRIMARY = colors.HexColor('#142840')
TEXT_MUTED   = colors.HexColor('#5a7a96')

MARGIN = 0.9 * inch
PAGE_W, PAGE_H = A4
AVAIL = PAGE_W - 2 * MARGIN
BODY_PDF = '/home/z/my-project/scripts/mi_body_003.pdf'
COVER_PDF = '/home/z/my-project/scripts/mi_cover_003.pdf'
FINAL_PDF = '/home/z/my-project/download/market-intel/briefs/cycle-003-brief.pdf'

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
    canvas.drawString(MARGIN, PAGE_H - 0.55 * inch, 'MARKET INTEL  |  CYCLE 003 COMPRESSION BRIEF')
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
    'Cycle 003 set out to sweep ten dated watchlist markers, verify six carry-forward items, and run deep-dives '
    'on the two structures the portfolio leans on hardest: the emerging-market payout leg and the tokenized-equity '
    'consent problem. What came back is best described as compression. Within a single week, three heavyweight '
    'incumbents bid for the payout leg simultaneously, the first public wholesale pricing floor surfaced at '
    '10-50bps effective, and the Nigerian float-yield engine that underwrites the off-ramp model was cut by a '
    '350bps policy move. At the same time the issuer-consent asset institutionalized: objections multiplied, a '
    'funded transfer-agent coalition formed, and the industry lobby asked the regulator to make consent mandatory. '
    'The evidence base itself got cleaner - the stablecoin supply discrepancy that has shadowed two cycles was '
    'reconciled to a measurement mechanism, and a phantom regulatory decision that shaped the exchange thesis was '
    'removed from the record.', body))
story.append(Paragraph(
    'The cycle\'s governing finding is that every moat Cycle 002 built still exists but now has a date and a '
    'price on it. The payout leg holds rank one because it remains the only whitespace position with verified, '
    'currently-priced cash flows - and because the consolidators are buying reach rather than signing exclusivity. '
    'That distinction is the whole ballgame: Coinbase bought distribution through Thunes, Visa internalized the '
    'conversion moment, and JPMorgan is building an onshore Nigerian franchise, but none of them has locked an '
    'exclusive mobile-money payout contract. The window in which those contracts can still be signed at the '
    'portfolio\'s price is measured in quarters, not years - the strategy portfolio now front-loads its '
    'payout-leg deployment into the next two quarters, before Circle\'s Tazapay acquisition closes.', body))
story.append(Paragraph(
    'The second governing finding concerns information quality. The "SEC decision" the exchange thesis has been '
    'waiting for does not exist: the Innovation Exemption took effect immediately on September 17, runs five '
    'years, and the live gates are objection mechanics, a possible SIFMA-driven amendment toward opt-in consent, '
    'and each venue\'s own go/no-go. Removing a phantom binary from the model is worth as much as adding a new '
    'finding - two strategy cards have been re-keyed onto the real gates, and one has been repositioned entirely. '
    'The stablecoin supply "record" that made headlines on October 19 was likewise decomposed into a scope '
    'difference, leaving the DefiLlama reading of $304.1B as the program\'s canonical trigger metric - a number '
    'that now sits inside the watchlist\'s confirm zone with no Fed hike required to put it there.', body))
story.append(Spacer(1, 4))
story.append(stat_row([
    ('$304.1B', 'Stablecoin float Oct 20 - inside the <$310B confirm zone with the Fed on hold'),
    ('16', 'Issuer objections vs OKXICE - 17 of 63 symbols removed; 80% of the >20 threshold'),
    ('10-50bps', 'Wholesale off-ramp floor discovered (Mavapay) - re-anchors the 80-150bps band'),
    ('8', 'Near-dated kill triggers inside 10 weeks - Oct 27 IST event through Dec Ghana regime'),
]))
story.append(Spacer(1, 8))
story.append(Paragraph('<b>Key judgments</b>', h2))
for k in [
    'The compression cycle is real, but the thesis survives it. The payout leg holds #1 because consolidators '
    'are buying reach, not signing exclusivity - and because Tazapay is agreed, not closed, which lengthens the '
    'window before Circle-owned EM pricing exists to 12-15 months.',
    'Durable edges are now contracts, not spreads: exclusivity signed before MNO verticalization closes (Airtel '
    'VCN and MTN-Ant International are products now), the last high-yield float (Nigeria, now the only one), '
    'premium-duration corridor selection (Ghana\'s 4.8-5.1% wedge; Kenya dead), and consent administration '
    'before coalitions lock it.',
    'The phantom SEC decision is gone. The Innovation Exemption has been live since Sept 17; the gates are '
    'objection-window expiries around Nov 3-8, the SIFMA amendment ask (opt-in consent plus universal opt-out), '
    'and venue go/no-go choices. Card 2 re-keyed onto all three; Card 6 repositioned rather than killed.',
    'The yield-ban perimeter globalizes as the US legislative path dies: CLARITY failed cloture 49-50, the ECB '
    'is pushing to widen MiCA, and Kenya bans stablecoin interest from November - yet the interpretive risk to '
    'the yield rider falls from 40-50% to 20-30% because the statutory vehicle is gone.',
    'The two-speed category inverted: float now rolls over with the Fed on hold while flow compounds 36% '
    'month-on-month. Rented-float fragility is visible in USD1\'s single-address redemption run and Tether\'s '
    'halved reserve buffer; any construct underwritten at 16.84% naira yield is stale at 15.90% and falling.',
    'Whitespace #6 died and was replaced the same cycle: the tokenized-credit second source never emerged after '
    'three cycles of watching, while off-hours and emerging-market demand for non-objected tokenized equities '
    'became the best-evidenced number in the program - 62% of bStocks volume trades outside US hours.',
]:
    story.append(Paragraph('\u2022 ' + k, bullet))

# ============ 2. VERIFICATION & CARRY-FORWARD ============
story.append(heading('2. Verification and Carry-Forward Wave'))
story.append(Paragraph(
    'Six items were queued from Cycle 002 for verification, and the sweep resolved four of them cleanly. The '
    'supply-scope reconciliation is the satisfying one: three dashboards, three different numbers, one mechanism. '
    'CoinMarketCap\'s $313.78B category includes yield-bearing tokens, non-dollar pegs and self-reported supplies; '
    'DefiLlama\'s $304.1B is a curated USD-pegged set; rwa.xyz\'s $290.39B counts only natively-issued on-chain '
    'assets. The core USDT and USDC readings agree across all three, so the program adopts DefiLlama as canonical '
    'for triggers and demotes headline "records" to category noise. The OCC final rule, by contrast, remains the '
    'one live unknown - verified absent from the Federal Register as of October 20, with the Comptroller\'s '
    'target moved up to October 31.', body))
story.append(make_table(
    ['Item', 'Verdict', 'Evidence and implication'],
    [
        ['Supply-scope reconciliation', 'CONFIRMED (mechanism)',
         'CMC $313.78B broadest (yield tokens, non-USD pegs); DefiLlama $304.1B curated; rwa.xyz $290.39B native-only; core USDT/USDC agree. Use DefiLlama for triggers.'],
        ['OCC final issuer rule', 'UNRESOLVED, dated',
         'Federal Register-verified absent Oct 20; only Treasury Sept 30 IFR and Aug 18 NPRM exist; target Oct 31. Trigger #1 live for 11 more days.'],
        ['Coinme $250M', 'CONFIRMED',
         'Polygon closed the acquisition Oct 14: 37 state MTLs, 11 exemptions, 48-state coverage. Cycle-001 item closes clean.'],
        ['Ghana cost stack + e-levy', 'CONFIRMED + update',
         'E-levy repealed Mar 2025; MTN Ghana 0.75% MoMo-to-bank fee from Jun 2026 replaces it; formal crypto regime due Dec 2026.'],
        ['Tether redemptions', 'PARTIAL',
         'No Q3 attestation yet; Q2 buffer halved to $4.11B = 2.2% of liabilities; USDT -0.65% off peak; EQIBank frozen after $89M seizure (claimed <0.034% exposure, unverified).'],
        ['Partna/M-Pesa restart', 'UNRESOLVED (silent)',
         'No restart since May 7; M-Pesa stablecoin energy goes direct (Visa-Onafriq DRC pilot). Kenya stays the weakest corridor.'],
    ],
    [0.24, 0.17, 0.59]))

# ============ 3. WATCHLIST SWEEP ============
story.append(heading('3. Watchlist Sweep and Fresh Structure'))
story.append(Paragraph(
    'Four of ten markers moved materially. The most consequential movement is on the consent front, where the '
    'objection count quadrupled in sixteen days and the industry lobby simultaneously asked the SEC to convert '
    'the opt-out default into affirmative opt-in - either development alone would harden the issuer-content veto '
    'from negotiating friction into permanent structure. The float rollover matters nearly as much: $304.1B is '
    'inside the confirm zone three months before the deadline, meaning the two-speed thesis no longer needs a '
    'hike to confirm. The quiet markers are informative too - silence on exchange-paid APY for a second straight '
    'cycle, and silence on FX-spread disclosure while Ghana\'s formal regime approaches in December.', body))
story.append(make_table(
    ['Marker', 'Status', 'What moved'],
    [
        ['1 GENIUS distribution scope', 'NO MOVEMENT (rule)',
         'No final rule text (FR-verified); 87 open comment questions; CLARITY failed cloture 49-50 - the legislative path died; extension now rides on Treasury/OCC interpretation alone.'],
        ['3 Two-speed split', 'MOVED',
         'Float rolled over to $304.1B (-1.3% off the Oct 6 peak), inside the <$310B confirm zone; flow $10.42T/mo +36%; USDC designated first "significant EMT" - EBA supervision starts Nov 12 on schedule.'],
        ['4 OKXICE objections', 'MOVED UP',
         'No SEC "decision" exists - the exemption has been live since Sept 17; objections ran 1-4-9-16 in 16 days; 17/63 symbols removed; Nasdaq opted out its own shares; SIFMA asked for opt-in + universal opt-out; Perpetuals PDC filed as a second venue.'],
        ['9 Tokenized credit', 'NEW DATA',
         'Represented $37.99B (+4.07%) but distributed fell 1.21%; Figure $24.02B flat at ~63% share; still no second issuer above $2B - the whitespace dies this cycle.'],
        ['6 OPay pricing', 'TERMS FIRMED',
         '~$4B valuation target, ~$500M raise, Standard Bank cornerstone up to $200M / 4.99%; pricing expected mid-November.'],
        ['8 Rail capture', 'CONSOLIDATION, NOT EVICTION',
         'Zero new evictions; Thunes-Coinbase 140-country payout alliance (Oct 19); Kora "One Rail" pan-African launch; Stanbic Ghana-RD Technologies settlement exploration.'],
    ],
    [0.20, 0.17, 0.63]))
story.append(Paragraph(
    'The fresh-event scan added fifteen findings, of which four reshape standing theses. JPMorgan\'s approach to '
    'an onshore Nigerian merchant-bank licence by December puts a G-SIB balance sheet inside the off-ramp\'s home '
    'market for the first time since the foreign-bank retreat. Japan\'s three megabanks completed a joint '
    'yen-stablecoin proof-of-concept, replicating the Qivalis consortium model in Asia and confirming that '
    'licensed-capacity redistribution is a jurisdiction-portable mechanism. Kenya\'s VASP rulebook bans paying '
    'interest on stablecoins from November - the yield-ban perimeter\'s first EM leg - while Cameroon\'s MNOs '
    'booked CFA21.5B of interest on customer float, quantifying exactly who harvests the float-yield pool today. '
    'And the demand side of tokenized equities produced the cycle\'s hardest number: Binance bStocks reached '
    '$1B AUM faster than any product in the category, on $40B cumulative volume with 62% traded outside US '
    'market hours.', body))

# ============ 4. STRUCTURAL PROBLEMS ============
story.append(heading('4. Structural Problems: Verdicts'))
story.append(Paragraph(
    'All nine standing problems were audited against this cycle\'s evidence; three new problems cleared the '
    'formalization bar. The pattern across the audit is uniform: the structural mechanisms identified in earlier '
    'cycles are strengthening, but their expression is shifting from confrontation to institutionalization. '
    'Regulators no longer threaten the off-ramp model - they date its constraint. Rail owners no longer evict '
    'off-ramp providers - they build competing products. Consent is no longer merely withheld - it is being '
    'absorbed into vertically integrated coalitions. Problems that express through institutional absorption are '
    'slower to bite but far harder to reverse.', body))
story.append(make_table(
    ['Problem', 'Verdict', 'What changed'],
    [
        ['P1 Float-yield reallocation', 'STRENGTHENED',
         'Two-way confirmation: float rolls over while flow accelerates; bank-issuer bloc goes multipolar (Japan megabanks; RLUSD into Cross River core banking); USD1\'s single-address redemption run shows rented-float fragility.'],
        ['P7 EM credit at rate peak', 'CONFIRMED + premise retired',
         'MPR cut 350bps to 23% ends the rate-peak premise; the diagnostic shifts to credit quality under refinancing relief - easing helps borrowers but signals declining float yields (new P12).'],
        ['P8 Issuer-content veto', 'STRENGTHENED',
         '1 to 16 objectors in 16 days; 17/63 symbols removed pre-launch; SIFMA pushes affirmative opt-in and a universal opt-out; the veto is at 80% of Card 6\'s kill threshold.'],
        ['P9 Last-mile rail capture', 'REFRAMED',
         'Capture via product, not eviction: zero new evictions; Airtel\'s Mastercard VCN and MTN-Ant International are shipping products; Cameroon MNOs\' CFA21.5B float income quantifies the incentive.'],
        ['P10 NEW Consent-institutionalization squeeze', 'FORMALIZED',
         'Bullish-Equiniti IST Coalition ($4.2B transfer agent closing Jan 2027) plus Securitize claim consent administration; SIFMA\'s opt-in would make it a compliance utility - a standalone gateway loses pricing power.'],
        ['P11 NEW Yield-ban perimeter globalization', 'FORMALIZED',
         'US interpretive path + ECB MiCA widening + Kenya\'s November ban move in one cycle; offshore-yield arbitrage closes progressively; surviving yield expression migrates to banks and securities wrappers.'],
        ['P12 NEW Float-yield decay', 'FORMALIZED',
         'The EM float-yield leg is macro-rented, not owned: NGN 15.90% and easing after a 350bps MPR cut; Ghana and Kenya no longer anchor; the durable-margin triad collapses toward wedge plus exclusivity.'],
    ],
    [0.26, 0.20, 0.54]))

# ============ 5. WHITESPACE MAP V3 ============
story.append(heading('5. Whitespace Map v3'))
story.append(Paragraph(
    'One position was killed and one born in the same cycle. The tokenized-credit second source dies after three '
    'cycles of watching: no non-Figure issuer cleared $2B, distributed volume is shrinking even as represented '
    'value rose, and the category\'s demand engine rotated to equities - Ondo\'s $4B TVL passing BlackRock\'s '
    'BUIDL is the symbolic handover. Its replacement is the cycle\'s best-evidenced opportunity: off-hours and '
    'emerging-market access to non-objected tokenized equities, anchored on 62% off-hours share, $25B of xStocks '
    'cumulative volume, and a bifurcated symbol universe in which crypto-native issuers stay silent while four '
    'mega-caps remain un-objected into early November. The top of the map holds but compresses: the EM off-ramp '
    'keeps rank one on verified cash flows while its moat re-anchors from spread level to exclusivity, float and '
    'duration.', body))
story.append(make_table(
    ['#', 'Position', 'Verdict', 'Anchor and horizon'],
    [
        ['1', 'EM off-ramp', 'HOLD #1 (degraded)',
         'Retail wedge ~2.1% NGN intact; wholesale floor 10-50bps discovered; float ~+40bps/10-day at 15.90%; 12-24mo; risk = consolidation at the floor.'],
        ['2', 'EU licensed-capacity redistribution', 'HOLD, hardened',
         'EBA supervision Nov 12 on schedule; Circle fighting 60% bank-reserve treatment; Japan megabank analog flagged as scope extension; 6-12mo.'],
        ['3', 'Merchant acquiring in free-A2A markets', 'HOLD (quiet)',
         'SA mid-2027 clock stands; Visa Direct internalizes the conversion moment; 12-30mo.'],
        ['4', 'Issuer-content / consent administration', 'HOLD, REFRAMED (contested)',
         'Content bps still unpriced after 3 cycles; SIFMA opt-in = compliance necessity; IST Coalition + Securitize claim the slot; 6-12mo (shortened).'],
        ['5', 'Compliance infrastructure', 'HOLD, strengthened',
         'Date-certain floors: EBA Nov 12; Kenya Nov; Ghana Dec 2026; CBN Jan 2027; GENIUS Jan 18; 6-18mo.'],
        ['6', 'NEW: Off-hours and EM access to non-objected tokenized equities', 'ADD',
         'bStocks $40B cumulative, 62% off-hours; xStocks $25B + 80K holders; bifurcated symbol set; 6-18mo.'],
        ['7', 'FX-attached yield routing (rider)', 'HOLD (survives kill review)',
         'CLARITY dead cuts kill probability to 20-30%; US seam alive, Kenya leg dies Nov; 6-12mo.'],
        ['8', 'EM compliant dollar-savings front end', 'HOLD (wait-state)',
         'OKX APY untouched a second cycle; Gate copying; issuer-health screen added (USD1, Tether buffer); 18-24mo.'],
        ['-', 'Tokenized private credit second source', 'KILLED',
         'No second issuer >$2B after 3 cycles; distributed volume shrinking; demand rotated equities-led; Figure-stress tail moves to the watchlist.'],
    ],
    [0.05, 0.27, 0.20, 0.48]))

# ============ 6. STRATEGY CONSTRUCTS V3 ============
story.append(heading('6. Strategy Constructs v3 and Portfolio'))
story.append(Paragraph(
    'The card audit produced no kills beyond Cycle 002\'s standing one, one repositioning, and two revisions that '
    'change the portfolio\'s operating cadence. Card 6\'s repositioning is the subtle one: the objection wave '
    'kills its licensing core while SIFMA\'s opt-in push grows its administration core, so the construct survives '
    'by changing what it sells - from signing issuers itself (contested by a $4.2B coalition) to administering '
    'consent neutrally across venues for the coalitions\' conflicted books, with the four un-objected mega-caps '
    'and the silent crypto-natives as the beachhead. Card 7\'s revision is the urgent one: exclusivity-first '
    'execution is hard-dated to two quarters, tolls re-price against the newly observed 10-50bps floor, and the '
    'whole construct now runs against an explicit 12-15 month Circle-Tazapay clock.', body))
story.append(make_table(
    ['Construct', 'Verdict', 'Core mechanic', 'Kill trigger'],
    [
        ['C1 Dual-Rail Merchant Network', 'REVISED (v3)',
         'Two-line model: at the wholesale floor, float income overtakes spread income; float re-anchored 15.90% (~40bps/10-day, declining); Ghana re-based on the 4.8-5.1% wedge net of MTN\'s 0.75% fee.',
         'NGN premium <1.0% for 2 consecutive months; de-platforming event.'],
        ['C2 Session-Bridge market-making', 'NARROWED',
         'Phantom SEC decision removed; stage-gate re-keyed to 2-of-3 real gates (objection expiries / SIFMA posture / venue go-no-go); $25-50M; hard expiry Mar 31, 2027 into API-only.',
         'Closed-session dislocation nets <5bps; blanket issuer approvals.'],
        ['C3 Yield Router', 'RIDER SURVIVES',
         'Kill probability 40-50% to 20-30% (statutory vehicle dead); perimeter watch added (Kenya Nov, MiCA widening); folds into the C1/C7 stack, no standalone funding.',
         'Treasury/OCC interpretive text extends "offer and sale" to distributors before Jan 18, 2027.'],
        ['C4 Warehouse-to-IPO credit platform', 'VALIDATED (v3, anchor)',
         'Exit leg broadened beyond Africa (Mynt $7B PSE oversubscribed; OPay $4B target; MNT-Halan imminent); Figure concentration still unchallenged; NGN easing cuts both ways.',
         'No second bank LP within 12 months; OPay credit-loss spike.'],
        ['C6 Issuer-Consent Gateway', 'REPOSITIONED',
         'Renamed Consent-Administration Substrate: sell neutral cross-venue consent administration into coalitions and the venue queue; beachhead = JPM, Walmart, Costco, Eli Lilly + silent crypto-natives; negligible capital; Oct 27 IST event is the first checkpoint.',
         'Blanket issuer refusals; IST signs all holdouts exclusively.'],
        ['C7 Payout-Leg Holdco', 'REVISED (v3)',
         'Exclusivity-first execution hard-dated (2 quarters, before Tazapay close); tolls re-priced 10-60bps bundle-tiered against the Mavapay floor (~$2-27M/yr/corridor); explicit 12-15mo Circle-Tazapay clock.',
         'FX-disclosure toll caps; MNO verticalization closes exclusivity; Circle direct integration in 5+ markets.'],
    ],
    [0.20, 0.13, 0.42, 0.25]))
story.append(Paragraph(
    'The portfolio\'s center of gravity remains the payout leg, with Card 4 as the capital anchor - and the two '
    'are deliberately distinct. Card 7 is the only asset class where the portfolio can buy a durable, non-policy '
    'moat (exclusivity contracts) inside a dated window: one week of incumbent bidding plus productized MNO '
    'verticalization is direct evidence the window decays monthly, whereas Card 4\'s evidence contains no decay '
    'term - nothing is lost by deploying in the second quarter instead of the first. Allocation guidance: Card 4 '
    'takes the largest single balance-sheet allocation; Cards 7-1 are funded as one unit, contract-first, with '
    '$15-40M committed across the next two quarters before Tazapay\'s close; Card 3 folds into the stack; Card 6 '
    'runs as a negligible-capital legal-and-business-development option; Card 2 stays stage-gated '
    'pre-positioning. Cards 2 and 6 are no longer correlated on a phantom SEC binary - both re-key onto a '
    'three-gate cluster uncorrelated with the emerging-market vertical. The consolidated monitor list carries 35 '
    'triggers, of which eight are near-dated between October 27 and the end of December.', body))

# ============ 7. WATCHLIST V3 ============
story.append(heading('7. Watchlist v3: Markers for Cycle 004'))
story.append(Paragraph(
    'The watchlist is rebuilt deadline-first. The October 31 OCC rule is now the single highest-frequency item in '
    'the program: the day it lands, the distribution-scope question either becomes concrete text or passes by. '
    'Marker 2 is reframed entirely - there is no SEC decision to watch, so the consent gates become a cluster of '
    'four dated events beginning with the October 27 IST Coalition issuer forum at the NYSE. The float confirm '
    'zone is already triggered and now functions as a sustain-test through January. Everything else carries '
    'forward with updated framing, including the Figure-stress tail inherited from the killed whitespace.', body))
story.append(make_table(
    ['#', 'Marker', 'Confirms if', 'Kills if', 'Deadline'],
    [
        ['1', 'OCC final rule + GENIUS distribution scope',
         'Extends yield ban to distributors or reads "offer and sale" broadly',
         'Silent on non-issuer distribution by Jan 18 AND CLARITY stays dead',
         'Oct 31, 2026'],
        ['2', 'Issuer-consent gates: IST event; objection expiries ~Nov 3-8; SEC response to SIFMA; venue go/no-go',
         '20+ objectors, or opt-in adopted, or universal opt-out granted',
         'Objectors 5 or fewer with mega-caps listed by Q2 2027 and rulemaking ignores opt-in',
         'Nov 8, 2026 - Q2 2027'],
        ['3', 'Float confirm zone + Fed discriminator',
         '<$310B sustained through Jan 31, or Tether drift >5%/qtr, or buffer erosion continues',
         '>$321B with USDT >$190B by Jan 31',
         'Jan 31, 2027'],
        ['4', 'Session-bridge decay: Nasdaq 23x5 Dec 6; Robinhood approval',
         'Dec 6 launch on time plus options hours live plus Robinhood approved',
         'Launch slips >1 quarter AND tokenized venues secure mega-cap content',
         'Dec 6, 2026'],
        ['5', 'EM exit bifurcation: OPay pricing mid-Nov; first filings; seed counts',
         'Below-range pricing, credit-loss spike, or seed stays at 2020 lows',
         'At/above-range pricing with stable NPLs and seed rebound >30%',
         'Mid-Nov 2026'],
        ['6', 'Ghana regime to FX-disclosure',
         'Regime embeds FX-spread disclosure, or CBN/BoG tables a rule',
         'No disclosure proposal in Nigeria or Ghana',
         'Dec 31, 2026'],
        ['7', 'Payout-leg consolidation: JPM licence; Tazapay close; evictions; renewals',
         'An eviction, or Circle-owned EM pricing post-close, or MNO refuses renewal',
         'Neutral-access SLAs standard AND multi-year exclusivity secured at 20-60bps',
         'Jun 30, 2027'],
        ['8', 'Yield-ban perimeter globalization',
         'MiCA widening adopted, or 2+ more EM bans by Mar 2027',
         'MiCA stalls AND OKX APY untouched at Mar 31, 2027',
         'Mar 31, 2027'],
        ['9', 'Tokenized credit second source / Figure stress',
         'Non-Figure issuer >$2B; any Figure funding or delinquency signal',
         'Represented >$40B through Apr 2027 with no second source and no stress',
         'Apr 30, 2027'],
        ['10', 'Binance terminal state',
         'DOJ settlement curtails perp book, or EU halt persists past June',
         'CASP licence + full restoration AND DOJ closes without perp restrictions',
         'Jun 30, 2027'],
    ],
    [0.05, 0.30, 0.25, 0.25, 0.15]))
story.append(Paragraph(
    'Carry-forward verification for Cycle 004: read the OCC rule text the day it lands, with distribution scope '
    'as the first search; capture the October 27 IST Coalition read-through for the consent architecture; track '
    'the JPMorgan Nigerian licence grant in December and Tazapay close filings through MAS; read the Ghana '
    'regime text in December for disclosure and yield terms; and establish the post-December-6 overnight-session '
    'share baseline so the session-bridge decay can be measured rather than asserted. Live exclusivity term-sheet '
    'pricing against the Mavapay floor is the single most valuable new datapoint the program can collect - it '
    'converts the portfolio\'s least-proven observed-price claim into a negotiated number.', muted))
story.append(Paragraph(
    'Program archive: findings bank (Wave 1 and Wave 2), discovery, analysis, strategy cards, and this brief are '
    'versioned in the program repository. PDF edition: briefs/cycle-003-brief.pdf.', muted))

# ---- build body ----
doc = SimpleDocTemplate(BODY_PDF, pagesize=A4,
                        leftMargin=MARGIN, rightMargin=MARGIN,
                        topMargin=MARGIN, bottomMargin=0.85 * inch,
                        title='Market Intel - Cycle 003 Compression Brief',
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
