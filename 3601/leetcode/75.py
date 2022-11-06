nums=[2,0,2,1,1,0]
a,b,c=nums.count(0),nums.count(1),nums.count(2)
new_nums=[]
new_nums=[0]*a+[1]*b+[2]*c
print(new_nums)
a=new_nums
print(a)