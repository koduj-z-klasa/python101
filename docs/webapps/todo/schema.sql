-- todo/schema.sql

-- tabela z zadaniami
drop table if exists zadania;
create table zadania (
    id integer primary key autoincrement, -- unikalny indentyfikator
    zadanie text not null, -- opis zadania do wykonania
    zrobione boolean not null, -- informacja czy zadania zostalo juz wykonane
    data_pub datetime not null -- data dodania zadania
);

-- pierwsze dane
insert into zadania (id, zadanie, zrobione, data_pub)
values (null, 'Wyrzucić śmieci', 0, datetime(current_timestamp));
insert into zadania (id, zadanie, zrobione, data_pub)
values (null, 'Nakarmić psa', 0, datetime(current_timestamp));
