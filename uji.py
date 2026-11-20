import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNGSI = Query(PY, '(function_definition name: (identifier) @nama) @fungsi')

BATAS_BARIS = 30
SKIP_DIRS = {"venv", ".venv", "env", ".git", "node_modules", "__pycache__", ".mypy_cache"}


def cari_error_pertama(node):
    """Kembalikan node ERROR atau MISSING pertama (preorder), atau None."""
    if node.is_error or node.is_missing:
        return node
    for child in node.children:
        hasil = cari_error_pertama(child)
        if hasil is not None:
            return hasil
    return None


def cek_file(path: Path) -> None:
    try:
        source = path.read_bytes()
    except OSError as exc:
        print(f"{path}: tidak bisa dibaca ({exc})")
        return

    tree = parser.parse(source)

    # Fitur 1: komentar TODO/FIXME
    captures = QueryCursor(Q_TODO).captures(tree.root_node)
    for node in captures.get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {teks}")

    # Fitur 2: fungsi yang panjangnya melebihi batas
    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        nama_node = cap.get("nama", [])
        fungsi_node = cap.get("fungsi", [])
        if not nama_node or not fungsi_node:
            continue
        nama = nama_node[0].text.decode(errors="replace")
        fungsi = fungsi_node[0]
        jumlah = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if jumlah > BATAS_BARIS:
            print(
                f"{path}:{fungsi.start_point[0] + 1}: "
                f"fungsi '{nama}' panjang {jumlah} baris"
            )

    # Fitur 3: file dengan error parse
    if tree.root_node.has_error:
        node = cari_error_pertama(tree.root_node)
        if node is not None:
            baris = node.start_point[0] + 1
            jenis = "MISSING" if node.is_missing else "ERROR"
            print(f"{path}:{baris}: parse {jenis}")


def iter_py(folder: Path):
    for path in folder.rglob("*.py"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def main() -> None:
    if len(sys.argv) != 2:
        print("Pemakaian: python cek.py <folder>")
        sys.exit(1)
    folder = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"Bukan folder: {folder}")
        sys.exit(1)
    for path in iter_py(folder):
        cek_file(path)


if __name__ == "__main__":
    main()
