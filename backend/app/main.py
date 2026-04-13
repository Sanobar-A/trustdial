from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.db.database import engine, Base
from app.api import business
import time
from sqlalchemy.exc import OperationalError

app = FastAPI(title="Trustdial")

# DB retry
for i in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        print("DB Connected")
        break
    except OperationalError:
        time.sleep(2)

app.include_router(business.router)

@app.get("/")
def root():
    return {"msg": "Trustdial running 🚀"}

@app.get("/ui", response_class=HTMLResponse)
def ui():
    with open("app/templates/index.html") as f:
        return f.read()