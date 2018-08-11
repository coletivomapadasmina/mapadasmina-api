FROM python:3.6.6
ADD . /app
WORKDIR /app
RUN pip install pipenv 
RUN pipenv install --dev
CMD ["python", "app.py"]