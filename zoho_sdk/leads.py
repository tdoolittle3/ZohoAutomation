class Leads:
    def __init__(self, client):
        """
        client: an instance of ZohoClient or your REST wrapper
        """
        self.client = client

    def list_leads(self, page=1, per_page=200):
        """
        Get a paginated list of leads.
        """
        params = {
            "page": page,
            "per_page": per_page
        }
        return self.client.get("/crm/v2/Leads", params=params)

    def get_lead(self, lead_id):
        """
        Retrieve a specific lead by ID.
        """
        return self.client.get(f"/crm/v2/Leads/{lead_id}")

    def create_lead(self, lead_data):
        """
        Create a new lead.
        lead_data: dict with fields like First_Name, Last_Name, Email, etc.
        """
        payload = {"data": [lead_data]}
        return self.client.post("/crm/v2/Leads", data=payload)

    def update_lead(self, lead_id, update_data):
        """
        Update an existing lead.
        update_data: dict of fields to update.
        """
        payload = {"data": [update_data]}
        return self.client.put(f"/crm/v2/Leads/{lead_id}", data=payload)

    def search_leads(self, criteria):
        """
        Search leads by criteria.
        criteria: Zoho API formatted string, e.g. '(Email:equals:john@example.com)'
        """
        params = {"criteria": criteria}
        return self.client.get("/crm/v2/Leads/search", params=params)
