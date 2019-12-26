FROM python:3.8

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1

ENV APP /{{cookiecutter.app_name}}

RUN pip3 install pipenv
RUN mkdir /log

RUN mkdir /$APP
WORKDIR $APP

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile
ADD . .

EXPOSE 5000

CMD ["pipenv", "run", "python", "run.py"]
