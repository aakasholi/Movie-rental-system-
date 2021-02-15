import Displaycode
def RetrunMovie():
    Movies=Displaycode.Displaycode()
    CusName=input("Enter your Name:")
    file=open(CusName+"-Return.txt","a")
    y=True
    while(y == True):
        x=True
        while(x==True):
            try:
                movID=int(input("Enter Return Movie Id:"))
                x=False
            except:
                print("Invalid value...")
                x=True
        if movID in Movies:
            y=False
        else:
            print("The List does not have the Id...")
            y=True
    z=True
    while(z==True):
        try:
            movquan=int(input("Enter quantity to be returned:"))
            z=False
        except:
            print("Invalid entry...")
            z=True
    change=int(Movies[movID][2])+movquan
    Movies[movID][2]=str(change)
    file1=open("Movies_name.txt","w")
    for key in Movies.keys():
        val=Movies[key]
        stn=",".join(val)
        file1.write(stn+"\n")
    file1.close()
    Fine=int(input("Number of renting days: "))
    if(Fine>0 and Fine<=10):
        money= 0
        print("No fine")
        sett=0
    elif(Fine>10):
        money=(Fine-10)*5
        sett=1
    container=Displaycode.Displaycode()
    file.write("Customer name:"+CusName+"\n"+"MovieID:"+str(movID)+"\nMovie Name:"+container[movID][0]+"\n"+"Quantity"+str(movquan)+"\n"+"Fine Status:$"+str(money)+"\n")
    print("Movie Returned")
    print("----------RETURN BILL----------")
    print("Customer Name:"+CusName)
    print("Movie ID:",movID)
    print("Movie name:",container[movID][0])
    print("Quantity:",movquan)
    if(sett==0):
        print("Fine:None",0)
    elif(sett==1):
        print("Fine: $",money,"For ",Fine,"Days")
    print("-------------------------------")
#RetrunMovie()
