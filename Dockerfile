FROM ubuntu:16.04

MAINTAINER Gabriel Oliveira <gabriel@gabrieloliveira.net>

RUN apt-get update
RUN apt-get install -y python python-pip supervisor