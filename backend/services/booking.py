def create_booking(user_id, station_id, time_slot):
    return {
        "user_id": user_id,
        "station_id": station_id,
        "time_slot": time_slot,
        "status": "CONFIRMED"
    }
