FROM alpine:latest
RUN apk update && apk add python3 && apk add py3-pip && pip install requests mcstatus
COPY --chown=lenni:lenni heartbeat.py /heartbeat.py
CMD ["python3", "/heartbeat.py"]