# CRM Manager MCP Server

A Model Context Protocol (MCP) server that provides an interface to manage contacts, leads, and deal stages in a CRM environment. Built with the **FastMCP** framework, this server allows AI assistants (like Claude) to search your database, create leads, and track revenue stats in real-time.

## 🚀 Features

### **Tools**

Tools allow the AI to perform actions or fetch specific data based on user intent.

* **`Contacts`**: Search the database by name or email.
* **`create_lead`**: Programmatically add new entries to the contact list.
* **`update_deal_stage`**: Modify the status of active deals (e.g., moving from "Negotiation" to "Closed Won").

### **Resources**

Resources provide the AI with read-only context or "knowledge" documents.

* **`crm://contacts/all`**: A full dump of the contact database.
* **`crm://stats`**: A high-level summary of lead counts and total revenue.

---

## 🛠 Installation

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd crm-server

```


2. **Install dependencies**:
Ensure you have Python 3.10+ installed.
```bash
pip install mcp

```



---

## 💻 Usage

### **Running Locally**

To start the server manually for testing:

```bash
python crm_server.py

```

### **Claude Desktop Integration**

To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "crm-manager": {
      "command": "python",
      "args": ["/absolute/path/to/your/crm_server.py"]
    }
  }
}

```

---

## 📊 Data Schema

The server currently operates on a mock in-memory database with the following structure:

| Entity | Fields |
| --- | --- |
| **Contact** | `id`, `name`, `email`, `status` (Lead/Customer) |
| **Deal** | `id`, `contact_id`, `amount`, `stage` |

---

## 🧪 Example Prompts

Once connected, you can ask your AI assistant:

* "Search for Alice in the CRM."
* "Add a new lead: John Doe at john@doe.com."
* "What is our total revenue right now?" (This triggers the `crm://stats` resource).
* "Mark deal #1 as Closed Won."

---

## ⚖️ License

MIT

---
