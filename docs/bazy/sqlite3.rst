.. _sqlite3:

Interpreter Sqlite
###################

Bazy SQLite przechowywane są w pojedynczych plikach, które łatwo archiwizować, przenosić
czy badać, podglądając ich zawartość. Podstawowym narzędziem jest interpreter
``sqlite3`` (``sqlite3.exe`` w Windows).

Aby otworzyć bazę zapisaną w przykładowym pliku :file:`test.db` wydajemy w terminalu
polecenie:

.. code-block:: bash

	~$ sqlite3 test.db

Później do dyspozycji mamy polecenia:

  - ``.databases`` – pokazuje aktualną bazę danych;
  - ``.schema`` – pokazuje schemat bazy danych, czyli polecenia SQL tworzące tabele i relacje;
  - ``.table`` – pokaże tabele w bazie;
  - ``.quit`` – wychodzimy z powłoki interpretera.

Możemy również wydawać komendy SQL-a operujące na bazie, np. kwerendy:
``SELECT * FROM klasa;`` – polecenia te zawsze kończymy średnikiem.

.. figure:: sqlite3.png

.. note::

	Bardziej zaawansowanym narzędziem umożliwiającym kompleksową obsługę baz SQLite
	za pomocą interfejsu graficznego jest program ``sqlitestudio``.