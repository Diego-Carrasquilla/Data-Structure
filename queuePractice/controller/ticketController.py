from model.ticket import Ticket
from model.node import Node

class TicketController:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self) -> bool:
        return self.head == None
    
    def enqueue(self, ticket: Ticket, priority: int = None) -> None:
        # Si la prioridad no se especifica, usar la del ticket
        if priority is None:
            priority = 1 if ticket.priority_attention else 0
        
        node = Node(ticket, priority)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            if current.priority < node.priority:
                node.next = current
                self.head = node
            else:
                while current.next != None and current.next.priority >= node.priority:
                    current = current.next
                node.next = current.next
                current.next = node

    def dequeue(self) -> Ticket:
        if self.is_empty():
            return None
        else:
            ticket = self.head.data
            self.head = self.head.next
            return ticket
        
    def peek(self) -> Ticket:
        if self.is_empty():
            return None
        else:
            return self.head.data
    
    def get_all_tickets(self) -> list:
        tickets = []
        current = self.head
        while current is not None:
            tickets.append(current.data)
            current = current.next
        return tickets
    
    def print_queue(self) -> None:
        current = self.head
        while current != None:
            print(f"Name: {current.data.name}, Priority: {current.priority}")
            current = current.next
        print("End of queue")