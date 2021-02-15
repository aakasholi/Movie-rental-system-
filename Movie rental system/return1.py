import Displaycode
def ReturnMovie(Movies):
    usernameused=input("Enter the name you gave while borrowing : ")
    file3=open(+name+"_Borrow.txt","a+")
    file3=file3.read()
    print(file3)
    print("\n\n")
    numbofreturn = int(input("\n Enter the quantity of movies you have borrowed :\n "))
    Moviereturn= int(input("Enter the movie id \n : ")
    change=str(int(Movies[Moviereturn][2])+numbofreturn)
    Movies[Moviereturn][2]=change 
    file3=open("Movies_name.txt","w")
    for mova in Movies:
            mova =str(mova)
            mova=mova.replace("[","")
            mova=mova.replace("]","")
            mova=mova.replace("'","")
            file3.write(mova)
            file3.write("\n")                        
        file3.close()                         
    file2 =  open(usernameused+"_Return.txt","a+")
    file2.write("\n Movie was returned by "+usernameused+"\n")                            
    file2.close()
    print("Thank you using our programme")
    ifexit= input("\n Do you want to exit ?? If yes then press Yes If no then you will be returend in main menu  :  ")
                                 
    if(ifexit.upper()=="Y"):
       exit()
    else:
         import Main as file                        
         file()  
ReturnMovie(Movies)
