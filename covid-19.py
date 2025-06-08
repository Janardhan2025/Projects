import requests
import time
from win10toast import ToastNotifier

def update():
    toast = ToastNotifier()
    while True:
        try:
            r = requests.get('https://disease.sh/v3/covid-19/all')
            data = r.json()
            text = f'🌍 Global COVID-19 Update:\n\nConfirmed: {data["cases"]}\nDeaths: {data["deaths"]}\nRecovered: {data["recovered"]}'

            toast.show_toast("Covid-19 Updates", text, duration=20)

        except Exception as e:
            toast.show_toast("Error", f"Failed to fetch data:\n{e}", duration=10)

        time.sleep(60)  # Wait 1 minute before next update

update()
