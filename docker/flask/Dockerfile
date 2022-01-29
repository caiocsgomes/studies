FROM python:3.8-bullseye


WORKDIR /src

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python", "app.py" ]