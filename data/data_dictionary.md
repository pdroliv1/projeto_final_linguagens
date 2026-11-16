# Dicionário de Dados

**Dataset:** Incidências de roubo de veículos — 1º quadrimestre, Rio de Janeiro (2003–2022)  
**Fonte:** [data.rio](https://www.data.rio/documents/5f63cb34f78b41eb9212f4de42401356/about)  
**Licença:** CC BY 4.0  
**Formato original:** Microsoft Excel (.xlsx)  
**Formato processado:** CSV comprimido (.csv.gz)

---

## Variáveis

| Coluna | Tipo | Descrição |
|---|---|---|
| `ano` | int | Ano de referência (2003 a 2022) |
| `incidencias` | int | Número total de roubos de veículos no 1º quadrimestre |
| `dif_absoluta` | int | Diferença absoluta em relação ao mesmo período do ano anterior |
| `dif_percentual` | float | Variação percentual em relação ao ano anterior (%) |
| `taxa_100k_hab` | float | Taxa de roubos por 100 mil habitantes |
| `media_mensal` | float | Média mensal de roubos dentro do 1º quadrimestre |

---

## Notas

- O 1º quadrimestre compreende os meses de janeiro, fevereiro, março e abril.
- Os valores de diferença e variação percentual para 2003 são `NaN` por ausência de ano anterior.
- A taxa por 100 mil habitantes normaliza o indicador pela população estimada do município.
- Dados produzidos pelo Instituto de Segurança Pública (ISP-RJ) e disponibilizados pela Prefeitura da Cidade do Rio de Janeiro.
