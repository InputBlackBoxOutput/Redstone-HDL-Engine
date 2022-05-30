# -> Build docker image
# docker build . -t rutuparn/redstone-hdl

# -> Create a container from the docker image
# docker run -d -p 5000:5000 rutuparn/redstone-hdl

FROM python:3.8-slim-buster

WORKDIR /application

RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y
RUN apt install yosys -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port", "$PORT"]