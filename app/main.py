import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from app.database.session import engine, Base

app = FastAPI()

@app.on_event("startup")
def startup():
    # Wait and retry until the database is ready
    max_tries = 10
    for i in range(max_tries):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected and tables created.")
            break
        except OperationalError:
            print(f"⏳ Attempt {i+1}/{max_tries}: Waiting for DB to be ready...")
            time.sleep(2)
    else:
        print("❌ Could not connect to the database after several attempts.")
        raise RuntimeError("Database connection failed.")

@app.get("/health")
def health_check():
    return {"status": "ok"}
