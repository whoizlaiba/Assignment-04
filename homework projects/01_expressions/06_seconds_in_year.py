# Question 7: Seconds in One Year

def seconds_in_year():
    days = 365
    hours = 24
    minutes = 60
    seconds = 60
    total_seconds = days * hours * minutes * seconds
    print(f"There are {total_seconds:,} seconds in one year.")

if __name__ == '__main__':
    seconds_in_year()
