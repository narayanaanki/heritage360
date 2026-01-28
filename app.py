import streamlit as st
from styles import inject_global_styles
from data import (
    load_unesco_sites,
    load_monuments,
    load_map_data,
    load_heritage_story_videos,
    load_sign_language_videos,
    load_video_recordings
)
from components import (
    render_title_banner,
    render_welcome_box,
    render_stats_counters,
    render_feature_cards,
    render_unesco_table,
    render_monuments_grid,
    render_footer
)
from explorer import render_unesco_explorer, render_explorer_note

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HERITAGE360 - Indian Heritage",
    page_icon="🕌",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

st.session_state.setdefault("video_path", None)
st.session_state.setdefault("video_title", None)

# ============================================================
# GLOBAL UI
# ============================================================

inject_global_styles()
render_title_banner()

# ============================================================
# TABS
# ============================================================

tab_home, tab_explorer, tab_stories, tab_sign, tab_recordings = st.tabs(
    [
        "🏠 Home",
        "🖼️ Heritage Sites",
        "📖 Heritage Stories",
        "🤟 Sign Language Videos",
        "🎥 Video Recordings"
    ]
)

# ============================================================
# HOME TAB
# ============================================================

with tab_home:
    st.session_state.video_path = None
    st.session_state.video_title = None

    render_welcome_box()
    render_stats_counters()
    render_feature_cards()
    render_unesco_table(load_unesco_sites())

    st.markdown("### 🗺️ Heritage Sites Map")
    st.map(load_map_data()[["lat", "lon"]])

    render_monuments_grid(load_monuments())
    render_footer()

# ============================================================
# HERITAGE SITES TAB
# ============================================================

with tab_explorer:
    st.session_state.video_path = None
    st.session_state.video_title = None
    render_unesco_explorer()
    render_explorer_note()

# ============================================================
# HERITAGE STORIES TAB
# ============================================================

with tab_stories:
    st.markdown("## 📖 Heritage Stories – Video")
    for i, row in load_heritage_story_videos().iterrows():
        col1, col2 = st.columns([6, 2])
        col1.markdown(f"**🏛️ {row['site']}**")
        if col2.button("▶ Play", key=f"story_{i}"):
            st.session_state.video_path = row["video_path"]
            st.session_state.video_title = row["site"]

# ============================================================
# SIGN LANGUAGE VIDEOS TAB
# ============================================================

with tab_sign:
    st.markdown("## 🤟 Sign Language Videos")
    for i, row in load_sign_language_videos().iterrows():
        col1, col2 = st.columns([6, 2])
        col1.markdown(f"**🏛️ {row['site']}**")
        if col2.button("▶ Play", key=f"sign_{i}"):
            st.session_state.video_path = row["video_path"]
            st.session_state.video_title = row["site"]

# ============================================================
# VIDEO RECORDINGS TAB
# ============================================================

with tab_recordings:
    st.markdown("## 🎥 Video Recordings")
    for i, row in load_video_recordings().iterrows():
        col1, col2 = st.columns([6, 2])
        col1.markdown(f"**🎞️ {row['title']}**")
        if col2.button("▶ Play", key=f"rec_{i}"):
            st.session_state.video_path = row["video_path"]
            st.session_state.video_title = row["title"]

# ============================================================
# VIDEO POPUP
# ============================================================

if st.session_state.video_path:
    @st.dialog(f"🎬 {st.session_state.video_title}")
    def video_popup():
        st.video(st.session_state.video_path)
        if st.button("❌ Close"):
            st.session_state.video_path = None
            st.session_state.video_title = None
    video_popup()