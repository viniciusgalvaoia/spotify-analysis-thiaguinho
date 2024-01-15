import pandas as pd


from utils import get_google_credentials, get_spotify_access_token, get_album, get_artist, get_track, get_track_features


def get_albums_data_from_api(albums_ids):
    albumns_data_list = []
    for album_id in albums_ids:
        album_response = get_album(access_token, album_id)
        albumns_data = {
            "album_id": album_response["id"],
            "artist_id": album_response["artists"][0]["id"],
            "album_name": album_response["name"],
            "popularity": album_response["popularity"],
            "release_date": album_response["release_date"],
            "total_tracks": album_response["total_tracks"],
            "tracks": [
                track_id["id"] for track_id in album_response["tracks"]["items"]
            ],
        }
        albumns_data_list.append(albumns_data)
    return albumns_data_list


def get_artists_data_from_api(albums_data):
    artists_data_list = []
    artist_ids = [album_data["artist_id"] for album_data in albums_data]
    unique_artist_ids = set(artist_ids)
    for artist_id in unique_artist_ids:
        artist_response = get_artist(access_token, artist_id)
        artist_data = {
            "artist_id": artist_response["id"],
            "artist_name": artist_response["name"],
            "followers": artist_response["followers"]["total"],
            "genres": artist_response["genres"][0],
            "popularity": artist_response["popularity"],
            "image": artist_response["images"][0]["url"],
            "href": artist_response["href"],
        }
        artists_data_list.append(artist_data)
    return artists_data_list


def get_tracks_data_from_api(albums_data):
    track_data_list = []
    for album_data in albums_data:
        for track_id in album_data["tracks"]:
            track_response = get_track(access_token, track_id)
            track_data = {
                "track_id": track_id,
                "album_id": album_data["album_id"],
                "artist_id": album_data["artist_id"],
                "track_name": track_response["name"],
                "popularity": track_response["popularity"],
                "href": track_response["href"],
                "duration_ms": track_response["duration_ms"],
            }
            track_data_list.append(track_data)
    return track_data_list


def get_track_features_data_from_api(albums_data):
    track_features_data_list = []
    for album_data in albums_data:
        for track_id in album_data["tracks"]:
            track_features_response = get_track_features(access_token, track_id)
            track_data = {
                "track_id": track_id,
                "acousticness": track_features_response["acousticness"],
                "danceability": track_features_response["danceability"],
                "duration_ms": track_features_response["duration_ms"],
                "energy": track_features_response["energy"],
                "instrumentalness": track_features_response["instrumentalness"],
                "key": track_features_response["key"],
                "liveness": track_features_response["liveness"],
                "loudness": track_features_response["loudness"],
                "mode": track_features_response["mode"],
                "speechiness": track_features_response["speechiness"],
                "tempo": track_features_response["tempo"],
                "time_signature": track_features_response["time_signature"],
                "valence": track_features_response["valence"],
            }
            track_features_data_list.append(track_data)
    return track_features_data_list


if __name__ == "__main__":
    project_id = "spotiflow-411208"
    credentials = get_google_credentials()
    access_token = get_spotify_access_token()
    thiaguinho_albums_ids = [
        "3JaIGz2Vm0RkGQoTEPZUoj",
        "6eD1BU8VeJKtc0N7Ns6UKW",
        "2pG3hkRXmUnsSMt4oxNocs",
        "1YkJK9hemjEQMQ7FirSio6",
        "0j2ZgqWilgGwN87wCI72Jv",
        "04tzF0EuVB13cbdgH0d9iV",
        "3H3Pd9vGhDAp9bt3JWUgCA",
        "4dvzwisuUWXvb6e0IGBCv6",
        "47l1S7yxz9zAO6K5gDori3",
        "2CXu75O6FO8v1QEdaJuD4N",
        "1Oxkn3Dk3wtsVqldd46cHi",
        "2N8l2cxeIlx0LKzQGUGQjy",
        "6zSN9UDV1jwdihKLvbRuKR",
        "4upLAEC3VhsPKkBUJI6KkS",
    ]
    albums_data = get_albums_data_from_api(thiaguinho_albums_ids)
    albums_df = pd.DataFrame(albums_data)
    albums_df.drop("tracks", axis=1, inplace=True)
    albums_df.to_gbq(
        destination_table="raw_spotify.albums",
        project_id=project_id,
        if_exists="append",
        credentials=credentials,
    )
    artists_data = get_artists_data_from_api(albums_data)
    artist_df = pd.DataFrame(artists_data)
    artist_df.to_gbq(
        destination_table="raw_spotify.artists",
        project_id=project_id,
        if_exists="append",
        credentials=credentials,
    )
    tracks_data = get_tracks_data_from_api(albums_data)
    tracks_df = pd.DataFrame(tracks_data)
    tracks_df.to_gbq(
        destination_table="raw_spotify.tracks",
        project_id=project_id,
        if_exists="append",
        credentials=credentials,
    )
    tracks_features_data = get_track_features_data_from_api(albums_data)
    tracks_features_df = pd.DataFrame(tracks_features_data)
    tracks_features_df.to_gbq(
        destination_table="raw_spotify.tracks_features",
        project_id=project_id,
        if_exists="append",
        credentials=credentials,
    )
