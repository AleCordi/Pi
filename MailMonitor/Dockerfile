# Usa un'immagine base Python
FROM python:3.9-slim

# Installa cron and libs for python script
RUN apt-get update && apt-get install -y cron
RUN pip install configparser --break-system-packages
RUN pip install secure-smtplib --break-system-packages

# Imposta la directory di lavoro
WORKDIR /usr/src/app/

# Copia il file di script nella directory di lavoro
COPY sendEmail.py /usr/src/app/

# Imposta il file di cronjob
RUN echo "*/5 * * * * python /usr/src/app/sendEmail.py" > /etc/cron.d/sendMail

# Da i permessi al file di cronjob
RUN chmod 0644 /etc/cron.d/sendMail

# Applica il file di cronjob al crontab di sistema
RUN crontab /etc/cron.d/sendMail

# Crea un file per i log del cronjob
RUN touch /var/log/cron.log

# Avvia il servizio cron e rimani in esecuzione
CMD cron && tail -f /var/log/cron.log
