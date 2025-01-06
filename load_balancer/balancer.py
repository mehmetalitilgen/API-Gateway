from load_balancer.round_robin import RoundRobinBalancer
from load_balancer.random_balancer import RandomBalancer
from load_balancer.least_connections import LeastConnectionsBalancer

def get_balancer(strategy, services):
    if strategy == "round_robin":
        return RoundRobinBalancer(services)
    elif strategy == "random":
        return RandomBalancer(services)
    elif strategy == "least_connections":
        balancer = LeastConnectionsBalancer()
        balancer.update_services(services)
        return balancer
    else:
        raise ValueError("Invalid load balancer strategy")
