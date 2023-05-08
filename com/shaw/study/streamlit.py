import streamlit as st
import pandas as pd

upload_files = st.file_uploader('Excel文件', type=['xlsx'])

if upload_files is None:
    st.stop()


@st.cache_data
def load_data(file):
    print("执行数据加载。。。")
    return pd.read_excel(file, None)


dfs = load_data(upload_files)

names = list(dfs.keys())
sheet_selects = st.multiselect('工作表', names, [])

if len(sheet_selects) == 0:
    st.stop()

tabs = st.tabs(sheet_selects)

for tab, name in zip(tabs, sheet_selects):
    with tab:
        df = dfs[name]
        st.dataframe(df)
