product = {}

menu = """
    Menu :
    press 1 for product manager
    press 2 for customer
"""
status = True
while status:
    print(menu)
    choice = int(input ("Enter your choice:"))

    if choice == 1:
        #addition
        manager_menu = """ Menu 
        1)Add prodeuct
        2)view product
        3)exit"""

        m_status = True

        while m_status:
          print(manager_menu)

        m_choice = int(input("Enter your choice:"))
        if m_choice == 1:

            sub_dict = {}
            product_name = input("Enter product name:")
            qty = input("Enter qty:")
            price = int(input("Enter price:"))

            if product_name in product.keys():

             sub_dict["qty"] = qty+product[product_name]["qty"]
             sub_dict["price"] =price
             #print(product)

            else:

             sub_dict["qty"] = qty
             sub_dict["price"] =price
              
             product[product_name] = sub_dict
             #print(product)
            
        elif m_choice == 2:

            print("----------PRODUCTS---------")

            for pro in product:
               print(f"Prodeuct name:{pro}")
               print(f"Qty:{product[pro]["qty"]}")

               print(f"price:{product[pro]["price"]}")

               print("------------------------")
                


        else:
            m_status = False    
    elif choice == 2:
        pass
    else:
        print("Invalid input")

    exit_choice = input("do you want to logout? press y for yes and N for no")
    if exit_choice == 'y' or exit_choice=="yes":
        status=False
    else:
        status = True

        