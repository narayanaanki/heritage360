# ============================================================
# explorer.py
# UNESCO Explorer logic for HERITAGE360
# ============================================================

import streamlit as st
from data import get_unesco_images

# ============================================================
# UNESCO DESCRIPTION REGISTRY
# ============================================================

def get_unesco_descriptions():
    """
    Returns textual descriptions for UNESCO sites.
    """
    return {
        "Taj Mahal": (
            "Taj Mahal, white marble mausoleum complex in Agra, western Uttar Pradesh state, northern India. The Taj Mahal was built by the Mughal emperor Shah Jahan in the memory of his wife Mumtaz Mahal who died in childbirth in 1631 . The monument houses a burial chamber where the tombs of both Shah Jahan and his wife are present . To construct this monument it took over 22 years . Shah Jahan had another plan , after the completion of Taj mahal he wanted build a similar one for himself made of black stone , but his son Aurangzeb found this project unnecessary and deposed the emperor imprisoning him in the Agra fort .  Shah Jahan spent his life gazing at The Taj mahal. The interesting part of Taj mahal is that it changes its colour 3 times a day . In the morning pink , noon bright white and under moon light bright gold ."
        ),
        "Qutub Minar": (
            "The Qutb Minar is a UNESCO World Heritage Site located in Delhi, India. It is one of the tallest brick minarets in the world, standing at 72.5 meters (238 feet) high. Construction was started around 1193 CE by Qutb-ud-din Aibak, the founder of the Delhi Sultanate, and completed by his successors, Iltutmish and Firoz Shah Tughlaq."
            "Built from red sandstone and marble, the tower has five distinct stories, each marked by intricately carved bands of inscriptions and geometric patterns. Its design reflects a blend of Indo-Islamic architecture, with influences from earlier Afghan styles."
            "The minaret was likely built to celebrate the beginning of Muslim rule in India and served as a victory tower and a minaret for calling the faithful to prayer at the adjacent Quwwat-ul-Islam Mosque. The complex also houses the famous Iron Pillar, which has resisted corrosion for centuries."
            "Today, the Qutb Minar remains a symbol of Delhi’s rich historical layers and is a major tourist attraction, representing both architectural brilliance and the complex history of medieval India."
        
        ),
        "Red Fort":(

            """The Red Fort (Lal Qila) is a famous historical monument located in Delhi, India. It was built in 1648 by the Mughal Emperor Shah Jahan when he shifted his capital from Agra to Delhi. The fort is made mainly of red sandstone, which gives it its distinctive color and name. It served as the main residence of Mughal emperors for nearly 200 years. Inside the fort are beautiful structures like the Diwan-i-Aam, Diwan-i-Khas, and Rang Mahal. The Red Fort showcases a blend of Persian, Timurid, and Indian architectural styles. It is surrounded by massive walls that were designed for protection. The fort witnessed many important events in Indian history. Today, it is a UNESCO World Heritage Site. Every year on 15th August, the Prime Minister of India hoists the national flag here, making it a powerful symbol of India’s independence and heritage."""
        ),
        "India Gate":(
            """India Gate is a prominent war memorial located in New Delhi, India. It was built to honor the Indian soldiers who lost their lives during World War I and the Third Anglo-Afghan War. The monument was designed by Sir Edwin Lutyens and completed in 1931. India Gate is made of sandstone and granite and stands about 42 meters tall. The names of over 13,000 soldiers are inscribed on its walls. Beneath the arch burns the Amar Jawan Jyoti, symbolizing the sacrifice of soldiers. The structure resembles the Arc de Triomphe in Paris. It is surrounded by lush green lawns and is a popular public gathering place. India Gate holds great national pride and emotional significance. It stands as a lasting symbol of courage, sacrifice, and remembrance."""
        ),
        "Gateway of India":(
            """The Gateway of India is a famous historical monument located in Mumbai, Maharashtra. It was built in 1924 to commemorate the visit of King George V and Queen Mary to India. The monument was designed by architect George Wittet. It is built in the Indo-Saracenic architectural style, combining Hindu and Muslim elements. The Gateway of India is made of yellow basalt and reinforced concrete. It stands facing the Arabian Sea, near the iconic Taj Mahal Palace Hotel. Historically, it was the ceremonial entrance point for British governors and viceroys. In 1948, the last British troops left India through this gateway, marking the end of colonial rule. Today, it is a major tourist attraction. The monument symbolizes India’s colonial history and cultural heritage."""
        ),
        "Fatehpur Sikri":(
                """Fatehpur Sikri is a historic city located near Agra in Uttar Pradesh, India. It was founded in 1569 by the Mughal Emperor Akbar as his capital. The city is built mainly of red sandstone and is known for its grand Mughal architecture. Fatehpur Sikri includes important structures like Buland Darwaza, Jama Masjid, and Panch Mahal. Buland Darwaza is one of the largest gateways in the world. The architecture reflects a blend of Islamic, Hindu, and Persian styles. The city was abandoned after a short period due to water scarcity. Despite this, the buildings remain well preserved. Fatehpur Sikri is a UNESCO World Heritage Site. It stands as a remarkable example of Mughal planning and artistic excellence."""
        ),
        "Mysore Palace":(
                """Mysore Palace, also known as Amba Vilas Palace, is a grand royal residence located in Mysuru, Karnataka. It was built in 1912 for the Wodeyar dynasty. The palace is designed in the Indo-Saracenic architectural style, blending Hindu, Muslim, Rajput, and Gothic elements. It served as the official residence of the Maharajas of Mysore. The palace has beautiful halls, stained glass windows, and ornate ceilings. It is surrounded by a large garden and courtyards. Mysore Palace is famous for its Dussehra celebrations, when it is illuminated with thousands of lights. The palace attracts millions of visitors every year. It is one of the most visited monuments in India. Mysore Palace represents the rich cultural and royal heritage of Karnataka."""
        ),
        "Sanchi Stupa":(
            """Sanchi Stupa is an important Buddhist monument located in Sanchi, Madhya Pradesh, India. It was originally built in the 3rd century BCE by Emperor Ashoka. The stupa was constructed to preserve the relics of Lord Buddha. It is made of stone and has a large hemispherical dome. The site is famous for its beautifully carved toranas (gateways) depicting scenes from Buddha’s life. Sanchi Stupa is one of the oldest stone structures in India. It played a major role in the spread of Buddhism. The monument reflects early Buddhist art and architecture. Sanchi Stupa is a UNESCO World Heritage Site. It stands as a symbol of peace, faith, and spiritual heritage."""
        ),
        "Victoria Memorial":(
            """Victoria Memorial is a magnificent historical monument located in Kolkata, West Bengal, India. It was built in 1921 in memory of Queen Victoria. The memorial was designed by architect Sir William Emerson. It is made of white Makrana marble, giving it a grand appearance. The architecture is a blend of British, Mughal, Venetian, and Egyptian styles. The building is surrounded by large, beautiful gardens. Inside, it houses a museum with paintings, artifacts, and historical documents. The memorial reflects the period of British rule in India. It is one of Kolkata’s most famous landmarks. Victoria Memorial stands as a symbol of India’s colonial history and artistic heritage."""
        ),
        "Shaniwar Wada":(
            """Shaniwar Wada is a historic fort located in Pune, Maharashtra, India. It was built in 1732 by Peshwa Bajirao I as the seat of the Maratha Empire. The fort was originally constructed using stone and wood. Shaniwar Wada is known for its massive gates and strong fortifications. It once served as the residence of the Peshwas, the prime ministers of the Maratha rulers. A major fire in 1828 destroyed much of the wooden structure. Today, only the stone walls and foundations remain. The fort is associated with many stories and legends from Maratha history. It is an important tourist attraction in Pune. Shaniwar Wada symbolizes the power and legacy of the Maratha Empire."""
        ),
        "Lal Mahal":(
            """Lal Mahal is a historic monument located in Pune, Maharashtra, India. It was built in 1630 by Shahaji Bhosale, the father of Chhatrapati Shivaji Maharaj. Lal Mahal is known as the childhood residence of Shivaji Maharaj. The palace is famous for the historic event where Shivaji Maharaj attacked Shaista Khan. It was originally made of red bricks, which gave it the name “Lal Mahal.” The original structure was damaged over time and rebuilt in 1988. Today, it houses paintings and exhibits depicting Maratha history. Lal Mahal is closely connected to the rise of the Maratha Empire. It is an important heritage site in Pune. The monument represents bravery, strategy, and Maratha pride."""
        ),
        "Sinhagad Fort":(
                """Sinhagad Fort is a historic hill fortress located near Pune, Maharashtra, India. It stands at an altitude of about 1,312 meters above sea level. The fort is famous for the Battle of Sinhagad in 1670, led by Tanaji Malusare under Chhatrapati Shivaji Maharaj. Sinhagad means “Lion’s Fort,” symbolizing bravery and strength. The fort has strong stone walls and strategically placed gates. It played an important role in the Maratha Empire’s defense system. The site offers stunning views of the surrounding valleys. Today, it is a popular destination for trekking and history lovers. Memorials dedicated to Tanaji Malusare are found inside the fort. Sinhagad Fort stands as a symbol of courage, sacrifice, and Maratha valor."""
        ),
        "Sun Temple, Konark": (
            "The Sun Temple, Konark is a magnificent 13th-century Hindu temple located in Odisha, dedicated to Surya, the Sun God. It was built around 1250 CE by King Narasimhadeva I of the Eastern Ganga dynasty."
            "The temple is renowned for its engineering precision, where the wheels also function as sundials. Though parts of the structure are now in ruins, it remains an outstanding example of ancient Indian craftsmanship."

            "In 1984, the Sun Temple was declared a UNESCO World Heritage Site and is considered one of the finest architectural marvels of India."
        ),
        "Group of Monuments at Hampi": (
            "The Group of Monuments at Hampi is a vast and magnificent heritage site located in Karnataka, on the banks of the Tungabhadra River. It was the capital of the Vijayanagara Empire, one of the greatest South Indian kingdoms, flourishing between the 14th and 16th centuries."
            " It is founded by Harihara and Bukka Raya."
            "Hampi is famous for its grand temples, royal complexes, marketplaces, and massive stone structures, reflecting the empire’s wealth and artistic excellence. The Vittala Temple’s Stone Chariot is one of the most iconic monuments in India."
            "In 1986, Hampi was declared a UNESCO World Heritage Site, and it stands today as a remarkable symbol of India’s medieval history, architecture, and cultural heritage."
        ),
        "Ajanta Caves": (
            "The Ajanta Caves are a group of ancient rock-cut Buddhist caves located in Maharashtra, carved into a horseshoe-shaped cliff along the Waghora River. They date from the 2nd century BCE to the 6th century CE and were developed during the Satavahana and Vakataka dynasties."
            "Ajanta is especially renowned for its exceptionally well-preserved paintings and sculptures, which represent a high point of ancient Indian art and storytelling. "
            "In 1983, the Ajanta Caves were declared a UNESCO World Heritage Site, recognized globally for their artistic, historical, and spiritual significance."
        ),
        "Ellora Caves": (
            "The Ellora Caves are a remarkable complex of rock-cut temples and monasteries located in Maharashtra, representing three major religions of India—Buddhism, Hinduism, and Jainism. They were carved between the 6th and 10th centuries CE."
            "The most famous monument at Ellora is the Kailasa Temple (Cave 16), a massive monolithic structure dedicated to Lord Shiva, carved from a single rock and considered an engineering marvel."
            "Ellora stands out for its architectural unity, artistic excellence, and religious harmony. In 1983, the Ellora Caves were designated a UNESCO World Heritage Site, making them one of India’s most significant cultural landmarks."
         )   
    }
