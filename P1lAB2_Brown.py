"""
CTI110 
P1LAB2 - Sales  
brownm
8/31
Simple point of sales program

"""
# setup our store



store_name = "Browns Shoe Palace"
product = "shoes"
stock = 20
price = 300

#Customer Greeting
print("Welcome to",store_name)
print("What's your name?")
customer_name = input()
print("Nice to meet you,", customer_name)

# Explain product
print("Our special today is:", product)
print("On sale for $", price)
print("They're going fast there is only",stock,"left!" )

#Take order
print("How many", product, "would you like?")
# inout gives us a string 
#order = int(order)
# or
order = int(input())

#finish up

total_price = order* price
print("So you would like")
print(order,product,"for a total of $", total_price)
print("Thank you for your purchase have a great day!")
