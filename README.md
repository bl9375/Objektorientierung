# EKG Dashboard

Eine Streamlit-App zur Visualisierung und Analyse von EKG-Daten. Personen können aus einer Datenbank geladen werden. Pro Person werden EKG-Zeitreihen dargestellt, R-Zacken (Peaks) automatisch erkannt und die durchschnittliche Herzfrequenz berechnet.

![Screenshot der App](screenshot.png)

## Features

- Personenauswahl mit Profilbild, Alter und maximaler Herzfrequenz
- Interaktiver EKG-Plot mit markierten Peaks
- Automatische Herzfrequenzberechnung aus den R-R-Intervallen


## Starten der App

Das Projekt verwendet PDM als Paketmanager!

```bash
# Abhängigkeiten installieren
pdm install

# App starten
pdm run streamlit run main.py
```

## Abhängigkeiten

- `streamlit`
- `pandas`
- `plotly`
- `scipy`
- `numpy`
- `Pillow`
