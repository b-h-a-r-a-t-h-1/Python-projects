#This program is to create a online food order system and the amount to be paid by the customer

print("welcome to our Restaurent 'Food is Good'")
print("Please find the Menu items")
#Menu card displaying
menucard={
    "IDLY":30,
    "VADAI":10,
    "PLAINDOSA":40,
    "ONIONDOSA":50,
    "MASALADOSA":60,
    "POORI":40,
    "CHAPPATI":30,
    "PAROTTA":40,
    "OMBLET":10,
    "HALFBOIL":10,
    "KALAKI":10,
    "PONGAL":60,
    "KESHARI":40,
    "VEGBRIYANI":50,
    "CURDRICE":40,
    "LEMONRICE":40,
    "TAMARINDRICE":40,
    "TOMATORICE":40
    }
print(menucard)



#getting the order
print("Please place your desired order based on the menu.\nEnter 1 to continue.\nEnter 2 to exit the order.")
try:
    i=int(input("Enter your choice:-"))
except:
    print("Choice Entered is not a number please enter a valid choice 1 or 2")
    i=int(input("Enter your choice:-"))
ordered_items=[]
quantity_of_items=[]
individual_order_value=[]
order_value=0
#bill amount calculating
while i==1:
    item_name=input("Enter the item name:-")
    try:
        item_quantity=int(input("Please Enter the quantity in numbers:-"))
    except:
        print("Item Quantity should be a number,Please Enter valid input")

    if item_name.upper() in menucard:
        ordered_items.append(item_name.capitalize())
        quantity_of_items.append(item_quantity)
        order_value=order_value+(menucard[item_name.upper()]*item_quantity)
        individual_order_value.append(menucard[item_name.upper()]*item_quantity)
    else:
        print("The Item order does not exist in our menu.Please check the availabitity")

    i=int(input("Please Enter 1 to add more items or Enter 2 to check out with current order:-"))


#bill amount printing
else:
    k=0
    for order in ordered_items:
        print(order,'|',quantity_of_items[k],'|',individual_order_value[k])
        k+=1
    GST=3
    SGST=CGST=order_value*(GST/100)
    total_order_amount=order_value+SGST+CGST
    print("Total Bill Amount Excluding GST:-",order_value)
    print("Total Tax Amount SGST:-",SGST)
    print("Total Tax Amount CGST:-",CGST)
    print("Total Bill Amount to be paid in INR:-","Rs.",round(total_order_amount))
    print("\nThanks for Visiting 'Food is Good'\nHope you have enjoy your food\nStriving hard to serve u better.")
