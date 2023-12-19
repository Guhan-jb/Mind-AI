import json
import streamlit as st
import matplotlib.pyplot as plt

def graph():
    # Read the JSON file
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    # Sort the data by score in descending order
    data.sort(key=lambda x: x["score"], reverse=True)

    # Extract the top 10 names and scores
    top_names = [item["name"] for item in data[:10]]
    top_scores = [item["score"] for item in data[:10]]

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(top_scores, labels=top_names, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Add a title
    ax.set_title("Mood graph")

    # Display the pie chart using Streamlit
    st.pyplot(fig)
