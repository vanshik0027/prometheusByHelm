# Use the official Python image as base
FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt /code

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /code

# ENTRYPOINT ["python"]
ENV FLASK_APP=main.py
EXPOSE 7000
CMD ["flask", "run", "--host=0.0.0.0", "--port=7000"]

