import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch1 = connection.channel()

ch1.queue_declare(queue='hello')
text = 'Hello World'
ch1.basic_publish(exchange='', routing_key='hello', body=text)

print()

connection.close()