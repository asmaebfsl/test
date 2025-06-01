import pandas as pd
import altair as alt
import pydeck as pdk

def load_emdat_data():
    return pd.read_csv("emdat_data.csv")

def plot_disasters_by_year(df):
    chart = alt.Chart(df).mark_bar().encode(
        x='Year:O',
        y='count()',
        color='DisasterType:N',
        tooltip=['Year', 'DisasterType', 'count()']
    ).properties(title="Nombre de catastrophes par année")
    return chart

def plot_map(df):
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position='[Longitude, Latitude]',
        get_radius=100000,
        get_fill_color='[200, 30, 0, 160]',
        pickable=True
    )
    view_state = pdk.ViewState(latitude=20, longitude=0, zoom=2)
    return pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{Country}, {DisasterType}"})