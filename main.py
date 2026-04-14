def get_lottery7_period():
    now = datetime.datetime.now(IST)
    date_str = now.strftime("%Y%m%d")
    
    # Total minutes since midnight
    total_minutes = (now.hour * 60) + now.minute
    
    # --- CORRECTION LOGIC ---
    # Aapke screenshot ke hisab se:
    # Game: 10627 | Bot: 957
    # Gap = 10627 - 957 = 9670
    # Isliye hum base number ko 9670 badha denge
    
    base_correction = 10001 + total_minutes + 9670
    
    # Final Format: Date + 1000 + Corrected Number
    return f"{date_str}1000{base_correction}"
