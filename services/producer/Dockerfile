FROM python:3

WORKDIR /usr/src/app/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

CMD [ "python", "main.py", "producer", "--bootstrap_server=kafka:9092" , "--topic=topic_test" ]

