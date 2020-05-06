FROM python:3.7-stretch
WORKDIR /opt/app
RUN mkdir -p /opt/app/logs/
COPY . ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["gunicorn", "core.app:application", "-c", "guniconf.py"]
