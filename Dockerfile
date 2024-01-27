FROM python:3.11.5-alpine
WORKDIR .
RUN pip install --upgrade.pip
RUN pip install requirements.txt .
COPY . .
CMD["python", "parser.py"]
