import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = "/Users/sherlynhuang/Desktop/Sherlyn_CV_hr.pdf"

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Sherlyn_Huang_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Sherlyn (Xueying) Huang")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** sherlyn.h815@outlook.com
    - **Student ID:** 64858371
    - **Location:** NOL(IANG)
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *Aug 2024 - Oct 2025*
    - GPA: 3.62/4.0
    - Outstanding Student Award 2024 with President's Commendation Letter

    **Bachelor of Commerce in Business Information System**
    - The University of Queensland
    - *Feb 2022 - Jul 2024*
    - GPA: 6.25/7.0
    - Dean's List 2024 - Top 10% Business School Students
    """)

    st.header("Professional Experience")
    st.markdown("""
    **Researcher Intern, Michael Page** - Shenzhen, China
    - *Jul 2024 – Sep 2024*
    - Mapped APAC-wide talent for AI/LLM roles, building candidate database via LinkedIn and email
    - Identified 18-22% salary premium range for LLM engineers vs traditional algorithm roles
    - Built global talent network across 50+ institutes through academic-industrial data fusion
    - Established ETH Zurich as the premier robotics talent pipeline for industrial applications
    
    **Sales Associate, T-Mate Mobile Accessories** - Brisbane, Australia
    - *Sep 2023 - Feb 2024*
    - Participated in launching cross-border training initiative with cultural adaptation guides
    - Assisted in developing CRM client value analysis system, boosting strategic accounts' revenue share
    
    **Human Resources Intern, Zhongshan Broadcasting & Television** - Zhongshan, China
    - *May 2023 - Jun 2023*
    - Analyzed employee performance data to identify retention trends and inform HR strategies
    - Optimized workforce allocation through Excel-based employee performance analysis
    
    **Consultant Intern, Michael Page** - Shenzhen, China
    - *Nov 2021 - Jul 2022*
    - Assisted in closing 2 key placements: AI Director & Senior Engineer for client's critical project
    - Participated in full-cycle recruitment for tech roles including sourcing, screening, and negotiations
    """)

    st.header("Projects")
    st.markdown("""
    **Baidu Netdisk AI Optimization Initiative – CUHK**
    - *Sep 2024 - Feb 2025*
    - Engineered web scraper harvesting 7,000+ iOS App Store reviews
    - Identified low download speed as root cause for 63.7% negative feedback
    - Conducted conjoint analysis revealing 23% choice probability increase per 10% speed boost

    **Lululemon Omnichannel Marketing Simulation - Forage, Australia**
    - *Sep 2023*
    - Developed integrated marketing plan for MIRROR platform focusing on brand alignment
    - Analyzed customer conversion rates, acquisition costs, and ROI
    - Implemented data-driven strategies for enhanced brand promotion
    """)

    st.header("Skills")
    st.markdown("""
    - **Languages:** Cantonese (Native), Mandarin (Native), English (Fluent)
    - **Technical:** SQL, Python, R, Google Analytics
    - **Software:** Microsoft Office Suite (Word, Excel, PowerPoint)
    """)

    st.markdown("---")
