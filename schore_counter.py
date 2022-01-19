class ScoreCounter:
    player_1 = None
    player_2 = None
    mark = 'X'
    x_score = 0
    o_score = 0
    current_player = player_1

    @staticmethod
    def score_counter():
        return f'{ScoreCounter.player_1} : {ScoreCounter.player_2} - {ScoreCounter.x_score}' \
               f' : {ScoreCounter.o_score}'

    @staticmethod
    def change_current_player():
        ScoreCounter.current_player = ScoreCounter.player_2 if ScoreCounter.current_player == ScoreCounter.player_1 \
            else ScoreCounter.player_1
        return ScoreCounter.current_player

    @staticmethod
    def change_mark():
        ScoreCounter.mark = 'X' if ScoreCounter.mark == 'O' else 'O'
        return ScoreCounter.mark



