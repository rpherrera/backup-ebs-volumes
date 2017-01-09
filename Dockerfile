FROM python:2.7.13-alpine
MAINTAINER Rafael de Paula Herrera <herrera.rp@gmail.com>

RUN apk add --update py-pip && \
    rm -rf /var/cache/apk/* && \
    pip install boto3 && \
    mkdir /backup-ebs-volumes

WORKDIR /backup-ebs-volumes

COPY backup-ebs-volumes.py /backup-ebs-volumes/backup-ebs-volumes.py
COPY ebs-snapshot-janitor.py /backup-ebs-volumes/ebs-snapshot-janitor.py

CMD ["python", "backup-ebs-volumes.py"]
