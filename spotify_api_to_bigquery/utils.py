import requests
from base64 import b64encode
from google.oauth2 import service_account


CLIENT_ID = "6d92254135614ab0831835413d209d4f"
CLIENT_SECRET = "f0a9aec6c96848c3a364a76080cf6ecd"


def get_google_credentials(credentials_path="./google_credentials/key.json"):
    return service_account.Credentials.from_service_account_file(
    credentials_path,
)

def get_spotify_access_token():
    auth_header = b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode('utf-8')
    
    auth_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + auth_header
        },
        'data': {
            'grant_type': 'client_credentials'
        }
    }

    response = requests.post(**auth_options)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('access_token')
    else:
        print(f"Failed to get access token. Status code: {response.status_code}")
        return None


def make_spotify_request(access_token, endpoint, params):
    api_url = f'https://api.spotify.com/v1/{endpoint}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(api_url, headers=headers, params=params) if params else requests.get(api_url, headers=headers)
    return response.json()


def get_album(access_token, album_id):
    return make_spotify_request(access_token, f"albums/{album_id}", "")

def get_artist(access_token, artist_id):
    return make_spotify_request(access_token, f"artists/{artist_id}", "")

def get_track(access_token, track_id):
    return make_spotify_request(access_token, f"tracks/{track_id}", "")

def get_track_features(access_token, track_id):
    return make_spotify_request(access_token, f"audio-features/{track_id}", "")

def get_track_analysis(access_token, track_id):
    return make_spotify_request(access_token, f"audio-analysis/{track_id}", "")

def get_recommendations(access_token, params):
    return make_spotify_request(access_token, f"recommendations", params=params)
