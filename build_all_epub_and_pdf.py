import os
import subprocess
import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable, Image
)
from reportlab.lib.utils import ImageReader

BASE_DIR = r"C:\Users\ocast\Desktop\proyectos\Escritorio\Althen"
AUTHOR = "Clark Castle"
SAGA_TITLE = "LOS ALTHEN"
CSS_PATH = os.path.join(BASE_DIR, "epub_style.css")

LIBROS = [
    {"book": "LIBRO I", "name": "LA SEMILLA", "start": 1, "end": 19, "safe": "La_Semilla", "cover": "portada_la_semilla.jpg"},
    {"book": "LIBRO II", "name": "LA DIVISIÓN", "start": 20, "end": 38, "safe": "La_Division", "cover": "portada_la_division.jpg"},
    {"book": "LIBRO III", "name": "LA HERENCIA", "start": 39, "end": 53, "safe": "La_Herencia", "cover": "portada_la_herencia.jpg"}
]


def chapter_path(n):
    return os.path.join(BASE_DIR, "CAPITULO_%d.md" % n)


def libro_files(libro):
    return [chapter_path(n) for n in range(libro["start"], libro["end"] + 1)]


def libro_root(libro):
    return os.path.join(BASE_DIR, "LOS_ALTHEN_%s" % libro["safe"])


