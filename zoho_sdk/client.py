import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ZohoClient:
    def __init__(self):
        self.client_id = os.getenv("ZOHO_CLIENT_ID")
        self.client_secret = os.getenv("ZOHO_CLIENT_SECRET")
        self.refresh_token = os.getenv("ZOHO_REFRESH_TOKEN")
        self.dc = os.getenv("ZOHO_DC", "us")
        self.base_url = f"https://www.zohoapis.com"
        self.access_token = self.refresh_access_token()

    def refresh_access_token(self):
        url = f"https://accounts.zoho.com/oauth/v2/token"
        params = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }
        res = requests.post(url, params=params)
        res.raise_for_status()
        if "access_token" not in res.json():
            print("Error refreshing access token:", res.json())
            raise ValueError("Failed to refresh access token. Check your credentials.")
        return res.json()["access_token"]

    def _request(self, method, path, **kwargs):
        url = f"{path}" if path.startswith("http") else f"{self.base_url}{path}"
        headers = {"Authorization": f"Zoho-oauthtoken {self.access_token}"}
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
            kwargs.pop("headers")

        res = requests.request(method, url, headers=headers, **kwargs)
        if res.status_code == 401:  # token expired
            self.access_token = self.refresh_access_token()
            headers["Authorization"] = f"Zoho-oauthtoken {self.access_token}"
            res = requests.request(method, url, headers=headers, **kwargs)
        if res.status_code >= 400:
            print(f"Error {res.status_code}: {res.text}")
            
        res.raise_for_status()
        if res.status_code in (204, 205):  # No content
            return "No records found."
        return res.json()

    def get(self, path, params=None):
        return self._request("GET", path, params=params)

    def post(self, path, data=None):
        return self._request("POST", path, json=data)

    def put(self, path, data=None):
        return self._request("PUT", path, json=data)

    def delete(self, path):
        return self._request("DELETE", path)
