FROM python:3.8

COPY . /loadtest
WORKDIR /loadtest
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
ENTRYPOINT python -u ./run_loadtest.py
