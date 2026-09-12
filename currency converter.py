# Currency Converter

print("===== CURRENCY CONVERTER =====")

rates = {
    "USD": 95.56,
    "EUR": 111.50,
    "GBP": 128.20
}

print("\nAvailable currencies:")
print("USD - US Dollar")
print("EUR - Euro")
print("GBP - British Pound")
print("INR - Indian Rupee")

amount = float(input("\nEnter amount: "))
currency = input("Enter currency (USD/EUR/GBP): ").upper()

if currency in rates:
    inr = amount * rates[currency]
    print(f"{amount} {currency} = ₹{inr:.2f}")
elif currency == "INR":
    print(f"{amount} INR = ₹{amount:.2f}")
else:
    print("Invalid currency!")

print("\nThank you for using the Currency Converter!")