FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic