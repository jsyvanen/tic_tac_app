from itertools import permutations as permuter
from random import choice as rdm_choice

class tac_game(object):
    
    winning_combos = [   # Rows
                         ['a'+ str(z) for z in range(1,4)],
                         ['b'+ str(z) for z in range(1,4)],
                         ['c'+ str(z) for z in range(1,4)],
                         # Columns
                         [z + '1' for z in 'abc'],
                         [z + '2' for z in 'abc'],
                         [z + '3' for z in 'abc'],
                         # Diagonal
                         [z + str('abc'.index(z) + 1) for z in 'abc'],
                         [z + str('cba'.index(z) + 1) for z in 'cba']   
                     ]
    
    complete_board = [a + str(b) for a in 'abc' for b in range(1,4)]

    def __init__(self,board = None):
        self.board = board

    def check_winner(self,board):
        for player in board.keys():
            board_state = list(permuter(board[player],3))
            for pos_win_combo in board_state:
                if list(pos_win_combo) in self.winning_combos:
                    return (player,1 if player == 'algo' else -1)
                else:
                    continue
        if len(board['player']) + len(board['algo']) == len(self.complete_board):
            return ('draw',0)
        else:
            return ('no',0)
        

    def get_move(self,opponent_type = None):
        choice_set = self.get_choice_set(self.board)
        if opponent_type == 'random':
            if len(choice_set) > 0:
                return rdm_choice(choice_set)
            else:
                return 'na'

        elif opponent_type == 'minmax':
            return self.iterate_moves(self.board,'algo')
            
    def get_choice_set(self,board):
        return [a for a in self.complete_board if a not in board['player'] and a not in board['algo']]

    def augment_state(self,player,move,direction=''):
        if direction == 'progress':
            self.board[player].append(move)
        else:
            self.board[player].remove(move)
    
    def switch_player(self,player):
        if player == 'algo':
            return 'player'
        else:
            return 'algo'
    
    def minimax(self,game_state,player):
        game_winner,score = self.check_winner(game_state)
        if game_winner in ('draw','algo','player'):
            return score
        if player == 'player':
            best_move = -2
        else:
            best_move = 2
        choice_set = self.get_choice_set(game_state)
        player = self.switch_player(player)
        for move in choice_set:
            self.augment_state(player,move,direction='progress')
            opp_ret_val = self.minimax(game_state, player)
            self.augment_state(player,move,direction='regress')
            if player == 'algo':
                if opp_ret_val > best_move:
                    best_move = opp_ret_val
            else:
                if opp_ret_val < best_move:
                    best_move = opp_ret_val
        return best_move
    
    def iterate_moves(self,game_state,player):
        game_winner,score = self.check_winner(game_state)
        baseline_score = -2
        choice_set = self.get_choice_set(game_state)
        if 'b2' in choice_set:
            return 'b2'
        elif 'b2' not in choice_set and len(choice_set) == 8:
            return rdm_choice(['a1','a3','c1','c3'])
        return_moves = []
        for move in choice_set:
            self.augment_state(player,move,direction='progress')
            opp_ret_val = self.minimax(game_state,player)
            self.augment_state(player,move,direction='regress')
            if opp_ret_val >= baseline_score:
                baseline_score = opp_ret_val
                return_moves.append((move,opp_ret_val))
        best_return_moves = [a[0] for a in return_moves if a[1] == max([a[1] for a in return_moves])]
        return rdm_choice(best_return_moves)