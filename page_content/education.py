import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing (Big Data)
    **The Chinese University of Hong Kong** | *August 2024 - October 2025*
    
    - GPA: 3.6/4.0
    - Award: Outstanding Student Award 2024 with President's Commendation Letter
    - Relevant Coursework: Marketing Research, Marketing Analytics, Machine Learning in Marketing, Customer Analytics, Business Negotiation

    
    ### Bachelor of Commerce in Business Information System
    **The University of Queensland** | *February 2021 - July 2024*
    
    - GPA: 6.25/7
    - Graduated with Dean's List 2024 - Top 10% Business School Students
    - Relevant Coursework: Database Systems, Computer Networks, Business Information System, Financial Analysis, Business Statistics, Business Communication
    """)
    
    st.markdown("---")
    

    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Baidu Netdisk AI Optimization Initiative 
    **<span style="font-size: 0.9em;">CUHK</span> (Sep 2024 - Feb 2025)**
    - Engineered web scraper harvesting 7,000+ iOS App Store reviews, pinpointing low download speed as root cause for 63.7% negative feedback
    - Conducted conjoint analysis revealing 23% choice probability increase per 10% speed boost (p<0.01) through mixed logit modeling
    
    ### Jellycat New Product Line Market Research & Development Analysis
    **<span style="font-size: 0.9em;">CUHK</span> (Aug 2024 - Nov 2024)**
    - Conducted comprehensive market research using Likert scales and focus groups to collect quantitative consumer preference data and in-depth target audience feedback
    - Performed statistical analysis using ANOVA and regression methods to identify market trends and consumer behavior patterns, providing data-driven insights for product development
    - Developed strategic recommendations and authored detailed market research report outlining key product development directions and innovative market differentiation strategies
    """, unsafe_allow_html=True)
    
    st.markdown("---") 