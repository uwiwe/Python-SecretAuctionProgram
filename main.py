from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

other_bidder = "yes"
bid_log = {}

while other_bidder == "yes":
  name = input("What is your name?:")
  bid = int(input("What's your bid?: $"))
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
  clear()
  bid_log[name] = bid

if bid_log:
  winner = max(bid_log, key=bid_log.get)
  print(f"The bid with the highest value is from {winner} with value {bid_log[winner]}!")
else:
  print("The dictionary is empty.")
  
# print("Final dictionary:", bid_log)