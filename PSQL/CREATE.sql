CREATE TABLE IF NOT EXISTS Genre (
id SERIAL PRIMARY KEY,
genre_name VARCHAR(60) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS Artist (
id SERIAL PRIMARY KEY,
artist_name VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS GenreArtist (
id_genre INTEGER REFERENCES Genre(id),
id_artist INTEGER REFERENCES Artist(id),
CONSTRAINT pk PRIMARY KEY (id_genre, id_artist)
);

CREATE TABLE IF NOT EXISTS Album (
id SERIAL PRIMARY KEY,
album_name VARCHAR(100) NOT NULL,
release_date INTEGER CHECK(release_date > 1900 AND release_date < 3000) NOT NULL
);

CREATE TABLE IF NOT EXISTS ArtistAlbum(
id_artist INTEGER REFERENCES Artist(id),
id_album INTEGER REFERENCES Album(id),
CONSTRAINT aa PRIMARY KEY (id_artist, id_album)
);

CREATE TABLE IF NOT EXISTS Track (
id SERIAL PRIMARY KEY,
track_name VARCHAR(200) NOT NULL,
long_time DECIMAL NOT NULL CHECK(long_time > 1 AND long_time < 60),
album_id INTEGER REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS Collection(
id SERIAL PRIMARY KEY,
collection_name VARCHAR(100) NOT NULL,
year_date INTEGER NOT NULL CHECK(year_date > 2000 AND year_date < 3000)
);

CREATE TABLE IF NOT EXISTS CollectionTrack(
id_track INTEGER REFERENCES Track(id),
id_collection INTEGER REFERENCES Collection(id),
CONSTRAINT ct PRIMARY KEY (id_track, id_collection)
);