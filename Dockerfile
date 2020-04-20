FROM continuumio/miniconda3:4.7.10

RUN pip install flask
COPY serve /usr/local/bin/
COPY train /usr/local/bin/
COPY serve /opt/conda/bin
COPY train /opt/conda/bin
EXPOSE 8080
