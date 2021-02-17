import pika

params = pika.URLParameters('amqps://cmubfdvq:1LEw5bR9lnpkdBp5Sw3Q8j8efv_K3lhZ@kangaroo.rmq.cloudamqp.com/cmubfdvq')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
