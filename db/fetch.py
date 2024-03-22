import requests
from datetime import datetime

def fetch_data(house: str):
    allowed_houses = ['house', 'senate']
    if house not in allowed_houses:
        raise ValueError(f"Invalid house of congress. Expected one of {allowed_houses}")
    
    if house=='senate':
        response = requests.get("https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json")
    elif house=='house':
        response = requests.get("https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json")
    else:
        raise NameError

    if response.status_code != 200:
        print("request failed.")

    data = response.json()
    data.sort(key = lambda x: x['transaction_date'], reverse = True)
    #data.sort(key = lambda x: datetime.strptime(x['disclosure_date'], '%m/%d/%Y'), reverse=True)
    return data


if __name__=="__main__":
    

    senate_data = fetch_data('senate')
    house_data = fetch_data('house')

    
