# QUICK SORT
- It is based on Divide and Conquer Paradigm.
- It is not inplace and not stable sort.
- It is the most practically used algorithm.
- It consumes relatively lower resources during execution.

## Algorithm
```md
quicksort(A,P,R)
{
  if(P < R)
  {
    Q = partition(A, P, R);
    quicksort(A, P, Q-1);
    quicksort(A, Q+1, R);
  }
}
```
