def main_menu():
    while True:
        print("===Games===")
        print("1.Guess The Password")
        print("2.Pong")
        print("3.Exit")
        choice = input("Enter the number corresponding to your choice: ")
        
        if choice == '1':
            import Software      
        if choice == '2':
            import Pong
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
