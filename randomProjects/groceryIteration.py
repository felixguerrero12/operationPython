shopping_list = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

food = {
	"banana" : 2,
	"apple"  : 3,
	"orange" : 4,
	"pear"	 : 5
}

def compute_bill(food):
    total=0
    for i in food:
        if stock[i] > 0: # Check if the item is still in stock.
            total += prices[i] # Add the prices of totals to grand.
            stock.update({i: stock[i]-1}) # Once added, remove one from stock.
    return total
print compute_bill(food)
