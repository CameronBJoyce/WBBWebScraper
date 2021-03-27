class Game:
    def __init__(self, wofford_team, opposing_team, score, game_log):
        self.game_log = game_log
        self.score = score
        self.opposing_team = opposing_team
        self.wofford_team = wofford_team

    def set_score(self, score):
        self.score = score

    def return_score(self):
        return self.score
