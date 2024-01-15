import requests
from base64 import b64encode
from google.oauth2 import service_account


CLIENT_ID = "6d92254135614ab0831835413d209d4f"
CLIENT_SECRET = "f0a9aec6c96848c3a364a76080cf6ecd"

GOOGLE_CREDENTIALS = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "project_id": "spotiflow-411208",
            "private_key_id": "93e826b82bd9993489c6f70724438f136d0a1380",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCe4iqb5GMB3jhl\nrYtzULM0S+ud4z/CpBuxLwLT9VShOdlx1MBia7Jh0Gb9vIQdULtFK7RuJIJupyOp\nk1YnGi+CxNFx2bBV66rI48/2Udwg9gGp6VVhv0OxbgMLiLsxaV2HMXssvKRZzPeL\nEU4enVQawlysaEdUcgQvPQKII8x166PWpCrgYZu/0Ai1DtZ8dZbChu5Juj53mOMm\njD8CckgipfLGfR3+2Uu2vOiyNB999Wz6+Dfg3cVcRB1tjuUngu57lAguuBE/Gm4Y\nnR5qR7wUib7aGFabTrME5gfPKH8bhfygxOATqFwf15WDmdMXIN69RjGwynVjFjGr\nHCs0quVvAgMBAAECggEAGWubIJ0OYC6jPFVjYdxQB7Z76KOCwIwMKDGa1LnERBVi\n3m0JKNYNUMwMpl0ikCQqCjufXx31Rmn0cT2zA4eTgWsnDX2kUmLlzMVyMPlQ7G8f\nvgUolX6KAJnW3+IM/S9b+PToPbSi4QFDu9rVcl1+ptdhB26Ztv+U/s/Wl1yO6nC7\nye5oRKiCeZdxxa6jFlSNYaA+xJrvm38lv1FT+yKwcDNNTRllVxoMpOELPvd50DLF\nhykAfH6/xdaeO9reMYiPRhwK69T3plE32u/zHrErcT8MijI6Epii3HZTN/VFv70h\nFBv8gIozBpNvcFK20eH0BuGpa2UrxNSLLSMcr6wyvQKBgQDecfsHzjCdLY7YU7YF\noqqUR+QH+TtGaoRvHufA04ZaJpPYJv/n2ErRsLUP5nMW8OKiS9FJ1WGVo60Pgoa4\nG049Hruq7CqnbWoxRp38sDT5IBcWWW8poxj1MZSInxhgykAtOZ1N3M3PHhz+u5nE\nTMDhzqE5l9QQ4wWIPVWTHLSUVQKBgQC22anHdBNBDMs4e5tstvyKuIMgZoy1jzQv\ntM0+8z98rcqbCMwGB4QYK9tJe0ci5wb1Edj+onvsa32/LnNXzNf1Wnge9PDd8MWC\nwJf9lvU6jVtu0SMlEEP2zpCtdXY9a+ZdkFDtR8SmNUso+3Atu9dwYYkE6fAHTzdG\nAgO7leh2swKBgF3jA84Gk/QzP2BE7MWyI4cUVMWcxwzwdlckVzLG1KUGNU59H3Ou\nkd2xVKqSXK8pGq7fi0U7f8WV4Lx0HgJk2//mEdWRemtSPgjwQkxd3u3rQnNXahjL\n0wPiWkvTwolPtAiikadEc8Vgc2J8sejtcFeeS+QwFfzOpQ4cvRqrefhFAoGAXU0p\nzeWT4ZCGrfacs1eX+6z08/Z//DDrXyBxzppOne8MQBm4CaeSJsdSKOenv86FBU4r\nHJuKgnPDAWfRYU7cL40PWDSCJ62xCuv9Yl/CGDODIUPEHCh1lZ2Hw4r5X5QMQ1fd\ng4YoeOsew/WxIxUDdIvAX+qDGSe5u5ZRk0mGCfMCgYEAjeIV+9+Tvh/8MXX+2JIY\nLn8Ok1bNlj4c0u2VWB6a5nACxNucEBdsGGSti9v5bjUez71swgWsk78aSYCqvyew\nCZCWJzdBwq063AeGeH/JxtNUSNwmLKB42NTRJC6ZB7ntIwmqcpBMhAasedamHX1M\no92fMO3bmaEIpfgQrIknqCg=\n-----END PRIVATE KEY-----\n",
            "client_email": "vinicius-110396@spotiflow-411208.iam.gserviceaccount.com",
            "client_id": "117176777261573817768",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vinicius-110396%40spotiflow-411208.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com",
        }
    )

def get_google_credentials(credentials_path="google_credentials/key.json"):
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
