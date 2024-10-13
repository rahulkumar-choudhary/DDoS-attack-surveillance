import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container {
        background: #f9f9f9;
    }
    .stButton {
        background-color: #ff4757;
        color: white;
        border-radius: 5px;
        font-weight: bold;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    .stButton:hover {
        background-color: #ff6b81;
    }
    .header {
        text-align: center;
        color: #2f3542;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .subheader {
        color: #576574;
    }
</style>
""", unsafe_allow_html=True)

# Set the correct CSV file path after unzipping
csv_file = r"C:\Users\admin\Downloads\DDoS-Dataset.csv"

def convert_datetime(datetime_str):
    datetime_str_cleaned = datetime_str.replace("Mountain Daylight Time", "").strip()
    return pd.to_datetime(datetime_str_cleaned, format='%d-%b %Y %H:%M:%S.%f', errors='coerce')

@st.cache_data
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    if 'frame.time' in data.columns:
        data['frame.time'] = data['frame.time'].apply(convert_datetime)
    return data

data = load_data(csv_file)

# Sidebar for navigation and filtering
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page:", ["Overview", "Metrics", "Visualizations", "Download"])

if page == "Overview":
    st.title('🌐 DDoS Attack Analytics Dashboard 🌐')
    st.write('## Dataset Overview')
    st.write(data.head())

elif page == "Metrics":
    st.title('📊 Key Metrics 📊')
    total_attacks = data[data['Label'] == 'DDoS'].shape[0]
    unique_ips = data['ip.src'].nunique()
    st.write(f"Total DDoS Attacks: {total_attacks} 🎯")
    st.write(f"Unique Source IPs: {unique_ips} 🌟")

elif page == "Visualizations":
    st.title('🎨 DDoS Attack Visualizations 🎨')

    # Date range filter
    start_date = st.date_input("Start Date", pd.to_datetime(data['frame.time']).min())
    end_date = st.date_input("End Date", pd.to_datetime(data['frame.time']).max())

    # Filter data based on the selected date range
    filtered_data = data[(data['frame.time'] >= pd.Timestamp(start_date)) & (data['frame.time'] <= pd.Timestamp(end_date))]

    # DDoS Attacks Over Time
    attack_over_time = filtered_data.groupby('frame.time')['Label'].value_counts().unstack().fillna(0)
    if 'DDoS' in attack_over_time.columns:
        fig = px.line(attack_over_time, x=attack_over_time.index, y='DDoS', title='DDoS Attacks Over Time', 
                      labels={'frame.time': 'Time', 'DDoS': 'Number of Attacks'},
                      color_discrete_sequence=['#ff4757'])  # Custom color
        st.plotly_chart(fig)
    else:
        st.write("No DDoS attacks found in the selected date range. 🕵️‍♂️")

    # Top Source IPs Initiating DDoS Attacks
    top_sources = filtered_data[filtered_data['Label'] == 'DDoS']['ip.src'].value_counts().head(10)
    st.bar_chart(top_sources)

    # Protocol Distribution During Attacks
    st.write('### Protocol Distribution During Attacks')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=filtered_data, x='ip.proto', hue='Label', palette='viridis', ax=ax)
    ax.set_title('Protocol Distribution During Attacks')
    st.pyplot(fig)

elif page == "Download":
    st.title('💾 Download Data 💾')
    download_option = st.selectbox("Select Download Option:", ["CSV", "Visualization"])
    
    if download_option == "CSV":
        st.download_button(
            label="Download CSV",
            data=data.to_csv(index=False).encode('utf-8'),
            file_name='DDoS_Dataset.csv',
            mime='text/csv'
        )
    
    elif download_option == "Visualization":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data[data['Label'] == 'DDoS']['frame.len'], label='DDoS', color='red', kde=True, ax=ax)
        ax.set_title('Packet Size Distribution')
        st.pyplot(fig)
        st.download_button(
            label="Download Visualization",
            data=fig_to_image(fig),
            file_name='DDoS_Packet_Size_Distribution.png',
            mime='image/png'
        )

st.write('## Insights and Conclusions')
st.write("From the analysis, we can observe that specific IPs frequently initiate attacks, and certain protocols are more common during attacks.")
