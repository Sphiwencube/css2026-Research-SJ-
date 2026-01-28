import streamlit as st
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sphiwe Joseph Ncube | CV",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
h1, h2, h3 {
    color: #0a2540;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.tag {
    display: inline-block;
    background-color: #e6f0ff;
    color: #0047ab;
    padding: 6px 12px;
    border-radius: 20px;
    margin: 4px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("📌 Sphiwe Ncube")

    selected = option_menu(
        menu_title=None,
        options=["Profile", "Skills", "Projects", "Education", "Experience", "Certifications"],
        icons=["person", "tools", "folder", "book", "briefcase", "award"],
        default_index=0,
    )

    st.markdown("---")
    st.markdown("📍 **Pretoria, Gauteng**")
    st.markdown("📞 **+27 64 843 3178**")
    st.markdown("✉️ **hhjnucbe22@gmail.com**")
    st.markdown("💻 [GitHub](https://github.com/sphiwencube)")

# ---------------- PROFILE ----------------
if selected == "Profile":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.title("👨‍💻 Sphiwe Joseph Ncube")
    st.subheader("Graduate | Junior Data Analyst | Junior Software Developer | Junior Data Scientist")

    st.write("""
    Postgraduate student registered for 2026 with a Bachelor of Science in Mathematical Sciences, specialising in computational problem-solving, data analysis, and artificial intelligence.
    Strong foundation in Python, SQL, statistics, and software development, with academic and project-based experience in data-driven systems and machine learning. I'm willing contribute to innovative,
    technology-focused research and industry-aligned solutions.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif selected == "Skills":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🛠 Technical Skills")

    st.subheader("Programming")
    for skill in ["Python", "SQL", "Object-Oriented Programming"]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.subheader("Data & Analytics")
    for skill in ["Data Analysis", "Data Cleaning", "Data Visualization", "Statistical Analysis"]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.subheader("Tools")
    for tool in ["GitHub", "Visual Studio Code"]:
        st.markdown(f"<span class='tag'>{tool}</span>", unsafe_allow_html=True)

    st.subheader("Other")
    for other in ["Problem Solving", "Communication", "Remote Collaboration"]:
        st.markdown(f"<span class='tag'>{other}</span>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selected == "Projects":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📂 Projects")

    st.subheader("Small Business ERP System")
    st.write("""
    - Designed and developed a **full-stack ERP system** for small businesses  
    - Implemented **financial tracking, expense management, and profit analysis**  
    - Built an **appointment scheduling module**  
    - Applied database design principles for reporting and consistency  
    """)

    st.subheader("Data Analysis & Machine Learning Projects")
    st.write("""
    - Performed **exploratory data analysis (EDA)** on structured datasets  
    - Cleaned and transformed raw data  
    - Applied **machine learning algorithms** to identify trends and patterns  
    - Tools: Python, Pandas, NumPy, ML Libraries  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
elif selected == "Education":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🎓 Education")

    st.subheader("Sefako Makgatho Health Sciences University")
    st.write("""
    **Bachelor of Science in Mathematical Sciences**  
    Completed: **2025**

    Coursework:
    - Programming
    - Data Structures
    - Statistics
    - Linear Algebra
    - Data Analysis
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------
elif selected == "Experience":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("💼 Experience")

    st.subheader("Junior Data Analyst / Software Developer")
    st.caption("Academic & Project-Based Experience | 2023 – Present")

    st.write("""
    - Applied **Python, SQL, and statistical methods** to analytical problems  
    - Worked on **data analysis, machine learning, and full-stack projects**  
    - Collaborated using **GitHub** and followed structured development practices  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CERTIFICATIONS ----------------
elif selected == "Certifications":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🏆 Certifications")

    certifications = [
        "Microsoft AI Fluency Certification – Microsoft (2025)",
        "Introduction to Data Sciences – CISCO (2024)",
        "Ethical Hacking Certification – CISCO (2024)",
        "Data Science with R & Stata – ChiSquare (2024)"
    ]

    for cert in certifications:
        st.write(f"✔️ {cert}")

    st.markdown("</div>", unsafe_allow_html=True)
