FROM python:3.8.14-alpine3.16
RUN apk -U upgrade && apk add gcc musl-dev libffi-dev openssl-dev curl-dev
RUN apk add g++
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENV DATABASEURI mysql+pymysql://root:12345678@MySQLServiceDB/flaskmysql
CMD [ "python","src/app.py" ]
