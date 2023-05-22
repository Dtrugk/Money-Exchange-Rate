import requests
from requests.structures import CaseInsensitiveDict

apikey = "4L8TjKJMgrRZRIGk2j9rnaWAP6qoUUFyXkBGEEJT"

def Latest_Exchange_Rates():
    base = input("Enter the base currency: ")
    currency = input("Enter the currency you want to convert to: ")
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&base_currency={base}&currencies={currency}"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    return resp.json()

def Historical_Exchange_Rates():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    url = f"https://api.freecurrencyapi.com/v1/historical?base_currency=USD&date_from={start_date}&date_to={end_date}&apikey={apikey}"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    return resp.json()  

def main():
    print("Welcome to the Currency Exchange Rate Program")
    print("1. Latest Exchange Rates")
    print("2. Historical Exchange Rates")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(Latest_Exchange_Rates())
    elif choice == 2:
        print(Historical_Exchange_Rates())
    elif choice == 3:
        exit()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
