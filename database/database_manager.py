import sqlite3


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect("leadhunter.db")
        self.cursor = self.connection.cursor()

        self.create_tables()

    # ===================================================
    # Create Tables
    # ===================================================

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS businesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                rating TEXT,
                reviews TEXT,
                phone TEXT,
                website TEXT,
                score TEXT,
                favorite INTEGER DEFAULT 0
            )
        """)

        self.connection.commit()

    # ===================================================
    # Save Business
    # ===================================================

    def save_business(self, business):

        self.cursor.execute("""
            INSERT INTO businesses
            (
                name,
                rating,
                reviews,
                phone,
                website,
                score,
                favorite
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            business.get("name", ""),
            business.get("rating", ""),
            business.get("reviews", ""),
            business.get("phone", ""),
            business.get("website", ""),
            business.get("score", ""),
            business.get("favorite", 0)
        ))

        self.connection.commit()

    # ===================================================
    # Get All Businesses
    # ===================================================

    def get_all_businesses(self):

        self.cursor.execute("""
            SELECT
                name,
                rating,
                reviews,
                phone,
                website,
                score,
                favorite
            FROM businesses
        """)

        rows = self.cursor.fetchall()

        businesses = []

        for row in rows:

            businesses.append({
                "name": row[0],
                "rating": row[1],
                "reviews": row[2],
                "phone": row[3],
                "website": row[4],
                "score": row[5],
                "favorite": row[6]
            })

        return businesses

    # ===================================================
    # Close Database
    # ===================================================

    def close(self):
        self.connection.close()