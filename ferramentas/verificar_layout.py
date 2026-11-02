#!/usr/bin/env python3
"""Verifica o layout dos PDFs dos módulos DevMobile.

Uso:  python3 ferramentas/verificar_layout.py modulos/*.pdf

Para cada PDF:
  * lê o .log correspondente e lista erros e "Overfull \\hbox" acima de 1 pt;
  * renderiza as páginas (pdftoppm) e acusa slides cujo conteúdo encosta
    no rodapé, o que indica texto transbordando do quadro.
Requer: poppler-utils (pdftoppm) e Pillow.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

RODAPE = (0x0E, 0x3B, 0x43)  # petroleoesc (parte esquerda do rodapé)
RODAPE_DIR = (0x0D, 0x30, 0x52)  # petroleo (parte direita do rodapé)


def perto(c, ref, tol=18):
    return all(abs(a - b) <= tol for a, b in zip(c[:3], ref))


def checar_log(pdf: Path):
    log = pdf.with_suffix(".log")
    problemas = []
    if not log.exists():
        return ["log não encontrado"]
    texto = log.read_text(errors="ignore")
    for m in re.finditer(r"^! (.*)$", texto, re.M):
        problemas.append(f"ERRO: {m.group(1)}")
    for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\).*?lines? (\d+)", texto):
        if float(m.group(1)) > 1.0:
            problemas.append(f"Overfull hbox {m.group(1)}pt (linha {m.group(2)})")
    for m in re.finditer(r"Overfull \\vbox \(([\d.]+)pt too high\) detected at line (\d+)", texto):
        if float(m.group(1)) > 1.0:
            problemas.append(f"Overfull vbox {m.group(1)}pt (slide terminando na linha {m.group(2)})")
    return problemas


def checar_paginas(pdf: Path, dpi=40):
    suspeitas = []
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(pdf), f"{tmp}/p"], check=True)
        for png in sorted(Path(tmp).glob("p-*.png")):
            n = int(png.stem.split("-")[1])
            im = Image.open(png).convert("RGB")
            w, h = im.size
            px = im.load()
            # slides de capa/seção têm fundo escuro: ignora
            amostra = [px[x, y] for x in range(0, w, 7) for y in range(0, h, 7)]
            if sum(1 for c in amostra if min(c) > 235) < 0.35 * len(amostra):
                continue
            # topo do rodapé = primeira linha (de baixo p/ cima) que deixa de ser cor do rodapé
            # a borda direita do rodapé (margem) não tem texto
            y = h - 2
            while y > h * 0.8 and (perto(px[w - 2, y], RODAPE_DIR) or perto(px[w - 2, y], RODAPE)):
                y -= 1
            topo = y - 3  # pula a barra de progresso
            faixa = [px[x, yy] for yy in range(topo - 3, topo + 1) for x in range(int(w * 0.03), int(w * 0.97))]
            sujos = sum(1 for c in faixa if sum(c) < 3 * 225)
            if sujos > 3:
                suspeitas.append(n)
    return suspeitas


def main(pdfs):
    total = 0
    for nome in pdfs:
        pdf = Path(nome)
        probs = checar_log(pdf)
        if not pdf.exists():
            print(f"[FALHOU] {pdf.name}: PDF não gerado")
            for p in probs:
                print(f"    - {p}")
            total += 1
            continue
        pags = checar_paginas(pdf)
        if pags:
            probs.append(f"conteúdo encostando no rodapé nas páginas {pags}")
        status = "OK" if not probs else f"{len(probs)} aviso(s)"
        print(f"[{status}] {pdf.name}")
        for p in probs:
            print(f"    - {p}")
        total += len(probs)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv[1:] or sorted(str(p) for p in Path("modulos").glob("*.pdf")))
