import pika
import json
import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Database config
DATABASE_URL = "postgresql://admin@db:5432/trustdial"

# Create DB connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Retry RabbitMQ connection (VERY IMPORTANT)
while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq")
        )
        print("✅ Connected to RabbitMQ")
        break
    except Exception as e:
        print("⏳ Waiting for RabbitMQ...", e)
        time.sleep(5)

channel = connection.channel()
channel.queue_declare(queue="verification_queue")


# Worker logic
def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        business_id = data["business_id"]

        print(f"📥 Received task for business {business_id}")

        # simulate processing delay
        time.sleep(3)

        # update DB
        db = SessionLocal()
        try:
            db.execute(
                text("UPDATE businesses SET status='verified' WHERE id=:id"),
                {"id": business_id}
            )
            db.commit()
            print(f"✅ Business {business_id} verified")
        except Exception as db_error:
            print("❌ DB Error:", db_error)
        finally:
            db.close()

    except Exception as e:
        print("❌ Worker Error:", e)


# Start consuming
channel.basic_consume(
    queue="verification_queue",
    on_message_callback=callback,
    auto_ack=True
)

print("Worker started and waiting for tasks...")

channel.start_consuming()