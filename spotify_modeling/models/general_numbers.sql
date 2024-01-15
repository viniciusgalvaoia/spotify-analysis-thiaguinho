{{ config(materialized="table") }}

WITH
  albums AS (
  SELECT
    1 AS id,
    COUNT(*) AS albums_count
  FROM
    `raw_spotify.albums`),
  tracks AS (
  SELECT
    1 AS id,
    COUNT(*) AS tracks_count,
    SUM(duration_ms) / 60000 AS total_tracks_duration
  FROM
    `raw_spotify.tracks` )
SELECT
  albums_count,
  tracks_count,
  total_tracks_duration
FROM
  albums
JOIN
  tracks
ON
  albums.id = tracks.id
