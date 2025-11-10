import requests
import pandas as pd
from datetime import datetime, timedelta


def fetch_weather_data(lat=59.33, lon=18.06):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "timezone": "Europe/Stockholm",
    }

    try:
        respons = requests.get(url, params=params).json()
        df = pd.DataFrame(
            {
                "time": pd.to_datetime(respons["hourly"]["time"]),
                "temperature": respons["hourly"]["temperature_2m"],
            }
        )
        return df

    except requests.exceptions.ConnectTimeout as e:
        print(f"Connection timeout: {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

    except requests.exceptions.InvalidJSONError as e:
        print(f"Incorrect format: {e}")
        return None

    except KeyError as e:
        print(f"Key error: {e}")
        return None


def process_weather_data(df):
    now = datetime.now()
    next_24h = now + timedelta(hours=24)

    if df is not None and not df.empty:

        try:
            df_24 = df[(df["time"] >= now) & (df["time"] <= next_24h)].reset_index()
            df_24 = df_24.drop(["index"], axis=1)

            return df_24
        except Exception as e:
            print(f"Error: {e}")
            return None
    else:
        print("Error occured: no data shown")
        return None


if __name__ == "__main__":
    df = fetch_weather_data()
    process_weather_data(df)