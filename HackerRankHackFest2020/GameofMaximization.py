#HackerRank HackFest 2020
#Game of Maximization
def maxStones(Lis):
    UpLis = Lis[0::2]
    DownLis = Lis[1::2]
    UpSum = sum(UpLis)
    DownSum = sum(DownLis)
    if DownSum<UpSum:
        print(DownSum*2)
    else:
        print(UpSum*2)
NP = int(input())
Lis = list(map(int,input().split()))
maxStones(Lis)



"""
There are  piles of stones, where the  pile has  stones. You need to collect the maximum number of stones from these piles, but you must fulfill the following condition:

Let's say you pick  stones from the  pile, then

For example, if  and , you can pick the stones as  becuase  and 

Find the maximum total number of stones you can pick.

Input Format

The first line of input contains a single integer  denoting the number of piles.

The second line of input contains  space separated integers , where the  integer denoted the number of stones in  pile.

Constraints

Output Format

Print a single integer denoting the maximum total number of stones you can pick.

Sample Input 0

4
5 1 1 4
Sample Output 0

10
Explanation 0

Let . hence  and total number of stones picked is . It can be checked that its not possible to pick any greater number of stones.

Sample Input 1

3
2 1 2
Sample Output 1

2
Explanation 1

Let . Hence , and the total number of stones picked is .
"""
