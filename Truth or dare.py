while True:
    game = input("Enter truth, dare or both (or type exit to stop): ").strip().lower()
    
    if game == "exit":
        print("Game ended. Bye!")
        break   

    choice = input("Enter your choice (from 1 to 5): ").strip()

    if game == "truth":
        print("Truth")
        
        if choice == "1":
            print("What is your salary?")
            print("20000")
        elif choice == "2":
            print("Who is your crush?")
            print("Rashmika")
        elif choice == "3":
            print("Are you in a relationship?")
            print("Maybe")
        elif choice == "4":
            print("What’s the last lie you told?")
            print("Passed interview")
        else:
            print("What’s the most childish thing you still do?")
            print("Chewing the thumb")

    elif game == "dare":
        print("Dare")
        
        if choice == "1":
            print("Propose anyone")
        elif choice == "2":
            print("Slap anyone")
        elif choice == "3":
            print("Prank anyone")
        elif choice == "4":
            print("Do your best celebrity impression")
        else:
            print("Call a random contact and sing 'Happy Birthday.'")

    elif game == "both":
        print("Truth and Dare Mix")

    else:
        print("Invalid input")

    print("\n--- Game Restarting ---\n")
