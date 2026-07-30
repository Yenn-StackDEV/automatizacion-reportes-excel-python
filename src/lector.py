"""
Módulo encargado de leer los archivos Excel/CSV desde una carpeta de entrada.
"""

from pathlib import Path
import pandas as pd


def leer_archivos(carpeta: str) -> list[pd.DataFrame]:
    """
    Lee todos los archivos .csv y .xlsx de una carpeta y los retorna como
    una lista de DataFrames de pandas.

    Args:
        carpeta: Ruta de la carpeta que contiene los archivos de entrada.

    Returns:
        Lista de DataFrames, uno por cada archivo leído.
    """
    ruta = Path(carpeta)
    dataframes = []

    if not ruta.exists():
        raise FileNotFoundError(f"La carpeta '{carpeta}' no existe.")

    archivos = sorted(list(ruta.glob("*.csv")) + list(ruta.glob("*.xlsx")))

    if not archivos:
        raise ValueError(f"No se encontraron archivos .csv o .xlsx en '{carpeta}'.")

    for archivo in archivos:
        if archivo.suffix == ".csv":
            df = pd.read_csv(archivo)
        else:
            df = pd.read_excel(archivo)
        df["archivo_origen"] = archivo.name
        dataframes.append(df)

    return dataframes
