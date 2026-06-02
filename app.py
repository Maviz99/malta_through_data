import streamlit as st

# 1. Seiteneinstellungen
st.set_page_config(page_title="Malta Trip", page_icon="🇲🇹", layout="centered")

# 2. Das "Gedächtnis" der App initialisieren
# Wenn die App zum ersten Mal startet, setzen wir die Seite auf "home"
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"


# DIE STARTSEITE

if st.session_state["current_page"] == "home":
    st.title("🇲🇹 Malta and Maryam's Trip Plan")
    
    try:
        st.image("malta.jpeg", caption="Our upcoming trip to Malta!")
    except:
        st.warning("⚠️ Bild 'malta.jpeg' nicht gefunden.")

    st.markdown("### Where do you want to go?")
    st.write("Choose a perspective to explore the trip planning:")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🗺️ Geographical Separation", use_container_width=True):
            st.session_state["current_page"] = "geographical"
            st.rerun() # Aktualisiert die App sofort

    with col2:
        if st.button("🎨 Artistic and Atmospheric Vibe", use_container_width=True):
            st.session_state["current_page"] = "atmosphere"
            st.rerun()
    with col3:
        if st.button("🎵 Music and Nightlife", use_container_width=True):
            st.session_state["current_page"] = "music"
            st.rerun()
    with col4:
        if st.button("📸 Photography", use_container_width=True):
            st.session_state["current_page"] = "photography"
            st.rerun()

#  GEOGRAPHICAL SEPARATION

elif st.session_state["current_page"] == "geographical":
    st.title("🗺️ Geographical Separation")
    
    # Der Zurück-Button, um wieder zur Startseite zu kommen
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.write("Hier ist  geografische Unterteilung:")
    
    #  Tabs für 4 Kategorien!
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏛️ Historical Malta", 
        "🏖️ Coastal Malta", 
        "🌿 Rural / Natural Malta", 
        "⛵ Gozo"
    ])
    
    with tab1:
        st.subheader("Historical Malta")
        st.write("Der Plan für die historischen Orte rein...")
        
    with tab2:
        st.subheader("Coastal Malta")
        st.write("Hier meine Strand- und Küstenausflüge...")
        
    with tab3:
        st.subheader("Rural / Natural Malta")
        st.write("Wanderungen, Klippen und Natur pur...")
        
    with tab4:
        st.subheader("Gozo")
        st.write("Der Plan für die Nachbarinsel Gozo...")


#  ARTISTIC & ATMOSPHERIC VIBE
elif st.session_state["current_page"] == "atmosphere":
    st.title("🎨 Artistic and Atmospheric Vibe")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.subheader("The Vibe of Malta")
    st.write("Hier wird später das Design, Farben, Stimmungen und Gefühle der Reise festghalten.")

elif st.session_state["current_page"] == "music":
    st.title("🎵 Music and Nightlife")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.subheader("Music and Nightlife in Malta")
    st.write("Hier werden die besten Bars, Clubs und Musikspots in Malta festgehalten.")

elif st.session_state["current_page"] == "photography":
    st.title("📸 Photography")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.subheader("Photography in Malta")
    st.write("Hier werden die besten Fotospots, Sonnenuntergänge und Instagrammable Orte in Malta festgehalten.")