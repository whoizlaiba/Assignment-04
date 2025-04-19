import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02}:{:02}'.format(mins, secs)  # Fixed typo with the second format specifier
        print(timer, end="\r")  # Display the countdown
        time.sleep(1)  # Wait for one second
        t -= 1  # Decrease the time by 1 second
    print("Timer completed!")  # Only print once the timer is done

# Get user input once before starting the countdown
t = int(input("Enter the time in seconds: "))
countdown(t)
