import os
import subprocess
import zipfile
import re
import tempfile

BASE_DIR = r"C:\Users\ocast\Desktop\proyectos\Escritorio\lonew"
STYLE_PATH = os.path.join(BASE_DIR, "epub_style.css")

AUTHOR = "Clark Castle"
SAGA_TITLE = "LOS ALTHEN"

LIBROS = [
    {
        "book": "LIBRO I",
        "name": "LA SEMILLA",
        "start": 1,
        "end": 19,
        "safe": "La_Semilla"
    },
    {
        "book": "LIBRO II",
        "name": "LA DIVISIÓN",
        "start": 20,
        "end": 38,
        "safe": "La_Division"
    },
    {
        "book": "LIBRO III",
        "name": "LA HERENCIA",
        "start": 39,
        "end": 57,
        "safe": "La_Herencia"
    }
]


def chapter_path(n):
    return os.path.join(BASE_DIR, "CAPITULO_%d.md" % n)


def chapter_md(n):
    with open(chapter_path(n), "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
    body = "\n".join(lines[3:])
    chapter_title = lines[2].lstrip("#").strip()
    return "# %s\n\n%s" % (chapter_title, body)


def clean_epub_toc(epub_path):
    with zipfile.ZipFile(epub_path, 'r') as z:
        files_data = {name: z.read(name) for name in z.namelist()}

    for name in sorted(files_data.keys()):
        if name.startswith('EPUB/text/ch'):
            html_str = files_data[name].decode('utf-8')
            m_head = re.search(r'<(h[1-6])[^>]*>(.*?)</\1>', html_str, re.DOTALL)
            if m_head:
                head_text = re.sub(r'<[^>]+>', '', m_head.group(2)).strip()
                html_str = re.sub(r'<title>.*?</title>', '<title>%s</title>' % head_text, html_str, flags=re.DOTALL)
                files_data[name] = html_str.encode('utf-8')

    if 'EPUB/nav.xhtml' in files_data:
        nav_str = files_data['EPUB/nav.xhtml'].decode('utf-8')
        nav_str = re.sub(r'<nav epub:type="landmarks".*?</nav>', '', nav_str, flags=re.DOTALL)
        nav_str = re.sub(r'href="(text/ch\d+\.xhtml)#[^"]*"', r'href="\1"', nav_str)
        files_data['EPUB/nav.xhtml'] = nav_str.encode('utf-8')

    if 'EPUB/toc.ncx' in files_data:
        ncx_str = files_data['EPUB/toc.ncx'].decode('utf-8')
        ncx_str = re.sub(r'src="(text/ch\d+\.xhtml)#[^"]*"', r'src="\1"', ncx_str)
        files_data['EPUB/toc.ncx'] = ncx_str.encode('utf-8')

    with zipfile.ZipFile(epub_path, 'w') as z:
        for name, data in files_data.items():
            z.writestr(name, data)


def build_with_pandoc(src_files, epub_path, title):
    cmd = [
        "pandoc",
        *src_files,
        "-o", epub_path,
        f"--css={STYLE_PATH}",
        "--epub-title-page=false",
        f"--metadata=title:{title}",
        f"--metadata=author:{AUTHOR}",
        "--metadata=language:es",
        "--metadata=toc-title:Índice",
        "--split-level=1",
        "--toc",
        "--toc-depth=2"
    ]
    return subprocess.run(cmd, capture_output=True, text=True)


def make_sources(libros):
    tmp = tempfile.mkdtemp(prefix="los_althen_epub_")
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
    return tmp, src_files


print("=== GENERANDO EPUBS CON TÍTULOS Y TOC LIMPIOS ===")

for b in LIBROS:
    epub_path = os.path.join(BASE_DIR, "LOS_ALTHEN_%s.epub" % b["safe"])
    if os.path.exists(epub_path):
        try:
            os.remove(epub_path)
        except Exception:
            pass

    tmp, src_files = make_sources([b])
    full_title = "%s — %s: %s" % (SAGA_TITLE, b["book"], b["name"])
    res = build_with_pandoc(src_files, epub_path, full_title)
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    if res.returncode == 0:
        print("[OK] EPUB Compilado: %s" % os.path.basename(epub_path))
        clean_epub_toc(epub_path)
    else:
        print("[ERROR] EPUB Falló para %s: %s" % (os.path.basename(epub_path), res.stderr))

omnibus_path = os.path.join(BASE_DIR, "LOS_ALTHEN_Edicion_Completa.epub")
if os.path.exists(omnibus_path):
    try:
        os.remove(omnibus_path)
    except Exception:
        pass

tmp, src_files = make_sources(LIBROS)
full_omni_title = "%s — Edición Completa (Trilogía)" % SAGA_TITLE
res_omni = build_with_pandoc(src_files, omnibus_path, full_omni_title)
import shutil
shutil.rmtree(tmp, ignore_errors=True)
if res_omni.returncode == 0:
    print("[OK] EPUB Ómnibus Compilado: %s" % os.path.basename(omnibus_path))
    clean_epub_toc(omnibus_path)
else:
    print("[ERROR] Ómnibus Falló: %s" % res_omni.stderr)

print("=== FINALIZADO CON ÉXITO ===")