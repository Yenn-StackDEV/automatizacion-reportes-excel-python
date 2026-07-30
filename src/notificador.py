"""
Módulo encargado de enviar el resumen ejecutivo por correo electrónico.

Las credenciales se leen siempre desde variables de entorno (nunca se
escriben directamente en el código). Si no hay credenciales configuradas,
el envío se simula y el resumen se imprime en consola, para poder probar
el proyecto sin exponer ninguna cuenta de correo real.
"""

import os
import smtplib
from email.mime.text import MIMEText


def enviar_resumen(asunto: str, cuerpo: str) -> None:
    """
    Envía el resumen por correo usando las credenciales de las variables
    de entorno. Si faltan credenciales, simula el envío imprimiendo en consola.
    """
    remitente = os.getenv("EMAIL_REMITENTE")
    password = os.getenv("EMAIL_PASSWORD")
    destinatario = os.getenv("EMAIL_DESTINATARIO")
    servidor = os.getenv("SMTP_SERVIDOR", "smtp.gmail.com")
    puerto = int(os.getenv("SMTP_PUERTO", "587"))

    if not remitente or not password or not destinatario:
        print("[SIMULACIÓN] No hay credenciales de correo configuradas.")
        print(f"Asunto: {asunto}")
        print(cuerpo)
        return

    mensaje = MIMEText(cuerpo)
    mensaje["Subject"] = asunto
    mensaje["From"] = remitente
    mensaje["To"] = destinatario

    with smtplib.SMTP(servidor, puerto) as smtp:
        smtp.starttls()
        smtp.login(remitente, password)
        smtp.sendmail(remitente, [destinatario], mensaje.as_string())

    print(f"Correo enviado correctamente a {destinatario}.")
