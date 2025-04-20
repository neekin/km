FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
COPY . /app/