import streamlit as st
import json
import requests

def main():
    st.title("Podcast Newsletter Dashboard")

    # Input fields
    rss_url = st.text_input("Enter Podcast RSS URL:")
    submit_button = st.button("Submit")

    if submit_button:
        # Call the backend API to process the podcast
        backend_url = "https://modal.com/apps/jsromerop/corise-podcast-project"  # Replace with your deployed backend URL
        data = {"url": rss_url}
        response = requests.post(backend_url, json=data)

        if response.status_code == 200:
            podcast_data = response.json()
            display_podcast_data(podcast_data)
        else:
            st.error("Error processing podcast. Please check the RSS URL.")

def display_podcast_data(data):
    st.subheader("Podcast Details")
    st.write("Podcast Title:", data['podcast_details']['podcast_title'])
    st.write("Episode Title:", data['podcast_details']['episode_title'])
    st.image(data['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

    st.subheader("Podcast Summary")
    st.write(data['podcast_summary'])

    st.subheader("Podcast Guest")
    st.write("Name:", data['podcast_guest']['name'])
    st.write("Summary:", data['podcast_guest']['summary'])

    st.subheader("Podcast Highlights")
    st.write(data['podcast_highlights'])

if __name__ == '__main__':
    main()
