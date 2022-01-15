def permute(nums):
    def dfs(cur_list, remain_list):
        if len(cur_list) == len(nums):
            ans.append(cur_list)

        for i, num in enumerate(remain_list):
            dfs(cur_list + [num], remain_list[:i] + remain_list[i+1:])
    ans=[]
    dfs([], nums)
    return ans

print(permute([x for x in range(1, 3+1)]))