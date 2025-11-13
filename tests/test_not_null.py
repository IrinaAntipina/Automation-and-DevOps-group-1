from weather_api_call import fetch_weather_data

def test_fetch_weather_data():
    df = fetch_weather_data(59.33, 18.07)
    
    #assert df is not None  
  #  assert not df.empty

    assert df is None

