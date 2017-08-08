# -*- coding: utf-8 -*-
# quiz-pw/main.py

import os
from app import app, baza
from models import *
from views import *
from dane import *

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        baza.create_tables([Pytanie, Odpowiedz], True)  # tworzymy tabele
        dodaj_pytania(pobierz_dane('pytania.csv'))
    app.run(debug=True)
