import streamlit as st
<<<<<<< HEAD
import source.read_person_data
import source.ekgdata
import matplotlib.pyplot as plt
from PIL import Image
from person import Person, get_person_data, get_person_object_by_full_name

#%% Zu Beginn

# Lade alle Personen als Objekt


# Anlegen diverser Session States
if "person_list" not in st.session_state:
    st.session_state.person_list = get_person_data()

# Selectbox Namen
if "selected_person" not in st.session_state:
    st.session_state.selected_person = "NONE"

# NEU: hier will ich die Person als Objekt haben, die gerade angezeigt wird
if "selected_person_object" not in st.session_state:
    st.session_state.selected_person_object = None


#%% Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sindst.session_state.selected_person  = st.selectbox("Wähle eine Versuchsperson", options=[person.get_full_name() for person in st.session_state.person_list])
st.session_state.selected_person  = st.selectbox("Wähle eine Versuchsperson", options=[person.get_full_name() for person in st.session_state.person_list])


st.session_state.selected_person_object = get_person_object_by_full_name(st.session_state.selected_person)

# Anzeigen eines Bilds mit Caption
st.image(st.session_state.selected_person_object.get_image(), caption=st.session_state.selected_person_object.get_full_name())


# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist


#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Per-son
current_egk_data = ekgdata.EKGdata(st.session_state.selected_person_object.ekg_tests[0])

#%% EKG-Daten als Matplotlib Plot anzeigen
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes
current_egk_data.plot_time_series()
# Zeige den Plot an
st.plotly_chart(current_egk_data.fig)

# %% Herzrate bestimmen
# Schätze die Herzrate 
#current_egk_data.estimate_hr()
# Zeige die Herzrate an
#st.write("Herzrate ist: ", int(current_egk_data.heat_rate)) 
=======
from src.person import get_person_data
from src.ekgdata import EKGdata

# ── Seiteneinstellungen ──────────────────────────────────────────────────────
st.set_page_config(page_title="EKG Dashboard", page_icon="🫀", layout="wide")
st.title("🫀 EKG Dashboard")

# ── Personen laden ───────────────────────────────────────────────────────────
persons = get_person_data()
person_names = [p.get_full_name() for p in persons]

# ── Sidebar: Person auswählen ────────────────────────────────────────────────
st.sidebar.header("Person auswählen")
selected_name = st.sidebar.selectbox("Person", person_names)
person = next(p for p in persons if p.get_full_name() == selected_name)

# ── Personen-Info ────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 3])

with col1:
    try:
        st.image(person.picture_path, width=180, caption=selected_name)
    except Exception:
        st.write("📷 Kein Bild verfügbar")

with col2:
    st.subheader(f"{person.firstname} {person.lastname}")
    st.write(f"**Geburtsjahr:** {person.date_of_birth}")
    st.write(f"**Alter:** {person.calc_age()} Jahre")
    st.write(f"**Geschlecht:** {person.gender}")
    st.write(f"**Max. Herzfrequenz:** {person.calc_max_heart_rate()} BPM")

st.divider()

# ── EKG-Daten ────────────────────────────────────────────────────────────────
if not person.ekg_tests:
    st.info("Keine EKG-Daten für diese Person vorhanden.")
else:
    st.subheader("EKG-Analyse")

    # EKG-Test auswählen (falls mehrere vorhanden)
    ekg_options = {f"EKG vom {t['date']} (ID {t['id']})": t for t in person.ekg_tests}
    selected_ekg_label = st.selectbox("EKG-Test auswählen", list(ekg_options.keys()))
    ekg_dict = ekg_options[selected_ekg_label]

    ekg = EKGdata(ekg_dict)
    ekg.find_peaks()
    hr = ekg.estimate_hr()

    # ── Kennzahlen ───────────────────────────────────────────────────────────
    m1, m2, m3 = st.columns(3)
    m1.metric("Gefundene Peaks", len(ekg.peaks))
    m2.metric("Herzfrequenz (Ø)", f"{hr} BPM")
    m3.metric("Max. Herzfrequenz", f"{person.calc_max_heart_rate()} BPM")

    # ── Plot ──────────────────────────────────────────────────────────────────
    fig = ekg.plot_time_series()
    st.plotly_chart(fig, use_container_width=True)
>>>>>>> 3f275923160912b8555ce607f24636b5b6657fcb
