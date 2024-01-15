{{ config(materialized='table') }}

SELECT
  track_name,
  popularity
FROM
  `raw_spotify.tracks`
ORDER BY
  popularity DESC
  