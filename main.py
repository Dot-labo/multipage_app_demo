import streamlit as st

if "name" not in st.session_state:
    st.session_state["name"] = ""

st.title("マルチページアプリのデモ")
st.header("ホームページ 🏠")
st.write("streamlitでは、 pages/ ディレクトリの下にあるpythonファイルはページとして使えるよ！")
st.write("左のページからいろいろ見てみよう！！")

name = st.text_input("名前を入力", value=st.session_state["name"])
st.session_state["name"] = name
st.write(f"あなたの名前は {st.session_state['name']} です。")