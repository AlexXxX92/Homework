
SELECT track_name, long_time FROM track
WHERE long_time = (SELECT max(long_time) FROM track);


SELECT track_name, long_time FROM track
WHERE long_time > 3.5;


SELECT collection_name FROM collection
WHERE year_date BETWEEN 2018 AND 2020;


SELECT artist_name FROM artist
WHERE artist_name NOT LIKE  '% %';


SELECT track_name FROM track
WHERE track_name LIKE '%Мой%';


SELECT g.genre_name, count(id_artist) FROM genre g 
JOIN genreartist ga ON g.id = ga.id_genre
GROUP BY g.genre_name;


SELECT a.album_name, count(t.id) FROM album a
JOIN track t ON t.album_id = a.id 
WHERE a.release_date BETWEEN 2019 AND 2020
GROUP BY a.album_name;


SELECT a.album_name, avg(t.long_time) FROM album a
JOIN track t ON t.album_id = a.id
GROUP BY a.album_name;


SELECT a.artist_name FROM artist a 
JOIN artistalbum aa ON a.id = aa.id_artist 
JOIN album al ON aa.id_album = al.id 
WHERE al.release_date != 2020
GROUP BY a.artist_name;


SELECT c.collection_name FROM collection c 
JOIN collectiontrack cc ON c.id = cc.id_collection 
JOIN track t ON cc.id_track = t.id 
JOIN album a ON t.album_id  = a.id
JOIN artistalbum aa ON aa.id_album = a.id 
JOIN artist ON artist.id = aa.id_artist 
WHERE artist.artist_name LIKE '%КиШ%'
GROUP BY c.collection_name;













