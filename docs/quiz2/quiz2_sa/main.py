# -*- coding: utf-8 -*-
# quiz_sa/main.py

from app import app, baza
from models import *
from views import *
from dane import *
import os

if __name__ == '__main__':
    if not os.path.exists('quiz.db'):
        baza.create_all() # tworzymy tabele
        dodaj_pytania(pobierz_dane('pytania.csv'))
    app.run(debug=True)
