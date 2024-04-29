INSERT INTO Genre VALUES 
	(1, 'Реп'),
	(2, 'Рок'),
	(3, 'Танцевальная');


INSERT INTO Artist VALUES
	(1, 'Guf'),
	(2, 'КиШ'),
	(3, 'DG Smash'),
	(4, 'Баста');


INSERT INTO GenreArtist VALUES
	(1, 1),
	(2, 2),
	(1, 4),
	(3, 3);


INSERT INTO Album VALUES
	(1, 'Город дорог', 2019),
	(2, 'Как в старой сказке', 2001),
	(3, 'Танцевальный', 2023);


INSERT INTO ArtistAlbum VALUES 
	(2, 2),
	(1, 1),
	(4, 1),
	(3, 3);


INSERT INTO Track VALUES 
	(1, 'Город дорог', 3.28, 1),
	(2, 'Новогодняя', 5.02, 1),
	(3, 'Гимн шута', 4.01, 2),
	(4, 'Проклятый старый дом', 2.22, 2),
	(5, 'Сансара', 3.11, 1),
	(6, 'Мой волна', 4.55, 3);

INSERT INTO Collection VALUES
	(1, 'Мегахит', 2007),
	(2, 'Хит', 2008),
	(3, 'Сборник', 2018),
	(4, 'FM', 2010);


INSERT INTO CollectionTrack VALUES 
	(1, 1),
	(2, 1),
	(3, 1),
	(4, 2);
		