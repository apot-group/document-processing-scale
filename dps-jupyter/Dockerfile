FROM jupyter/pyspark-notebook
LABEL author="Duy Nguyen"
USER root
RUN pip install findspark confluent_kafka pyspark nltk
# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

COPY ./requirements.txt ./requirements.txt 
RUN pip install -r requirements.txt

ENV JUPYTER_ENABLE_LAB="yes"