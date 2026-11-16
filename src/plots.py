from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

raiz = Path(__file__).resolve().parent.parent
arquivo = next((raiz / "data" / "processed").glob("*.csv.gz"))
saida = raiz / "docs" / "assets"
saida.mkdir(exist_ok=True)

df = pd.read_csv(arquivo)

fig1 = go.Figure(
    go.Scatter(x=df["ano"], y=df["incidencias"], mode="lines+markers", line=dict(color="#1a3a5c"))
)
fig1.update_layout(
    title="Roubos de veículos no 1º quadrimestre (2003-2022)",
    xaxis_title="Ano",
    yaxis_title="Número de roubos",
    template="plotly_white",
)
fig1.write_html(saida / "fig_rq1_evolucao.html", include_plotlyjs="cdn")

fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(
    go.Bar(x=df["ano"], y=df["taxa_100k_hab"], name="Taxa por 100 mil hab.", marker_color="#1a3a5c"),
    secondary_y=False,
)
fig2.add_trace(
    go.Scatter(x=df["ano"], y=df["dif_percentual"], name="Variação percentual", mode="lines+markers", line=dict(color="#c0392b")),
    secondary_y=True,
)
fig2.update_layout(title="Taxa por 100 mil habitantes e variação percentual", xaxis_title="Ano", template="plotly_white")
fig2.update_yaxes(title_text="Taxa por 100 mil hab.", secondary_y=False)
fig2.update_yaxes(title_text="Variação percentual", secondary_y=True)
fig2.write_html(saida / "fig_rq2_taxa.html", include_plotlyjs="cdn")

fig3 = go.Figure(
    go.Bar(
        x=df["ano"],
        y=df["media_mensal"],
        marker=dict(color=df["media_mensal"], colorscale="Reds"),
    )
)
fig3.update_layout(
    title="Média mensal de roubos de veículos no 1º quadrimestre",
    xaxis_title="Ano",
    yaxis_title="Média mensal",
    template="plotly_white",
)
fig3.write_html(saida / "fig_rq3_media.html", include_plotlyjs="cdn")