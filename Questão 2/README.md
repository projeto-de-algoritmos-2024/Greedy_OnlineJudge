### Sherlock and MiniMax
Dificuldade: Difícil

[Link para enunciado completo](https://www.hackerrank.com/challenges/sherlock-and-minimax/problem)

Enunciado:

Watson gives Sherlock an array of integers. Given the endpoints of an integer range, for all M in that inclusive range, determine the minimum(abs(arr[i]-M) for all 1 <= i <=|arr|). Once that has been determined for all integers in the range, return the M which generated the maximum of those values. If there are multiple 's that result in that value, return the lowest one.

For example, your array [3, 5, 7, 9] and your range is from p = 6 to q = 8 inclusive.

M	|arr[1]-M|	|arr[2]-M|	|arr[3]-M|	|arr[4]-M|	Min
6	   3		   1		   1		   3		 1
7	   4		   2		   0		   2		 0
8	   5		   3		   1		   1		 1
We look at the Min column and see the maximum of those three values is 1. Two M's result in that answer so we choose the lower value, .

### Function Description

Complete the sherlockAndMinimax function in the editor below. It should return an integer as described.

sherlockAndMinimax has the following parameters:
- arr: an array of integers
- p: an integer that represents the lowest value of the range for 
- q: an integer that represents the highest value of the range for 

### Input Format

The first line contains an integer , the number of elements in .
The next line contains  space-separated integers .
The third line contains two space-separated integers  and , the inclusive endpoints for the range of .

### Output Format

Print the value of M on a line.

Submissões: <br>
![image](Imagem da submissão)