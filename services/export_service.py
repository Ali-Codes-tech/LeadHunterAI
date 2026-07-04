import csv


class ExportService:

    def export_csv(self, leads, filename):

        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Business",
                "Phone",
                "Website",
                "Rating",
                "Reviews",
                "Score"
            ])

            for lead in leads:

                writer.writerow([
                    lead.business_name,
                    lead.phone,
                    lead.website,
                    lead.rating,
                    lead.reviews,
                    lead.score
                ])