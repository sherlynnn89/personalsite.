import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Xueying Huang</h4>
        <p>Recent Master's Graduate in Marketing<br>
        The Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:sherlyn.h815@outlook.com">sherlyn.h815@outlook.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    # 设置图片路径，使用相对路径而不是绝对路径
    image_path = "/Users/sherlynhuang/Desktop/IMG_1170.jpg"  # 使用绝对路径
    try:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            right_col.image(image, width=200)
        else:
            right_col.warning("图片文件不存在，请检查路径")
    except Exception as e:
        right_col.error(f"加载图片时出错: {str(e)}")
    st.markdown("---")

    st.markdown(
        """
        ### About Me
        Welcome to my personal website! I'm Sherlyn Huang, currently pursuing a Master of Science in Marketing with a concentration in Big Data at The Chinese University of Hong Kong (CUHK). My academic journey began at The University of Queensland (UQ), where I earned a Bachelor of Commerce in Business Information System. I'm passionate about leveraging data to drive marketing strategies and uncovering insights that can lead to business growth.
        """
    )
    st.markdown(
        """
        ### Skills
        - **Marketing & Strategy:** Brand alignment, community engagement, cross-cultural marketing, CRM client value analysis, customer conversion analysis
        - **Product Management:** Web scraping, mixed logit modeling, project delivery support, talent pipeline development, AI/LLM talent mapping
        - **Data Analysis:** Python (web scraping), SQL, Excel, conjoint analysis, descriptive/inferential statistics
        - **Language Skills:** English (fluent), Cantonese (native), Mandarin (native)
        - **Office & Tools:** Microsoft Office Suite, LinkedIn, Google Analytics, CRM systems, academic databases
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 