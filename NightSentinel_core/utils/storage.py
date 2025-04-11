import sqlite3
import threading
from hashlib import sha256
import orjson
from lxml import html

class SQLiteStorageSystem:
    """Thread-safe SQLite storage system for managing web elements."""
    def __init__(self, storage_file: str, url: str = None):
        self.storage_file = storage_file
        self.url = url
        self.lock = threading.Lock()
        self.connection = sqlite3.connect(self.storage_file, check_same_thread=False)
        self.connection.execute("PRAGMA journal_mode=WAL")
        self.cursor = self.connection.cursor()
        self._setup_database()

    def _setup_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS storage (
                id INTEGER PRIMARY KEY,
                url TEXT,
                identifier TEXT,
                element_data TEXT,
                UNIQUE (url, identifier)
            )
        """)
        self.connection.commit()

    def save(self, element: html.HtmlElement, identifier: str):
        """Saves the unique properties of a web element."""
        element_data = orjson.dumps(self._element_to_dict(element))
        with self.lock:
            self.cursor.execute("""
                INSERT OR REPLACE INTO storage (url, identifier, element_data)
                VALUES (?, ?, ?)
            """, (self.url, identifier, element_data))
            self.connection.commit()

    def retrieve(self, identifier: str):
        """Retrieves the unique properties of a web element."""
        with self.lock:
            self.cursor.execute(
                "SELECT element_data FROM storage WHERE url = ? AND identifier = ?",
                (self.url, identifier)
            )
            result = self.cursor.fetchone()
            return orjson.loads(result[0]) if result else None

    def close(self):
        """Closes the database connection."""
        with self.lock:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def _element_to_dict(self, element):
        """Converts an HTML element to a dictionary."""
        if element is None:
            return {}
        return {
            'tag': element.tag,
            'attributes': element.attrib,
            'text': element.text,
            'tail': element.tail
        }