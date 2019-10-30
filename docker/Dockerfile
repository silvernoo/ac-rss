ARG ARCH
FROM $ARCH/python:alpine

ARG QEMU_BIN
COPY $QEMU_BIN /usr/bin

WORKDIR /usr/src/app

COPY . .

RUN chmod +x docker/start.sh

RUN	apk update && \
	apk add --no-cache git

RUN /usr/bin/crontab docker/crontab.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["docker/start.sh"]