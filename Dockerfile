FROM python:3-slim
ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
WORKDIR /
run apt install libseccomp2

COPY /misc/requirements.txt /
RUN python -m pip install -r requirements.txt
COPY . /
