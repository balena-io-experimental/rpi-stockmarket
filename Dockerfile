FROM resin/rpi-raspbian:latest

# Install Python.
RUN apt-get update
RUN apt-get install -y python python-dev python-pip python-pygame libraspberrypi-bin

ADD /src/ /usr/src/app

RUN pip install pygame

CMD ["bash", "/usr/src/app/start.sh"]