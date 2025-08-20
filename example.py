from zoho_sdk import ZohoClient, CRM, Inventory, Desk, Leads, InventoryCRM


# Init client
client = ZohoClient()

# Inventory example
inventory = Inventory(client, 897235104)
invoice = inventory.get_invoice(invoice_id=6950729000000095039)
print("InvoiceNumber:", invoice["invoice"]["salesorder_number"])
print("Total", invoice["invoice"]["total"])
salesorder_id = invoice["invoice"]["reference_number"]
print("Sales Order ID:", salesorder_id)


# CRM example
crm = CRM(client)
search_results = crm.search("Sales_Orders", criteria=f"(SO_Number:equals:{salesorder_id})")
print("Sales Orders:", search_results)

shouldCreateInvoice = False
if search_results != "No records found." and search_results["data"]:
    sales_order = search_results["data"][0]
    print("Sales Order ID:", sales_order["id"])
    print("Sales Order Status:", sales_order["Status"])
    if sales_order["Status"] == "Invoiced":
        print("This Sales Order has already been invoiced.")
    else:
        print("This Sales Order is not yet invoiced.")
        shouldCreateInvoice = True

if shouldCreateInvoice:
    print("Creating invoice for Sales Order ID:", salesorder_id)
    # Create invoice in InventoryCRM
    inventory_crm = InventoryCRM(client)
    invoice_data = {
        "Customer_Name": sales_order["Customer_Name"]["name"],
        "Sales_Order": {"id": salesorder_id},
        "Line_Items": sales_order["Line_Items"]
    }
    new_invoice = inventory_crm.create_invoice(invoice_data)
    print("New Invoice Created:", new_invoice)



'''
### OTHER EXAMPLES ###

desk = Desk(client, org_id="897209611")  # Desk Org ID (different from CRM/Inventory Org IDs!)

# List tickets
tickets = desk.list_tickets(limit=5)
print("Tickets:", tickets)

leads = Leads(client)

# List leads
print("Listing leads: ", leads.list_leads(per_page=10))

# Get a lead
print("Getting lead:", leads.get_lead("6961498000000572001"))

# Create a new lead
new_lead = leads.create_lead({
    "First_Name": "Alice",
    "Last_Name": "Smith",
    "Email": "alice.smith@example.com",
    "Company": "Example Corp"
})
print("New lead:", new_lead)

# Update a lead
updated = leads.update_lead("6961498000000572001", {"Phone": "9876543210"})
print(updated)
'''