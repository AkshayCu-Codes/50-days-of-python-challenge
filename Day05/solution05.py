def my_discount():
    price= int(input("Please enter the original price: "))
    discount=int(input("Please enter the discount: "))
    return f'Final price will be {price*(100-discount)/100:.1f} after {discount} % discount!!'

print(my_discount())

# Output

# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge> python solution05.py"
# Please enter the original price: 100
# Please enter the discount: 15
# Final price will be 85.0 Price 15 % discount!!
# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge> python solution05.py"
# Please enter the original price: 150
# Please enter the discount: 15
# Final price will be 127.5 after 15 % discount!!