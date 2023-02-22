import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
work=True
while work:
    time.sleep(0.1)
    channel.queue_declare(queue='niger')
    channel.basic_publish(exchange='',
                          routing_key='niger',
                          body=b'Hello World!')
    print(" [x] Sent 'Hello World!'")
connection.close()
