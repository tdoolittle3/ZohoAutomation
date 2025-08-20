# Zoho API Python Client

A lightweight Python wrapper around the Zoho REST APIs (CRM, Inventory, Desk, etc.), designed to replace Deluge scripts with standard Python code.

## ✨ Features
- Simple `ZohoClient` class for handling authentication and API calls
- Module-specific helpers:
  - `CRM` – Manage Leads, Sales Orders, Invoices, etc.
  - `Inventory` – Fetch organizations, invoices, products
  - `Desk` – List, create, update tickets
  - `Leads` – Paginated search and retrieval
- Full OAuth2 support (access + refresh tokens)
- Easy `.env` configuration

---

## 📦 Installation

```bash
git clone <your-repo-url>
cd <repo-name>
pip install -r requirements.txt
