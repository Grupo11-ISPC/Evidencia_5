import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "smarthome.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Habilitamos foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")

# ===== TABLAS =====
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    rol TEXT NOT NULL CHECK (rol IN ('admin','user'))
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dispositivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    estado INTEGER NOT NULL DEFAULT 0,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL
)
''')

