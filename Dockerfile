FROM python:3.6-stretch


WORKDIR /usr/src/app
COPY ./requirements.txt ./
COPY ./kafka-example ./
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY . .

CMD [ "tail", "-f" "/dev/null" ]
