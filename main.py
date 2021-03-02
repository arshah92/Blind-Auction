from art import logo            # OR import art and print(art.logo)
from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.\n")

# Function if you need to prin the list of all bidders and their bid.
#final_list = []
#def add_to_disc(name, amount):
  # bid_details = {}
  # bid_details["name"] = name
  # bid_details["amount"] = amount
  # final_list.append(bid_details)

bid = {}
def find_max_bidder(max_amount):
  max_bid = 0
  max_bidder = ""
  for bidder in max_amount:
    bid_amount = max_amount[bidder]
    if bid_amount > max_bid: 
      max_bid = bid_amount
      max_bidder = bidder
  print(f"The winner is {max_bidder} with a bid of ${max_bid}")


while_var = True

while while_var:
  user_name = input("What is your name?\n").lower()
  user_bid = int(input("What is your bid?\n"))
  
  bid[user_name] = user_bid

  next_bidder = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
  clear()
  
  if next_bidder != 'yes':
    while_var = False
    find_max_bidder(bid)