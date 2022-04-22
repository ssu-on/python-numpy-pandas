def print_menu() :
    print("="*5+"Checking Year Program"+"="*5,"\n",
      "%24s" % "1.Check Leap Year","\n",
      "%24s" % "2.Check total day","\n",
      "%8s.%10s" % ("3","Exit"));print("="*30)

print_menu()
num = int(input("Select : "))

while num != 3 :
    if num == 1 :
        year = int(input("Enter year to check : "))
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) :
            print(year,"is leap year.")
            print_menu()
            num = int(input("Select : "))
        else :
            print(year,"is not leap year.")
            print_menu()
            num = int(input("Select : "))
    elif num == 2 :
        print("Enter month and date")
        month, date = map(int,input("Month, Date :").split())
        Date = [31,28,31,30,31,30,31,31,30,31,30,31]
        sum = 0
        for day in Date[0:month-1] :
            sum = sum + day
        total_day = sum + date
        print("2022."+str(month)+"."+str(date)+" is "+str(total_day)+"th day in 2022.")
        print_menu()
        num = int(input("Select : "))
    else :
        print_menu()
        num = int(input("Select : "))

print("Thanks for using program.")
