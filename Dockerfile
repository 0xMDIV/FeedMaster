FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

ENV APPDIR "/app"
RUN mkdir -p $APPDIR

RUN apt-get update && apt-get -y install python3 python3-dev python3-pip python3-wheel libsqlclient-dev libssl-dev default-libmysqlclient-dev  libmysqlclient-dev mysql-client

COPY requirements.txt $APPDIR
RUN pip install --upgrade pip
RUN pip install -r $APPDIR/requirements.txt

EXPOSE 22
EXPOSE 8000

WORKDIR $APPDIR

COPY . $APPDIR

CMD python manage.py runserver 0.0.0.0:8000