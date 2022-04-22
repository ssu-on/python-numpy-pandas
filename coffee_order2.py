menu = {'Americano':1800,'Cafe latte':2200,'Cafe Mocha':2800}
cup = {}
Pay = []
Total = []
coffee_list= menu.keys()

def print_menu() :
    print("="*7+"Cafe"+"="*7)
    print("1. Select coffee menu")
    print("2. Check your order")
    print("3. Pay total price")
    print("4. Get change")


def print_coffeeMenu(coffee):
    print(" "+coffee,str(menu[coffee])+"won")


def select_menu(coffee,cups) :
    if coffee in cup:
        cup[coffee] += int(cups)
    else :
        cup[coffee] = int(cups)

def check_order() :
    for coffee,number in cup.items() :
        print(str(coffee)+"\t"+str(number)+" cups")

def calculate_price() :
    if 'Americano' not in cup :
        cup['Americano']= 0
    if 'Cafe latte' not in cup :
        cup['Cafe latte']= 0
    if 'Cafe Mocha' not in cup :
        cup['Cafe Mocha'] = 0
    total = int(cup['Americano'])*1800 + int(cup['Cafe latte'])*2200 + int(cup['Cafe Mocha'])*2800
    Total.append(total)
    print("TotalPrice :",total)
    pay = int(input("Pay money : "))
    while pay < total :
        print("Too small..\n")
        pay = int(input("Pay money : "))
    if pay >= total :
        Pay.append(pay)

def get_change(change) :
    if change // 50000 > 0 :
        print("50000 won : "+str(change//50000))
    if change % 50000 >= 10000 :
        print("10000 won : "+str((change%50000)//10000))
    if change % 10000 >= 5000 :
        print("5000 won: 1")
    if change % 5000 >= 1000 :
        print("1000 won : "+str((change%5000)//1000))
    if change % 1000 >= 500 :
        print("500 won : 1")
    if change % 500 > 0 :
        print("100 won : "+str((change % 500)//100))
        
print_menu()
num = input("\nchoose : ")

while int(num) != 4 :
    if int(num) == 1 :
        print("\n[Cafe Menu]")
        for i in coffee_list :
            print_coffeeMenu(i)
        
        coffee = input("\nSelect Menu : ")
        while coffee not in menu.keys() :
            print("You selected wrong menu..")
            coffee = input("Select Menu : ")
        if coffee in menu.keys() :
            cups = input("How many cups ? ")
        select_menu(coffee,cups)

        print_menu()
        num = input("\nchoose : ")
        
    elif int(num) == 2 :

        check_order()
            
        print_menu()
        num = input("\nchoose : ")

    elif int(num) == 3 :
       
        calculate_price()

        print_menu()
        num = input("\nchoose : ")

    else :
        print_menu()
        num = input("\nchoose : ")
    

if int(num) == 4 :
    pay = Pay[-1]
    total = Total[-1]
    change = int(pay) - int(total)
    print("Your change is",change," won.")
    print("="*28)
    get_change(change)
    print("\nThank you for using our machine")
