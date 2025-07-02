# ADK‑AGENT

> **ADK‑AGENT** is a demo project that shows how to expose a SQLite database as a set of Model Context Protocol (MCP) tools using **Google’s Agent Development Kit (ADK)** and **FastMCP**. It enables an interactive AI agent—accessible via a browser interface—to perform database operations like creating tables, viewing rows, and more through natural conversation.

---

## ✨ Key Features

| Feature                  | Description                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| **💬 Chat UI (ADK Web)** | You can interact with the AI agent using natural language via a local web interface.                  |
| **🔌 ADK Tooling**       | Functions are decorated with `@mcp.tool()` so they automatically become ADK tools.                    |
| **📜 FastMCP Server**    | `server.py` creates a FastMCP server that allows the agent to communicate with the database tools.    |
| **🗄️ SQLite Storage**   | Uses a local SQLite database (path configurable via `DB_PATH` env var). No external service required. |
| **🧪 Example CRUD**      | Sample tools for `create_table`, `list_tables`, `view_rows`, `insert_row`, `delete_row`, etc.         |

---

## 📁 Repository Layout

```
ADK-AGENT/
├─ Database-Agent/
│  ├─ agent.py          # Launches the ADK web frontend (chat interface)
│  ├─ server.py         # Hosts FastMCP server that registers database tools
│  ├─ db_utils.py       # SQLite helper layer (get_conn, create/init helpers)
│  └─ requirements.txt  # Project Python dependencies
└─ README.md            # ← you are here
```

---

## 🚀 How It Works

1. **Run the ADK Web Agent**

   ```bash
   python agent.py
   ```

   This launches a web-based chat interface (ADK Web) hosted locally.

2. **Start the FastMCP Tool Server** In a separate terminal:

   ```bash
   python server.py
   ```

   This exposes a set of database tools (via MCP) that the AI agent can call.

3. **Interact with Your AI Agent**

   * Open the URL shown in the terminal (e.g., `http://127.0.0.1:8000` or ADK Web link).
   * Ask natural language questions like:

     > "Create a table named users with columns id and name" "Show all rows in the 'users' table"

The AI agent calls MCP tools through FastMCP (`server.py`) to perform the operations on your SQLite database.

---

## 🛠️ Available Tools

| Tool                           | Signature                               | Purpose                                                          |
| ------------------------------ | --------------------------------------- | ---------------------------------------------------------------- |
| `list_tables()`                | `()-> List[str]`                        | List all user‑defined tables.                                    |
| `create_table(table, columns)` | `(str, List[str])-> str`                | Create a new table with column definitions.                      |
| `view_rows(table)`             | `(str)-> Tuple[List[str], List[Tuple]]` | Return column names & all rows.                                  |
| `insert_row(table, values)`    | `(str, List[Any])-> str`                | Insert a row (not shown in convo but included for completeness). |
| `delete_row(table, where)`     | `(str, str)-> str`                      | Delete rows that match a WHERE clause.                           |

---

## 📝 Configuration

You can configure values via environment variables or a `.env` file:

| Variable       | Default         | Description                    |
| -------------- | --------------- | ------------------------------ |
| `DB_PATH`      | `./database.db` | SQLite file location.          |
| `FASTMCP_PORT` | `8000`          | Port to expose the MCP server. |

To use a `.env` file:

```bash
DB_PATH=./database.db
```

---

## 📦 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/jeetezh/ADK-AGENT.git
   cd ADK-AGENT/Database-Agent
   ```

2. **Create and activate a virtual environment** (optional)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run both agent and tool server as shown above.**

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Commit your changes (`git commit -m "feat: add cool stuff"`)
4. Push to GitHub (`git push origin feat/my-feature`)
5. Open a pull request 😀

---

## 📄 License

This project is licensed under the **MIT License** – see `LICENSE` for details.

---

## 🙏 Acknowledgements

* [Agent Development Kit (ADK)](https://github.com/google/adk-python)
* [FastMCP](https://github.com/jlowin/fastmcp)
* SQLite — the zero‑config SQL database

---

> *Built with ❤️ by ****Jeetesh R**** as a learning project on July 2025.*
