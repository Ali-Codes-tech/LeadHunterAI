class FilterService:

    def filter_reviews(self, leads, maximum):

        return [
            lead
            for lead in leads
            if lead.reviews <= maximum
        ]

    def filter_rating(self, leads, maximum):

        return [
            lead
            for lead in leads
            if lead.rating <= maximum
        ]