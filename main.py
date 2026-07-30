"""
Script principal: orquesta la lectura, limpieza, generación de resumen
y envío de correo para la automatización de reportes.

Todos los datos de ejemplo en data/entrada/ son ficticios.
"""

from dotenv import load_dotenv

from src.lector import leer_archivos
from src.limpieza import consolidar
from src.resumen import generar_resumen, resumen_a_texto
from src.notificador import enviar_resumen

CARPETA_ENTRADA = "data/entrada"
ARCHIVO_SALIDA = "reporte_consolidado.xlsx"


def main():
    load_dotenv()

    dataframes = leer_archivos(CARPETA_ENTRADA)
    consolidado = consolidar(dataframes)
    consolidado.to_excel(ARCHIVO_SALIDA, index=False)
    print(f"Reporte consolidado generado en '{ARCHIVO_SALIDA}'.")

    resumen = generar_resumen(consolidado)
    texto_resumen = resumen_a_texto(resumen)

    enviar_resumen("Resumen ejecutivo de ventas", texto_resumen)


if __name__ == "__main__":
    main()
