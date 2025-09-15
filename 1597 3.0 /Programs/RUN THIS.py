print("Welcome to 1597 3.0 MACINTOSH")
print("To use software, just type the number that lines up with the option you want to select and press enter")  
print("Build Compiled on: 9/15/25")
def main_menu():
    while True:
        print("===Mac Apps===")
        print("1. Launch Finder")
        print("2. Launch Music")
        print("3.Launch Mail")
        print("4. Launch Notes")
        print("===1597===")
        print("5. Calender ")
        print("6. Clock")
        print("7. Ping Pong Game")
        print("8. GTSP (Trial)")
        print("9. Guess The Password")
        print("10. 1597 1.5")
        print("11. Credits")
        print("12. Exit")
        choice = input("Enter the number corresponding to your choice: ")
        
        if choice == '1':
            import openapp1 
        if choice == '2':
            import openapp2 
        elif choice == '3':
            import openapp3
        elif choice == '4':
            import openapp4
        elif choice == '5':
            import Calender
        elif choice == '6':
            import Time
        elif choice == '7':
            import Pong
        elif choice == '8':
            import GTSP
        elif choice == '9':
            import GTP
        elif choice == '10':
            import oldsoftware
        elif choice == '11':
            import cred
        elif choice == '801AB74':
            print ("Welcome To MLauncher 0.1! jk")
        elif choice == '12':
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
