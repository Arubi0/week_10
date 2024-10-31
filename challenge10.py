#asking user for the details
order_type = input("What is your order type?")
location = input("What is your location?") 


#standard options
if order_type == "standard":
    if location == "local": 
        print("Estimated delivery in 5-7 days.")#prints for local prices
    else: print ("Estimated delivery in 15-20 days. ")#prints for international prices

#express options
if order_type == "express":
    if location == "local":
        print("Estimated delivery in 1-2 days.") #prints for local prices
    else: print ("Estimated delivery in 5-10 days. ") #prints for international prices