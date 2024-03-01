from datetime import datetime

def get_time():

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return f'Time: {dt_string}'