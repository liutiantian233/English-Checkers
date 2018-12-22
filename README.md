# English-Checkers
English Checkers Artificial Intelligence

Will implement a classical board game called **Checkers** in Python using classes. **Checkers** is a group of strategy board games for two players which involve diagonal moves of uniform game pieces and mandatory captures by jumping over opponent pieces. The game is usually played on an 8x8 “checkered” board. For an 8x8 board, there are twelve black and twelve white identical game pieces called **Pawns** (or **Men**).

## Game Rules and Objective

Checkers is played by two opponents, on opposite sides of the game board. One player has the black pieces; the other has the white pieces. Players alternate turns. A player may not move an opponent's piece. A move consists of moving a piece diagonally (forward from the player’s side) to an adjacent unoccupied square. If the adjacent square contains an opponent's piece, and the square immediately beyond it is vacant, the piece may be captured (and removed from the game) by jumping over it. Only the dark squares of the checkered board are used. A piece may move only diagonally into an unoccupied square. Capturing is mandatory in most official rules. In almost all variants, the player without pieces remaining, or who cannot move due to being blocked, loses the game.

**Pawn/Man**: Uncrowned pieces, i.e pawns, move one step diagonally forwards, and capture an opponent's piece by moving two consecutive steps in the same line, jumping over the piece on the first step. Multiple enemy pieces can be captured in a single turn provided this is done by successive jumps made by a single piece; the jumps do not need to be in the same line and may "zigzag" (change diagonal direction). In English Checkers pawns can jump only forwards.

**Kings**: When a pawn reaches the kings row (also called crownhead, the farthest row forward), it becomes a king, and is marked by placing an additional piece on top of the first pawn, and acquires additional powers including the ability to move backwards and (in variants where they cannot already do so) capture backwards. Like pawns, a king can make successive jumps in a single turn provided that each jump captures an enemy pawn or king. More details on this game can be found here:
