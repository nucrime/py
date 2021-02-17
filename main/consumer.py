import pika

params = pika.URLParameters('amqps://cmubfdvq:1LEw5bR9lnpkdBp5Sw3Q8j8efv_K3lhZ@kangaroo.rmq.cloudamqp.com/cmubfdvq')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()