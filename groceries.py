# groceries.py

#from pprint import pprint

#PACKAGES

import operator


# FUNCTIONS
def to_usd(my_price):
    return f"${my_price:,.2f}"

def sort_by_name(any_product):
    return (any_product['name'])

def prods_from(any_dept):
    return [i for i in products if i['department']==any_dept]

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
print("--------------")
print("THERE ARE ", len(products)," PRODUCTS:",sep="")
print("--------------")

# SORTING PRODUCTS

#sorted_products = sorted(products,key=sort_by_name) #sorted function - products as the 'iterable' or list to sort, second param is key
sorted_products=sorted(products,key=operator.itemgetter('name')) #using the operator module

# LISTING PRODUCTS AND PRICES

for item in sorted_products:
    #print("+ ",item["name"]" (${0:,.2f})".format(item["price"]),sep="")
    #print(f"+ {item['name']} (${item['price']:,.2f})")
    #print("+ ",item['name']" (",to_usd(item['price']),")",sep="")
    print(f"+ {item['name']} ({to_usd(item['price'])})")


# MAKE LIST OF DEPARTMENTS

dept = []

#APPROACH 1
#for item in products:
#    if item['department'] not in dept:
#        dept.append(item['department'])

#APPROACH 2
for item in products:
    dept.append(item['department']) not in dept

dept=list(set(dept)) #set takes unique elements and makes it a set variable, list turns it back to list

dept = sorted(dept)
#dept.sort() #mutating function - does the sorting directly to the variable

dept_cnt = len(dept)

print("--------------")
print("THERE ARE "+str(dept_cnt)+" DEPARTMENTS:")
print("--------------")

for d in dept:
    #dept_prods = prods_from(d)     #using a function that does list comprehension
    dept_prods = [i for i in products if i['department']==d]    #doing list comprehension directly
    if len(dept_prods)!=1:
        plural = " products)"
    else:
        plural = " product)"

    print("+ "+d.title()+" ("+str(len(dept_prods))+plural)
