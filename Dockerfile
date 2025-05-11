
FROM jupyter/base-notebook

COPY requirements.txt /tmp/


RUN pip install --no-cache-dir -r /tmp/requirements.txt


WORKDIR /home/jovyan/work

COPY . /home/jovyan/work


EXPOSE 8888


CMD ["start-notebook.sh", "--NotebookApp.token=''"]
