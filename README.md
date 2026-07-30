# Automatización de Reportes Excel/CSV con Python

Proyecto de portafolio que simula una necesidad real de análisis de datos: consolidar múltiples archivos Excel/CSV generados por distintas áreas, limpiar la información y enviar un resumen ejecutivo por correo automáticamente. Este tipo de automatización refleja el trabajo diario de reportería y consolidación de KPIs en operaciones de e-commerce y cuentas de servicio al cliente.

Todos los datos usados en este proyecto son **ficticios**, generados únicamente con fines demostrativos.

## Problema

En muchas áreas comerciales y de datos, los reportes llegan repartidos en varios archivos Excel o CSV (por ejemplo, uno por región, canal o semana). Consolidarlos manualmente cada vez es lento y propenso a errores, y compartir el resultado por correo suele hacerse copiando y pegando a mano.

## Solución

Este proyecto automatiza el flujo completo:

1. Lee todos los archivos `.xlsx` y `.csv` de una carpeta de entrada.
2. Limpia y estandariza las columnas con pandas (tipos de datos, valores nulos, nombres de columnas).
3. Consolida todos los archivos en un único DataFrame y calcula un resumen (totales, promedios, top categorías).
4. Genera un reporte consolidado en Excel.
5. Envía ese resumen por correo electrónico usando `smtplib`, con las credenciales tomadas de variables de entorno (nunca escritas en el código).

## Tecnologías

- Python 3.10+
- pandas y openpyxl (lectura/escritura de Excel)
- smtplib y email (envío de correo, librerías estándar de Python)
- python-dotenv (manejo de variables de entorno)
- pytest (pruebas unitarias)

## Estructura del repositorio

```
automatizacion-reportes-excel-python/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── main.py
├── src/
│   ├── __init__.py
│   ├── lector.py
│   ├── limpieza.py
│   ├── resumen.py
│   └── notificador.py
├── data/
│   └── entrada/
│       ├── ventas_norte.csv
│       └── ventas_sur.csv
└── tests/
    └── test_limpieza.py
```

## Cómo ejecutarlo

1. Clonar el repositorio e instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Copiar `.env.example` a `.env` y completar tus propias credenciales de correo (nunca subir el archivo `.env` real; ya está incluido en `.gitignore`).

3. Colocar los archivos Excel/CSV a consolidar dentro de `data/entrada/`.

4. Ejecutar:

```bash
python main.py
```

5. El script generará un archivo `reporte_consolidado.xlsx` y, si las credenciales de correo están configuradas, enviará el resumen ejecutivo por correo. Si no hay credenciales configuradas, el envío se simula y el resumen se imprime en consola (esto permite probar el proyecto sin exponer ninguna cuenta real).

## Resultado esperado

Un archivo Excel consolidado con todos los datos de entrada limpios, más un correo (o mensaje simulado en consola) con un resumen ejecutivo: total de ventas, promedio por archivo y las categorías con mejor desempeño.

## Nota de seguridad

Este proyecto **nunca** contiene contraseñas ni credenciales reales. El archivo `.env` con credenciales verdaderas está excluido mediante `.gitignore` y solo `.env.example` (con valores de ejemplo) se sube al repositorio.
