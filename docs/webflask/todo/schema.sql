-- todo/schema.sql

-- tabela z zadaniami
DROP TABLE IF EXISTS zadania;
CREATE TABLE zadania (
    id integer primary key autoincrement, -- unikalny indentyfikator
    zadanie text not null, -- opis zadania do wykonania
    zrobione boolean not null, -- informacja czy zadania zostalo juz wykonane
    data_pub datetime not null -- data dodania zadania
);

-- pierwsze dane
INSERT INTO zadania (id, zadanie, zrobione, data_pub)
VALUES (null, 'Wyrzucić śmieci', 0, datetime(current_timestamp));
INSERT into zadania (id, zadanie, zrobione, data_pub)
VALUES (null, 'Nakarmić psa', 0, datetime(current_timestamp));
