import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title ="Please drink water now",
            message ="improved Digestion. Proper digestion is vital for extracting nutrients from the food we eat. ...",
            timeout= 12
        )
    # time.sleep(60)
    time.sleep(60*60)