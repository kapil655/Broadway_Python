import requests
def sector_performance():
    url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

    r = requests.get(url=url)

    if r.status_code == 200:
        data = r.json()
        response = data['response']

        positive = []
        negative = []

        for item in response:
            if item['points_change'] < 0:
                negative.append(item['indices'])
            else:
                positive.append(item['indices'])

        print("positive------------>", len(positive))
        print("negative------------>", len(negative))
        


while True:
    print("\n===== MENU =====")
    print("1. Premier League Teams")
    print("2. Sector Performance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        premier_league_teams()

    elif choice == "2":
        sector_performance()

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Try again.")