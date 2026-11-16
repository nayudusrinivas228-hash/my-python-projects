import requests
url = "https://openexchangerates.org/"
try:
    # Get user input
    amount = float(input("Enter Amount: "))
    from_currency = input("Convert From (USD): ").upper()
    to_currency = input("Convert To (INR): ").upper()
    # Validate amount
    if amount <= 0:
        print("Please enter an amount greater than zero!")
    else:
        # Get exchange rate
        params = {
            "base": from_currency,
            "quote": to_currency
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Extract exchange rate
        rate = data["rate"]
        # Currency conversion
        converted_amount = amount * rate
        # Display result
        print("\n===== CURRENCY CONVERTER =====")
        print("Original Amount:", amount, from_currency)
        print("Exchange Rate:", rate)
        print("Converted Amount:",
              round(converted_amount, 2), to_currency)
except ValueError:
    print("Please enter a valid amount!")
except requests.exceptions.RequestException as e:
    print("API Connection Error:", e)
except (KeyError, TypeError):
    print("Invalid API response!")
    