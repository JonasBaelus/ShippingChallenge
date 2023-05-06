FROM python:3.10.0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api

CMD [ "uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]