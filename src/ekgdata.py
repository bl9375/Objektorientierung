import json
import pandas as pd
import plotly.express as px
from scipy.signal import find_peaks

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])
        self.df = self.df.iloc[:5000]  # Entferne die erste Zeile, da sie nur die Spaltennamen enthält


    def plot_time_series(self):
        fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        peak_df = self.df.iloc[self.peaks[self.peaks < 2000]]
        fig.add_scatter(x=peak_df["Zeit in ms"], y=peak_df["Messwerte in mV"],
                        mode="markers", name="Peaks")
        return fig
       
    

    def find_peaks(self):
        peaks, _ = find_peaks(self.df["Messwerte in mV"], height=340, distance=200)
        self.peaks = peaks
        return peaks
    
    def estimate_hr(self):
    # Zeit zwischen Peaks = Abstände in ms → Umrechnen in BPM
        peak_times = self.df["Zeit in ms"].iloc[self.peaks]
        diffs = peak_times.diff().dropna()
        mean_interval_ms = diffs.mean()
        hr = 60000 / mean_interval_ms  # ms → BPM
        return round(hr, 1)

if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())