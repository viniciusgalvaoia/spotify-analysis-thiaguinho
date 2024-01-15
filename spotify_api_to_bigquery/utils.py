from base64 import b64encode

import requests
from google.oauth2 import service_account

CLIENT_ID = ""
CLIENT_SECRET = ""


def get_google_credentials(credentials_path="./google_credentials/key.json"):
    """
    Retrieves Google Cloud credentials from the specified JSON file.

    Args:
        credentials_path (str): Path to the JSON file containing Google Cloud credentials.

    Returns:
        google.auth.credentials.Credentials: Google Cloud credentials.

    Example:
        >>> credentials = get_google_credentials()
    """
    return service_account.Credentials.from_service_account_file(
        credentials_path,
    )


def get_spotify_access_token():
    """
    Retrieves an access token for Spotify API.

    Returns:
        str: The access token.

    Note:
        This function uses client credentials flow for authentication.

    Example:
        >>> access_token = get_spotify_access_token()
    """
    auth_header = b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode("utf-8")

    auth_options = {
        "url": "https://accounts.spotify.com/api/token",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + auth_header,
        },
        "data": {"grant_type": "client_credentials"},
    }

    response = requests.post(**auth_options)

    if response.status_code == 200:
        data = response.json()
        return data.get("access_token")
    else:
        print(f"Failed to get access token. Status code: {response.status_code}")
        return None


def make_spotify_request(access_token, endpoint, params):
    """
    Makes a request to the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        endpoint (str): The API endpoint to request.
        params (dict, optional): Additional parameters to include in the request.

    Returns:
        dict: The JSON response from the Spotify API.

    Note:
        This function supports both authenticated and unauthenticated requests.

    Example:
        >>> access_token = "your_access_token"
        >>> endpoint = "search"
        >>> params = {"q": "query_string", "type": "track"}
        >>> response = make_spotify_request(access_token, endpoint, params)
    """
    api_url = f"https://api.spotify.com/v1/{endpoint}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = (
        requests.get(api_url, headers=headers, params=params)
        if params
        else requests.get(api_url, headers=headers)
    )
    return response.json()


def get_album(access_token, album_id):
    """
    Retrieves album data from the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        album_id (str): The ID of the album to retrieve.

    Returns:
        dict: The JSON response containing album data.

    Example:
        >>> access_token = "your_access_token"
        >>> album_id = "album_id"
        >>> album_data = get_album(access_token, album_id)
    """
    return make_spotify_request(access_token, f"albums/{album_id}", "")


def get_artist(access_token, artist_id):
    """
    Retrieves artist data from the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        artist_id (str): The ID of the artist to retrieve.

    Returns:
        dict: The JSON response containing artist data.

    Example:
        >>> access_token = "your_access_token"
        >>> artist_id = "artist_id"
        >>> artist_data = get_artist(access_token, artist_id)
    """
    return make_spotify_request(access_token, f"artists/{artist_id}", "")


def get_track(access_token, track_id):
    """
    Retrieves track data from the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        track_id (str): The ID of the track to retrieve.

    Returns:
        dict: The JSON response containing track data.

    Example:
        >>> access_token = "your_access_token"
        >>> track_id = "track_id"
        >>> track_data = get_track(access_token, track_id)
    """
    return make_spotify_request(access_token, f"tracks/{track_id}", "")


def get_track_features(access_token, track_id):
    """
    Retrieves audio features data for a track from the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        track_id (str): The ID of the track for which to retrieve features.

    Returns:
        dict: The JSON response containing audio features data.

    Example:
        >>> access_token = "your_access_token"
        >>> track_id = "track_id"
        >>> features_data = get_track_features(access_token, track_id)
    """
    return make_spotify_request(access_token, f"audio-features/{track_id}", "")


def get_track_analysis(access_token, track_id):
    """
    Retrieves audio analysis data for a track from the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        track_id (str): The ID of the track for which to retrieve analysis.

    Returns:
        dict: The JSON response containing audio analysis data.

    Example:
        >>> access_token = "your_access_token"
        >>> track_id = "track_id"
        >>> analysis_data = get_track_analysis(access_token, track_id)
    """
    return make_spotify_request(access_token, f"audio-analysis/{track_id}", "")


def get_recommendations(access_token, params):
    """
    Retrieves track recommendations from the Spotify API.

    Args:
        access_token (str): The access token for Spotify API authentication.
        params (dict): Additional parameters to customize the recommendations.

    Returns:
        dict: The JSON response containing track recommendations.

    Example:
        >>> access_token = "your_access_token"
        >>> params = {"seed_artists": "artist_id", "seed_tracks": "track_id"}
        >>> recommendations_data = get_recommendations(access_token, params)
    """
    return make_spotify_request(access_token, f"recommendations", params=params)
