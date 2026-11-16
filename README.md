# Análise de Roubos de Veículos no Rio de Janeiro (2003–2022)

**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python  
**Curso:** Bacharelado em Sistemas de Informação — 6º Período  
**Instituição:** UnilaSalle Rio de Janeiro  
**Autor:** Pedro Oliv  

---

## Resumo

Análise da evolução histórica dos roubos de veículos no Município do Rio de Janeiro,
com base nos registros do 1º quadrimestre de cada ano entre 2003 e 2022.
O projeto segue os princípios FAIR e disponibiliza o artigo acadêmico completo via GitHub Pages.

**Palavras-chave:** segurança pública, roubo de veículos, Rio de Janeiro, Python, ciência aberta.

## Fonte dos dados

[data.rio — ISP/RJ](https://www.data.rio/documents/5f63cb34f78b41eb9212f4de42401356/about)  
Licença: CC BY 4.0

## Artigo publicado

> 🌐 [Ver artigo no GitHub Pages](https://pdroliv1.github.io/projeto_final_linguagens/)

## Estrutura do repositório

```
projeto_final_linguagens/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── download_data.py    # script para baixar o dataset
│   ├── processed/              # dados limpos (.csv.gz) — gerado pelo ETL
│   └── data_dictionary.md
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── __init__.py
│   └── etl.py
└── docs/
    ├── index.html
    └── assets/                 # figuras interativas (.html) — geradas pelo notebook
```

## Como executar

```bash
git clone https://github.com/pdroliv1/projeto_final_linguagens.git
cd projeto_final_linguagens
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python data/raw/download_data.py  # baixa o Excel original
python src/etl.py                  # processa e salva em data/processed/
# abra notebooks/analise_exploratoria.ipynb para explorar e gerar as figuras
```

## Licença

Código: [MIT](LICENSE)  
Dados e texto: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
