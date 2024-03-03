def main():
    print("Welcome to Adaptify!")
    print("Are you ready for a new beginning?")
   
    answer = input("Enter 'yes' or 'no': ").lower()
   
    if answer == 'yes':
        educode = input("Please enter the edu-code: ")
        if educode == '123':
            print("\nInformation:")
            print("Country: USA")
            print("State: New Jersey")
            print("University: Princeton")
            print("Country of Origin: India")
            print("Monthly Credit: 5000 USD")
           
            confirm = input("Is this information correct? (Enter 'confirm' or 'edit'): ").lower()
            if confirm == 'confirm':
                print("\nThank you for confirming.")
                print("What can we help you with?")
                print("1. Financial Advisor")
                print("2. Language Barriers")
                print("3. Cultural Differences")
                print("4. Homesickness")
                print("5. Accommodation")
                print("6. Currency")
                print("7. Safety")
               
                help_with = input("Enter the number corresponding to your query: ")
                if help_with == '1':
                    print("\nAccording to your Monthly Credit:")
                    print("- Spend $2000 on rent and bills")
                    print("- Spend $500 on groceries")
                    print("- Spend $500 on entertainment")
                    print("- Spend $500 on clothes")
                    print("- Spend $500 on other wants")
                    print("- Save $1000")
                elif help_with == '2':
                    print("You selected Language Barriers.")
                elif help_with == '3':
                    print("You selected Cultural Differences.")
                elif help_with == '4':
                    print("You selected Homesickness.")
                elif help_with == '5':
                    print("You selected Accommodation.")
                elif help_with == '6':
                    print("You selected Currency.")
                elif help_with == '7':
                        print("Who is your top contact")
                if answer == '1234567890':
                        print("We will contact this number in case of emergencies")
            elif confirm == 'edit':
                print("Please edit your information.")
                # Add code to edit information if needed
            else:
                print("Invalid input. Please enter 'confirm' or 'edit'.")
        else:
            print("Invalid edu-code. Please try again.")
    elif answer == 'no':
        print("That's okay. Take your time. We'll be here when you're ready.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()