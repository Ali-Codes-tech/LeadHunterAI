class ScoreService:

    def calculate(self, lead):

        score = 0

        if lead.rating < 4:
            score += 25

        if lead.reviews < 30:
            score += 20

        if not lead.website:
            score += 20

        if not lead.email:
            score += 15

        return min(score, 100)