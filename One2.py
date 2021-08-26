import streamlit as st
import s_calculate as sl
import s_plot as sp


st.set_page_config(layout = 'centered')

st.title('One2')

user_stock = st.text_input('Stock', '^NSEI')

try:
	data = sl.download_data(stock = user_stock)
	data_i = sl.all_indicators(data)

	mpl_fig_01 = sp.plot_01(data_i)
	st.pyplot(mpl_fig_01)
except:
	st.write('Invalid symbol!')
