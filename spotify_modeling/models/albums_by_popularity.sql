{{ config(materialized='table') }}

SELECT
  album_name,
  popularity
FROM
  `raw_spotify.albums`
ORDER BY
  popularity DESC
  