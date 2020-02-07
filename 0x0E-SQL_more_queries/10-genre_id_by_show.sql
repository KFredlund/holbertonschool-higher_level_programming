-- Import a given database dump to your server
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id IS NOT NULL
AND tv_show_genres.show_id = tv_shows.id
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
