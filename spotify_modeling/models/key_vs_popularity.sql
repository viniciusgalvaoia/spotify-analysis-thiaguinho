{{ config(materialized="table") }}

WITH
  tracks AS (
  SELECT
    CASE
      WHEN tf.key = 0 THEN "C"
      WHEN tf.key = 1 THEN "C#"
      WHEN tf.key = 2 THEN "D"
      WHEN tf.key = 3 THEN "D#"
      WHEN tf.key = 4 THEN "E"
      WHEN tf.key = 5 THEN "F"
      WHEN tf.key = 6 THEN "F#"
      WHEN tf.key = 7 THEN "G"
      WHEN tf.key = 8 THEN "G#"
      WHEN tf.key = 9 THEN "A"
      WHEN tf.key = 10 THEN "A#"
      WHEN tf.key = 11 THEN "B"
    ELSE
    ""
  END
    AS track_key,
    t.popularity
  FROM
    `raw_spotify.tracks` AS t
  INNER JOIN
    `raw_spotify.tracks_features` tf
  ON
    t.track_id = tf.track_id )
SELECT
  track_key,
  AVG(popularity) AS avg_popularity
FROM
  tracks
GROUP BY
  track_key
ORDER BY
  avg_popularity DESC
  