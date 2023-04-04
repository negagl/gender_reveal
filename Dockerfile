FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m venv env
RUN source env/bin/activate
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]