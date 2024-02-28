FROM ubuntu:latest
LABEL authors="antdiscript"
WORKDIR /ukrchatbot
RUN pip install .
COPY . .
