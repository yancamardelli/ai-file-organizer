# 🗂️ AI File Organizer (offline version)

Projeto de **automação em Python** que organiza automaticamente arquivos de uma pasta usando um classificador local (offline) baseado em:
- extensão do ficheiro
- palavras-chave no nome

## ✅ O que faz
- Lê ficheiros em `input/`
- Classifica em: `docs`, `images`, `videos`, `audio`, `code`, `archives`, `others`
- Move para `organized/<categoria>/`
- Gera um relatório em `reports/report.json`

## ▶️ Como executar
1) Coloque ficheiros dentro de `input/`
2) Execute:
```bash
python main.py
