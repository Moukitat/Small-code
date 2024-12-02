def contribution():
    try:
        contributed_today = input("Have you contributed today? (yes/no): ").strip().lower()
        
        if contributed_today == "yes":
            previous_amount = float(input("Previous amount: "))
            contributed_amount = float(input("Enter the contributed amount: "))
            
            total_amount = previous_amount + contributed_amount
            print(f"The new total amount is: {total_amount}")
        
        elif contributed_today == "no":
            previous_amount = float(input("Previous amount: "))
            print(f"Your total amount remains: {previous_amount}")
        
        else:
            print("Input error")
    
    except ValueError:
        print("Error: Please enter valid numbers for the amounts.")

contribution()
