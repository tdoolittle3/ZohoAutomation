class CRM:
    def __init__(self, client):
        self.client = client

    def search(self, module, word=None, criteria=None):
        params = {}
        if word:
            params["word"] = word
        if criteria:
            params["criteria"] = criteria
        return self.client.get(f"/crm/v2/{module}/search", params=params)

    def get_record(self, module, record_id):
        return self.client.get(f"/crm/v2/{module}/{record_id}")

    def create(self, module, data):
        return self.client.post(f"/crm/v2/{module}", data={"data": [data]})

    def update(self, module, record_id, data):
        return self.client.put(f"/crm/v2/{module}/{record_id}", data={"data": [data]})

    def delete(self, module, record_id):
        return self.client.delete(f"/crm/v2/{module}/{record_id}")
