cabocha-python
===============
This is a python wrapper for CaboCha Japanese Dependency Structure Analyzer.

NOTE: It does not sopport Windows Python 64bit version.

`Japanese document <https://taku910.github.io/cabocha/>`_ is available.

USAGE
============

.. code:: python

  >>> import CaboCha
  >>> c = CaboCha.Parser()
  >>> sentence = "太郎はこの本を二郎を見た女性に渡した。"
  >>> print(c.parseToString(sentence))
  太郎は-----------D
      この-D       |
        本を---D   |
        二郎を-D   |
            見た-D |
            女性に-D
            渡した。
  EOS
  >>> tree = c.parse(sentence)
  >>> print(tree.toString(CaboCha.FORMAT_TREE))
  太郎は-----------D
      この-D       |
        本を---D   |
        二郎を-D   |
            見た-D |
            女性に-D
            渡した。
  EOS

  >>> print(tree.toString(CaboCha.FORMAT_LATTICE))
  * 0 6D 0/1 -2.457381
  太郎	名詞,固有名詞,人名,名,*,*,太郎,タロウ,タロー
  は	助詞,係助詞,*,*,*,*,は,ハ,ワ
  * 1 2D 0/0 1.488413
  この	連体詞,*,*,*,*,*,この,コノ,コノ
  * 2 4D 0/1 0.091699
  本	名詞,一般,*,*,*,*,本,ホン,ホン
  を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
  * 3 4D 0/1 2.266072
  二郎	名詞,固有名詞,人名,名,*,*,二郎,ジロウ,ジロー
  を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
  * 4 5D 0/1 1.416783
  見	動詞,自立,*,*,一段,連用形,見る,ミ,ミ
  た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
  * 5 6D 0/1 -2.457381
  女性	名詞,一般,*,*,*,*,女性,ジョセイ,ジョセイ
  に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
  * 6 -1D 0/1 0.000000
  渡し	動詞,自立,*,*,五段・サ行,連用形,渡す,ワタシ,ワタシ
  た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
  。	記号,句点,*,*,*,*,。,。,。
  EOS

License
============
CaboCha is copyrighted free software by Taku Kudo <taku@chasen.org> is released under any of the the LGPL (see the file LGPL) or the BSD License (see the file BSD).
