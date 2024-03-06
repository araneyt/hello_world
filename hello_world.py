# Streamlit hello world app
import streamlit as st
import pandas as pd

def main():
    st.title('Das ist die Übung von der KW9')
    st.subheader(" Textelement in Form einer Caption")
    st.write('This is a simple hello world app in Streamlit.')
    st.metric(label="Temperatur", value="70 °C", delta="3 °C")
    st.write('To run this app, use the following command:')
    st.code('streamlit run hello_world.py')
data = pd.read_csv("death-rate-from-suicides-gho(1).csv")
st.dataframe(data)
st.write("Das zweite Element ist eine DataFrame")
st.area_chart(data=data, x="Entity" , y="Year")
st.write("Das dritte Element ist ein Chart Element")

choice = st.selectbox('Welches ist deiner Meinung nach das Gemüse des Monates?', 
                      ['Topinambur', 'Pak Choi', 'Okra', 'Schwammgurke', 'Bittermelone'],
                      key="gemuese_selectbox")
st.write('Das vierte Element ist ein Input Widgets')
choice = st.sidebar.selectbox('Welches ist deiner Meinung nach das Gemüse des Monates?', 
                              ['Topinambur', 'Pak Choi', 'Okra', 'Schwammgurke', 'Bittermelone'],
                              key="gemuese_selectbox_2")
st.write("Das fünfte Element ist ein Sidebar")
if 'x' not in st.session_state:
    st.session_state['x'] = 0

button = st.button('Increment x by 1')

if button:
    st.session_state['x'] += 1
    st.write ('x:', st.session_state['x'])
if __name__ == '__main__':
    main()
