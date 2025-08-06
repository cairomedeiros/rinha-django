FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 9999

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:9999"]
