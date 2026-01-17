# Smart Calendar

This is a month-based calendar system that supports persistent notes.

How it works:
1. The backend constructs a full calendar grid for a given month.
2. The grid always starts on Sunday and ends on Saturday.
3. Days outside the selected month are still shown but dimmed.
4. Today is highlighted automatically.
5. Notes are stored in a JSON file (`calendar_notes.json`) on the server.
6. Notes persist across page refreshes and server restarts.
