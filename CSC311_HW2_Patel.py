import os
def head(n):
    with open("CSC311_HW2_Harness_Patel.txt") as myfile:
        head = [next(myfile) for i in range(n)]
        print(head)
        myfile.close()
        return

def more():
     with open("CSC311_HW2_Harness_Patel.txt") as myfile:
        more = myfile.read()
        print(more)
        myfile.close()
        return

ans=True
while ans:
    print("""
          1. head
          2. more
          3. split
          4. tail 
          5. wc
          6. diff
          7. Exit the Program
          """)

    ans = input("please enter the number of the option you would like to select: ")

    if ans =="1":
        print(head(10))


    elif ans =="2":
        os.system('cls')
        more = input("Press the Enter Key to show one more line of text or Press the Space key to show more screen of the text shown")
        if more =="":
            with open("CSC311_HW2_Harness_Patel.txt") as myfile:
                print(myfile.read())
                myfile.close()
        elif more == " ":
             with open("CSC311_HW2_Harness_Patel.txt") as myfile:
                print(myfile.read())
                myfile.close()
        #print(more())

    elif ans == "3":

        print("split function")

    elif ans == "4":
        print ("tail function")

    elif ans == "5":
        print("wc function")

    elif ans == "6":
        print("diff function")

    elif ans == "7":
        break

    else:
        print("\n not a valid choice. please try again.")
  
