
from flask import Flask,render_template,jsonify,request
from tic_tac_engine import tac_game

tac_app = Flask(__name__)


board = {'player':[],
		 'algo':[]
		}

@tac_app.route("/algo_play",methods = ['GET','POST'])
def algo_play():

	the_move = request.args.get('the_move')

	if the_move in board['player'] or the_move in board['algo']:
		return jsonify(error='occupied')

	board['player'].append(the_move)
	game_state = tac_game(board)
	game_winner_player = game_state.check_winner(board)[0]
	#print game_winner_player
	if game_winner_player == 'player':
		del board['player'][:]
		del board['algo'][:]
		return jsonify(winner = game_winner_player)

	counter_move = game_state.get_move(opponent_type = 'random')
	board["algo"].append(counter_move)
	game_winner_algo = game_state.check_winner(board)[0]
	print counter_move,game_winner_algo
	if game_winner_algo == 'algo':
		del board['player'][:]
		del board['algo'][:]
		return jsonify(winner = game_winner_algo,the_move = counter_move)

	elif game_winner_algo == 'draw':
		del board['player'][:]
		del board['algo'][:]
		return jsonify(winner = 'draw')

	else:
		return jsonify(the_move = counter_move)
		

@tac_app.route("/")
def main():
	return render_template('tac_layout.html')

if __name__ == '__main__':
	tac_app.run()