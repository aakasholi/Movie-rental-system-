import Displaycode
import datetime
def Borrow():
    #print(container)
    cus_name=input("Enter Your Name:")
    file=open(cus_name+"-Borrow.txt","a")
    print("Welcome,"+cus_name+" In our Rental shope........")
    grant=0
    yes="y"
    while(yes=="y"):
        y=True
        while(y== True):
            x=True
            while(x== True):
                container=Displaycode.Displaycode()#call function for dictionary
                try:
                    mov_id=int(input("Enter Movie Id you want to rent:"))
                    if mov_id in container:
                        x=False
                    else:
                        print("Choose available once...")
                        x=True
                except:
                    print("Invalid entry....")
                    x=True
            quan=int(container[mov_id][2])
            if(quan!=0):
                z=True
                while(z==True):
                    w=True
                    while(w== True):
                        try:
                            mov_quan=int(input("Enter quantity for movie borrowing:"))
                            w=False
                        except:
                            print("Invalid input....")
                            w=True
                    if(mov_quan>int(container[mov_id][2])):
                        print("Limit quantity...")
                        z=True
                    elif(mov_quan>0 and mov_quan<int(container[mov_id][2])):
                        quantity=int(container[mov_id][2])-mov_quan
                        container[mov_id][2]=str(quantity)
                        file1=open("Movies_name.txt","w")
                        for key in container.keys():
                            lst=container[key]
                            copy=",".join(lst)
                            file1.write(copy+"\n")
                        file1.close()
                        print("File Updated!!")
                        z=False
                    else:
                        print("Enter again....")
                y=False
            else:
                print("No Stock Left.....")
                y=True
        price=container[mov_id][1].replace("$","")
        total=float(price)*mov_quan
        grant=total+grant
        #print(total)
        time=datetime.datetime.now()
        file.write("Customer Name:"+cus_name+"\nMovie Id:"+str(mov_id)+"\nMovie Name:"+container[mov_id][0]+"\nQuantity:"+str(mov_quan)+"\nPrice:"+str(total)+"\nDateTime:"+str(time)+"\n")
        print("File Recorded")
        print("---------------Borrow BILL----------------")
        print("Customer Name:"+cus_name)
        print("Movie Name:"+container[mov_id][0])
        print("Price:"+"$",total)
        print("Quantity:",mov_quan)
        print("Date:",time.strftime("%Y %m %d %H:%M:%S"))
        print("------------------------------------------")
        yes=input("Do ypu want to continue(y/n):")
        print("Grand Total:"+"$",grant)
    
#Borrow()
