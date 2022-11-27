# Double Factorial

### Algorithm
```md
Step 1: START
Step 2: Take the number as input
Step 3: If number == 0 then retrun 1 and moves to Step 11
Step 4: If number == 1 then return 1 and moves to Step 11 
Step 5: If number is even and greater than 0 then moves to Step 7
Step 6: Moves to Step 11
Step 7: Compute: number * (number-2) * ... * 4 * 2 and moves to Step 11
Step 8: If number is odd and greater than 1 then moves to Step 10
Step 9: Moves to Step 11
Step 10: Compute: number * (number-2) * ... * 3 * 1
Step 11: STOP
```
