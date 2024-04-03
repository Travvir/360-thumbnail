FROM python:3.8

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

RUN pip install Flask opencv-python

ENV FLASK_APP=main

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
