import requests
from pathlib import Path

URL = "https://www.arcgis.com/sharing/rest/content/items/5f63cb34f78b41eb9212f4de42401356/data"
OUTPUT = Path(__file__).parent / "roubos_veiculos_rio.xlsx"

def main():
    print("Baixando dataset de roubos de veículos — data.rio...")
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    OUTPUT.write_bytes(r.content)
    print(f"Salvo em {OUTPUT} ({len(r.content) / 1024:.1f} kB)")

if __name__ == "__main__":
    main()
