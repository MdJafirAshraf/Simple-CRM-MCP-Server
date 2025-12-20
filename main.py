# crm_server.py
from mcp.server.fastmcp import FastMCP
from typing import Dict, List, Optional

# Create the MCP server
mcp = FastMCP("CRM_Manager")

# Mock Database
db = {
    "contacts": [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "status": "Lead"},
        {"id": 2, "name": "Bob Jones", "email": "bob@work.com", "status": "Customer"},
    ],
    "deals": [
        {"id": 1, "contact_id": 2, "amount": 5000, "stage": "Closed Won"}
    ]
}

### --- Tools ---

@mcp.tool()
def search_contact(query: str) -> List[dict]:
    """Search for contacts by name or email."""
    return [c for c in db["contacts"] if query.lower() in c["name"].lower() or query.lower() in c["email"].lower()]

@mcp.tool()
def create_lead(name: str, email: str) -> dict:
    """Add a new lead to the CRM."""
    new_id = len(db["contacts"]) + 1
    new_contact = {"id": new_id, "name": name, "email": email, "status": "Lead"}
    db["contacts"].append(new_contact)
    return {"success": True, "contact": new_contact}

@mcp.tool()
def update_deal_stage(deal_id: int, stage: str) -> str:
    """Update the stage of an existing deal (e.g., 'Negotiation', 'Closed Won')."""
    for deal in db["deals"]:
        if deal["id"] == deal_id:
            deal["stage"] = stage
            return f"Deal {deal_id} updated to {stage}."
    return "Deal not found."

### --- Resources ---

@mcp.resource("crm://contacts/all")
def list_all_contacts() -> str:
    """Get a raw list of all contacts in the system."""
    return str(db["contacts"])

@mcp.resource("crm://stats")
def get_crm_stats() -> str:
    """Get a quick summary of CRM health."""
    lead_count = len([c for c in db["contacts"] if c["status"] == "Lead"])
    total_revenue = sum(d["amount"] for d in db["deals"] if d["stage"] == "Closed Won")
    return f"Leads: {lead_count} | Total Revenue: ${total_revenue}"

if __name__ == "__main__":
    mcp.run()