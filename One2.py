import pandas as pd
import streamlit as st
import s_calculate as sl
import s_plot as sp


st.set_page_config(layout = 'wide')

df = pd.read_csv('stocks_list.csv')

user_type = st.selectbox('Choose', ['Manual Search'] + list(df.columns))
if(user_type == 'Manual Search'):
	user_search = st.text_input('Search', '^NSEI')
else:
	user_search = st.selectbox('Stock', df[user_type].dropna())


user_wide = st.checkbox('Wide')

if(user_wide):
	sp.DIMS = (25, 20)
else:
	sp.DIMS = (12, 16)

st.title(user_search)

try:
	data = sl.download_data(stock = user_search)
	data_i = sl.all_indicators(data)

	mpl_fig_01 = sp.plot_01(data_i)
	st.pyplot(mpl_fig_01)
	pass
except:
	st.write('Error!')

