def combi(nums, k):
    def dfs(idx, sub_list):
        if len(sub_list) == k:
            ans.append(sub_list)
            return

        for i in range(idx, len(nums)):
            dfs(i+1, sub_list + [nums[i]])
    ans=[]
    dfs(0, [])
    return ans

print(combi([x for x in range(1, 4+1)], 2))