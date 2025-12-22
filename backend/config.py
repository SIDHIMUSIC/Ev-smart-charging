import os

APP_NAME = "EV Smart Charging"

DEBUG = True

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "ev_smart_charging"
