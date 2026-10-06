from confluent_kafka import Consumer

conf = {'bootstrap.servers':'kafka:9092','group.id':'1','auto.offset.reset':'earliest'}


cons = Consumer(conf)
topics = ['authentifications']

cons.subscribe(topics)
message = None
messages = []
while True:
    message = cons.poll(timeout=1.0)
    if message:
        if message.error():
            print("error")
            continue
        message = message.value().decode('utf-8')
        messages.append(message)
        message = None




