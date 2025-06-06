import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Algorithm Recruitment Specialist
    **ByteDance** | *April 2025 - Now*
    
    - Collaborate with local universities and research institutions to establish a strong algorithm talent pipeline
    - Source and screen algorithm talent, conduct technical assessments to match candidates with ByteDance's project requirements
    - Work closely with recruitment teams across Asia Pacific regions to ensure consistent hiring strategies and facilitate knowledge sharing
    """)
    
    st.markdown("""
    ### Researcher Intern
    **Michael Page** | *July 2024 – September 2024*
    
    - Mapped APAC - wide talent for AI/LLM roles, built candidate database via LinkedIn and email, identified 18 - 22% salary premium range for LLM engineer’s vs traditional algorithm role
    - Built global talent network across 50+ institutes through academic - industrial data fusion, established ETH Zurich as the premier robotics talent pipeline for industrial applications
    - Identified 10 key academic hubs through publication analysis (e.g., CVPR/ICRA 2023 - 24)
    - Assisted in building Singapore - based cross - cultural team, resolving language barriers
    """)
    
    st.markdown("""
    ### Sales Associate
    **T - Mate Mobile Accessories** | *September 2023 - February 2024*
    
    - Participated in launching cross - border training initiative with cultural adaptation guides
    - Assisted in developing CRM client value analysis system, boosting strategic accounts' revenue share
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Campus Partner at OfferMate",
            "description": "Startup project focused on career development services for university students.",
            "skills": ["Market Research", "User Experience", "Strategic Partnership", "Data Analysis"],
            "outcome": "Successfully established long-term partnership with CUHK Career Center and improved product features based on user feedback."
        },
        {
            "title": "Lululemon Omnichannel Marketing Simulation",
            "description": "Virtual experience program focused on marketing strategy and analytics for MIRROR fitness platform.",
            "skills": ["Marketing Strategy", "Data Analysis", "ROI Analysis", "Brand Management"],
            "outcome": "Developed comprehensive marketing plan with data-driven strategies, analyzing key metrics including conversion rates, CAC, and ROI."
        },
        {
            "title": "Varsity Athlete - CUHK Taekwondo Team",
            "description": "Represented The Chinese University of Hong Kong in competitive Taekwondo.",
            "skills": ["Team Leadership", "Physical Training", "Competition Strategy", "Time Management"],
            "outcome": "Led women's team to overall championship and secured third place in individual category at Hong Kong Taekwondo University Competition."
        },
        {
            "title": "Volunteer at I-Care Centre",
            "description": "Engaged with senior citizens through recreational activities and support services.",
            "skills": ["Event Planning", "Senior Care", "Communication", "Community Service"],
            "outcome": "Successfully organized Finnish Game sessions and social activities, managed communication platform for 10 seniors, ensuring prompt assistance and engagement."
        }
    ]
    
    # 添加这段代码来显示项目
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")


    

    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL
        - **Computer:** Microsoft Word, Excel, and PowerPoint, Google Analytics
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Language:** Cantonese (native), Mandarin (native), English (fluent)
        """)
    
    st.markdown("---") 