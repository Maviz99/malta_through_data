import streamlit as st
import pandas as pd

# Seiteneinstellungen
st.set_page_config(page_title="Malta Trip", page_icon="🇲🇹", layout="centered")

# Daten laden (Pandas)
@st.cache_data # Die Datei mussnicht bei jedem Klick neu geladen werden - das spart Zeit!
def load_data():
    # CSV-Datei
    df = pd.read_csv("malta_places.csv")
    # Leerzeichen aus den Spaltennamen entfernen
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Fehler beim Laden der CSV-Datei: {e}")
    st.stop()

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

    # 2x2 Raster für die Buttons (sieht sauberer aus)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        if st.button("🗺️ Geographical Separation", use_container_width=True):
            st.session_state["current_page"] = "geographical"
            st.rerun()
    with row1_col2:
        if st.button("🎨 Artistic and Atmospheric Vibe", use_container_width=True):
            st.session_state["current_page"] = "atmosphere"
            st.rerun()

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        if st.button("🎵 Music and Nightlife", use_container_width=True):
            st.session_state["current_page"] = "music"
            st.rerun()
    with row2_col2:
        if st.button("📸 Photography", use_container_width=True):
            st.session_state["current_page"] = "photography"
            st.rerun()



# GEOGRAPHICAL SEPARATION (MIT KARTEN!)

elif st.session_state["current_page"] == "geographical":
    st.title("🗺️ Geographical Separation")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.write("Hier ist deine geografische Unterteilung basierend auf deinen Daten:")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏛️ Historical Malta", 
        "🏖️ Coastal Malta", 
        "🌿 Rural / Natural Malta", 
        "⛵ Gozo"
    ])
    
    with tab1:
        st.subheader("Historical Malta")
        #Orte mit hohem Kunst/Kultur-Faktor (art >= 4), die NICHT auf Gozo liegen
        historical_df = df[(df["art"] >= 4) & (~df["mood_tags"].str.contains("Gozo", na=False))]
        st.write(f"{len(historical_df)} Orte gefunden:")
        st.dataframe(historical_df[["place", "type", "notes"]])
        # Die magische Streamlit-Karte
        st.map(historical_df)
        
    with tab2:
        st.subheader("Coastal Malta")
        #Orte mit hohem Meer-Faktor (sea >= 4)
        coastal_df = df[df["sea"] >= 4]
        st.write(f"{len(coastal_df)} Küstenorte gefunden:")
        st.dataframe(coastal_df[["place", "type", "notes"]])
        st.map(coastal_df)
        
    with tab3:
        st.subheader("Rural / Natural Malta")
        #Orte mit hohem Natur-Faktor (nature >= 4)
        nature_df = df[df["nature"] >= 4]
        st.write(f"{len(nature_df)} Naturspots gefunden:")
        st.dataframe(nature_df[["place", "type", "notes"]])
        st.map(nature_df)
        
    with tab4:
        st.subheader("Gozo")
        #Orte, die das Wort "Gozo" in den Notes oder Tags haben
        gozo_df = df[df["notes"].str.contains("Gozo", na=False) | df["mood_tags"].str.contains("Gozo", na=False)]
        st.write(f"{len(gozo_df)} Orte auf Gozo gefunden:")
        st.dataframe(gozo_df[["place", "type", "notes"]])
        st.map(gozo_df)



# MUSIC & NIGHTLIFE

elif st.session_state["current_page"] == "music":
    st.title("🎵 Music and Nightlife")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.subheader("Party & Music Spots")
    #Orte mit hohem Fun-Faktor (fun >= 4)
    music_df = df[df["fun"] >= 4]
    st.dataframe(music_df[["place", "type", "notes"]])
    st.map(music_df)



# PHOTOGRAPHY

elif st.session_state["current_page"] == "photography":
    st.title("📸 Photography")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.subheader("Instagrammable Spots & Views")
    #Orte, die das Tag "photography" oder "sunset" in den mood_tags haben
    photo_df = df[df["mood_tags"].str.contains("photography|sunset", na=False, case=False)]
    st.dataframe(photo_df[["place", "type", "notes"]])
    st.map(photo_df)



# ARTISTIC & ATMOSPHERIC VIBE
elif st.session_state["current_page"] == "atmosphere":
    st.title("🎨 Artistic and Atmospheric Vibe")
    
    if st.button("⬅️ Back to Home"):
        st.session_state["current_page"] = "home"
        st.rerun()
        
    st.subheader("The Vibe of Malta")
    st.write("Hier filtern wir Orte nach ihrer Stimmung (Mood Tags).")
    
    # Ein interaktiver Filter für dich!
    all_tags = set()
    df["mood_tags"].dropna().str.split(";").apply(lambda x: all_tags.update([t.strip() for t in x]))
    
    selected_tag = st.selectbox("Wähle eine Stimmung aus:", sorted(list(all_tags)))
    
    filtered_df = df[df["mood_tags"].str.contains(selected_tag, na=False)]
    st.dataframe(filtered_df[["place", "type", "notes"]])