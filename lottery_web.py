import streamlit as st
import random

st.set_page_config(page_title="抽奖工具", page_icon="🎲")
st.title("🎁 幸运抽奖工具")

names = st.text_area("请输入参与抽奖的名单（每行一个名字）", height=200)
if names:
    name_list = [n.strip() for n in names.split("\n") if n.strip()]
    st.write(f"共 **{len(name_list)}** 人参与")

    if st.button("🎲 开始抽奖"):
        winner = random.choice(name_list)
        st.balloons()
        st.success(f"🏆 恭喜中奖者：**{winner}** 🎉")
else:
    st.info("请输入名单开始抽奖")
