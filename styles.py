import streamlit as st


def inject_global_styles():
    st.markdown(
        """
        <style>

        /* ======================================================
           MAIN TITLE (STICKY HEADER – FIXED)
           ====================================================== */
        .main-title-container {
            position: sticky;
            top: 0;
            z-index: 50;
            background: linear-gradient(135deg, #0d47a1 0%, #1a237e 50%, #311b92 100%);
            padding: 30px 20px;
            border-radius: 15px;
            margin: 20px 0 30px 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            border: 3px solid #FFD700;
            text-align: center;
        }

        .main-title {
            color: #FFFFFF;
            font-size: 3.5rem;
            font-weight: 800;
            margin: 10px 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            letter-spacing: 1px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .main-title-gradient {
            background: linear-gradient(90deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            color: #FFD700;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 10px;
        }

        .subtitle-italic {
            font-style: italic;
            color: #E3F2FD;
            font-size: 1.2rem;
        }

        /* ======================================================
           STREAMLIT TABS FIX
           ====================================================== */
        div[data-testid="stTabs"] {
            margin-top: 25px;
            z-index: 10;
        }

        /* ======================================================
           INFO / WELCOME BOX
           ====================================================== */
        .info-box {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            border-radius: 20px;
            padding: 30px;
            margin: 25px 0;
            border-left: 6px solid #1a237e;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        }

        .info-box h3 {
            margin-top: 0;
            color: #1a237e;
            font-weight: 700;
        }

        .info-box p {
            color: #263238;
            font-size: 1.05rem;
            line-height: 1.6;
        }

        /* ======================================================
           FEATURE CARDS
           ====================================================== */
        .feature-card {
            background: linear-gradient(145deg, #ffffff 0%, #f5f5f5 100%);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
        }

        .feature-orange { border-top: 6px solid #FF9933; }
        .feature-green  { border-top: 6px solid #138808; }
        .feature-blue   { border-top: 6px solid #0d6efd; }

        /* ======================================================
           STATS CARDS
           ====================================================== */
        .stats-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            background: #f7f9fb;
            border-radius: 18px;
            border: 2px solid #e0e5ec;
            padding: 30px 10px;
            margin: 40px 0;
        }

        .stat-item {
            text-align: center;
            position: relative;
            padding: 10px 5px;
        }

        .stat-item:not(:last-child)::after {
            content: "";
            position: absolute;
            right: 0;
            top: 15%;
            height: 70%;
            width: 1px;
            background-color: #cfd8dc;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            color: #1a237e;
        }

        .stat-label {
            font-size: 1rem;
            color: #607d8b;
        }

        /* ======================================================
           HERITAGE CARDS
           ====================================================== */
        .heritage-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 22px;
            border: 2px solid #e0e0e0;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            margin-bottom: 24px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .heritage-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 35px rgba(0, 0, 0, 0.12);
        }

        /* ======================================================
           HERITAGE SITE TITLE (EXPLORER)
           ====================================================== */
        .heritage-title {
            font-size: 26px;
            font-weight: 800;
            color: #8B0000;
            margin-bottom: 10px;
        }

        /* ======================================================
           FOOTER
           ====================================================== */
        .footer {
            margin-top: 60px;
            padding: 30px 20px;
            background: linear-gradient(135deg, #f7f9fb 0%, #eef2f7 100%);
            border-top: 3px solid #1a237e;
            border-radius: 16px 16px 0 0;
            text-align: center;
        }

        @media (max-width: 900px) {
            .stats-container {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 480px) {
            .stats-container {
                grid-template-columns: 1fr;
            }
            .main-title {
                font-size: 2.5rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )
