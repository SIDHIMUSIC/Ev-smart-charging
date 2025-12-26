from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "EV Smart Charging Backend is running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
    
from services.booking import create_booking

@app.route("/api/book")
def api_book():
    booking = create_booking(
        user_id=1,
        station_id="ST001",
        time_slot="6PM-7PM"
    )
    return booking
