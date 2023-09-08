
import chess
import whatsappbot2 as wtb2

board = chess.Board()
while True:
	move = str(input())
	moves_t = str(board.legal_moves)[37:-1] # Get the tuple as string
	moves_t = moves_t.replace(", ", "', '") # Converting all the SAN names into strings
	moves_t = moves_t.replace("(", "('")
	moves_t = moves_t.replace(")", "')")
	moves_t = eval(moves_t) # Using eval function to turn into tuple
	moves = [] # Creates list to store values
	for i in moves_t: # Go through all values
		moves.append(i)
	if move in moves_t:
		board.push_san(move)
		print('')
		print('')
		print(board)
		wtb2.SendPos(board.fen())
		outcome = board.outcome()
		if outcome:
		    if outcome.winner == chess.WHITE:
		        print("white won")
		        exit()
		    elif outcome.winner == chess.BLACK:
		        print("black won")
		        exit()
		    else:
		        print("draw")
		        exit()
		print('')
		print('')

	else:
		print("the move you just inputed is not a legal move please input a legal move")