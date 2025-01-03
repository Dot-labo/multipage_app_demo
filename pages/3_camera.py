import streamlit as st

st.set_page_config(page_icon="📷️", page_title="カメラをつかおう")
st.title("カメラを使おう")
st.camera_input(label="カメラ")