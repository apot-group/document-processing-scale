FROM python:3.8.5

LABEL author="Duy Nguyen"

WORKDIR /work

COPY ./requirements.txt ./requirements.txt 

RUN pip install jupyterlab==3.2.9

RUN pip install -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["jupyter-lab", "--ip 0.0.0.0", "--allow-root"]