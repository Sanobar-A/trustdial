import pika
import json

def send_verification_task(business_id):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )
    channel = connection.channel()

    channel.queue_declare(queue="verification_queue")

    channel.basic_publish(
        exchange="",
        routing_key="verification_queue",
        body=json.dumps({"business_id": business_id})
    )

    connection.close()
