FROM python:3.9 as build
ENV PYTHONUNBUFFERED=1
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.9-alpine
RUN apk update && apk add mariadb-connector-c
ENV PYTHONUNBUFFERED=1
COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /code/
EXPOSE 8000
WORKDIR /code
