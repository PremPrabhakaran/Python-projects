passenger_name = "Shreya"       
destination = "Kerala"             
ticket_price = 850.50           
number_of_tickets = 3           
is_available = True             
 
print("\nPassenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: $", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
  
total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount
 
print("Total Cost: $", total_cost)
print("Discount: $", discount)
print("Final Cost: $", final_cost)
 
print("Double Ticket Price: $", ticket_price * 2)
print("Ticket Price After $50 Increase: $", ticket_price + 50)
print("Half Ticket Price: $", ticket_price / 2)
 
print("Is ticket price under $1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination Kerala?", destination == "Kerala")
print("Is final cost more than $2000?", final_cost > 2000)
  
travel_message = passenger_name + " is travelling to " + destination + "."
print("Travel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))
  
morning_ticket_price = 700
evening_ticket_price = 900
 
print("Before Swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)
 
morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
 
print("After Swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)
  
print("\n================================")
print("TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: $", final_cost)
print("Booking Confirmed?", is_available)
