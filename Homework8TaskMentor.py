import json
import random
shop = {}
with open('shop.json', 'w') as f:
    json.dump(shop, f, indent=4, ensure_ascii=False)

try:
    with open('shop.json', 'r') as f:
        data_shop = json.load(f)

except:
    print('shop.json is empty')
    data_shop = {}

def save_data_shop():
    with open('shop.json', 'w') as f:
        json.dump(data_shop, f, indent=4, ensure_ascii=False)

def menu():
    print('======SwordsShop by Sparta======\n'
          '===)MENU(===)\n'
          '1. Sword of Angry-45$\n'
          '2. Sword of Love-80$\n'
          '3. Sword of Hope-60$\n'
          '4. Sword of Fire-35$')
def new_order_data():
    new_order_menu = {
         '1': ['Sword of Angry',45],
        '2': ['Sword of Love',80] ,
        '3': ['Sword of Hope',60],
        '4': ['Sword of Fire',35]               
    }
    return new_order_menu





def shop_of_swords():
    while True:
        print('Wellcome to:===>>>')
        print('======SwordsShop by Sparta======')
        print('1. Create a new order')
        print('2. Create account')
        print('3. View all items in shop')
        print('4. Check order')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            attemps = 3
            while attemps > 0:
                email = input('Enter your email:')
                password = input('Enter your password:')
                if email not in data_shop.keys() or password != data_shop[email]['password']:    
                    attemps -= 1
                    print(f'Invalid email or password,{attemps} left') 
                    continue      
                else:
                    print('Login successful')
                    
                    while True:
                        print(f'What would you like to order dear {data_shop[email]['name']}')
                        print(new_order_data())
                        choice = input('Enternumber of product:')
                        if choice not in ['1', '2', '3','4']:
                            print('Invalid choice')
                            continue
                         
                        # try:
                        #    
                        # except ValueError:
                        #     print('Invalid quantity')
                        #     continue
                        # if quantity <= 0:
                        #     print('Quantity must be positive')
                        #     continue
                        else:
                            quantity = input('Enter quantity:')
                            if quantity <= 0:
                                print('Quantity must be positive')
                                continue
                            else:
                                id = random.randint(100,9999)
                                new_order_menu = new_order_data()
                                selected_item = new_order_menu[choice]
                                product_name = selected_item[0]
                                product_price = selected_item[1]
                                total_price = product_price * quantity
                                order = {
                                    'product': product_name,
                                    'quantity': quantity,
                                    'total_price': total_price
                                }
                                if 'orders' not in data_shop[email]:
                                    data_shop[email]['orders'] = {}
                                data_shop[email]['orders'][id] = order 
                                
                                print(f"Order placed successfully! Order ID: {id}, Total: ${total_price}")
                                save_data_shop()
                                break
                    break
        elif choice == '2':
            while True:
                email = input('Enter your email address:').strip()
                if email in data_shop.keys():
                    print('Email already exists, try another')
                    continue
                else:
                    name = input('Enter your name:').strip()
                    surname = input('Enter your surname:').strip()
                    password = input('Enter your password:').strip()
                    data_shop[email] = {
                        'name': name,
                        'surname': surname,
                        'password': password,
                        'orders': {} 
                        }
                    print('Account created successfully')
                    save_data_shop()
                    break
        elif choice == '3':
            menu()
                    
    
shop_of_swords = shop_of_swords()           

