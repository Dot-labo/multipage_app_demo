import streamlit as st

st.set_page_config(page_icon="🎈", page_title="風船で遊ぼう")
st.title("風船を飛ばそう!")

if "name" not in st.session_state:
    st.session_state["name"] = ""

if st.button("ボタンを押してみよう！"):
    st.balloons()
    if st.session_state.name:
        st.write(f"{st.session_state.name} さん、おめでとう！")

