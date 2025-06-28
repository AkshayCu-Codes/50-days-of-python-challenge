def your_vat():

    while True:
        try:
            price=float(input("Enter the price of an item: "))
            vat=float(input("Enter VAT (%): "))
            break
        except ValueError:
            print("Please enter valid numbers for price and VAT.")
    
    vat_amount=price*(vat/100)
    total_price=price+vat_amount

    print(f"Total price including VAT is: {total_price:.2f}")

your_vat()