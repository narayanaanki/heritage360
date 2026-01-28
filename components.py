import streamlit as st
import pandas as pd


# ============================================================
# TITLE BANNER
# ============================================================

def render_title_banner():
    st.markdown("""
    <div class="main-title-container">
        <div class="main-title">
            <span class="main-title-gradient">HERITAGE 360</span>
            <span class="main-title-flag">INDIA</span>
        </div>
        <div class="subtitle">Preserving India's Rich Cultural Legacy</div>
        <div class="subtitle-italic">
            A Digital Initiative for Heritage Conservation
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# WELCOME / INTRO BOX
# ============================================================

def render_welcome_box():
    st.markdown("""
    <div class="info-box">
        <h3>Welcome to HERITAGE360 – Indian Heritage</h3>
        <p>
        Explore and manage India's rich cultural heritage through our
        comprehensive digital platform.
        </p>
        <p>
        From UNESCO World Heritage Sites to protected monuments and
        archaeological treasures, HERITAGE360 aims to preserve,
        promote, and digitally document India's legacy spanning over
        <b>5,000 years of civilization</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# STATS COUNTERS
# ============================================================

def render_stats_counters():
    st.markdown("""
    <div class="stats-container">
        <div class="stat-item">
            <div class="stat-number">42</div>
            <div class="stat-label">UNESCO Sites</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">3,650+</div>
            <div class="stat-label">Protected Monuments</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">29</div>
            <div class="stat-label">States Covered</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">5,000+</div>
            <div class="stat-label">Years of History</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FEATURE CARDS
# ============================================================

def render_feature_cards():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card feature-orange">
            <h2>🏛️</h2>
            <h3>UNESCO Sites</h3>
            <p>
            Complete and searchable database of India’s
            UNESCO World Heritage Sites.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card feature-green">
            <h2>🏰</h2>
            <h3>ASI Monuments</h3>
            <p>
            Detailed records of more than 3,650
            protected monuments across India.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card feature-blue">
            <h2>💾</h2>
            <h3>Digital Preservation</h3>
            <p>
            Digital archiving, virtual tours,
            and future-ready heritage conservation.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# UNESCO TABLE
# ============================================================

def render_unesco_table(df: pd.DataFrame):
    if df.empty:
        st.warning("No UNESCO data available.")
        return

    st.dataframe(
        df,
        column_config={
            "name": "Site Name",
            "state": "State / UT",
            "year": "Year Listed",
            "type": "Type",
            "category": "Category"
        },
        hide_index=True,
        use_container_width=True
    )


# ============================================================
# MONUMENTS GRID
# ============================================================

def render_monuments_grid(df: pd.DataFrame):
    if df.empty:
        st.warning("No monument data available.")
        return

    cols = st.columns(2)

    for idx, monument in enumerate(df.to_dict("records")):
        with cols[idx % 2]:
            status_class = (
                "status-protected"
                if monument["status"] == "Protected"
                else "status-endangered"
            )

            st.markdown(f"""
            <div class="heritage-card">
                <div class="heritage-name">{monument['name']}</div>
                <div class="heritage-location">
                    📍 {monument['city']}
                </div>
                <div class="heritage-location">
                    🏗️ {monument['architecture']} Architecture
                </div>
                <div class="heritage-location">
                    📅 Built: {monument['built']}
                </div>
                <div class="{status_class}">
                    {monument['status']}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

def render_footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-title">HERITAGE360 © 2023</div>
        <p>
        Indian Cultural Heritage Management System | Version 2.1.0
        </p>
        <p>
        In partnership with Archaeological Survey of India &
        Ministry of Culture, Government of India
        </p>
        <p>
        Data Sources: UNESCO, ASI, National Archives of India
        </p>
    </div>
    """, unsafe_allow_html=True)