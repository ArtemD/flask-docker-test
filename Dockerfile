FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app/
RUN pip install Flask
RUN pip install markdown

EXPOSE 5000

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]