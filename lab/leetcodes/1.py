def twosum(nums, target):
    d={}
    ret =[]
    for i, val in enumerate(nums):
        if target -val in d:
            ret.append(i)
            ret.append(d[target-val])
            return ret
        d[val]=i
arr =[12,3,4,5,7]
print(twosum(arr, 9))