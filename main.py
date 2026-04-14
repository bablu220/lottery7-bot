def get_lottery7_period():
    now = datetime.datetime.now(IST)
    total_minutes = (now.hour * 60) + now.minute
    
    # --- YAHAN CHANGE KAREIN ---
    # Purana tha: 9722 + total_minutes
    # Naya Correction: 9671 (bot ko 51 number piche karne ke liye)
    current_period_suffix = 9671 + total_minutes
    
    date_str = now.strftime("%Y%m%d")
    return f"{date_str}1000{current_period_suffix}"
