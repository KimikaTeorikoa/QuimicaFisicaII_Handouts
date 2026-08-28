#!/usr/bin/env python3
"""Ejecuta los cuadernos de figuras y regenera los PDF de ../figs/.

    python run_notebooks.py                    # todos los nb*.ipynb
    python run_notebooks.py nb03_sistemas_modelo.ipynb nb05_hidrogeno.ipynb

Los cuadernos se ejecutan en memoria: el .ipynb del disco **no se modifica**,
de modo que en el repositorio nunca se guardan salidas. Lo que imprimen las
celdas (los nombres de fichero y las comprobaciones numéricas) se reenvía a
la terminal, y un error en cualquier celda aborta con código de salida 1.
"""
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

AQUI = Path(__file__).resolve().parent


def ejecutar(ruta):
    nb = nbformat.read(str(ruta), as_version=4)
    cliente = NotebookClient(nb, timeout=600, kernel_name="python3",
                             resources={"metadata": {"path": str(AQUI)}})
    cliente.execute()
    for celda in nb.cells:
        for salida in celda.get("outputs", []):
            if salida.get("output_type") == "stream":
                sys.stdout.write(salida.get("text", ""))


def main(argv):
    cuadernos = ([AQUI / a for a in argv] if argv
                 else sorted(AQUI.glob("nb*.ipynb")))
    if not cuadernos:
        sys.exit("no hay cuadernos que ejecutar")
    fallos = []
    for ruta in cuadernos:
        print("=== %s" % ruta.name, flush=True)
        try:
            ejecutar(ruta)
        except CellExecutionError as err:
            fallos.append(ruta.name)
            print("    FALLA: %s" % str(err).strip().splitlines()[-1],
                  file=sys.stderr)
    if fallos:
        sys.exit("cuadernos con errores: " + ", ".join(fallos))


if __name__ == "__main__":
    main(sys.argv[1:])
