# Abstraction

# Reduce complexity by hiding unnecessary details

# Cnnect to server
# Authenticate user
# Match to deriver
# Make payment
# Disconnect from server

class UberService:
    def __init__(self, driver, user):
        self.driver = driver
        self.user = user

    # Cnnect to server
    def _connect_server(self):
        print("Connecting to Uber Server...")

    # Authenticate user
    def _authentication(self):
        print("Authenticating...")

    # Match to deriver
    def _match_driver(self):
        print("Finding nearby driver...")

    # Find ride
    def find_ride(self):
        self._connect_server()
        self._authentication()
        self._match_driver()
        print(f"Your driver is {self.driver} and your ride is KDP 123Y Silver Mazda CX-5")
        self._disconnect_server()

    # Disconnect from server
    def _disconnect_server(self):
        print("Disconnecting from Uber Server...")


user = UberService("Annie", "Nelson")
user.find_ride()