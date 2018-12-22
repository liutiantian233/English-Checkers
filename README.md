# English-Checkers
**English Checkers Artificial Intelligence**

Will implement a classical board game called **Checkers** in Python using classes. **Checkers** is a group of strategy board games for two players which involve diagonal moves of uniform game pieces and mandatory captures by jumping over opponent pieces. The game is usually played on an 8x8 “checkered” board. For an 8x8 board, there are twelve black and twelve white identical game pieces called **Pawns** (or **Men**). -- [Wikipedia](https://en.wikipedia.org/wiki/Draughts)

## Game Rules and Objective

Checkers is played by two opponents, on opposite sides of the game board. One player has the black pieces; the other has the white pieces. Players alternate turns. A player may not move an opponent's piece. A move consists of moving a piece diagonally (forward from the player’s side) to an adjacent unoccupied square. If the adjacent square contains an opponent's piece, and the square immediately beyond it is vacant, the piece may be captured (and removed from the game) by jumping over it. Only the dark squares of the checkered board are used. A piece may move only diagonally into an unoccupied square. Capturing is mandatory in most official rules. In almost all variants, the player without pieces remaining, or who cannot move due to being blocked, loses the game.

**Pawn/Man**: Uncrowned pieces, i.e pawns, move one step diagonally forwards, and capture an opponent's piece by moving two consecutive steps in the same line, jumping over the piece on the first step. Multiple enemy pieces can be captured in a single turn provided this is done by successive jumps made by a single piece; the jumps do not need to be in the same line and may "zigzag" (change diagonal direction). In English Checkers pawns can jump only forwards.

**Kings**: When a pawn reaches the kings row (also called crownhead, the farthest row forward), it becomes a king, and is marked by placing an additional piece on top of the first pawn, and acquires additional powers including the ability to move backwards and (in variants where they cannot already do so) capture backwards. Like pawns, a king can make successive jumps in a single turn provided that each jump captures an enemy pawn or king.

More details on this game can be found here: -- [Wikipedia](https://en.wikipedia.org/wiki/Draughts)

**Learning Objectives**
- Class
- just Class
- important Class

-------------------

## The game play:
Unfortunately we don't have any nice user interface for the game. What you are going to implement is a text based command line interface. When you start/run the game, it will look like this:
```python
"""
  ____ _               _                     
 / ___| |__   ___  ___| | _____ _ __ ___    
| |   | '_ \ / _ \/ __| |/ / _ \ '__/ __|    
| |___| | | |  __/ (__|   <  __/ |  \__ \    
 \____|_| |_|\___|\___|_|\_\___|_|  |___/    
Developed by The TianTian Inc.
About The AI
Michigan State University
East Lansing, MI, USA.
"""
```

## Pick a color:
First the game will ask for which color you are going to choose, then you type **black** or **white**. Once chosen yours and opponent's color are fixed. **In our case, *black* will always play the first move.** In our case the pawns will be denoted by **b** and **w**, the kings will be denoted by **B** and **W** (for black and white respectively). The board is composed of 8x8 “cells” and initialized with 12 black and 12 white pieces (for 10x10 board there will be 20 black and 20 white pieces etc.). In the starting position the pieces are placed on the first three rows closest to the players. This leaves two central rows empty. The whites will be placed at the bottom rows and blacks on the top. The last white row will start from the bottom left corner and the pieces will be placed by skipping every other cell. The rows on the board is numbered as **a, b, c, ..., h** and the columns as **1, 2, 3, ..., 8** etc.
![image](https://github.com/liutiantian233/English-Checkers/blob/master/Figure0.png)

## Game Commands:
In order to play the game, there is a set of commands that you are going to use (i.e. type at the prompt) --
- **exit** If you type exit on the prompt, the game will exit by showing the final outcome of the game.
- **pass** If you type pass, this will cause you to give up the game and admit defeat, no winning condition will be checked.
- **move x y** This command will move a piece from position **x** to **y**, where **x** and **y** are diagonal to each other. Each position is denoted with a string board position like **'a2'**, **'c4'** etc. Each pawn only can move forward diagonals., but kings can move either forward or backward diagonals.
> **Invalid moves will trigger Exceptions accordingly**
- **jump x y** This command will cause a piece to jump from position **x** to **y**, where **x** and **y** are diagonals that are one cell away. This command will be used to capture an opponent piece between the positions **x** and **y**.
> **This command will also display similar message on the event of an invalid jump.**
- **hints** If you type this command it’s going to show the moves or jumps that you have on the board. If there are jumps, no move is allowed and **hints** will show them accordingly.
- **apply n** when you type hints, it’s going to show you the available m number of moves (or jumps) numbered from **1**. If you type **apply n** then **n-th** move (or jump) from the hints will be applied to the board.
- **When the game finishes, the program will end the game by declaring the winner with the difference in the number of piece count.**

-------------------

**If you run the program (main.py), the game will start**

## Feedback and suggestions
- E-mail：<liutia20@msu.edu>

---------
Thanks for reading this help document
