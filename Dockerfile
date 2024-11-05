FROM python:3.12 as base

WORKDIR /app
COPY . .

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501"]