# ============================================================
# MAIN EXPLORER RENDERER
# ============================================================

def render_unesco_explorer():
    """
    Renders the UNESCO Explorer section with dropdown, image, and description.
    """

    st.markdown("## 🏛️ Explore UNESCO World Heritage Sites")

    # Load data
    unesco_data = get_unesco_images()
    descriptions = get_unesco_descriptions()

    site_names = list(unesco_data.keys())

    if not site_names:
        st.warning("No UNESCO site data available.")
        return

    selected_site = st.selectbox(
        "Select a UNESCO World Heritage Site",
        site_names
    )

    site_data = unesco_data.get(selected_site, {})

    image_url = site_data.get("image")
    description = descriptions.get(
        selected_site,
        "Description not available for this site."
    )

    col1, col2 = st.columns([1, 1])

    # -------------------------------
    # IMAGE PANEL
    # -------------------------------
    with col1:
        if isinstance(image_url, str):
            st.image(image_url, use_container_width=True)
        else:
            st.info("Image not available for this site.")

    # -------------------------------
    # DESCRIPTION PANEL
    # -------------------------------
    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">{selected_site}</div>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# EDUCATIONAL NOTE
# ============================================================

def render_explorer_note():
    """
    Displays an educational note below the explorer.
    """
    st.markdown(
        """
        <div class="info-box">
            <h3>Why UNESCO World Heritage Matters</h3>
            <p>
                UNESCO World Heritage Sites are places of outstanding cultural
                or natural importance to the common heritage of humanity.
                Protecting these sites ensures that future generations can
                learn from and experience them.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )