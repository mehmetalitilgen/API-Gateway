import random

class RandomBalancer:
    def __init__(self, services):
        self.services = services

    def get_next_service(self):
        if not self.services:
            raise Exception("No services available")
        return random.choice(self.services)
