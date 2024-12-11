import requests 

class APIConnection:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}', headers=self.headers)
        return response
    
    def post(self, endpoint, data):
        response = requests.post(f'{self.base_url}/{endpoint}', json=data, headers=self.headers)
        return response
    
    def put(self, endpoint, data):
        response = requests.put(f'{self.base_url}/{endpoint}', json=data, headers=self.headers)
        return response
    
    def delete(self, endpoint):
        response = response.delete(f'{self.base_url}/{endpoint}', headers=self.headers)
        return response