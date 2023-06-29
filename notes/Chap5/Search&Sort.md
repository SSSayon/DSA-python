# 搜索和排序

## 搜索

### 顺序搜索、二分搜索

### 散列 (Hash)

#### Hash table

- It is an abstract data type (ADT) that **maps keys to values**. A hash table uses a **hash function** to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

  Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ **an imperfect hash function**, which might cause **hash collisions** where the hash function generates the same index for more than one key. 

  *Hashing is an example of a* ***space-time tradeoff.***  

- **Load Factor (载荷因子)** 
  $$
  \text{load factor} \quad \lambda = \frac{n}{m},
  $$
  where $n$ is the the number of keys, $m$ is the number of buckets. $0.6 < \lambda < 0.75$ is acceptable.

#### Hash function

- A hash function may be considered to perform three functions:

  - Convert variable-length keys into **fixed length** (usually machine word length or less) values, by folding them by words or other units using a parity-preserving operator like ADD or XOR.
  - Scramble the bits of the key so that the resulting values are **uniformly distributed** over the keyspace.
  - Map the key values into ones **less than or equal to the size** of the table.

  A good hash function satisfies two basic properties: 1) it should be very fast to compute; 2) it should minimize duplication of output values (collisions). 

- **Testing and measurement**

  - **Chi-Squared Test (卡方检验)** 

    $\dfrac{\sum_{j=0}^{m-1}\left(b_j\right)\left(b_j+1\right) / 2}{(n / 2 m)(n+2 m-1)} \in (0.95, 1.05)$ indicates the hash function has an expected **uniform distribution**, where $b_j$ is the number of items in bucket $j$. 

  -  **Strict Avalanche Criterion (严格雪崩准则)**

    Whenever **a single input bit** is complemented, **each of the output bits** changes with a **50%** probability. 

    <img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/image-20230629195043785.png" alt="image-20230629195043785" style="zoom: 67%;" />

#### Hash collision

- when two pieces of data in a hash table share the same hash value

- Collision Resolution

  - **Open addressing (开放定址法)** 

    Cells in the hash table are assigned one of three states in this method – occupied, empty, or deleted. If a hash collision occurs, the table will **be probed to move the record to an alternate cell that is stated as empty.** 

    -  linear probing (线性探测), double hashing (双散列), quadratic probing (平方探测)

    采用线性探测策略，搜索成功的平均比较次数为 $\dfrac12\left(1+\dfrac{1}{1-\lambda}\right)$，搜索失败的平均比较次数为 $\dfrac12 \left[1+\left(\dfrac{1}{1-\lambda}\right)^2\right]$.

  - **Separate chaining (分离链接法)** 

    If two records are being directed to the same cell, both would go into that cell **as a linked list.** 

    搜索成功的平均比较次数为 $1 + \dfrac{\lambda}{2}$，搜索失败的平均比较次数为 $\lambda$.

#### Implement ADT Map using Hash table 用哈希表实现映射

- 实现 `key` 为整数，`Hash function` 为取余函数的简单情形

- `HashTable` 类的实现

  ```python
  class HashTable:
      def __init__(self):
          self.size = 11 # 素数
          self.slots = [None] * self.size
          self.data = [None] * self.size
  
      def put(self, key, data): # 处理冲突时，采用线性探测法
          hashvalue = self.hashfunction(key, len(self.slots))
  
          if self.slots[hashvalue] == None:
              self.slots[hashvalue] = key
              self.data[hashvalue] = data
          else:
              if self.slots[hashvalue] == key:
                  self.data[hashvalue] = data
              else:
                  nextslot = self.rehash(hashvalue, len(self.slots))
                  while self.slots[nextslot] != None and \
                  		self.slots[nextslot] != key:
                      nextslot = self.rehash(nextslot, \ 
                                             len(self.slots))
  
                  if self.slots[nextslot] == None:
                      self.slots[nextslot] = key
                      self.data[nextslot] = data
                  else:
                      self.data[nextslot] = data
  
      def hashfunction(self, key, size): # 采用简单的取余函数
          return key % size
  
      def rehash(self, oldhash, size):
          return (oldhash + 1) % size
  
      def get(self, key):
          startslot = self.hashfunction(key, len(self.slots))
  
          data = None
          stop = False
          found = False
          position = startslot
          while self.slots[position] != None and \ 
          		not found and not stop:
              if self.slots[position] == key:
                  found = True
                  data = self.data[position]
              else:
                  position=self.rehash(position, len(self.slots))
                  if position == startslot:
                      stop = True
          return data
  
      # 重载了 __getitem__ 和 __setitem__ , 以通过 [] 进行访问
      def __getitem__(self, key):
          return self.get(key)
  
      def __setitem__(self, key, data):
          self.put(key, data)
  ```


## 排序

### 冒泡排序、选择排序

### 插入排序、希尔排序 (Shell sort)

#### 插入排序

- 图示

<center class="half">
<img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/insertionSort1.png" width=300/>
<img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/insertionSort2.png" width=300/>
</center>

#### 希尔排序

- 希尔排序也称“递减增量排序”，它对插入排序做了改进，将列表分成数个子列表，并**对每一个子列表应用插入排序**。**如何切分列表**是希尔排序的关键——并不是连续切分，而是使用增量 $i$ 选取所有间隔为 $i$ 的元素组成子列表。

  增量 $i$ 递减，最后一步 $i=1$，即为基本的插入排序（但已不需要多次比较或移动）。

