class HighScores(object):
    """
    This contains all the high scores.
    """

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """
        Returns the last score in the score list
        """
        return self.scores[-1:][0]

    def personal_best(self):
        """
        Returns highest score
        """

        high_score = 0
        for score in self.scores:
            if score > high_score:
                high_score = score

        return high_score

    def personal_top(self):
        """
        Returns top three scores in descending order
        """

        top_scores = list(self.scores)
        top_scores.sort(reverse=True)
        return top_scores[:3]

    def report(self):
        """
        Reports latest score and compares it to highest score
        """

        latest_score = self.latest()
        highest_score = self.personal_best()
        message = f"Your latest score was {latest_score}."

        if latest_score < highest_score:
            message += (
                f" That's {highest_score - latest_score} short of your personal best!"
            )
        else:
            message += " That's your personal best!"

        return message
