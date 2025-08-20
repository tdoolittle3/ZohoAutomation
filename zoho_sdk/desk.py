class Desk:
    def __init__(self, client, org_id):
        self.client = client
        self.org_id = org_id
        # override base url for desk
        self.base_url = f"https://desk.zoho.com/api/v1"

    def list_tickets(self, department_id=None, limit=10, from_index=1):
        params = {
            "limit": limit,
            "from": from_index
        }
        if department_id:
            params["departmentId"] = department_id

        return self.client._request(
            "GET",
            f"{self.base_url}/tickets",
            params=params,
            headers={"orgId": self.org_id}
        )

    def get_ticket(self, ticket_id):
        return self.client._request(
            "GET",
            f"{self.base_url}/tickets/{ticket_id}",
            headers={"orgId": self.org_id}
        )

    def create_ticket(self, department_id, subject, contact_id=None, email=None, description=None, priority="Medium"):
        data = {
            "subject": subject,
            "departmentId": department_id,
            "priority": priority
        }
        if contact_id:
            data["contactId"] = contact_id
        if email:
            data["email"] = email
        if description:
            data["description"] = description

        return self.client._request(
            "POST",
            f"{self.base_url}/tickets",
            json=data,
            headers={"orgId": self.org_id}
        )
