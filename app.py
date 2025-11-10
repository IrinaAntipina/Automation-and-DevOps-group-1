import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from weather_api_call import process_weather_data, fetch_weather_data
import matplotlib.ticker as mticker

st.title("Temperature Next 24 Hours – Open-Meteo")

cities = {
    "Stockholm": (59.33, 18.07),
    "Oxelösund": (58.67, 17.10),
    "Saint Petersburg": (59.57, 30.19),
    "Tashkent": (41.18, 69.16),
}

city = st.selectbox("Select city", list(cities.keys()))
lat, lon = cities[city]

df = fetch_weather_data(lat, lon)

df_24 = process_weather_data(df)

if df_24 is not None:

    df_24 = df_24.copy()
    df_24["time"] = df_24["time"].dt.strftime("%Y-%m-%d %H:%M")

    st.subheader(f"Temperature data for {city} (next 24 hours)")
    st.dataframe(df_24, hide_index=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_24["time"], df_24["temperature"], color="tab:blue", marker="o")
    ax.set_title(f"Temperature for the next 24 hours in {city}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)
    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.5))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

else:
    st.subheader(f"Temperature data for {city} (next 24 hours)")

    st.error(
        "No available temperature data for the next 24 hours.\n"
        "Try reloading the page or try later."
    )

    empty_df = pd.DataFrame({"time": [], "temperature": []})
    st.dataframe(empty_df, hide_index=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title(f"No Temperature Data – {city}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.text(
        0.5,
        0.5,
        "No data\navailable",
        fontsize=14,
        ha="center",
        va="center",
        transform=ax.transAxes,
    )
    ax.grid(True)

    st.pyplot(fig)