def chapter_md(n):
    with open(chapter_path(n), "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
    body = "\n".join(lines[3:])
    chapter_title = lines[2].lstrip("#").strip()
    return "# %s\n\n%s" % (chapter_title, body)


def build_epub(libro, libros, epub_path):
    with tempfile.TemporaryDirectory() as tmp:
        src_files = []
        portada = ["# " + SAGA_TITLE]
        for lb in libros:
            portada.append("\n## %s: %s" % (lb["book"], lb["name"]))
        portada_path = os.path.join(tmp, "00_portada.md")
        with open(portada_path, "w", encoding="utf-8") as f:
            f.write("\n".join(portada))
        src_files.append(portada_path)

        i = 1
        for lb in libros:
            for n in range(lb["start"], lb["end"] + 1):
                cap_path = os.path.join(tmp, "%02d_cap%02d.md" % (i, n))
                with open(cap_path, "w", encoding="utf-8") as f:
                    f.write(chapter_md(n))
                src_files.append(cap_path)
                i += 1

        cmd = [
            "pandoc",
            *src_files,
            "-o", epub_path,
            "--split-level=1",
            f"--metadata=title:{SAGA_TITLE} — {libro['book']}: {libro['name']}",
            f"--metadata=author:{AUTHOR}",
            "--metadata=language:es",
            "--metadata=toc-title:Índice",
            "--toc",
            "--toc-depth=2"
        ]
        if os.path.exists(CSS_PATH):
            cmd.append(f"--css={CSS_PATH}")
        cover = libro.get("cover")
        if cover:
            cover_path = os.path.join(BASE_DIR, cover)
            if os.path.exists(cover_path):
                cmd.append(f"--epub-cover-image={cover_path}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("[OK] EPUB: %s" % epub_path)
        else:
            print("[ERROR] EPUB %s: %s" % (epub_path, result.stderr))


def build_epubs():
    print("\n--- GENERANDO EPUBS ---")
    for libro in LIBROS:
        build_epub(libro, [libro], libro_root(libro) + ".epub")
    build_epub(LIBROS[0], LIBROS, os.path.join(BASE_DIR, "LOS_ALTHEN_Edicion_Completa.epub"))


class NumberedCanvas(canvas.Canvas):
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

    def draw_header_footer(self, page_count):
        if self._pageNumber <= 2:
            return
        self.saveState()
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#555555"))
        self.drawString(54, 800, SAGA_TITLE)
        self.drawRightString(558, 800, AUTHOR)
        self.setStrokeColor(colors.HexColor("#DDDDDD"))
        self.setLineWidth(0.5)
        self.line(54, 792, 558, 792)
        self.line(54, 48, 558, 48)
        self.drawCentredString(306, 34, "— %d —" % self._pageNumber)
        self.restoreState()


def build_single_pdf(tomo):
    pdf_path = tomo["pdf_path"]
    files = tomo["files"]

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=64
    )

    styles = getSampleStyleSheet()

    style_cover_saga = ParagraphStyle(
        'CoverSaga', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=20, leading=24,
        textColor=colors.HexColor("#D4AF37"), alignment=1, spaceAfter=15
    )
    style_cover_title = ParagraphStyle(
        'CoverTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=30, leading=36,
        textColor=colors.HexColor("#1A1A24"), alignment=1, spaceAfter=20
    )
    style_cover_author = ParagraphStyle(
        'CoverAuthor', parent=styles['Normal'], fontName='Helvetica', fontSize=15, leading=19,
        textColor=colors.HexColor("#4A4A5A"), alignment=1, spaceAfter=30
    )
    style_chapter_title = ParagraphStyle(
        'ChapterTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, leading=24,
        textColor=colors.HexColor("#111827"), spaceBefore=20, spaceAfter=15, keepWithNext=True
    )
    style_section_title = ParagraphStyle(
        'SectionTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, leading=17,
        textColor=colors.HexColor("#374151"), spaceBefore=15, spaceAfter=10, keepWithNext=True
    )
    style_body = ParagraphStyle(
        'BookBody', parent=styles['Normal'], fontName='Times-Roman', fontSize=11, leading=16,
        textColor=colors.HexColor("#1F2937"), spaceAfter=9, firstLineIndent=18
    )
    style_dialogue = ParagraphStyle(
        'BookDialogue', parent=style_body, firstLineIndent=12, spaceAfter=5
    )
    style_code = ParagraphStyle(
        'BookCode', parent=styles['Normal'], fontName='Courier', fontSize=9, leading=12,
        textColor=colors.HexColor("#059669"), backColor=colors.HexColor("#F3F4F6"),
        borderColor=colors.HexColor("#E5E7EB"), borderWidth=1, borderPadding=6, spaceBefore=8, spaceAfter=10
    )

    story = []
    cover_img = tomo.get("cover")
    if cover_img:
        cover_path = cover_img if os.path.isabs(cover_img) else os.path.join(BASE_DIR, cover_img)
        if os.path.exists(cover_path):
            try:
                ir = ImageReader(cover_path)
                iw, ih = ir.getSize()
                max_w = 360
                ratio = max_w / iw
                story.append(Image(cover_path, width=max_w, height=ih * ratio))
                story.append(Spacer(1, 30))
            except Exception:
                pass
    story.append(Spacer(1, 60))
    story.append(Paragraph(tomo["saga"], style_cover_saga))
    story.append(Paragraph(tomo["short_title"], style_cover_title))
    story.append(HRFlowable(width="60%", thickness=2, color=colors.HexColor("#D4AF37"), spaceBefore=10, spaceAfter=20))
    story.append(Paragraph("Por <b>%s</b>" % AUTHOR, style_cover_author))
    story.append(Spacer(1, 150))
    if tomo.get("subtitle"):
        story.append(Paragraph("<i>%s</i>" % tomo["subtitle"], style_cover_author))
    story.append(PageBreak())

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.split('\n')
        code_block = False
        code_text = []

        for line in lines:
            line_str = line.strip()
            if line_str.startswith("```"):
                if code_block:
                    story.append(Paragraph("<br/>".join(code_text), style_code))
                    code_text = []
                    code_block = False
                else:
                    code_block = True
                continue

            if code_block:
                code_text.append(line_str.replace("<", "&lt;").replace(">", "&gt;"))
                continue

            if not line_str:
                continue

            if line_str.startswith("# "):
                continue
            elif line_str.startswith("## "):
                txt = line_str[3:].replace("<", "&lt;").replace(">", "&gt;")
                story.append(Paragraph("<b>%s</b>" % txt, style_section_title))
            elif line_str.startswith("### ") or line_str.startswith("#### "):
                clean_text = line_str.lstrip("#").strip().replace("<", "&lt;").replace(">", "&gt;")
                if "CAPÍTULO" in line_str.upper():
                    story.append(PageBreak())
                    story.append(Paragraph(clean_text, style_chapter_title))
                    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1A1A24"), spaceAfter=15))
                else:
                    story.append(Paragraph("<i>%s</i>" % clean_text, style_section_title))
            elif line_str.startswith("***") or line_str.startswith("---"):
                story.append(Spacer(1, 10))
                story.append(Paragraph("* * *", style_cover_author))
                story.append(Spacer(1, 10))
            else:
                txt = line_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                txt = txt.replace("***", "@@@").replace("**", "@@").replace("@@@", "@@")
                import re
                txt = re.sub(r'@@(.*?)@@', r'<b>\1</b>', txt)
                txt = re.sub(r'\*(.*?)\*', r'<i>\1</i>', txt)

                if txt.startswith("—") or txt.startswith("-"):
                    story.append(Paragraph(txt, style_dialogue))
                else:
                    story.append(Paragraph(txt, style_body))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("[OK] PDF: %s" % pdf_path)


def build_pdfs():
    print("\n--- GENERANDO PDFs ---")
    for libro in LIBROS:
        tomo = {
            "pdf_path": libro_root(libro) + ".pdf",
            "files": libro_files(libro),
            "saga": SAGA_TITLE,
            "short_title": "%s: %s" % (libro["book"], libro["name"]),
            "subtitle": "",
            "cover": libro.get("cover")
        }
        build_single_pdf(tomo)

    all_files = []
    for libro in LIBROS:
        all_files.extend(libro_files(libro))
    tomo = {
        "pdf_path": os.path.join(BASE_DIR, "LOS_ALTHEN_Edicion_Completa.pdf"),
        "files": all_files,
        "saga": SAGA_TITLE,
        "short_title": "EDICIÓN COMPLETA",
        "subtitle": "Los Tres Libros de la Heredad",
        "cover": LIBROS[0]["cover"]
    }
    build_single_pdf(tomo)


if __name__ == "__main__":
    build_epubs()
    build_pdfs()
    print("\n[LISTO] EPUB Y PDF GENERADOS PARA %s" % SAGA_TITLE)