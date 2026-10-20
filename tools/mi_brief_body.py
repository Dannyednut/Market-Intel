#!/usr/bin/env python3
"""Market Intel - Cycle 001 Brief (body) + cover merge.
Pipeline: ReportLab body -> pypdf merge with Playwright cover -> final PDF.
Palette: Template 07 Crystal Blue body tiers (fixed, per typesetting/cover.md).
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
BODY_PDF = '/home/z/my-project/scripts/mi_body.pdf'
COVER_PDF = '/home/z/my-project/scripts/mi_cover.pdf'
FINAL_PDF = '/home/z/my-project/download/market-intel/briefs/cycle-001-brief.pdf'

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
    # header
    canvas.setFont('FreeSerif', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, PAGE_H - 0.55 * inch, 'MARKET INTEL  |  CYCLE 001 BASELINE BRIEF')
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(1.2)
    canvas.line(MARGIN, PAGE_H - 0.62 * inch, PAGE_W - MARGIN, PAGE_H - 0.62 * inch)
    # footer
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
    'This brief is the baseline output of the Market Intel program: a continuous, multi-agent research operation '
    'covering fintech, exchanges, and the cross-market infrastructure that connects them. Cycle 001 ran three '
    'parallel research agents across the mandated landscapes, producing 42 verified findings, which discovery, '
    'analysis, and strategy-engineering cells then worked into a structured intelligence picture. All claims below '
    'are traceable to the findings bank that accompanies this brief in the program archive, and every figure cites '
    'at least one primary or high-quality secondary source.', body))
story.append(Paragraph(
    'Three structural shifts govern the current landscape. First, the stablecoin float-yield engine is being '
    'reallocated to banks by law: the GENIUS Act bans issuer-paid yield, the Federal Reserve sits at 3.75 to 4.00 '
    'percent, and yield is rerouting into bank-controlled tokenized money-market funds and deposits ahead of the '
    '21-bank consortium stablecoin expected in the first half of 2027. Second, regulator-mandated free instant '
    'payments in emerging markets, from the Philippines fee cap to the UEMOA PI-SPI network, are decommissioning '
    'the transfer-fee layer that agent banking and P2P wallets depended on. Third, the exchange moat is flipping '
    'from liquidity to licences, as MiCA enforcement and the SEC Innovation Exemption reward regulated venues '
    'while offshore leaders face escalating legal pressure.', body))
story.append(Paragraph(
    'The investment posture that follows from the evidence is asymmetric. Capital is crowding into the issuer and '
    'venue layers, where 45 percent of all fintech venture dollars now land, while the scarce assets sit elsewhere: '
    'emerging-market licences, last-mile payout networks, and the compliance seam between non-yielding stablecoins '
    'and affiliated yield products. The whitespace map in Section 4 and the engineered constructs in Section 5 are '
    'built directly on that asymmetry.', body))
story.append(Spacer(1, 4))
story.append(stat_row([
    ('$300.9B', 'Stablecoin float, Oct 1 - down 6% from Apr-May peak'),
    ('$433B/mo', 'Offshore TradFi perps in Aug - roughly 15x January'),
    ('$103.1B', 'H1 2026 fintech funding - 45% into digital assets'),
    ('15%', 'US spot exchange share - roughly doubled in 12 months'),
]))
story.append(Spacer(1, 8))
story.append(Paragraph('<b>Key judgments</b>', h2))
for k in [
    'The stablecoin contraction is rate-driven rather than risk-off: Tether shrank while RLUSD grew 50 percent '
    'month over month, so float is being routed, not abandoned.',
    'Free A2A rails convert payments volume into a public good within roughly 18 months per market; margin '
    'migrates to credit, merchant acquiring, and cross-border FX.',
    'African fintech capital is flipping from venture equity to bank balance sheets, anchored by the Absa-Lendable '
    'credit fund and public listings such as OPay and MNT-Halan.',
    'The two hard clocks in the system are the SA non-bank payments opening in mid-2027 and the bank consortium '
    'stablecoin launch in H1 2027; both convert whitespace into sequencing decisions.',
]:
    story.append(Paragraph('• ' + k, bullet))

# ============ 2. MARKET STRUCTURE SHIFTS ============
story.append(heading('2. Market Structure Shifts'))
story.append(Paragraph(
    'The cycle\u2019s verified moves concentrate in three arenas: who may issue dollar liquidity, who may hold the '
    'customer relationship, and who carries regulatory permission to operate. On the first, the GENIUS Act '
    'rulemaking plus the 21-bank consortium commitment mark the arrival of regulated issuers with deposit-funded '
    'balance sheets, while MiCA hard-gates the EU market to 25 authorized issuers and excludes Tether entirely. '
    'On the second, exchanges are buying banks, brokers, and clearinghouses, and TradFi venues are reciprocating '
    'with venture stakes and joint ventures, collapsing the boundary between crypto rails and market '
    'infrastructure. On the third, the SEC Innovation Exemption creates a five-year legal lane for tokenized '
    'equities that incumbents are already filling with filings.', body))
story.append(Paragraph(
    'The table below lists the moves with the highest structural information content from this cycle. Each is '
    'verified against at least two quality sources in the findings bank, and the read column states the '
    'implication rather than restating the headline.', body))
story.append(make_table(
    ['Domain', 'Verified move', 'Read'],
    [
        ['Funding', 'Ramp raises $1.85B at about $60B; Brex exits to Capital One for $5.15B',
         'Spend management consolidates around one independent leader; exits clear only at monopoly or control premia.'],
        ['M&A', 'Circle agrees to acquire Tazapay for $400M',
         'The largest regulated issuer is pivoting from float income to cross-border flow; over $25B volume, ~60% already stablecoin-based.'],
        ['Africa', 'OPay files for NYSE IPO; MNT-Halan IPO draws 11x institutional demand on EGX',
         'EM lenders monetize through public markets while lending supplies roughly 60% of OPay revenue - credit risk moves to public holders.'],
        ['Regulation', 'SEC issues 5-year Innovation Exemption for tokenized NMS stocks; OKX-ICE JV files for 63 symbols',
         'Permissioned AMMs become a legal venue class; incumbents pre-fill the lane before rules finalize.'],
        ['Venues', 'Kraken parent agrees to buy Saldo Bank; Nasdaq invests $100M at $21B',
         'Licences displace liquidity as the exchange moat; TradFi capital now holds crypto equity.'],
        ['Stablecoins', '21 global banks commit to a joint USD stablecoin company for H1 2027',
         'Settlement migrates onto bank balance sheets; the yield seam collapses toward deposit wrappers.'],
        ['Nigeria', 'CBN cuts 350bp to 23%; stablecoins written into Payments System Vision 2028',
         'The largest SSA stablecoin market opens the rails while cutting the rate that funded fintech lending.'],
        ['Payments', 'Philippines caps instant-transfer fees near cost; transfer volumes rise about 50%',
         'Template for regulator-driven fee compression; free A2A is spreading across emerging markets.'],
    ],
    [0.13, 0.38, 0.49]))

# ============ 3. STRUCTURAL PROBLEMS ============
story.append(heading('3. Structural Problems'))
story.append(Paragraph(
    'Analysis isolated five problems that are structural rather than cyclical: each is driven by legislation, rail '
    'design, or capital-structure forces that competition alone cannot reverse. Their common signature is a margin '
    'pool being closed by rule while the beneficiaries are pre-positioned on the other side of the rule. The '
    'second-order chains matter more than the problems themselves: yield-ban effects push wallets into flow '
    'monetization, free-A2A pushes operators into credit, and both migrations concentrate risk in balance sheets '
    'just as public markets are invited in through IPOs.', body))
story.append(make_table(
    ['Problem', 'Mechanism', 'Most exposed', 'Severity'],
    [
        ['Float-yield reallocation',
         'GENIUS bans issuer-paid yield; yield reroutes to bank-controlled tokenized MMFs and deposits; consortium stablecoin lands 2027.',
         'Pure-play issuers; APY resellers on offshore apps.', 'High'],
        ['Free-A2A fee decommissioning',
         'Regulator-mandated free instant payments commoditize transfers; agent transaction sets collapse (Onafriq winding down Baxi).',
         'Agent networks; P2P-fee wallets; payout franchises.', 'High'],
        ['Exit-market bifurcation',
         'Only monopoly or strategic-control premia clear; median African seed fell to $1.2M and deal counts are at 2020 lows.',
         'Seed and Series A founders; sub-scale funds.', 'Medium-high'],
        ['Licence moat strands offshore leaders',
         'MiCA enforcement plus a DOJ probe squeeze Binance while rivals acquire banks, clearinghouses, and custody mandates.',
         'Binance EU flow; USDT\u2019s EU role.', 'High'],
        ['EM credit concentration at the rate peak',
         'Lending is the only scalable line left after fee compression; IPOs transfer peak-cycle credit risk to public markets.',
         'Public investors in EM lender IPOs; pivot operators.', 'Medium'],
    ],
    [0.20, 0.38, 0.26, 0.16]))
story.append(Paragraph(
    'Three implication chains deserve standing attention. If the yield ban holds and rates stay above 3.5 percent, '
    'expect two to four acquisitions of remittance and payout rails within 12 to 18 months, and at least one '
    'enforcement action against exchange-paid APY products. If free A2A propagates, expect transfer revenue '
    'lines in emerging-market operator filings to fall 20 percent year over year by H1 2027, with at least one '
    'post-IPO consumer lender reporting a credit-loss spike. If the offshore TradFi perp book keeps growing while '
    'onshore tokenized venues await approval, single-stock perpetuals become the next enforcement flashpoint '
    'within 6 to 12 months.', body))

# ============ 4. WHITESPACE MAP ============
story.append(heading('4. Whitespace Map'))
story.append(Paragraph(
    'Discovery ranked seven whitespace positions and killed one candidate outright: neutral cross-rail clearing '
    'between tokenized and conventional equities, because 24-hour session extension removes its core wedge and '
    'venues are vertically integrating their own rails. The six survivors are ranked by evidence strength times '
    'timing. Each names its proof points from the findings bank, a realistic horizon, and the primary risk that '
    'would invalidate the position.', body))
story.append(make_table(
    ['Whitespace position', 'Evidence anchors', 'Horizon', 'Primary risk'],
    [
        ['EM off-ramp and licence consolidation (Africa corridors)',
         'Circle-Tazapay; Kora One Rail; dLocal-WU payouts; Egypt licence freeze; Nigeria formalization.',
         '12-24 mo', 'Payout fee caps once regulators obtain corridor-level cost data.'],
        ['Yield-routing stack (non-yielding stablecoin front end into tokenized MMFs)',
         'GENIUS yield ban; $14.9B tokenized Treasuries; Fed at 3.75-4.00%; OKX 10% APY seam.',
         '6-18 mo', 'Market-structure bill extends the yield ban to platforms and affiliates.'],
        ['EU licensed-capacity redistribution',
         'Binance MiCA probes and DOJ escalation; only 25 authorized issuers; Kraken buying an EU bank.',
         '6-12 mo', 'A Binance settlement restores EU access on compressed terms.'],
        ['EM compliant dollar-savings front end',
         'USDG 10% APY vs falling naira deposit rates; Nigeria holding ~60% of SSA stablecoin inflows.',
         '12-24 mo', 'Capital-control backlash; the regulatory embrace is one executive order old.'],
        ['Tokenized private credit second source',
         'Figure supplies $15B of an $18-19B category; Absa-Lendable shows bank LP demand for originator pipelines.',
         '12-24 mo', 'A Figure credit event taints the whole category for several quarters.'],
        ['Merchant acquiring in free-A2A markets (SA opens mid-2027)',
         'Philippines volume elasticity of +50% under fee caps; PI-SPI free rails; SA licensing timeline known.',
         '12-30 mo', 'Free A2A extends to merchant QR and compresses acquiring too.'],
    ],
    [0.27, 0.33, 0.10, 0.30]))

# ============ 5. STRATEGY CONSTRUCTS ============
story.append(heading('5. Strategy Constructs'))
story.append(Paragraph(
    'The engineering cell converted the whitespace map into five constructs with explicit mechanics, revenue '
    'engines, moats, and kill criteria. They are deliberately diversified across regulatory dependency: three '
    'share the Nigeria PSV 2028 and GENIUS boundary clocks and should be monitored by one regulatory-scenario '
    'watch; the market-making construct carries a built-in decay clock as venue hours converge; and the credit '
    'warehouse is counter-cyclical to rate policy and monetizes the equity-funding gap rather than any single '
    'regulatory window. Full cards with first-90-day moves live in the archive document '
    'cycle-001-strategy-cards.md.', body))
story.append(make_table(
    ['Construct', 'Core mechanic', 'Capital intensity', 'Kill trigger'],
    [
        ['Dual-Rail Merchant Network',
         'Collect domestically on free national rails such as PI-SPI at zero MDR; settle cross-border on stablecoins; earn 60-100bps FX spread on converted volume.',
         'Asset-light', 'Corridor spreads compress below 150bps roundtrip for two quarters.'],
        ['Session-Bridge market-making',
         'Quote tokenized US stocks during closed sessions pinned to futures-adjusted fair value; hedge at the open; sell the routing API white-label.',
         'Balance-sheet', 'Realized closed-session dislocation nets under 5bps after hedge costs.'],
        ['Yield Router',
         'Never issue and never pay yield; route idle EM fintech stablecoin float into tokenized MMF wrappers; earn 25-50bps placement plus FX legs.',
         'Asset-light', 'US legislation extends the yield ban to distribution and affiliates.'],
        ['Warehouse-to-IPO credit platform',
         'Buy African fintech loan books in local currency against bank-anchored senior tranches; season, then refinance via EGX or bank sales.',
         'Balance-sheet-heavy', 'No second or third bank LP signs within 12 months.'],
        ['Agent-Network Reversal',
         'Acquire wind-down agent networks at distress multiples; convert tellers into stablecoin cash-in and cash-out nodes under a licensed lead.',
         'Moderate', 'Agent retention below 60% at six months post-acquisition.'],
    ],
    [0.19, 0.42, 0.14, 0.25]))

# ============ 6. WATCHLIST ============
story.append(heading('6. Watchlist: Markers for Cycle 002'))
story.append(Paragraph(
    'Each structural claim above is paired with falsifiable markers so the program updates on evidence rather '
    'than narrative. The verification wave in the next cycle will re-check the single-source figures that carry '
    'the most weight: the $433B offshore TradFi perp month, the Citi custody packaging detail, and the '
    'vendor-published stablecoin remittance cost claim that a G7 central bank has publicly disputed. Cycle 002 '
    'will also sweep the watchlist events below and deepen the two highest-conviction whitespace positions with '
    'corridor-level unit economics.', body))
story.append(make_table(
    ['Marker', 'Confirms the thesis if', 'Kills the thesis if'],
    [
        ['Stablecoin supply through Q1 2027',
         'Aggregate falls below $280B or Tether redemptions accelerate.',
         'Supply reclaims $321B within two quarters of a Fed pause.'],
        ['Regulator touch on APY or offshore single-stock perps',
         'Guidance or enforcement lands by mid-2027.',
         'Silence persists through 2027 while volumes keep compounding.'],
        ['H1 2027 EM operator filings (post free-A2A)',
         'Transfer revenue down 20% year over year, or an NPL spike at a lending-led super-app.',
         'Transfer-fee revenue stable or rising across filings.'],
        ['Tokenized credit second source',
         'A non-Figure issuer crosses $2B, defusing concentration.',
         'A Figure stress event confirms the contagion channel instead.'],
        ['African seed funding counts, H2 2026 to H1 2027',
         'Counts stay near 2020 lows; banks keep replacing venture LPs.',
         'Seed counts rebound more than 30% from the H1 2026 base.'],
        ['Venue structure events (OKX-ICE approval; Binance EU and DOJ)',
         'Two or more events resolve toward regulated venues absorbing flow.',
         'Binance re-enters the EU with no action on its perp book.'],
    ],
    [0.28, 0.37, 0.35]))
story.append(Paragraph(
    'Archive note: the complete evidence base for this brief - 42 findings with sources, the discovery map, the '
    'analysis chains, and the five full strategy cards - is versioned alongside this document in the Market Intel '
    'repository under findings/, together with the program worklog that records each cycle\u2019s agent '
    'assignments and outputs.', muted))

# ---- build body ----
doc = SimpleDocTemplate(BODY_PDF, pagesize=A4,
                        leftMargin=MARGIN, rightMargin=MARGIN,
                        topMargin=MARGIN, bottomMargin=0.85 * inch,
                        title='Market Intel - Cycle 001 Baseline Brief',
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
