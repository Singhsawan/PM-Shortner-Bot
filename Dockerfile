FROM python:3.11

WORKDIR /Pm-Shortner

COPY . /Pm-Shortner

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
