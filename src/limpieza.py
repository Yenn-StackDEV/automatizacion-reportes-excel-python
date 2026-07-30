"""
Módulo de limpieza y consolidación de datos con pandas.
"""

import pandas as pd


def limpiar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia un DataFrame individual: estandariza nombres de columnas,
    elimina filas totalmente vacías y convierte tipos de datos básicos.
    """
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    df = df.dropna(how="all")

    if "cantidad" in df.columns:
        df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce").fillna(0)

    if "precio_unitario" in df.columns:
        df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce").fillna(0)

    return df


def consolidar(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Limpia y concatena una lista de DataFrames en uno solo, calculando
    el total por línea cuando existen las columnas necesarias.
    """
    limpios = [limpiar_dataframe(df) for df in dataframes]
    consolidado = pd.concat(limpios, ignore_index=True)

    if "cantidad" in consolidado.columns and "precio_unitario" in consolidado.columns:
        consolidado["total_linea"] = consolidado["cantidad"] * consolidado["precio_unitario"]

    return consolidado
