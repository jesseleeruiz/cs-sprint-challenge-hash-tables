#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    dataset = {}
    route = []

    for ticket in tickets:
        dataset[ticket.source] = ticket.destination
        
    route.append(dataset["NONE"])

    for index in range(length):
        if route[index] in dataset:
            if dataset[route[index]] == route[0]:
                continue
            else:
                route.append(dataset[route[index]])

    return route
