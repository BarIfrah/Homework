# Seagate Home Assignment
**By Bar Ifrah - ifrahbarm@gmail.com**

### Part one: Ladder Jumps
This part required a recursive function that solves a ladder jumps problem.\
This was a fibonacci sequence problem with a nice costume.\
1a. A recursive function that solves the problem\
1b. Describes the recursion calls on the run.
I'll go left-to-right\
8 calls 7 and 6\
7 calls 6 and 5\
6 calls 5 and 4\
5 calls 4 and 3\
4 calls 3 and 2\
3 calls 2 and 1, returns 3\
4 returns 3's result's- 3 + 2 --> 5\
5 returns 4's result's- 5 + 3's result's- 3 --> 8\
6 returns 5's result's- 7 + 4's result's- 5 --> 13\
7 returns 6's result's- 13 + 5's result's- 8 --> 21\
**Now to right side:**\
6 calls 5 and 4\
5 calls 4 and 3\
4 calls 3 and 2\
3 calls 2 and 1, returns 3\
4 returns 3's result's- 3 + 2 --> 5\
5 returns 4's result's- 5 + 3's result's- 3 --> 8\
6 returns 5's result's- 7 + 4's result's- 5 --> 13\
**8 returns 7's result's- 21 + 6's result's- 13 --> 34**\

1c. The improvements made to the original recursive function. The main improvement is\
The main improvement is the dictionary that stores passed calls and their results,\
so when we reach the certain value we return its dictionary value instead of computing all over again.\

Tree visit is "post-order"ish (ish because its not really a binary tree). Tree scheme attached as PDF.\
![GIF of postorder visit](https://miro.medium.com/max/1000/1*UGrzA4qtLCaaCiNAKZyj_w.gif)
### Part two: Maximum Subarray
In this part I'm using a variation of Kadane's algorithm.\
Using one iteration as required.
