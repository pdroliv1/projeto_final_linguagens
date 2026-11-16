from pathlib import Path
import pandas as pd

RAW = Path(__file__).parents[1] / "data" / "raw" / "roubos_veiculos_rio.xlsx"
PROCESSED = Path(__file__).parents[1] / "data" / "processed" / "roubos_veiculos_rio.csv.gz"

COLUMN_MAP = {
    0: "ano",
    1: "incidencias",
    2: "dif_absoluta",
    3: "dif_percentual",
    4: "taxa_100k_hab",
    5: "media_mensal",
}


def load_raw() -> pd.DataFrame:
    df = pd.read_excel(RAW, header=0)
    df.columns = [str(c).strip() for c in df.columns]
    return df


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    if list(df.columns) == list(COLUMN_MAP.values()):
        return df

    # Try positional rename when columns are unnamed or Portuguese variants
    if len(df.columns) >= 6:
        df = df.iloc[:, :6].copy()
        df.columns = list(COLUMN_MAP.values())
    else:
        raise ValueError(f"Formato inesperado: colunas encontradas = {list(df.columns)}")

    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = _normalize_columns(df)

    # Drop rows where ano is not a 4-digit year
    df = df[pd.to_numeric(df["ano"], errors="coerce").between(2000, 2030)].copy()
    df["ano"] = df["ano"].astype(int)

    numeric_cols = ["incidencias", "dif_absoluta", "dif_percentual", "taxa_100k_hab", "media_mensal"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values("ano").reset_index(drop=True)
    return df


def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df[["incidencias", "taxa_100k_hab", "media_mensal"]].describe().round(2)


def run():
    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    df_raw = load_raw()
    df = clean(df_raw)
    df.to_csv(PROCESSED, index=False, compression="gzip")
    print(f"Processado: {len(df)} linhas → {PROCESSED}")
    return df


if __name__ == "__main__":
    run()
