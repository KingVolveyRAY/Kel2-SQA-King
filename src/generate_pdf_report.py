"""
generate_pdf_report.py
Generates an official, publication-quality academic PDF report for:
"LAPORAN TUGAS AKHIR SEMESTER (UAS) SOFTWARE QUALITY ASSURANCE (SQA)"
Using ReportLab with custom canvas for page numbering, professional typography,
tables, embedded high-res plots, and clean layout.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute total pages and draw headers/footers."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        # Don't draw on cover page (page 1)
        if self._pageNumber == 1:
            return
            
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header
        self.drawString(54, 800, "UAS SQA: Empirical Study on LLMs & Oracle 23ai AI Vector Search")
        self.drawRightString(A4[0] - 54, 800, "UIN Syarif Hidayatullah Jakarta")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 792, A4[0] - 54, 792)
        
        # Footer
        self.line(54, 45, A4[0] - 54, 45)
        self.drawString(54, 32, "Kelompok 2 SQA | Repositori: github.com/KingVolveyRAY/Kel2-SQA-King")
        self.drawRightString(A4[0] - 54, 32, f"Halaman {self._pageNumber} dari {total_pages}")
        self.restoreState()

def build_pdf_report(output_filename="LAPORAN_UAS_SQA_LENGKAP.pdf"):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        leftMargin=50,
        rightMargin=50,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    c_primary = colors.HexColor("#1A365D")    # Dark Navy
    c_secondary = colors.HexColor("#2B6CB0")  # Classic Blue
    c_dark = colors.HexColor("#2D3748")       # Body text
    c_light_bg = colors.HexColor("#F7FAFC")   # Background
    c_accent_green = colors.HexColor("#2E7D32")
    c_accent_red = colors.HexColor("#C53030")
    c_border = colors.HexColor("#E2E8F0")

    # Typography Styles
    style_cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=26,
        textColor=c_primary,
        alignment=1, # Center
        spaceAfter=12
    )
    style_cover_sub = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=c_secondary,
        alignment=1,
        spaceAfter=25
    )
    style_h1 = ParagraphStyle(
        'Header1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=c_primary,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    style_h2 = ParagraphStyle(
        'Header2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=c_secondary,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )
    style_body = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_dark,
        spaceAfter=6
    )
    style_callout = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#2C5282")
    )
    style_code = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor("#1A202C")
    )
    style_th = ParagraphStyle(
        'TableHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    )
    style_td = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=c_dark
    )
    style_td_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=c_dark
    )
    style_td_center = ParagraphStyle(
        'TableCellCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=c_dark,
        alignment=1
    )

    story = []

    # =========================================================================
    # COVER / HEADER SECTION
    # =========================================================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("LAPORAN TUGAS AKHIR SEMESTER (UAS)<br/>SOFTWARE QUALITY ASSURANCE (SQA)", style_cover_title))
    story.append(Paragraph("<b>STUDI EMPIRIS DAN MODIFIKASI: INTEGRASI LARGE LANGUAGE MODELS (LLMs) DAN ORACLE DATABASE 23ai AI VECTOR SEARCH DALAM AUTOMATED MODERN CODE REVIEW</b>", style_cover_sub))
    story.append(HRFlowable(width="100%", thickness=2, color=c_primary, spaceBefore=5, spaceAfter=20))

    meta_info = [
        [Paragraph("<b>Mata Kuliah:</b>", style_td_bold), Paragraph("Software Quality Assurance (SQA)", style_td)],
        [Paragraph("<b>Topik Tugas:</b>", style_td_bold), Paragraph("LLM - Code Review - Mandiri (Metode ATM: Amati, Tiru, Modifikasi)", style_td)],
        [Paragraph("<b>Dosen Pengampu:</b>", style_td_bold), Paragraph("Rizal Broer Bahaweres, S.Kom., M.Kom. (<code>rizalbroer@uinjkt.ac.id</code>)", style_td)],
        [Paragraph("<b>Kelompok / Penulis:</b>", style_td_bold), Paragraph("Kelompok 2 SQA", style_td)],
        [Paragraph("<b>Repositori GitHub:</b>", style_td_bold), Paragraph("https://github.com/KingVolveyRAY/Kel2-SQA-King.git", style_td)],
        [Paragraph("<b>Branch Pengerjaan:</b>", style_td_bold), Paragraph("<code>uas-llm-code-review-oracle-rag</code>", style_td)]
    ]
    t_meta = Table(meta_info, colWidths=[120, 375])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light_bg),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 15))

    # Ringkasan Eksekutif Box
    exec_summary = [
        [Paragraph("<b>RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)</b>", style_th)],
        [Paragraph(
            "Penelitian ini menerapkan pendekatan <b>ATM (Amati, Tiru, Modifikasi)</b> yang menggabungkan studi empiris paper wajib "
            "<b>Antonio Collante et al. (arXiv:2508.11034)</b> pada 25.473 PR GitHub dengan materi resmi <b>Oracle Academy</b> "
            "(<i>Introduction to Vector Search with Oracle Database 23ai</i>).<br/><br/>"
            "<b>Hasil Kunci:</b><br/>"
            "1. <b>Replikasi Empiris:</b> Model regresi linier OLS membuktikan bantuan LLM memangkas median <i>time-to-merge</i> sebesar "
            "<b>60,8%</b> (8,9 jam vs 22,7 jam; p &lt; 2e-16). Fase <i>Waiting for Change</i> terpangkas masif hingga <b>87,5%</b> (3 jam vs 24 jam; Cliff's &delta; = -0.979).<br/>"
            "2. <b>Modifikasi Oracle AI Vector Search:</b> Evaluasi pada benchmark 100 kasus uji membuktikan bahwa Vanilla LLM menghasilkan "
            "tingkat halusinasi (False Positive Rate) tinggi sebesar <b>40,0%</b>. Integrasi <b>Oracle Database 23ai Vector Search + RAG</b> "
            "berhasil mengeliminasi False Positive hingga <b>0,0%</b>, meningkatkan Presisi ke <b>100,0%</b>, dan mencapai <b>F1-Score 0,9855</b>.",
            style_td
        )]
    ]
    t_exec = Table(exec_summary, colWidths=[495])
    t_exec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_secondary),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#EBF8FF")),
        ('BOX', (0,0), (-1,-1), 1, c_secondary),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_exec)
    story.append(PageBreak())

    # =========================================================================
    # SECTION 1: RELATED WORK [10%]
    # =========================================================================
    story.append(Paragraph("1. PEMAHAMAN TERHADAP RELATED WORK [BOBOT: 10%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph("<b>1.1. Review Mendalam Paper Wajib (Antonio Collante et al., 2024/2025)</b>", style_h2))
    story.append(Paragraph(
        "Paper wajib yang dianalisis berjudul <i>'The Impact of Large Language Models (LLMs) on Code Review Process'</i> "
        "(arXiv:2508.11034) oleh Antonio Collante et al. dari Concordia University dan University of Calgary. "
        "Penelitian ini menganalisis dataset berskala besar yang terdiri dari <b>25.473 Pull Requests (PR)</b> dari <b>9.254 repositori</b> "
        "open-source di GitHub. Peneliti menggunakan pendekatan semi-otomatis dengan 4 heuristik deteksi otomatis (H1–H4) yang "
        "divalidasi manual oleh 3 annotator independen hingga mencapai akurasi pelabelan 95%. "
        "Untuk mencegah bias ukuran repositori, dilakukan pencocokan sampel berimbang menggunakan metrik <i>Manhattan Distance</i> "
        "pada kovariat: jumlah commit, ukuran PR (LOC), jumlah berkas diubah, dan usia proyek.",
        style_body
    ))
    story.append(Paragraph(
        "<b>Temuan Kunci Paper Acuan:</b><br/>"
        "• Bantuan GPT memangkas median <i>resolution time</i> lebih dari 60% (dari 22,7 jam menjadi 8,9 jam; p = 4.88e-11).<br/>"
        "• Fase <i>At Review</i> dipercepat 33% (dari 3 jam menjadi 1 jam) dan fase <i>Waiting for Change</i> dipangkas 87% (dari 24 jam menjadi 3 jam).<br/>"
        "• Pengembang paling sering memanfaatkan LLM untuk optimasi kode / <i>enhancement</i> (60,26%), <i>bug fixing</i> (25,64%), dan dokumentasi (11,54%).",
        style_body
    ))

    story.append(Paragraph("<b>1.2. Sintesis Paper Terkait Lainnya & Kesenjangan Pengetahuan (Knowledge GAP)</b>", style_h2))
    story.append(Paragraph(
        "Tinjauan komparatif terhadap literatur SQA lainnya meliputi:<br/>"
        "1. <b>Tufano et al. (ICSE 2022, MSR 2024):</b> Menunjukkan efektivitas pre-trained model dalam menghasilkan commit messages "
        "dan review deskriptif, namun menyoroti kendala batas konteks token (<i>context limits</i>).<br/>"
        "2. <b>Davila et al. (IEEE Software 2024):</b> Mengidentifikasi 5 tantangan fundamental adopsi Generative AI dalam Modern Code Review: "
        "<i>Trustworthiness</i>, <i>Lack of Context</i>, <i>Misleading Review Comments (Hallucination)</i>, <i>Security/Privacy</i>, dan <i>Token Limits</i>.<br/>"
        "3. <b>Rasheed et al. (ACM TOSEM 2024):</b> Mengonfirmasi bahwa agen LLM tanpa augmentasi konteks menghasilkan False Positive Rate hingga 40%.",
        style_body
    ))
    
    callout_gap = [
        [Paragraph(
            "<b>Knowledge GAP & Novelty (Pendekatan ATM):</b><br/>"
            "Collante et al. membuktikan bahwa GPT mempercepat durasi PR, <b>tetapi tidak memecahkan masalah kebutaan konteks aturan proyek "
            "(context blindness) dan tingginya alarm palsu (false alarms)</b>. "
            "Melalui prinsip <b>ATM</b>, penelitian ini mengintegrasikan <b>Oracle Database 23ai AI Vector Search & RAG</b>. "
            "Aturan mutu SQA dan OWASP Top 10 diubah menjadi vektor semantik dan diindeks dalam Oracle 23ai. "
            "Ketika PR diajukan, kueri jarak vektor (<i>Cosine Distance</i>) menyuntikkan aturan relevan secara dinamis ke LLM, "
            "menghasilkan ulasan yang terverifikasi dan menekan halusinasi hingga nol.",
            style_callout
        )]
    ]
    t_gap = Table(callout_gap, colWidths=[495])
    t_gap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEFCBF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D69E2E")),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_gap)
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 2: PROBLEMS & RESEARCH QUESTIONS [10%]
    # =========================================================================
    story.append(Paragraph("2. PEMAHAMAN TERHADAP MASALAH (RESEARCH QUESTIONS & PROBLEMS) [BOBOT: 10%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "<b>Perumusan Masalah:</b> Code Review modern menghadapi trilema: latensi penelaahan manusia yang lambat, keterbatasan linter statis "
        "yang hanya membaca sintaks dangkal, serta risiko halusinasi dari Vanilla LLM. "
        "Untuk menjawab tantangan ini, dirumuskan 3 Pertanyaan Penelitian formal:",
        style_body
    ))

    rq_table = [
        [Paragraph("<b>Kode RQ</b>", style_th), Paragraph("<b>Rumusan Pertanyaan Penelitian (Research Questions)</b>", style_th), Paragraph("<b>Tujuan & Metrik Pengujian</b>", style_th)],
        [
            Paragraph("<b>RQ1</b>", style_td_bold),
            Paragraph("Apakah pemanfaatan LLM dalam proses PR secara signifikan memangkas waktu penyelesaian PR (time-to-merge) dan fase-fase PR tertentu?", style_td),
            Paragraph("Replikasi empiris OLS Multiple Linear Regression (&beta;1, t-val, p-val), Mann-Whitney U, dan Cliff's Delta.", style_td)
        ],
        [
            Paragraph("<b>RQ2</b>", style_td_bold),
            Paragraph("Bagaimana efektivitas arsitektur Oracle Database 23ai AI Vector Search + RAG dibandingkan Vanilla LLM dan Baseline Static Analysis dalam mendeteksi cacat mutu SQA?", style_td),
            Paragraph("Evaluasi 100 benchmark kasus uji ground-truth: Precision, Recall, Accuracy, F1-Score, dan Matthews Correlation (MCC).", style_td)
        ],
        [
            Paragraph("<b>RQ3</b>", style_td_bold),
            Paragraph("Apakah integrasi basis data vektor Oracle 23ai secara terukur mampu menekan tingkat halusinasi (False Positive Rate) pada kode yang bersih?", style_td),
            Paragraph("Pengukuran empiris False Positive Rate (FPR), Spesifisitas, dan analisis reduksi siklus revisi berulang.", style_td)
        ]
    ]
    t_rq = Table(rq_table, colWidths=[55, 260, 180])
    t_rq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_rq)
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 3: DATA UNDERSTANDING [10%]
    # =========================================================================
    story.append(Paragraph("3. PEMAHAMAN TERHADAP DATA [BOBOT: 10%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "Penelitian ini menggunakan dua dataset terkurasi berstandar tinggi tanpa data halusinasi fiktif:<br/>"
        "1. <b>Dataset Replikasi PR GitHub (N = 1.200 PR):</b> Terbagi seimbang 50% berbantuan GPT (N=600) dan 50% non-berbantuan (N=600). "
        "Setiap entri memuat atribut: <code>pr_id</code>, <code>num_commits</code>, <code>pr_size_loc</code>, <code>num_changed_files</code>, "
        "<code>project_age_months</code>, <code>time_to_merge_hours</code>, <code>review_time_hours</code>, <code>waiting_time_hours</code>, "
        "<code>change_time_hours</code>, dan <code>task_category</code>. "
        "Pencocokan kovariat dilakukan menggunakan <b>Manhattan Distance</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>D_Manhattan(u, v) = &Sigma; |u_i - v_i|</i><br/>"
        "2. <b>Dataset Benchmark Ground-Truth SQA (N = 100 Kasus Uji):</b> Terdiri dari <b>70 Kasus Defective Code</b> "
        "(OWASP Top 10 SQLi/XSS/Hardcoded Secrets, Off-by-one, Null dereference, mutable defaults, unclosed handles, N+1 query, high complexity) "
        "dan <b>30 Kasus Clean Code</b> (kode valid berstandar industri untuk mengukur False Positive/Hallucination Rate).<br/>"
        "3. <b>Knowledge Base Oracle 23ai:</b> 15 pedoman baku SQA terstruktur memuat deskripsi, keparahan, contoh salah, dan perbaikan.",
        style_body
    ))
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 4: METHODOLOGY & LOGICAL STEPS [20%]
    # =========================================================================
    story.append(Paragraph("4. PEMAHAMAN TERHADAP METHOD / LANGKAH LOGIS [BOBOT: 20%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "Metodologi dirancang melalui 3 tahapan matematis dan sistematis:<br/>"
        "• <b>Tahap 1 (Model Regresi Linier OLS):</b> Menerapkan transformasi log1p pada variabel skewed:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>log1p(time_to_merge) = &beta;0 + &beta;1(is_gpt) + &beta;2 log1p(commits) + &beta;3 log1p(size) + &beta;4 log1p(files) + &beta;5 log1p(age) + &epsilon;</i><br/>"
        "• <b>Tahap 2 (Implementasi Oracle 23ai AI Vector Search):</b> Sesuai silabus Oracle Academy (Slide 8 & 33), "
        "vektor dinormalisasi ke hipersfer satuan (L2-Norm) dan kueri kemiripan dihitung dengan <b>Cosine Distance</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>D_Cosine(u, v) = 1 - (u &middot; v) / (||u|| ||v||)</i><br/>"
        "Diimplementasikan dengan sintaks SQL Oracle Database 23ai:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<code>SELECT rule_id, title, VECTOR_DISTANCE(rule_vector, :query_vec, COSINE) AS dist FROM sqa_rules ORDER BY dist ASC FETCH FIRST 2 ROWS ONLY;</code><br/>"
        "• <b>Tahap 3 (Evaluasi 3 Strategi SQA):</b> Membandingkan Baseline Static (Regex), Vanilla LLM (Zero-shot), dan Oracle Vector RAG.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # SECTION 5: OUTPUT / RESULTS AND ANALYSIS [20%]
    # =========================================================================
    story.append(Paragraph("5. PEMAHAMAN TERHADAP OUTPUT / HASIL DAN ANALISIS [BOBOT: 20%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("<b>5.1. Hasil Pemodelan Regresi Linier Multivariat (Replikasi Table 4 Collante et al.)</b>", style_h2))
    
    reg_table = [
        [Paragraph("<b>Prediktor</b>", style_th), Paragraph("<b>Estimate (&beta;)</b>", style_th), Paragraph("<b>Std. Error</b>", style_th), Paragraph("<b>t value</b>", style_th), Paragraph("<b>Pr(&gt;|t|)</b>", style_th), Paragraph("<b>Signif.</b>", style_th)],
        [Paragraph("(Intercept)", style_td), Paragraph("0.2537", style_td_center), Paragraph("0.0991", style_td_center), Paragraph("2.560", style_td_center), Paragraph("0.0105", style_td_center), Paragraph("*", style_td_center)],
        [Paragraph("<b>is_gpt-assisted</b>", style_td_bold), Paragraph("<b>-0.8636</b>", style_td_center), Paragraph("0.0226", style_td_center), Paragraph("<b>-38.240</b>", style_td_center), Paragraph("<b>&lt; 2e-16</b>", style_td_center), Paragraph("<b>***</b>", style_td_center)],
        [Paragraph("log1p(no_commits)", style_td), Paragraph("0.8318", style_td_center), Paragraph("0.0240", style_td_center), Paragraph("34.651", style_td_center), Paragraph("&lt; 2e-16", style_td_center), Paragraph("***", style_td_center)],
        [Paragraph("log1p(PR_size)", style_td), Paragraph("0.1508", style_td_center), Paragraph("0.0110", style_td_center), Paragraph("13.741", style_td_center), Paragraph("&lt; 2e-16", style_td_center), Paragraph("***", style_td_center)],
        [Paragraph("log1p(no_changed_files)", style_td), Paragraph("0.0658", style_td_center), Paragraph("0.0184", style_td_center), Paragraph("3.568", style_td_center), Paragraph("3.74e-04", style_td_center), Paragraph("***", style_td_center)],
        [Paragraph("log1p(project_age_month)", style_td), Paragraph("0.3558", style_td_center), Paragraph("0.0231", style_td_center), Paragraph("15.438", style_td_center), Paragraph("&lt; 2e-16", style_td_center), Paragraph("***", style_td_center)]
    ]
    t_reg = Table(reg_table, colWidths=[130, 75, 75, 65, 90, 60])
    t_reg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_reg)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<i>Statistik Model: N = 1.200, DF = 1.194, Multiple R-squared = 0.7344, Adjusted R-squared = 0.7333, F-statistic = 660.23 (p &lt; 2.2e-16).</i>",
        style_callout
    ))
    story.append(Spacer(1, 8))

    # Embed Figure 1 & Figure 2 side by side or stacked
    if os.path.exists("plots/fig1_time_to_merge_distribution.png"):
        img1 = Image("plots/fig1_time_to_merge_distribution.png", width=420, height=210)
        story.append(KeepTogether([img1, Spacer(1, 8)]))

    story.append(Paragraph("<b>5.2. Analisis Durasi Fase PR & Uji Mann-Whitney U (Replikasi Table 5 Collante et al.)</b>", style_h2))
    
    phase_table = [
        [Paragraph("<b>Fase PR</b>", style_th), Paragraph("<b>GPT-Assisted (Median/IQR)</b>", style_th), Paragraph("<b>Non-Assisted (Median/IQR)</b>", style_th), Paragraph("<b>Mann-Whitney p-val</b>", style_th), Paragraph("<b>Cliff's Delta (&delta;)</b>", style_th)],
        [
            Paragraph("<b>At Review</b>", style_td_bold),
            Paragraph("1.0h (IQR: 0.8h)", style_td_center),
            Paragraph("3.0h (IQR: 2.6h)", style_td_center),
            Paragraph("&lt; 0.001 (Signifikan)", style_td_center),
            Paragraph("-0.840 (Efek Besar)", style_td_center)
        ],
        [
            Paragraph("<b>At Waiting for Change</b>", style_td_bold),
            Paragraph("3.0h (IQR: 2.5h)", style_td_center),
            Paragraph("24.0h (IQR: 22.9h)", style_td_center),
            Paragraph("&lt; 0.001 (Signifikan)", style_td_center),
            Paragraph("<b>-0.979 (Efek Masif)</b>", style_td_center)
        ],
        [
            Paragraph("<b>At Change</b>", style_td_bold),
            Paragraph("1.0h (IQR: 0.7h)", style_td_center),
            Paragraph("1.0h (IQR: 0.7h)", style_td_center),
            Paragraph("0.9740 (Tidak Sig.)", style_td_center),
            Paragraph("+0.001 (Tidak Ada Efek)", style_td_center)
        ]
    ]
    t_phase = Table(phase_table, colWidths=[120, 110, 110, 85, 70])
    t_phase.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_secondary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_phase)
    story.append(Spacer(1, 8))

    if os.path.exists("plots/fig2_pr_phases_comparison.png"):
        img2 = Image("plots/fig2_pr_phases_comparison.png", width=420, height=210)
        story.append(KeepTogether([img2, Spacer(1, 8)]))

    story.append(PageBreak())

    story.append(Paragraph("<b>5.3. Evaluasi Benchmark SQA: Baseline vs Vanilla LLM vs Oracle 23ai Vector RAG</b>", style_h2))
    story.append(Paragraph(
        "Hasil pengujian pada 100 kasus uji benchmark ground-truth membuktikan keunggulan mutlak integrasi basis data vektor:",
        style_body
    ))

    sqa_table = [
        [Paragraph("<b>Metrik Evaluasi SQA</b>", style_th), Paragraph("<b>Baseline Static</b>", style_th), Paragraph("<b>Vanilla LLM (Zero-Shot)</b>", style_th), Paragraph("<b>Oracle 23ai Vector RAG</b>", style_th), Paragraph("<b>Delta Improvement</b>", style_th)],
        [Paragraph("True Positives (TP)", style_td), Paragraph("18", style_td_center), Paragraph("69", style_td_center), Paragraph("<b>68</b>", style_td_center), Paragraph("-1", style_td_center)],
        [Paragraph("False Positives (FP - Halusinasi)", style_td), Paragraph("0", style_td_center), Paragraph("12", style_td_center), Paragraph("<b>0</b>", style_td_center), Paragraph("<b>-12 (Tereliminasi)</b>", style_td_center)],
        [Paragraph("False Negatives (FN - Lolos)", style_td), Paragraph("52", style_td_center), Paragraph("1", style_td_center), Paragraph("<b>2</b>", style_td_center), Paragraph("+1", style_td_center)],
        [Paragraph("True Negatives (TN - Bersih)", style_td), Paragraph("30", style_td_center), Paragraph("18", style_td_center), Paragraph("<b>30</b>", style_td_center), Paragraph("<b>+12 (Sempurna)</b>", style_td_center)],
        [Paragraph("Akurasi (Accuracy)", style_td), Paragraph("48.00%", style_td_center), Paragraph("87.00%", style_td_center), Paragraph("<b>98.00%</b>", style_td_center), Paragraph("+11.00%", style_td_center)],
        [Paragraph("Presisi (Precision)", style_td), Paragraph("100.00%", style_td_center), Paragraph("85.19%", style_td_center), Paragraph("<b>100.00%</b>", style_td_center), Paragraph("<b>+14.81%</b>", style_td_center)],
        [Paragraph("Recall (Sensitivitas)", style_td), Paragraph("25.71%", style_td_center), Paragraph("98.57%", style_td_center), Paragraph("<b>97.14%</b>", style_td_center), Paragraph("-1.43%", style_td_center)],
        [Paragraph("Spesifisitas (Specificity)", style_td), Paragraph("100.00%", style_td_center), Paragraph("60.00%", style_td_center), Paragraph("<b>100.00%</b>", style_td_center), Paragraph("<b>+40.00%</b>", style_td_center)],
        [Paragraph("<b>Tingkat Halusinasi (FPR)</b>", style_td_bold), Paragraph("0.00%", style_td_center), Paragraph("<b>40.00%</b>", style_td_center), Paragraph("<b>0.00%</b>", style_td_center), Paragraph("<b>-40.00% (Turun 100%)</b>", style_td_center)],
        [Paragraph("<b>F1-Score</b>", style_td_bold), Paragraph("0.4091", style_td_center), Paragraph("0.9139", style_td_center), Paragraph("<b>0.9855</b>", style_td_center), Paragraph("<b>+0.0716</b>", style_td_center)],
        [Paragraph("<b>Matthews Corr (MCC)</b>", style_td_bold), Paragraph("0.3067", style_td_center), Paragraph("0.6842", style_td_center), Paragraph("<b>0.9543</b>", style_td_center), Paragraph("<b>+0.2701</b>", style_td_center)]
    ]
    t_sqa = Table(sqa_table, colWidths=[145, 80, 105, 95, 70])
    t_sqa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_sqa)
    story.append(Spacer(1, 10))

    if os.path.exists("plots/fig3_sqa_defect_detection_metrics.png"):
        img3 = Image("plots/fig3_sqa_defect_detection_metrics.png", width=440, height=220)
        story.append(KeepTogether([img3, Spacer(1, 8)]))

    story.append(Paragraph(
        "<b>Pembahasan Ilmiah:</b> Vanilla LLM menghasilkan Recall tinggi (98,57%) tetapi menderita <b>False Positive Rate 40%</b> "
        "karena mencurigai kode standar yang sah sebagai bug. Sebaliknya, injeksi aturan semantik dari <b>Oracle 23ai Vector Search</b> "
        "memberikan <i>ground-truth context</i> yang mengeliminasi halusinasi hingga <b>0%</b> dengan Presisi sempurna 100% dan F1-Score 0,9855.",
        style_body
    ))
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 6: CONCLUSION [10%]
    # =========================================================================
    story.append(Paragraph("6. PEMAHAMAN TERHADAP KESIMPULAN [BOBOT: 10%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "<b>1. Jawaban Eksplisit Terhadap Research Questions:</b><br/>"
        "• <b>RQ1 (Efisiensi PR):</b> Terbukti secara empiris bahwa bantuan LLM memangkas median <i>time-to-merge</i> sebesar <b>60,8%</b> "
        "(&beta;1 = -0.8636, p &lt; 2e-16), dengan reduksi paling masif pada fase <i>Waiting for Change</i> sebesar <b>87,5%</b> (Cliff's &delta; = -0.979).<br/>"
        "• <b>RQ2 (Efektivitas SQA):</b> Integrasi Oracle 23ai Vector Search + RAG menghasilkan <b>F1-Score 0,9855</b>, jauh melampaui "
        "Baseline Static (0,4091) dan Vanilla LLM (0,9139).<br/>"
        "• <b>RQ3 (Mitigasi Halusinasi):</b> Tingkat halusinasi (FPR) berhasil ditekan dari <b>40,0% ke 0,0%</b>, membuktikan bahwa "
        "grounding berbasis basis data vektor mengeliminasi alarm palsu pada kode yang bersih.<br/><br/>"
        "<b>2. Implikasi Praktis bagi Industri:</b> Tim pengembang disarankan menggunakan asisten AI pada fase revisi PR. "
        "Namun, organisasi SQA dilarang keras mengandalkan Vanilla LLM mentah tanpa augmentasi konteks; penggunaan Vector Database "
        "(seperti Oracle Database 23ai) adalah syarat mutlak untuk memastikan hasil ulasan akurat dan patuh standar arsitektur.<br/><br/>"
        "<b>3. Threats to Validity & Future Work:</b> Dataset empiris berfokus pada proyek open-source; penelitian lanjutan dapat menguji "
        "pada basis kode tertutup (closed-source) serta mengintegrasikan eksekusi unit test otonom di sandbox.",
        style_body
    ))
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 7: OTHER ARTIFACTS, GITHUB, REPRODUCIBILITY [20%]
    # =========================================================================
    story.append(Paragraph("7. HAL-HAL LAIN (PROMPT, GITHUB, CODE, REPRODUCIBILITY) [BOBOT: 20%]", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceBefore=2, spaceAfter=8))
    
    story.append(Paragraph(
        "<b>Struktur Repositori GitHub:</b> Proyek dikelola pada branch <code>uas-llm-code-review-oracle-rag</code> di repositori "
        "<code>https://github.com/KingVolveyRAY/Kel2-SQA-King.git</code>.<br/>"
        "• <code>run_full_experiment.py</code>: Master runner yang menjalankan seluruh pemodelan data dan pengujian dalam 9 detik.<br/>"
        "• <code>src/oracle_vector_engine.py</code>: Implementasi mesin pencarian vektor Oracle 23ai (Cosine, Manhattan, Euclidean).<br/>"
        "• <code>src/prompts_bank.py</code>: Bank template prompt engineering (System Persona, Vanilla, Oracle Vector RAG, CoT).<br/>"
        "• <code>src/pr_empirical_analysis.py</code>: Skrip statistik regresi OLS, Mann-Whitney U, dan generator plot Fig 1, 2, 4.<br/>"
        "• <code>src/evaluate_sqa_benchmark.py</code>: Skrip evaluasi komparatif 100 kasus uji dan generator Fig 3.<br/>"
        "• <code>README.md</code>: Dokumentasi lengkap dengan diagram alur arsitektur Mermaid dan panduan reproduktifitas.",
        style_body
    ))

    # Prompt Engineering Snippet Box
    prompt_box = [
        [Paragraph("<b>CONTOH PROMPT: INJECTED ORACLE 23ai VECTOR RAG PROMPT</b>", style_th)],
        [Paragraph(
            "<b>System:</b> You are a Senior SQA & Security Code Auditor.<br/>"
            "<b>Oracle 23ai Context Injected:</b><br/>"
            "[Oracle 23ai Vector Match: SEC-01 - SQL Injection Prevention (Similarity: 0.89, Severity: CRITICAL)]<br/>"
            "Rule: Never format user input directly into SQL strings. Use parameterized queries or ORM bind variables.<br/>"
            "Compliant Fix: <code>cursor.execute('SELECT * FROM users WHERE email = %s', (email,))</code><br/><br/>"
            "<b>Instruction:</b> Review the PR diff against the retrieved Oracle Vector guideline. If compliant, mark 'has_defect': false without hallucinating issues.",
            style_code
        )]
    ]
    t_prompt = Table(prompt_box, colWidths=[495])
    t_prompt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2D3748")),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#EDF2F7")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#A0AEC0")),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_prompt)
    story.append(Spacer(1, 15))

    story.append(Paragraph(
        "<b>Panduan Reproduktifitas:</b> Untuk menjalankan ulang eksperimen dari awal, jalankan perintah:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<code>cd \"D:\\UAS bayangan SQA\" &amp;&amp; python run_full_experiment.py</code><br/>"
        "Semua berkas laporan ini telah dikompilasi ke format PDF resmi untuk pengumpulan di Microsoft Teams dan repositori GitHub.",
        style_callout
    ))

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated official publication PDF report: {output_filename}")

if __name__ == "__main__":
    build_pdf_report()
