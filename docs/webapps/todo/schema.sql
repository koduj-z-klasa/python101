-- todo/schema.sql

-- tabela z zadaniami
drop table if exists entries;
create table entries (
    id integer primary key autoincrement, -- unikalny indentyfikator
    title text not null, -- opis zadania do wykonania
    is_done boolean not null, -- informacja czy zadania zostalo juz wykonane
    created_at datetime not null -- data dodania zadania
);

-- pierwsze dane
insert into entries (id, title, is_done, created_at)
values (null, 'Wyrzucić śmieci', 0, datetime(current_timestamp));
insert into entries (id, title, is_done, created_at)
values (null, 'Nakarmić psa', 0, datetime(current_timestamp));
