import streamlit as st
from PIL import Image

# 標題
st.markdown(
    "<h1 style='text-align: center;'>🎉 35歲生日快樂 🎉</h1>", unsafe_allow_html=True
)

# 固定照片
image_path = "Steven.PNG"  # 確保圖片檔案位於專案資料夾內
image = Image.open(image_path)
st.image(image, caption="你的生日照片！", use_column_width=True)

# 自訂祝福訊息
st.subheader("輸入你的祝福訊息")
message = st.text_area("糖糖大家在這輸入祝福", "祝你生日快樂，年年有今日，歲歲有今朝！")

# 顯示祝福卡
if st.button("生成生日祝福卡"):
    st.markdown("## 🎂 你的生日祝福卡 🎂")
    st.image(image, use_column_width=True)
    st.markdown(f"### {message}")
    st.balloons()

# 頁尾
st.write("---")