######################################################################
# IMAGE for airflow
######################################################################
FROM python:3.8.5-buster

LABEL maintainer="Duy Nguyen <duyngunyenngoc@hotmail.com>"

WORKDIR /usr/local/airflow

COPY ./requirements.txt requirements.txt

COPY ./airflow/ /usr/local/airflow/

RUN pip3 install apache-airflow[crypto,password,ssh]==2.2.0

# RUN pip3 install cattrs==1.0.0

RUN pip3 install -r requirements.txt

EXPOSE 8080 5555
