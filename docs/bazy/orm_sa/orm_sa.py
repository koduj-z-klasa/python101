import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session

plik_bazy = 'baza_sa.db'
if os.path.exists(plik_bazy):
    os.remove(plik_bazy)

# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///' + plik_bazy)  # ':memory:'

# klasa bazowa dla modeli
class Base(DeclarativeBase):
    pass

# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi
class Klasa(Base):
    __tablename__ = 'klasa'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nazwa: Mapped[str] = mapped_column(String(100), nullable=False)
    profil: Mapped[str] = mapped_column(String(100), default='')
    uczniowie: Mapped[List["Uczen"]] = relationship(back_populates='klasa')


class Uczen(Base):
    __tablename__ = 'uczen'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    imie: Mapped[str] = mapped_column(String(100), nullable=False)
    nazwisko: Mapped[str] = mapped_column(String(100), nullable=False)
    klasa_id: Mapped[int] = mapped_column(ForeignKey('klasa.id'), nullable=False)
    klasa: Mapped["Klasa"] = relationship(back_populates="uczniowie")

# tworzymy tabele
Base.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
with Session(baza) as sesja:

    # dodajemy dwie klasy
    klasa1 = Klasa(nazwa='1A', profil='matematyczny')
    klasa2 = Klasa(nazwa='1B', profil='humanistyczny')
    sesja.add(klasa1)
    sesja.add(klasa2)

    sesja.commit()

    uczniowie = [
        Uczen(imie='Tomasz', nazwisko='Nowak', klasa_id=klasa1.id),
        Uczen(imie='Jan', nazwisko='Kos', klasa_id=klasa2.id),
        Uczen(imie='Piotr', nazwisko='Kowalski', klasa_id=klasa2.id)
    ]
    # dodajemy dane wielu uczniów
    sesja.add_all(uczniowie)

    sesja.commit()

exit()

def czytajdane():
    # if not sesja.query(Klasa).count():
    for uczen in sesja.query(Uczen).join(Klasa).all():
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()


czytajdane()
# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
# klasa1 = sesja.query(Klasa).filter_by(nazwa='1A').one()
# zmiana klasy ucznia o identyfikatorze 2
inst_uczen = sesja.query(Uczen).filter(Uczen.id == 2).one()
inst_uczen.klasa_id = sesja.query(Klasa.id).filter(
    Klasa.nazwa == '1B').scalar()

# usunięcie ucznia o identyfikatorze 3
sesja.delete(sesja.get(Uczen, 3))

czytajdane()

# zapisanie zmian w bazie i zamknięcie sesji
sesja.commit()
sesja.close()
