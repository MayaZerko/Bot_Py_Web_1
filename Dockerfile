FROM python:3.10

RUN mkdir -p /usr/src/app
RUN pip install -U pipenv
RUN pipenv install

WORKDIR usr/src/app

COPY . /usr/src/app

CMD ["pipenv", "run", "python", "src/assistant.py"]