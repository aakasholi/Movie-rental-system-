import Displaycode
import Borrow1
import return2
def main():
    hello = True
    while (hello==True):
        askuser=input(str("What to do , Return or Borrow ???\nIf you want to Borrow please press 1 or If you want to Return then Press 2 and If you want to exit please press 3:"))
        if(askuser=="1"):
           Borrow1.Borrow()
           hello=True
        elif(askuser=="2"):
            return2.RetrunMovie()
            hello=True
        elif(askuser=="3"):
            print("Thank you for visiting:")
            hello=False
        else:
           print("You have entered wrong button!!!!")
           hello=True
main()
