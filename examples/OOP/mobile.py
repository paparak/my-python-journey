class Mobile:
    # Class attribute
    brand = "Apple"

    def __init__(self, model, battery=100):
        self.model = model
        self.battery = battery

    def call(self):
        """Simulate making a call if battery is sufficient."""
        if self.battery > 5:
            print(f"Calling from {self.model}...")
        else:
            print("Battery too low to call!")

    def use_app(self):
        """Simulate app usage and reduce battery level."""
        self.battery -= 10

        if self.battery <= 0:
            self.battery = 0
            print(f"Battery is now {self.battery}%.")
            print("Phone is turning off...")
        else:
            print(f"Battery is now {self.battery}%.")

    def charge(self):
        """Charge the phone without exceeding 100%."""
        self.battery += 20
        if self.battery > 100:
            self.battery = 100
        print(f"Charging... Battery is now {self.battery}%.")


if __name__ == "__main__":
    my_phone = Mobile("iPhone 13", 100)
    my_phone.use_app()
    my_phone.use_app()
    my_phone.call()
