#!/usr/bin/env python3


class Passenger:
    passenger_names =[]
    total_weight = 46
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    
    def register(self,name):
        self.passenger_names.append(name)
        for passenger in self.passenger_names:
            return passenger
        
    def weight_count(self,weight): 
        if weight > self.total_weight:
            print(f"{self.name}Too much weight")
        else:
            print(f"Passengers {self.name} carrying {weight}")


class Vip_passenger(Passenger):
    def __init__(self, name, weight, class_level):
        super().__init__(name, weight)
        self.class_level=class_level

    def eligible_for_class(self):
        print(f"{self.name} is {'eligible to access VIP class' if self.class_level else 'not eligible for VIP'}")




class EconomicPassenger(Passenger):
    def __init__(self, cost):
        super().__init__(name, weight)
        self.ticket_price = cost
    

    def eligible_to_flight(self):
        user_payment = float(input("Pay in USD"))
        if user_payment >= self.ticket_price:
            print(f"Have a safe flight: {self.name}")
            diff = user_payment - self.ticket_price
            return f"The diff is {diff} USD"
        else:
            print(f"Pay the full amount {self.ticket_price}USD before travelling")


amazing = Vip_passenger("Amazing",32, 1)
Twariq= EconomicPassenger("Twariq",32, 100)
amazing.eligible_for_class()
Twariq.eligible_to_flight()

