#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    This scales directly with input size.

b) O(n log n)
    As the input grows, the number of operations increase. Making this n log n.

c) O(n!)
    This one will recur infinitely because unless you start at 1 or 0, the loop will cycle forever. If it's 0, it passes immediately. If it's 1, it becomes 0 entering the second pass before it hits the recursion. If it's 2 or greater, it hits the recursion and loops infinitely. This makes it exponential.
## Exercise II

1. Remember the lowest floor and the highest floor of the building. 
2. Start in the middle of these floors and drop an egg. 
3. If the egg cracks, our guess was too high. Our highest floor is now the current floor.
4. Go down to the middle floor between our current highest and the lowest. Repeat until the egg doesn't crack. When the egg doesn't crack, this floor is now our current lowest floor. 
6. Move to the middle floor between the highest and lowest floors and drop an egg. If it cracks, this is now our current highest. Repeat step 4.
7. Repeat this process of finding your highest and lowest until there is only one floor left. 

This would be log(n) as the number of processes increases very slowly compared to the number of floors.

