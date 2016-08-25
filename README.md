# Tic Tac Toe

A first shot simple implementation of tic tac toe for use in browser. The server side is implemented in python using a Flask micro-service. The client side uses jquery for formatting and interaction with the server.

Opponent play is provided by a simple minmax algorithm with some early game pruning. At the moment, after the first move, a full tree search is made. With slightly more work many of the branches could be pruned using ab pruning and other heuristics and the matrix operations vectorized using Numpy or the like for speed but the permutation count is low enough that it would have little effect on user experience.

The algorithm should play a perfect game-- i.e. win or draw every game.
Dependencies
-----------
You will need to install the flask library.
```
$pip install flask
```
All other dependencies should be included in the python standard library >= 2.7

Usage
-----
In shell, run:

```
$python tic_tac_flask.py
```

Go to the URL shown in response to the command.
The player always gets the first move, and the board immediately clears upon a draw or win by either the player or the algorithm.

Enjoy!