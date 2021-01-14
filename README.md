# ChessOO

### Try to experiment with making an automated chess bot for the ASCII-Chess project using AI

## AI Creation thinking process

Most of the time was thinking about the logic for the AI Bot rather than actually coding, so there isn't as much tangible code here yet.
Wanted to use tensorflow, so I looked into that for a couple days but it's very complicated so I decided to use this instead --
Essentially, the computer will look at a certain set of moves, and then evaluate which is the best one out of them based on certain factors, and then execute the highest scoring move.

Factors to be taken into consideration

Checkmating
Capturing pieces
Checking
Defending own pieces / saving pieces
Controlling center

How to choose which moves to analyze
Depends on how long the run time of the actual scoring system is, if we need to lower the amound of moves checked to make it compute faster, then -

If a piece is being attacked
If a piece can attack an enemy piece
If a piece other than king can move away from the back line

Potentially have different systems for choosing moves in the beginning, mid, and endgame

Beginning - Focus more on moving pieces away from starting positions
Midgame - Focus on protecting pieces and attacking high value pieces
Endgame - Focus on protecting pieces, attacking high value pieces, protecting king, blocking enemy kings movement

Gamestate can be determined by piece values on board

Integrate into code when finished by adding a menu option that will start a normal game, but call this program to choose a move every time it is the computers turn.