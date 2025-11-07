-- projekty_flask/todo/modele.sql

-- tabela z użytkownikami
DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- unikalny identyfikator
  login TEXT UNIQUE NOT NULL, -- nazwa użytkownika
  haslo TEXT NOT NULL -- hasło użytkownika
);
-- przykładowy użytkownik
INSERT INTO user (id, login, haslo)
VALUES (null, 'adam', 'scrypt:32768:8:1$b6ySf4OhUqADg4os$9fab79b9175c7e1ac341d06b72a3bb3e3a213733c6211bfa7f2b388988065e837df630be38e7eb5729d59db4f5e7d0abd7886e0697125f1a0e8a0eadd6a9eb3a');

-- tabela z zadaniami
DROP TABLE IF EXISTS zadanie;
CREATE TABLE zadanie (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- unikalny identyfikator zadania
    user_id INTEGER, -- identyfikator użytkownika
    zadanie TEXT NOT NULL, -- opis zadania do wykonania
    zrobione BOOLEAN NOT NULL, -- informacja czy zadania zostało juz wykonane
    data_pub DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- data dodania zadania
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE -- wskazanie klucza obcego
);

-- początkowe dane
INSERT INTO zadanie VALUES (null, 1, 'Wyrzucić śmieci', 0, CURRENT_TIMESTAMP);
INSERT into zadanie VALUES (null, 1, 'Nakarmić psa', 0, CURRENT_TIMESTAMP);
