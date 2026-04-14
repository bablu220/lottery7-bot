def get_lottery7_period():
    now = datetime.datetime.now(IST)
    date_str = now.strftime("%Y%m%d")
    # Total minutes since midnight
    total_minutes = (now.hour * 60) + now.minute
    
    # Lottery 7 format: Date + 1000 + (10001 + minutes)
    # Aapke screenshot ke hisab se format match karne ke liye:
    period_number = 10001 + total_minutes
    return f"{date_str}1000{period_number}"
    
