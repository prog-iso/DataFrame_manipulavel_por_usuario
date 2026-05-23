from pathlib import Path

arq = Path(__file__).parent / "arquivo_de_texto.md"

with arq.open(encoding="utf-8") as leitura:
    compras = [line for line in leitura.read().splitlines() if line.startswith("* ")]

new_arq = Path(__file__).parent /( "apenas_compras.md")
new_arq.write_text("\n".join(compras),"utf-8")