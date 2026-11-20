import tree_sitter_python as tspython
from tree_sitter import Language, Parser

# PY_LANGUAGE = Language(tspython.language())
# parser = Parser(PY_LANGUAGE)
#
# tree = parser.parse(b"def halo(Amy):\n    return Amy\n")
# print(tree.root_node)  # mencetak S-expression pohon

parser = Parser(Language(tspython.language()))

# kode = b"x = 1\n"

# kode = b"a = 2\n\ndef cek(a):\n    if a == 0:\n        return 0\n    else:\n        return 1\n"

kode = b"class Kehadiran:\n     def hadir(siswa)\n     return 'Hadir!'"

tree = parser.parse(kode)
print(tree.root_node)



for c in tree.root_node.children[0].children:
    print(c.type, "bernama" if c.is_named else "anonim")
