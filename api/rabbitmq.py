import json
import pika
import os

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'user')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', 'pass')

def publish_event(event_type, data):
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='book_created', exchange_type='fanout')

    message = json.dumps({
        'type': event_type,
        'data': data
    })
    channel.basic_publish(
        exchange='book_created',
        routing_key='',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # persistent
        )
    )
    connection.close()
