import os
import sqlite3
from contextlib import closing  # sorgt dafür, dass Verbindungen sauber geschlossen werden


class BaseDal:
    def __init__(self, db_connection_str: str = None):
        # Wenn kein Verbindungsstring übergeben wurde, versuche ihn aus der Umgebungsvariable DB_FILE zu lesen
        if db_connection_str is None:
            self.__db_connection_str = os.environ.get("DB_FILE")
            if self.__db_connection_str is None:
                raise Exception("DB_FILE environment variable and parameter path is not set.")
        else:
            # Ansonsten verwende den übergebenen Pfad zur Datenbank
            self.__db_connection_str = db_connection_str

    def get_connection(self):
        # Öffnet eine neue SQLite-Verbindung und aktiviert automatische Datums-Konvertierung (DATE zu datetime.date)
        return sqlite3.connect(self.__db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple | None = ()):
        # Führt eine SELECT-Abfrage aus und gibt genau einen Datensatz zurück
        with closing(self.get_connection()) as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchone()  # gibt ein Tupel zurück oder None
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def fetchall(self, sql: str, params: tuple | None = ()) -> list:
        # Führt eine SELECT-Abfrage aus und gibt eine Liste aller Treffer zurück
        with closing(self.get_connection()) as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchall()  # gibt Liste von Tupeln zurück
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def execute(self, sql: str, params: tuple | None = ()) -> (int, int):
        # Führt eine INSERT/UPDATE/DELETE-Abfrage aus
        with closing(self.get_connection()) as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)  # SQL-Anweisung mit Platzhaltern (?, ?, ...)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()  # Bestätigt die Änderungen in der Datenbank
            finally:
                cur.close()
        return cur.lastrowid, cur.rowcount  # Gibt ID der letzten eingefügten Zeile + Anzahl betroffener Zeilen zurück
