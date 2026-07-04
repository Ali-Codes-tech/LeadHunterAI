import sqlite3


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("leadhunter.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS businesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                rating TEXT,
                reviews TEXT,
                phone TEXT,
                website TEXT,
                score TEXT
            )
        """)
        self.connection.commit()

    def save_business(self, business):
        self.cursor.execute("""
            INSERT INTO businesses
            (name, rating, reviews, phone, website, score)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            business["name"],
            business["rating"],
            business["reviews"],
            business["phone"],
            business["website"],
            business["score"]
        ))

        self.connection.commit()

    def get_all_businesses(self):
        self.cursor.execute("""
            SELECT
                name,
                rating,
                reviews,
                phone,
                website,
                score
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
                "score": row[5]
            })

        return businesses