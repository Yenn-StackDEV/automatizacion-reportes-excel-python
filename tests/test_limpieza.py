"""
Pruebas unitarias para el módulo de limpieza y consolidación de datos.
"""

import pandas as pd

from src.limpieza import limpiar_dataframe, consolidar


def test_limpiar_dataframe_estandariza_columnas():
    df = pd.DataFrame({"Cantidad ": ["3", "5"], "Precio Unitario": ["10.5", "20"]})
    resultado = limpiar_dataframe(df)

    assert "cantidad" in resultado.columns
    assert "precio_unitario" in resultado.columns
    assert resultado["cantidad"].sum() == 8


def test_limpiar_dataframe_elimina_filas_vacias():
    df = pd.DataFrame({"cantidad": [1, None], "precio_unitario": [10, None]})
    resultado = limpiar_dataframe(df)

    assert len(resultado) == 1


def test_consolidar_calcula_total_linea():
    df1 = pd.DataFrame({
        "cantidad": [2],
        "precio_unitario": [10],
        "categoria": ["Electrónica"],
        "archivo_origen": ["a.csv"],
    })
    df2 = pd.DataFrame({
        "cantidad": [1],
        "precio_unitario": [50],
        "categoria": ["Hogar"],
        "archivo_origen": ["b.csv"],
    })

    resultado = consolidar([df1, df2])

    assert "total_linea" in resultado.columns
    assert resultado["total_linea"].tolist() == [20, 50]
