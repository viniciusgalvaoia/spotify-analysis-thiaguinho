{{ config(materialized='table') }}


SELECT
  t.track_name,
  a.album_name,
  t.popularity,
  tf.acousticness,
  tf.danceability,
  tf.duration_ms,
  tf.energy,
  tf.instrumentalness,
  CASE
      WHEN tf.key = 0 THEN "C"
      WHEN tf.key = 1 THEN "C#/Db"
      WHEN tf.key = 2 THEN "D"
      WHEN tf.key = 3 THEN "D#/Eb"
      WHEN tf.key = 4 THEN "E"
      WHEN tf.key = 5 THEN "F"
      WHEN tf.key = 6 THEN "F#/Gb"
      WHEN tf.key = 7 THEN "G"
      WHEN tf.key = 8 THEN "G#/Ab"
      WHEN tf.key = 9 THEN "A"
      WHEN tf.key = 10 THEN "A#/Bb"
      WHEN tf.key = 11 THEN "B"
    ELSE
    ""
  END
    AS track_key,
  tf.liveness,
  tf.loudness,
  tf.speechiness,
  tf.valence
FROM
  `raw_spotify.tracks` AS t
LEFT JOIN
  `raw_spotify.albums` AS a
ON
  t.album_id = a.album_id
LEFT JOIN
  `raw_spotify.tracks_features` AS tf
ON
  t.track_id = tf.track_id
ORDER BY t.popularity DESC
