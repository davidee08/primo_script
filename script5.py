import csv
import smtplib
from email.message import EmailMessage

# -----------------------------
# DATI SMTP (da compilare)
# -----------------------------
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = ""      # <-- la tua email
SMTP_PASSWORD = "b0f6a7ddf724d01b744e8c243e53196aS"

# -----------------------------
# TEMPLATE EMAIL
# -----------------------------
templates = [
    "Ciao {nome} {cognome},\nBenvenuto nel nostro servizio!",
    "Ciao {nome},\nAbbiamo una promozione speciale per te!"
]

# -----------------------------
# LETTURA CSV
# -----------------------------
with open("email_list.csv", newline="", encoding="utf-8") as file:
    righe = list(csv.DictReader(file))

# -----------------------------
# CICLO DI INVIO
# -----------------------------
for persona in righe:
    nome = persona["nome"]
    cognome = persona["cognome"]
    email = persona["email"]
    template_index = int(persona["template"])

    # Testo email dal template
    testo = templates[template_index].format(
        nome=nome,
        cognome=cognome
    )

    # Crea email
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = email
    msg["Subject"] = "Email automatica"
    msg.set_content(testo)

    # Invia email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)

    print("Email inviata a:", email)
