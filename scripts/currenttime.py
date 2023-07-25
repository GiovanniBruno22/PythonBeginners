# imports
import time
from datetime import timezone, timedelta, datetime

def time_is_relative():
    '''
    This script displays the time in London/New York/Mumbai when run from the terminal
    '''
    # getting utc time
    dt = datetime.now(timezone.utc)
    utc_timestamp = dt.replace(tzinfo=timezone.utc)

    # define list of tuples for timezone deltas accounting for DST
    deltas = [('London', 1), ('New York', -5 + time.daylight), ('Mumbai', 5.5)]

    #iterate over time deltas for different cities, formatting, and printing
    for i, j in deltas:
        local_time = (utc_timestamp + timedelta(hours=j)).strftime("%H:%M:%S")
        print(f"The current time in {i} is {local_time}.")

if __name__ == "__main__":
    time_is_relative()