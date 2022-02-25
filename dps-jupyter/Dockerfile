FROM python:3.8.5

LABEL author="Duy Nguyen"

WORKDIR /

COPY ./requirements.txt ./requirements.txt 

RUN pip install jupyterlab

RUN pip install -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab"]