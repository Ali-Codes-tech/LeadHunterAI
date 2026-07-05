import csv
import os


class ExportService:

    def export_csv(self, businesses, filename):

        # Create exports folder if it doesn't exist
        os.makedirs("exports", exist_ok=True)

        filepath = os.path.join("exports", filename)

        with open(filepath, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Business",
                "Rating",
                "Reviews",
                "Phone",
                "Website",
                "Score"
            ])

            for item in businesses:

                writer.writerow([
                    item.get("name", ""),
                    item.get("rating", ""),
                    item.get("reviews", ""),
                    item.get("phone", ""),
                    item.get("website", ""),
                    item.get("score", "")
                ])

        return filepath