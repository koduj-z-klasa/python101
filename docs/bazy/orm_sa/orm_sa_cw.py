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