- 先为 $n/2$ 个子列表排序，再对 $n/4$ 个子列表排序，...，采用这种增量的 Python 实现：

  ```python
  def shellSort(alist):
      sublistcount = len(alist) // 2
      while sublistcount > 0:
          for startposition in range(sublistcount):
              gapInsertionSort(alist, startposition, sublistcount)
          sublistcount = sublistcount // 2
  
  def gapInsertionSort(alist, start, gap):
      for i in range(start+gap, len(alist), gap):
          currentvalue = alist[i]
          position = i
          while position >= gap and \ 
          		alist[position-gap] > currentvalue:
              alist[position] = alist[position-gap]
              position = position-gap
          alist[position] = currentvalue
  ```

- most proposed gap sequences

![image-20230629204414057](https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/image-20230629204414057.png)

### 归并排序、快速排序

#### 快速排序

- 图示

  <img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/quickSort.png" alt="quickSort" style="zoom:50%;" />

- 时间复杂度：$O(n\log n)$，最坏情况 $O(n^2)$

  - 原因：分割点偏向某一端，导致切分不均匀；例如待排序列部分有序时

  - 优化：**选择基准值**，不再始终选择头部元素/尾部元素

    - 随机选取 `rand()` 

    - 三数取中法（考虑头元素、中间元素和尾元素）

- 进一步优化：处理重复数组时，时间复杂度仍是 $O(n^2)$

  - 优化方案：
    - 当待排序序列的长度分割到较小后，使用插入排序
    - 在一次分割结束后，可以把与基准值 `key` 相等的元素聚在一起，继续下次分割时，不用再对与 `key` 相等的元素分割

  - 实现
  
    ```python
    def quickSort(lst, low, high): # low, high 相向移动，按key分割
        first, last = low, high # first, last 固定不动，指向片段头尾
        left, right = low, high # left, right 指向=key的元素的两个边界
        leftLen, rightLen = 0, 0 # 记录两端各有多少=key的元素，实际即为 leftLen = left - first, rightLen = last - right
        
        if high - low + 1 < 10: # 短片段进行插排
            insertionSort(lst, low, high)
            return
        
        key = selectPivotMedianOfThree(lst, low, high) # 三数取中法
    
        while low < high: # 正常快排
            while high > low and lst[high] >= key:
                if lst[high] == key:
                    lst[right], lst[high] = lst[high], lst[right]
                    right -= 1
                    rightLen += 1
                high -= 1
            lst[low] = lst[high]
            while high > low and lst[low] <= key:
                if lst[low] == key:
                    lst[left], lst[low] = lst[low], lst[left]
                    left += 1
                    leftLen += 1
                low += 1
            lst[high] = lst[low]
        lst[low] = key
        
        # 将两端=key的元素移到中间key的左右
        i, j = low - 1, first 
        while j < left and lst[i] != key:
            lst[i], lst[j] = lst[j], lst[i]
            i -= 1
            j += 1
        i, j = low + 1, last
        while j > right and lst[i] != key:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
            
        # 中间一列=key的片段不再参与排序
        quickSort(lst, first, low - 1 - leftLen) 
        quickSort(lst, low + 1 + rightLen, last)
        
    def selectPivotMedianOfThree(lst, low, high):
        mid = (low + high) // 2
        if lst[mid] > lst[high]:
            lst[mid], lst[high] = lst[high], lst[mid]
        if lst[low] > lst[high]:
            lst[low], lst[high] = lst[high], lst[low]
        if lst[mid] > lst[low]:
            lst[mid], lst[low] = lst[low], lst[mid]
        return lst[low]
    
    def insertionSort(lst, low, high):
        for i in range(low + 1, high + 1):
            key = lst[i]
            j = i - 1
            while j >= low and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
    ```
  
  - 优化效果（C++; 数组大小 100 万）
    | 算法 | 随机数组 | 升序数组 | 降序数组 | 重复数组 |
    | --- | --- | --- | --- | --- |
    | 固定基准值 | $133 \mathrm{~ms}$ | $745125 \mathrm{~ms}$ | $644360 \mathrm{~ms}$ | $755422 \mathrm{~ms}$ |
    | 随机基准值 | $218 \mathrm{~ms}$ | $235 \mathrm{~ms}$ | $187 \mathrm{~ms}$ | $701813 \mathrm{~ms}$ |
    | 三数取中 | $141 \mathrm{~ms}$ | $63 \mathrm{~ms}$ | $250 \mathrm{~ms}$ | $705110 \mathrm{~ms}$ |
    | 三数取中+插入排序 | $131 \mathrm{~ms}$ | $63 \mathrm{~ms}$ | $250 \mathrm{~ms}$ | $699516 \mathrm{~ms}$ |
    | 三数取中+插排+聚集相等元素 | $110 \mathrm{~ms}$ | $32 \mathrm{~ms}$ | $31 \mathrm{~ms}$ | $10 \mathrm{~ms}$ |
    | STL 中的 Sort 函数 | $125 \mathrm{~ms}$ | $27 \mathrm{~ms}$ | $31 \mathrm{~ms}$ | $8 \mathrm{~ms}$ |
    

