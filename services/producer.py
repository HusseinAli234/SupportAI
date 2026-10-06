from confluent_kafka import Producer

conf = {'bootstrap.servers':'kafka:9092'}

producer = Producer(conf)

a = 'New authentification!'

res = a.encode('utf-8')

producer.produce(topic="authentifications",value=res)


producer.flush()


