# [Problem C: Woozle Breeding](https://nbhspc22.kattis.com/contests/nbhspc22/problems/nbhspc22.woozlebreeding)

The latest trend in pandemic pets is the woozle fad. As we all know, woozles are small, cute, but sneaky and sharp-toothed creatures. Woozles breed only in early May. A given female woozle will mate with a single male woozle, but a given male woozle may mate with several females. Four months later, each bred female woozle gives birth to one baby woozle. By Christmas time, each young woozle has grown to its eventual size and is ready to be sold to its new home. A young woozle’s size is the average of the sizes of its parents.

Because woozles are in such demand, breeders like you are getting orders from customers already. Customers are fussy, and they specify the only acceptable size for the young woozle they want. As a breeder, you want to choose which of your males and females should be bred together, to meet the needs of as many of your customers as possible.

Your breeding stock consists of two male woozles and 10 female woozles.

## Input
The first line of the input contains the size of Male#1, the size of Male#2, and the number K of customer size requests. Each number is a positive integer, and a space separates numbers. Furthermore, both males’ sizes are even numbers no larger than 100, and K is at most 20.

Next, we have a line with ten positive integers separated from each other by single spaces. The first number gives the size of Female#1 in your breeding stock; the second gives the size of Female#2 in your breeding stock, and so forth. The females’ sizes are all even numbers and are at most 100.

Finally, we have a line with K positive integers separated from each other by single spaces. Each number gives the requested size of a young woozle, and each of these requested sizes is at most 100.

## Output
The output contains a single integer, which is the number of young woozles we can sell to the customers who have requested them. Remember, if a customer requests a particular size of woozle, the customer will only buy a young woozle of that size.

## Sample Input 1
```
2 10 3
4 4 4 4 4 4 4 4 8 8
2 3 5
```

## Sample Output 1
```
2
```

## Sample Input 2
```
2 10 3
10 4 4 4 4 4 4 4 4 4
6 10 6
```

## Sample Output 2
```
1
```
