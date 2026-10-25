# scenario
# if it's hot
#   it's a hot day
#   drink plenty of water
# otherwise if its cold
#   it's a cold day
#   wear warm clothes
# otherwise
#   it's a lovely day

is_hot = False
is_cold = False
if is_hot : # first condition
    print("it's a hot day") 
    print("drink plenty of water")
elif is_cold : # second condition
    print("it's a cold day")
    print("wear warm clothes")
else : 
    print("it's a lovely day")

# Example01
# Price eof a house is $1M, if a buyer has good credit, they need to put down 10%. Otherwise, they need to put down 20%.
price = 1000000
good_credit = True
if good_credit :
    down_payment = 0.1 * price
else : 
    down_payment = 0.2 * price
print(f"Down payment: {down_payment}") 