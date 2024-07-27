### 191. Cutting Boards
Dificuldade: Difícil

[Link para enunciado completo](https://www.hackerrank.com/challenges/board-cutting/problem)

Enunciado:

Alice gives Bob a board composed of \(1 \times 1\) wooden squares and asks him to find the minimum cost of breaking the board back down into its individual squares. To break the board down, Bob must make cuts along its horizontal and vertical lines.

To reduce the board to squares, Bob makes horizontal and vertical cuts across the entire board. Each cut has a given cost, \( \text{cost\_y}[i] \) or \( \text{cost\_x}[j] \) for each cut along a row or column across one board, so the cost of a cut must be multiplied by the number of segments it crosses. The cost of cutting the whole board down into \(1 \times 1\) squares is the sum of the costs of each successive cut.

Can you help Bob find the minimum cost? The number may be large, so print the value modulo \(10^9 + 7\).

For example, you start with a \(2 \times 2\) board. There are two cuts to be made at a cost of \( \text{cost\_y}[1] = 3 \) for the horizontal and \( \text{cost\_x}[1] = 1 \) for the vertical. Your first cut is across 1 piece, the whole board. You choose to make the horizontal cut between rows 1 and 2 for a cost of \(1 \times 3 = 3\). The second cuts are vertical through the two smaller boards created in step 1 between columns 1 and 2. Their cost is \(2 \times 1 = 2\). The total cost is \(3 + 2 = 5\) and \(5 \% (10^9 + 7) = 5\).

### Function Description

Complete the `boardCutting` function in the editor below. It should return an integer.

`boardCutting` has the following parameter(s):

- `cost_x`: an array of integers, the costs of vertical cuts
- `cost_y`: an array of integers, the costs of horizontal cuts

Submissões: <br>
![image](https://github.com/user-attachments/assets/41ae9749-610e-40c2-b36d-d4c71cf2748e)
<br>
![image](https://github.com/user-attachments/assets/799016dc-f0f3-460c-a590-8fecfe482c8f)
