import Displaycode
def Borrow() :
    Movies=Displaycode.Displaycode()
    username=input("Enter the borrower name : ")
    print("Hello "+username+" choose the movie you want to borrow ")
    hello=False
    while (hello==False):
        Movie_ID= int(input("Enter the Movie id you want to borrow : "))
        for a in range(len(Movies)+1):
            if (Movie_ID ==a):
                Movie_Name1=Movies[Movie_ID][0]
                hello=True
            elif (Movie_ID)>len (Movies):
                    print("\n error !! \n check the Movie id again")
                    hello=False
                    break
        print("So, you want ",Movie_ID)
        Moviepresent=False
        while (Moviepresent == False):
            maximum= True
            while (maximum == True):
                noofmovies= int(input("How many "+Movie_Name1+"do"+username+ " like to borrow?"))
                break
            break
        if (noofmovies <= int(Movies[Movie_ID][2])): 
            Movies[Movie_ID][2] =str(int(Movies[Movie_ID][2]) - noofmovies)
            costprice = Movies[Movie_ID] [2]
            print("The " +username+" will pay $" ,costprice, " for borrowing " ,Movie_ID," for the next 10 days")

            file2=open("Movies_name.txt","w")
            for key in Movies.keys() :
                mova=Movies[key]
                each=",".join(mova)
                #mova=mova.replace("'","")
                file2.write(each+"\n")
                #file2.write("\n")
            file2.close()
                
        import datetime
        now=datetime.datetime.now()
        todaysDate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #returnday=(date.today() + timedelta(days=10)).isoformat()

        file2=open(username+"_Borrow.txt","a+")
        file2.write("Movie Rental by the "+username+"\n")
        file2.write("Date Time:"+str(now))
        #file2.write("\nInvoice:"+str(date.today().isoformat())+"\tdate: "+str(date.today().isoformat())+"\tTime: "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)+"\t\tBook Submission Date: "+str(returnday))
        file2.write("\n________________________________________________________________________________________________________________________")
        file2.write("\nName of Student: "+username)
        file2.write("\n________________________________________________________________________________________________________________________\n")
        file2.write("Cost"+str(costprice))
        file2.write("\n________________________________________________________________________________________________________________________\n")

        file2.close()
        #file3=open("_Borrow.txt".format(username),"r")
        #file3=file2.read()
        print("File Recorded")
        '''Moviepresent = True

        menu=str(input("\n Do you wanna rent a another movie ? \n Enter Y for Yes and N for NO :- " ))
        if menu =="Y" :
            print("\n\n")
            import Main as file
            file2()
        else:
            print("Thank you for using our movie store")'''
Borrow()
