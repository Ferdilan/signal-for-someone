# boot_sequence.py
# When a transmitter falls in love with a receiver coded in Python.

class LoveBot:
    def __init__(self, name="You", language="Python"):
        self.name = name
        self.language = language
        self.status = "idle"
        self.heartbeat = 60  # bpm (before she appeared)

    def start_over(self):
        print(f"{self.name}, rebooting connection... 🌀")
        self.status = "booting"
        self.heartbeat += 20  # she accelerates the system

    def fall_in_love(self):
        if self.language == "Python":
            self.status = "falling"
            print(f"In love with a girl who debugs her feelings better than me.")
            print("Her smile? More elegant than Pythonic syntax.")
        else:
            raise Exception("Incompatible love language.")

    def send_heartbeat(self):
        print(f"Ping: Thinking of {self.name}...")

# Initiate sequence
if __name__ == "__main__":
    d = LoveBot(name="Someone who said 'lstart over'")
    d.start_over()
    d.fall_in_love()
    while True:
        d.send_heartbeat()
