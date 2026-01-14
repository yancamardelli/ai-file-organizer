from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Config:
    input_dir: Path
    output_dir: Path
    reports_dir: Path


CATEGORY_EXTENSIONS = {
    "docs": {".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"},
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"},
    "videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "audio": {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"},
    "code": {".py", ".js", ".ts", ".html", ".css", ".json", ".yml", ".yaml", ".sql", ".sh"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

KEYWORDS_HINTS = {
    "docs": ["boleto", "fatura", "invoice", "nota", "recibo", "contrato", "cv", "curriculo", "currículo"],
    "images": ["foto", "img", "image", "screenshot", "print", "scan"],
    "videos": ["video", "vídeo", "aula", "lesson", "curso"],
    "audio": ["audio", "áudio", "podcast", "music", "musica", "música"],
    "code": ["script", "code", "codigo", "código", "projeto", "project"],
}


def ensure_dirs(cfg: Config) -> None:
    cfg.input_dir.mkdir(exist_ok=True)
    cfg.output_dir.mkdir(exist_ok=True)
    cfg.reports_dir.mkdir(exist_ok=True)


def guess_category(file_path: Path) -> str:
    """Classificador local simples: por extensão e por palavras no nome."""
    ext = file_path.suffix.lower()
    name = file_path.stem.lower()

    # 1- extensão
    for category, exts in CATEGORY_EXTENSIONS.items():
        if ext in exts:
            return category

    # 2- palavras-chave (keywords) no nome
    for category, keywords in KEYWORDS_HINTS.items():
        if any(k in name for k in keywords):
            return category

    return "others"


def move_file(src: Path, dst_dir: Path) -> Path:
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name

    # Se já existir, cria um nome novo "arquivo (1).ext"
    if dst.exists():
        base = src.stem
        ext = src.suffix
        i = 1
        while True:
            candidate = dst_dir / f"{base} ({i}){ext}"
            if not candidate.exists():
                dst = candidate
                break
            i += 1

    shutil.move(str(src), str(dst))
    return dst


def build_report(moves: list[dict]) -> dict:
    return {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "total_moved": len(moves),
        "moves": moves,
    }


def main() -> None:
    project_root = Path(__file__).parent

    cfg = Config(
        input_dir=project_root / "input",
        output_dir=project_root / "organized",
        reports_dir=project_root / "reports",
    )
    ensure_dirs(cfg)

    files = [p for p in cfg.input_dir.iterdir() if p.is_file()]

    print("=== AI File Organizer (offline) ===")
    print(f"Pasta de entrada: {cfg.input_dir}")
    print(f"Pasta de saída:   {cfg.output_dir}")
    print(f"Arquivos encontrados: {len(files)}\n")

    if not files:
        print("Nenhum arquivo encontrado em input/.")
        print("Coloque alguns arquivos na pasta input/ e rode novamente.")
        return

    moves: list[dict] = []

    for f in files:
        category = guess_category(f)
        dest_dir = cfg.output_dir / category
        dest_path = move_file(f, dest_dir)

        moves.append(
            {
                "original": str(f),
                "category": category,
                "moved_to": str(dest_path),
            }
        )

        print(f" {f.name}  »»  {category}/")

    report = build_report(moves)
    report_path = cfg.reports_dir / "report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n Relatório gerado em:", report_path)
    print("Arquivos organizados!")


if __name__ == "__main__":
    main()
