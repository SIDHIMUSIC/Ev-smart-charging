def forecast_load(total_bookings):
    if total_bookings < 3:
        return "Low Load"
    elif total_bookings < 6:
        return "Medium Load"
    else:
        return "High Load"
