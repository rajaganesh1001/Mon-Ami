
import streamlit as st
import pandas as pd

st.set_page_config(page_title='NIFTY 50 Volatility Dashboard', layout='wide')
st.title('📊 NIFTY 50 Volatility Dashboard')

# Static metrics
st.subheader('Volatility Parameters')
st.markdown('**Yearly Closing Price:** ₹23645')
st.markdown('**India VIX:** 14.45')
st.markdown('**Trading Days:** 365')
st.markdown('**√Days:** 19')
st.markdown('**VIX / √Days:** 0.76')
st.markdown('**Daily Range Threshold:** ₹180')

# Tabular data
st.subheader('Daily Volatility Table')
data = {'Date': [Timestamp('2025-08-23 00:00:00'), Timestamp('2025-08-24 00:00:00'), Timestamp('2025-08-25 00:00:00'), Timestamp('2025-08-26 00:00:00'), Timestamp('2025-08-27 00:00:00'), Timestamp('2025-08-28 00:00:00'), Timestamp('2025-08-29 00:00:00'), Timestamp('2025-08-30 00:00:00'), Timestamp('2025-08-31 00:00:00'), Timestamp('2025-09-01 00:00:00')], 'High': [23680, 23690, 23650, 23630, 23620, 23610, 23600, 23590, 23580, 23570], 'Low': [23500, 23510, 23520, 23530, 23540, 23550, 23560, 23570, 23580, 23590], 'Range': [180, 180, 130, 100, 80, 60, 40, 20, 0, -20], 'Volatility Threshold': [180, 180, 180, 180, 180, 180, 180, 180, 180, 180], 'Compression': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.markdown('---')
st.markdown('Designed for expansion to include multiple indexes and stocks.')
