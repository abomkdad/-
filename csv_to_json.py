import csv
import json
from pathlib import Path


def csv_to_json(csv_path: Path, json_path: Path) -> None:
    with csv_path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            cleaned = { (k or '').strip(): (v.strip() if isinstance(v, str) else v) for k, v in row.items() if k is not None }
            rows.append(cleaned)

    with json_path.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
        f.write('\n')


if __name__ == '__main__':
    pairs = [
        ('branches.csv', 'branches.json'),
        ('products.csv', 'products.json'),
    ]

    for src, dst in pairs:
        src_path = Path(src)
        dst_path = Path(dst)
        if src_path.exists():
            csv_to_json(src_path, dst_path)
            print(f'Converted {src_path} -> {dst_path}')
        else:
            print(f'Skipped missing file: {src_path}')
