print("Welcome to the movie rental Shop")
def Displaycode(): #here we code for the display
    Movie =[]
    print("--------------------------------------------------------------------")
    print ("Movie-ID        Movie-Name     Price  Quantity")
    print("--------------------------------------------------------------------")
    file=open("Movies_name.txt","r")
    a=1
    for line in file:
        print("  ",a,"\t\t"+line.replace(",","\t"))
        a=a+1
    print("--------------------------------------------------------------------")
    
    file1=open("Movies_name.txt","r")
    d={}
    s=1
    for line in file1:
        line=line.replace("\n","")
        d[s]= line.split(",")
        s=s+1
    return d
Displaycode()

