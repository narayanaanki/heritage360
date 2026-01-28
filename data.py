import pandas as pd
import os

# ============================================================
# BASE DIRECTORY (PROJECT ROOT)
# ============================================================

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

IMAGE_DIR = os.path.join(ASSETS_DIR, "images", "unesco")
SIGN_VIDEO_DIR = os.path.join(ASSETS_DIR, "videos", "sign")
STORY_VIDEO_DIR = os.path.join(ASSETS_DIR, "videos", "stories")

def asset_path(*paths):
    """
    Build OS-independent path inside assets folder
    """
    return os.path.join(ASSETS_DIR, *paths)

# ============================================================
# UNESCO WORLD HERITAGE SITES DATA
# ============================================================

def load_unesco_sites():
    data = [
        {"name": "Taj Mahal", "state": "Uttar Pradesh", "year": 1983, "type": "Cultural", "category": "Mughal Architecture"},
        {"name": "Qutub Minar", "state": "Delhi", "year": 1993, "type": "Cultural", "category": "Indo-Islamic Architecture"},
        {"name": "Red Fort", "state": "Delhi", "year": 2007, "type": "Cultural", "category": "Mughal Fort"},
        {"name": "Sun Temple, Konark", "state": "Odisha", "year": 1984, "type": "Cultural", "category": "Temple Architecture"},
        {"name": "Group of Monuments at Hampi", "state": "Karnataka", "year": 1986, "type": "Cultural", "category": "Vijayanagara Empire"},
        {"name": "Ajanta Caves", "state": "Maharashtra", "year": 1983, "type": "Cultural", "category": "Rock-cut Architecture"},
        {"name": "Ellora Caves", "state": "Maharashtra", "year": 1983, "type": "Cultural", "category": "Rock-cut Architecture"},
        {"name": "Great Living Chola Temples", "state": "Tamil Nadu", "year": 1987, "type": "Cultural", "category": "Chola Architecture"},
        {"name": "Khajuraho Group of Monuments", "state": "Madhya Pradesh", "year": 1986, "type": "Cultural", "category": "Temple Architecture"},
        {"name": "Mahabodhi Temple", "state": "Bihar", "year": 2002, "type": "Cultural", "category": "Buddhist Architecture"}
    ]
    return pd.DataFrame(data)

# ============================================================
# PROTECTED MONUMENTS DATA
# ============================================================

def load_monuments():
    data = [
        {"name": "Victoria Memorial", "city": "Kolkata", "built": 1921, "architecture": "Indo-Saracenic", "status": "Protected"},
        {"name": "Gateway of India", "city": "Mumbai", "built": 1924, "architecture": "Indo-Saracenic", "status": "Protected"},
        {"name": "India Gate", "city": "Delhi", "built": 1931, "architecture": "War Memorial", "status": "Protected"},
        {"name": "Charminar", "city": "Hyderabad", "built": 1591, "architecture": "Islamic", "status": "Protected"},
        {"name": "Jaisalmer Fort", "city": "Jaisalmer", "built": 1156, "architecture": "Rajput", "status": "Protected"},
        {"name": "Mysore Palace", "city": "Mysore", "built": 1912, "architecture": "Indo-Saracenic", "status": "Protected"},
        {"name": "Sanchi Stupa", "city": "Sanchi", "built": "3rd Century BCE", "architecture": "Buddhist", "status": "Protected"},
        {"name": "Brihadeeswarar Temple", "city": "Thanjavur", "built": 1010, "architecture": "Chola", "status": "Protected"}
    ]
    return pd.DataFrame(data)

# ============================================================
# MAP DATA
# ============================================================

def load_map_data():
    data = [
        {"city": "Delhi", "lat": 28.6139, "lon": 77.2090},
        {"city": "Agra", "lat": 27.1751, "lon": 78.0421},
        {"city": "Hampi", "lat": 15.2993, "lon": 76.4071},
        {"city": "Mumbai", "lat": 18.9217, "lon": 72.8332},
        {"city": "Jaisalmer", "lat": 26.9157, "lon": 70.9083},
        {"city": "Mysore", "lat": 12.2958, "lon": 76.6394},
        {"city": "Ajanta", "lat": 20.5519, "lon": 75.7033},
        {"city": "Thanjavur", "lat": 10.7867, "lon": 79.1378}
    ]
    return pd.DataFrame(data)

# ============================================================
# REQUIRED BY explorer.py
# ============================================================

def get_unesco_images():
    return {
        "Taj Mahal": {"image": os.path.join(IMAGE_DIR, "taj_mahal.jpg")},
        "Qutub Minar": {"image": os.path.join(IMAGE_DIR, "qutub_minar.jpg")},
        "Red Fort": {"image": os.path.join(IMAGE_DIR, "red_fort.jpg")},
        "India Gate": {"image": os.path.join(IMAGE_DIR, "india_gate.jpg")},
        "Gateway of India": {"image": os.path.join(IMAGE_DIR, "gateway_of_india.jpg")},
        "Fatehpur Sikri": {"image": os.path.join(IMAGE_DIR, "fatehpur_sikri.jpg")},
        "Mysore Palace": {"image": os.path.join(IMAGE_DIR, "mysore_palace.jpg")},
        "Sanchi Stupa": {"image": os.path.join(IMAGE_DIR, "sanchi_stupa.jpg")},
        "Victoria Memorial": {"image": os.path.join(IMAGE_DIR, "victoria_memorial.jpg")},
        "Shaniwar Wada": {"image": os.path.join(IMAGE_DIR, "shaniwar_wada.jpg")},
        "Lal Mahal": {"image": os.path.join(IMAGE_DIR, "lal_mahal.jpg")},
        "Sinhagad Fort": {"image": os.path.join(IMAGE_DIR, "sinhagad_fort.jpg")}
    }

# ============================================================
# SIGN LANGUAGE VIDEOS
# ============================================================

def load_sign_language_videos():
    return pd.DataFrame([
        {
            "site": "Taj Mahal",
            "language": "Indian Sign Language",
            "video_path": os.path.join(SIGN_VIDEO_DIR, "tajmahal.mp4")
        }
    ])

# ============================================================
# HERITAGE STORY VIDEOS
# ============================================================

def load_heritage_story_videos():
    return pd.DataFrame([
        {
            "site": "Taj Mahal",
            "video_path": os.path.join(STORY_VIDEO_DIR, "TahmahalSite.mp4")
        },
        {
            "site": "Red Fort",
            "video_path": os.path.join(STORY_VIDEO_DIR, "red_fort_story.mp4")
        }
    ])

# ============================================================
# VIDEO RECORDINGS TAB
# ============================================================

def load_video_recordings():
    return pd.DataFrame([
        {"title": "Hindi", "video_path": os.path.join(STORY_VIDEO_DIR, "hindi.mp3")},
        {"title": "Redfort in Telugu", "video_path": os.path.join(STORY_VIDEO_DIR, "red_fort_telugu.mp3")},
        {"title": "TajMahal Male", "video_path": os.path.join(STORY_VIDEO_DIR, "taj_mahal_male.mp3")},
        {"title": "TajMahal Female", "video_path": os.path.join(STORY_VIDEO_DIR, "taj_mahal_female.mp3")}
    ])