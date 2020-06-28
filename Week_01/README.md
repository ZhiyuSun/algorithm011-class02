# 学习笔记

### 如何刷题

1. 不要死磕

   确实，有很多算法题的思路很难想到，这时候就要果断放弃，去参考大牛们的解法，毕竟很多题目的解法都很巧妙，光靠埋头苦想肯定是得不到答案的，刷算法题也是一个学习的过程，遇到难的题目，不求第一遍全部理解，只要依葫芦画瓢地写出答案就行。先从模仿开始，至于理解，交给时间。

2. 多看高手代码

   在leetcode上，有很多别人的题解可以参照学习，除了国内站，国际站也应该需要多关注。另外，在学习别人的题解的过程中，除了解题思路，也要多关注算法的时间和空间复杂度，同时学会举一反三。

3. 构建体系

   将知识点分解，构建结构化的知识体系，推荐用脑图。

4. 刻意练习

   光是看懂了别人的算法思路还不够，要多动手，多刷题，把好的思路，好的解法转化为自己的。正确的刷题方式，不是看做题的数量，而是看做题的遍数，只有把一道题练到得心应手的程度，才算真正掌握。

5. 主动输出

   教授给别人是最好的学习方法。尝试把自己学到的知识，按自己的理解表达出来，假想如果要教给别人，你该怎么做，由此去增进自己对知识的理解。

### 刷题心得

下面，我会以这周练习的部分算法题举例，来谈一谈我的刷题心得。

### 爬楼梯

[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

> 假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。
>
> 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

面对这道题，乍一看会无从下手，其实，关键就是要找到其中的规律，把问题分成多个子问题。

如果爬1阶楼梯，只有1种方法

如果爬2阶楼梯，可以有“1阶 + 1阶”，“2阶”两种方法

如果爬3阶楼梯，可以有“1 阶 + 1 阶 + 1 阶”，“1 阶 + 2 阶”，“2 阶 + 1 阶”三种方法

……

爬上n阶楼梯的方法数量，等于2部分之和：

1. 爬上 n-1 阶楼梯的方法数量。因为再爬1阶就能到第n阶
2. 爬上 n-2 阶楼梯的方法数量，因为再爬2阶就能到第n阶

所以我们得到公式：*f*(*x*)=*f*(*x*−1)+*f*(*x*−2)。这道题实际上是斐波那契数列。

对于斐波那契数列算法的实现，也可以有多种写法。

1. 递归

   ```python
   class Solution:
       @functools.lru_cache(100)  # 缓存装饰器
       def climbStairs(self, n: int) -> int:
           if n == 1: return 1
           if n == 2: return 2
           return self.climbStairs(n-1) + self.climbStairs(n-2)
   ```

   这是一种非常经典的解法，但是要注意，因为递归会有很多的重复计算，需要加上缓存（在python中可以使用lru_cache的装饰器，或者构造一个字典来存储之前的变量），否则算法执行效率会特别低下。

2. 动态规划

   ```python
   class Solution:
       def climbStairs(self, n: int) -> int:
           if n==1 or n==2: return n
           a, b, temp = 1, 2, 0
           for i in range(3,n+1):
               temp = a + b
               a = b
               b = temp
           return temp
   ```

   如果递归是一种自顶向下的解法，那动态规划就是自底向上。通过观察递推公式，数组的每个值依赖于前面两个值，所以只需要两个临时即可，通过迭代来达到我们所需要的计算结果。



### 两数之和

[两数之和](https://leetcode-cn.com/problems/two-sum/)

> 给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

这是一道很经典的题，而且不像上一道需要找到特定规律，一般人总能想到一种解法，这就需要我们不断去减小算法时间复杂度和空间复杂度，探索最优解。

1. 暴力法

   ```python
   class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
           for i in range(len(nums)):
               for j in range(i+1,len(nums)):
                   if nums[i]+nums[j]==target:
                       return [i,j]
           return []
   ```

   

   这是最容易想到的答案。因为有双层循环，时间复杂度*O*(*n*2)，不是最优解

2. 利用哈希表

   ```python
   class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
           hashset={}
           for i in range(len(nums)):
               if hashset.get(target-nums[i]) is not None :
                   return [hashset.get(target-nums[i]),i]
               hashset[nums[i]]=i
   ```

   利用空间换时间的思路，构建一个哈希表，能够高效的从数组中查询到某个元素，查询效率从O(n)退化到O(1)。

   这是整个算法的复杂度讲到了O(n)

3. 双指针法

   ```python
   class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
           temp=nums.copy()
           temp.sort()
           i, j=0, len(nums)-1
           while i<j:
               if (temp[i]+temp[j])>target:
                   j=j-1
               elif (temp[i]+temp[j])<target:
                   i=i+1
               else:
                   break
           p=nums.index(temp[i])
           nums.pop(p)
           k=nums.index(temp[j])
           if k>=p:
               k=k+1
           return [p,k]
   ```

   先将数组排好序，再用两个指针从两端往中间靠拢，直至它们的和为预期值。

   算法时间复杂度为O(nlogn)。

在实际运行中，解法2和解法3的差别相差不大，但从理解上来说，解法2对这道题会更适合。另外，“**空间换时间**”和“**双指针法**”都是两种特别重要的思路，如能融会贯通，就能把这两种方法很好的运用到其他算法题中。

### 合并两个有序数组





