from weather_api_call import fetch_weather_data
import pandas as pd

def test_fetch_weather_data():
    df = fetch_weather_data(59.33, 18.07)

    assert isinstance(df, pd.DataFrame)

    assert 'time' in df.columns
    assert 'temperature' in df.columns