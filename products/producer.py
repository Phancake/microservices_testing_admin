import pika, json

params = pika.URLParameters('amqps://fzlmpfmx:DsFd5Fykjt_bxCKgUHC--K1peZBn6N7q@gerbil.rmq.cloudamqp.com/fzlmpfmx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)