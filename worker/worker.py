import pika
import json
import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin@db:5432/trustdial"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def callback(ch, method, properties, body):
    data = json.loads(body)
    business_id = data["business_id"]

    print(f"Processing {business_id}")

    time.sleep(3)

    db = SessionLocal()
    db.execute(
        text("UPDATE businesses SET status='verified' WHERE id=:id"),
        {"id": business_id}
    )
    db.commit()
    db.close()

    print(f"Verified {business_id}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq")
)

channel = connection.channel()
channel.queue_declare(queue="verification_queue")

channel.basic_consume(
    queue="verification_queue",
    on_message_callback=callback,
    auto_ack=True
)

print("Worker running...")
channel.start_consuming()