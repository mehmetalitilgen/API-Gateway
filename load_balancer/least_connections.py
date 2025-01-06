import random

class LeastConnectionsBalancer:
    def __init__(self):
        self.service_connections = {}

    def update_services(self, services):
        for service in services:
            if service not in self.service_connections:
                self.service_connections[service] = 0

    def increment_connection(self, service):
        self.service_connections[service] += 1

    def decrement_connection(self, service):
        if self.service_connections[service] > 0:
            self.service_connections[service] -= 1

    def get_next_service(self):
        if not self.service_connections:
            raise Exception("No services available")
        return min(self.service_connections, key=self.service_connections.get)
