# 🗂️ AI File Organizer (Offline)

Projeto de **automação em Python** que organiza automaticamente ficheiros de uma pasta local, utilizando regras de classificação **offline**, sem dependência de APIs externas ou ligação à internet.

Este projeto foi desenvolvido com foco em **automação de processos**, uma competência essencial para funções de **RPA Developer Jr** e **Python Developer Jr**.

---

## 📌 Sobre o projeto

Em muitos contextos profissionais e pessoais, é comum lidar com pastas desorganizadas, contendo documentos, imagens, vídeos e código misturados, o que dificulta a produtividade e o acesso rápido à informação.

O **AI File Organizer** resolve este problema ao automatizar a organização de ficheiros, analisando:
- a **extensão do ficheiro**
- **palavras-chave no nome**

Com base nessas regras, os ficheiros são automaticamente classificados e movidos para pastas específicas, gerando ainda um **relatório em formato JSON** com o resultado do processo.

O objetivo do projeto é demonstrar competências práticas em:
- automação
- manipulação de ficheiros
- lógica de classificação
- desenvolvimento em Python aplicado a problemas reais

---

## ✅ O que o projeto faz

- Lê automaticamente os ficheiros colocados na pasta `input/`
- Classifica os ficheiros nas seguintes categorias:
  - `docs`
  - `images`
  - `videos`
  - `audio`
  - `code`
  - `archives`
  - `others`
- Move os ficheiros para `organized/<categoria>/`
- Gera um relatório detalhado em `reports/report.json`
- Funciona totalmente **offline**

---

## 🖼️ Demonstração

> 📸 Sugestão: adicionar prints da pasta antes e depois da execução  
> (ex.: `assets/before.png` e `assets/after.png`)

```text
input/        → pasta com ficheiros desorganizados
organized/    → ficheiros organizados por categoria
reports/      → relatório JSON gerado automaticamente
