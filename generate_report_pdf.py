"""Builds the Lab Task 02 report PDF.

Put the phone screenshots in the screenshots/ folder with these names, then run:
    python generate_report_pdf.py

    01_course_list.png        - the scrolling course list
    02_no_layout_manager.png  - the app run without setLayoutManager()
    03_details_course_1.png   - details screen of a first course
    04_details_course_2.png   - details screen of a second course
    05_details_course_3.png   - details screen of a third course
    06_email_app.png          - email app opened by "Email Instructor"

A missing screenshot shows as a grey placeholder box.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(HERE, "LabTask2_RecyclerView_70147860_Report.pdf")
IMG_DIR = os.path.join(HERE, "screenshots")
REPO_URL = "https://github.com/Leetfraud/LabTask2_RecyclerView_70147860"
PROFILE_URL = "https://github.com/Leetfraud"


def create_report():
    doc = SimpleDocTemplate(PDF_PATH, pagesize=letter, rightMargin=36, leftMargin=36,
                            topMargin=28, bottomMargin=26)
    styles = getSampleStyleSheet()

    title = ParagraphStyle('T', parent=styles['Heading1'], fontSize=15, leading=18,
                           textColor=colors.HexColor('#003366'), alignment=1, fontName='Helvetica-Bold')
    sub = ParagraphStyle('S', parent=styles['Normal'], fontSize=10.5, leading=14,
                         textColor=colors.HexColor('#333333'), alignment=1)
    h1 = ParagraphStyle('H1', parent=styles['Heading2'], fontSize=12, leading=15,
                        textColor=colors.HexColor('#003366'), spaceBefore=7, spaceAfter=4,
                        fontName='Helvetica-Bold')
    h2 = ParagraphStyle('H2', parent=styles['Heading3'], fontSize=10.5, leading=13,
                        textColor=colors.HexColor('#1B5E20'), spaceBefore=7, spaceAfter=3,
                        fontName='Helvetica-Bold')
    body = ParagraphStyle('B', parent=styles['Normal'], fontSize=8.8, leading=12,
                          textColor=colors.HexColor('#222222'))
    bullet = ParagraphStyle('BL', parent=body, fontSize=8.5, leading=11, leftIndent=12)
    caption = ParagraphStyle('C', parent=body, fontSize=8, leading=10.5, alignment=1,
                             textColor=colors.HexColor('#444444'), fontName='Helvetica-Bold')
    callout = ParagraphStyle('CO', parent=body, textColor=colors.HexColor('#003366'))

    def box(text, bg, border):
        t = Table([[Paragraph(text, callout)]], colWidths=[7.1 * inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(bg)),
            ('BOX', (0, 0), (-1, -1), 1.2, colors.HexColor(border)),
            ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        return t

    def shot(name, w=1.53 * inch, h=3.4 * inch):
        path = os.path.join(IMG_DIR, name)
        if os.path.exists(path):
            return Image(path, width=w, height=h)
        ph = Table([[Paragraph("Screenshot missing:<br/>" + name, caption)]], colWidths=[w], rowHeights=[h])
        ph.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#E5E7EB')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        return ph

    def shot_row(items, col_w):
        t = Table([[shot(f) for f, _ in items], [Paragraph(c, caption) for _, c in items]],
                  colWidths=[col_w] * len(items))
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('TOPPADDING', (0, 0), (-1, -1), 2),
        ]))
        return t

    s = []

    # Header
    s.append(Paragraph("THE UNIVERSITY OF LAHORE", title))
    s.append(Paragraph("Faculty of Information Technology | Department of Software Engineering", sub))
    s.append(Paragraph("<b>Mobile Application Development (CS02310) — Lab Task No. 02 Report</b>", sub))
    s.append(Paragraph("<b>UOL Course Catalogue — RecyclerView List App</b>",
                       ParagraphStyle('SS', parent=sub, textColor=colors.HexColor('#1B5E20'), fontSize=11.5)))
    s.append(Spacer(1, 8))
    s.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#003366'), spaceAfter=10))

    link = "<font color='#003366'><u>%s</u></font>"
    meta = Table([
        [Paragraph("<b>Student Name:</b>", body), Paragraph("<b>Faseeh Ur Rehman</b>", body),
         Paragraph("<b>Course Code:</b>", body), Paragraph("CS02310 (Mobile App Dev)", body)],
        [Paragraph("<b>SAP ID:</b>", body), Paragraph("<b>70147860</b>", body),
         Paragraph("<b>Programme & Sem:</b>", body), Paragraph("BS Software Engineering (7th Sem)", body)],
        [Paragraph("<b>Section:</b>", body), Paragraph("<b>Section S</b>", body),
         Paragraph("<b>Mapped CLO:</b>", body), Paragraph("CLO-4 (Bloom's: C6 / Modern Tool Usage)", body)],
        [Paragraph("<b>GitHub Repo:</b>", body), Paragraph(link % REPO_URL, body),
         Paragraph("<b>Term:</b>", body), Paragraph("Fall 2026", body)],
        [Paragraph("<b>GitHub Profile:</b>", body), Paragraph(link % PROFILE_URL, body),
         Paragraph("", body), Paragraph("", body)],
    ], colWidths=[1.3 * inch, 2.3 * inch, 1.4 * inch, 2.1 * inch])
    meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    s.append(meta)
    s.append(Spacer(1, 6))

    # Required write-ups
    s.append(Paragraph("<b>Scenario 1, Step 5 — Running the List Without setLayoutManager()</b>", h1))
    s.append(box(
        "<b>What I saw:</b> with the <code>setLayoutManager()</code> line removed, the app opened but the list area "
        "was completely empty — no course cards were shown at all.<br/>"
        "<b>Why:</b> a RecyclerView does not position items by itself. The LayoutManager decides how and where each "
        "card is measured and placed, so without one the RecyclerView never asks the adapter for any cards and "
        "draws nothing. After restoring <code>rvCourses.setLayoutManager(new LinearLayoutManager(this))</code>, "
        "the vertical list came back.", '#FFF8E1', '#F59E0B'))
    s.append(Spacer(1, 6))

    s.append(Paragraph("<b>Scenario 2, Step 5 — Why the Position Is Used to Fetch the Data</b>", h1))
    s.append(box(
        "The position passed to <code>onItemClick()</code> is the index of the tapped card in the adapter, and it is "
        "the same index as that course in the <code>courses</code> ArrayList, so "
        "<code>courses.get(position)</code> returns exactly the tapped course.<br/>"
        "Card views are recycled and reused for different courses while scrolling, so the view itself cannot "
        "identify the course — only the position reliably does, which is why only that course's data is sent.",
        '#EFF6FF', '#3B82F6'))

    # Step descriptions
    s.append(Paragraph("<b>Step-by-Step Implementation Summary</b>", h1))
    s.append(Paragraph("<b>Scenario 1 — The Course List</b>", h2))
    for t in [
        "<b>Step 1 (Model class):</b> <code>Course</code> has private fields <code>code</code>, <code>title</code>, "
        "<code>instructor</code>, <code>email</code>, <code>description</code> (String) and <code>creditHours</code> "
        "(int), one constructor that sets every field, and a public getter for each.",
        "<b>Step 2 (Card layout):</b> <code>item_course.xml</code> has a <code>CardView</code> as its root with "
        "<code>app:cardCornerRadius=\"12dp\"</code> and <code>app:cardElevation=\"4dp\"</code>, and three TextViews "
        "for the course code, title and credit hours.",
        "<b>Step 3 (Adapter):</b> <code>CourseAdapter</code> extends <code>RecyclerView.Adapter</code>. Its static "
        "inner <code>ViewHolder</code> finds the three TextViews once in its constructor. "
        "<code>onCreateViewHolder()</code> inflates the card, <code>onBindViewHolder()</code> writes one course's "
        "data into it, and <code>getItemCount()</code> returns the list size.",
        "<b>Step 4 (Data and LayoutManager):</b> <code>MainActivity</code> builds an ArrayList of ten BS-SE courses, "
        "sets a <code>LinearLayoutManager</code> on <code>rvCourses</code> and attaches the adapter with "
        "<code>setAdapter()</code>.",
        "<b>Step 5 (List test):</b> scrolled through all ten courses, then ran the app once without "
        "<code>setLayoutManager()</code> (observation above, Figure 2) and restored the call.",
    ]:
        s.append(Paragraph("• " + t, bullet))

    s.append(Paragraph("<b>Scenario 2 — The Course Details Screen</b>", h2))
    for t in [
        "<b>Step 1 (Click interface):</b> <code>CourseAdapter</code> declares the interface "
        "<code>OnItemClickListener</code> with <code>onItemClick(int position)</code>. The ViewHolder constructor "
        "attaches a click listener to <code>itemView</code> that reports <code>getBindingAdapterPosition()</code>, "
        "and <code>MainActivity</code> implements the interface.",
        "<b>Step 2 (Explicit Intent):</b> <code>onItemClick()</code> reads the tapped course with "
        "<code>courses.get(position)</code> and opens <code>CourseDetailActivity</code> with an explicit Intent, "
        "sending only that course's data through <code>putExtra()</code> with <code>public static final</code> key "
        "constants (<code>EXTRA_CODE</code>, <code>EXTRA_TITLE</code>, etc.).",
        "<b>Step 3 (Details screen):</b> <code>CourseDetailActivity</code> is declared in "
        "<code>AndroidManifest.xml</code>. It reads the values with <code>getStringExtra()</code> and "
        "<code>getIntExtra()</code>, shows the title, instructor, credit hours and description, and calls "
        "<code>setTitle(code)</code> so the screen title is the course code.",
        "<b>Step 4 (Email Instructor):</b> the button builds an <code>ACTION_SENDTO</code> Intent with "
        "<code>\"mailto:\" + email</code>, so the email app opens addressed to that course's instructor only. "
        "<code>startActivity()</code> is inside try–catch and a Toast is shown on "
        "<code>ActivityNotFoundException</code>.",
        "<b>Step 5 (Item click test):</b> tapped three different courses; each opened a details screen showing only "
        "the tapped course: SE-3102, SE-3205 and SE-4101 (Figures 3–5). Tapping \"Email Instructor\" on SE-3301 opened Gmail addressed only to nida.farooq@se.uol.edu.pk (Figure 6).",
    ]:
        s.append(Paragraph("• " + t, bullet))

    s.append(PageBreak())

    # Screenshots
    s.append(Paragraph("<b>App Screenshots</b>", h1))
    s.append(Spacer(1, 6))
    s.append(shot_row([
        ("01_course_list.png", "<b>Figure 1:</b> Course List"),
        ("02_no_layout_manager.png", "<b>Figure 2:</b> Without setLayoutManager()"),
        ("06_email_app.png", "<b>Figure 6:</b> Email app (SE-3301 instructor)"),
    ], 2.36 * inch))
    s.append(Spacer(1, 10))
    s.append(shot_row([
        ("03_details_course_1.png", "<b>Figure 3:</b> Details — SE-3102"),
        ("04_details_course_2.png", "<b>Figure 4:</b> Details — SE-3205"),
        ("05_details_course_3.png", "<b>Figure 5:</b> Details — SE-4101"),
    ], 2.36 * inch))

    doc.build(s)
    print("Report generated: " + PDF_PATH)


if __name__ == "__main__":
    create_report()
