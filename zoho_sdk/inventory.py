'''This module provides access to both Zoho Inventory and CRM Plus APIs.'''


class InventoryCRM:
    def __init__(self, client):
        self.client = client

    def get_invoice(self, invoice_id):
        """Get a single invoice by ID from CRM Plus."""
        return self.client.get(f"/crm/v2/Invoices/{invoice_id}")

    def list_invoices(self, page=1, per_page=200):
        """Get a paginated list of invoices from CRM Plus."""
        params = {"page": page, "per_page": per_page}
        return self.client.get("/crm/v2/Invoices", params=params)

    def create_invoice(self, data):
        """Create a new invoice in CRM Plus."""
        return self.client.post("/crm/v2/Invoices", data={"data": [data]})

    def search_sales_orders(self, search_text):
        """Search Sales Orders in CRM Plus."""
        params = {"criteria": search_text}
        return self.client.get("/crm/v2/Sales_Orders/search", params=params)

    def list_products(self, page=1, per_page=200):
        """List products in CRM Plus."""
        params = {"page": page, "per_page": per_page}
        return self.client.get("/crm/v2/Products", params=params)
    

class Inventory:
    def __init__(self, client, org_id):
        self.client = client
        self.org_id = org_id

    def get_invoice(self, invoice_id):
        return self.client.get(
            f"/inventory/v1/invoices/{invoice_id}",
            params={"organization_id": self.org_id}
        )

    def list_invoices(self, page=1):
        return self.client.get(
            "/inventory/v1/invoices",
            params={"organization_id": self.org_id, "page": page}
        )

    def create_invoice(self, data):
        return self.client.post(
            "/inventory/v1/invoices",
            data=data | {"organization_id": self.org_id}
        )

