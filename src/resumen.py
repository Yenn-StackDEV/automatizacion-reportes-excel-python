"""
Módulo para calcular el resumen ejecutivo a partir de los datos consolidados.
"""

import pandas as pd


def generar_resumen(df: pd.DataFrame) -> dict:
    """
    Calcula métricas clave a partir del DataFrame consolidado:
    total de ventas, promedio por archivo y top categorías.
    """
    resumen = {}

    if "total_linea" in df.columns:
        resumen["total_ventas"] = round(df["total_linea"].sum(), 2)
        resumen["promedio_por_archivo"] = round(
            df.groupby("archivo_origen")["total_linea"].sum().mean(), 2
        )
    else:
        resumen["total_ventas"] = 0
        resumen["promedio_por_archivo"] = 0

    if "categoria" in df.columns and "total_linea" in df.columns:
        top = (
            df.groupby("categoria")["total_linea"]
            .sum()
            .sort_values(ascending=False)
            .head(3)
        )
        resumen["top_categorias"] = top.to_dict()
    else:
        resumen["top_categorias"] = {}

    return resumen


def resumen_a_texto(resumen: dict) -> str:
    """
    Convierte el diccionario de resumen en un texto legible para el correo.
    """
    lineas = [
        "Resumen ejecutivo de ventas",
        "============================",
        f"Total de ventas: ${resumen['total_ventas']:,.2f}",
        f"Promedio por archivo: ${resumen['promedio_por_archivo']:,.2f}",
        "",
        "Top categorías:",
    ]
    for categoria, total in resumen["top_categorias"].items():
        lineas.append(f"  - {categoria}: ${total:,.2f}")

    return "\n".join(lineas)
