"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . 
Please use list comprehensions rather than multiple loops, as a learning exercise.
ex
1
1
1
2
o/p
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
    print(l)
    

   ###Alter Nate Methong without Using Comprehensions###
x = int(input())
y = int(input())
z = int(input())
n = int(input())
for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
	  ##if ((i+j+k) != n):
      if((i+j+k)!= n):
        print([[i,j,k]])
