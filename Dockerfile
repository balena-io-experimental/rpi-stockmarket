#Base image
FROM resin/rpi-raspbian:jessie-2015-02-18

RUN apt-get update
RUN apt-get install -y python python-dev python-pip python-pygame

ADD /src/ /usr/src/app

RUN pip install pygame

CMD ["bash", "/usr/src/app/start.sh"]