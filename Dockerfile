FROM ubuntu:alpine
RUN apt-get update -y
RUN apt-get install python3 -y
WORKDIR /app
COPY /app /app
CMD [ "python3", "./app/jerrin.py" ]