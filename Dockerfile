FROM python:2.7.13-alpine
MAINTAINER Rafael de Paula Herrera <herrera.rp@gmail.com>

RUN apk add --update py-pip && \
    pip install boto3 && \
    rm -rf /var/cache/apk/* && \
    mkdir /backup-ebs-volumes

WORKDIR /backup-ebs-volumes

COPY backup-ebs-volumes.py /backup-ebs-volumes/backup-ebs-volumes.py

CMD ["python", "backup-ebs-volumes.py"]
