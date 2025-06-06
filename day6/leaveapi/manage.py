#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


from confluent_kafka import Consumer, KafkaError
from dotenv import load_dotenv
import os

from mongoengine import connect

from leave.models import Employee

load_dotenv()
connect(
    db=os.getenv("dbname"),
    host=os.getenv("host"),
    port=int(os.getenv("port")),
    #username=os.getenv("MONGO_USERNAME"),
    #password=os.getenv("MONGO_PASSWORD")
)

# Create your views here.
def consume():
  print("Starting Kafka Consumer...")
  # sets the consumer group ID and offset
  config={}
  config["bootstrap.servers"] = os.getenv("bootstrap.servers")
  config["security.protocol"] = os.getenv("security.protocol")
  config["sasl.mechanism"] = os.getenv("sasl.mechanism")
  config["sasl.username"] = os.getenv("sasl.username")
  config["sasl.password"] = os.getenv("sasl.password")
  config["enable.auto.commit"] = True
  config["client.id"] = os.getenv("client.id")
  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"

  # creates a new consumer instance
  consumer = Consumer(config)
  topic = os.getenv("KAFKA_TOPIC_NAME")
  # subscribes to the specified topic
  consumer.subscribe([topic])

  try:
    while True:
      # consumer polls the topic and prints any incoming messages
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(f"Consumed message from topic {topic}: key = {key:12} value = {value:12}")
        record=Employee(metadata=value)
        record.save()

  except KeyboardInterrupt:
    pass
  finally:
    # closes the consumer connection
    consumer.close()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leave_api.settings')
    try:
        from django.core.management import execute_from_command_line
        consume()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    

if __name__ == '__main__':
    main()
