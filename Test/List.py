Nums = [11,56,21,58,45,78,12,34,90]
print("Original List: ",Nums) 

Nums.sort()
print("Sorted List: ",Nums)

Names = ['Saurabh','Dipak','Satish']
print("Original List: ",Names)

Names.sort()
print("Sorted List: ",Names)

mix = Nums + Names
print("Mixed List: ",mix)

mix.append('67')    
print("Mixed List after append: ",mix)

mix.pop(0)
print("Mixed List after pop: ",mix)

mix.reverse()
print("Mixed List after reverse: ",mix)

min = min(Names)
print("Minimum of Names: ",min)

sum1 = sum(Nums)
print("Sum of Mixed List: ",sum1)

type1 = type(Nums)
print("Type of Nums: ",type1)