# 图 Graph

  ## 定义与实现

图 G = (V, E) ，其中 V 是顶点集合，E 是边集合

### 常用术语

- 顶点 (vertex)
  - 度数 / 入度、出度
- 边 (edge)
- 权重 (weight)
- 路径 (path)
- 环 (ring)
  - 无环图
    - 有向无环图 (DAG, directed acyclic graph)

### 实现

#### 方法

![image-20230708225553929](https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/20230708225601_image-20230708225553929.png)

#### 用邻接矩阵实现

<div style="display: flex; justify-content: center;">
  <div style="margin-right: 45px;">
    <img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/20230708225903_g.png" width="250" />
  </div>
  <div style="margin-left: 45px;">
    <img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/20230708225903_g1.png" width="250" />
  </div>
</div>

问题：矩阵稀疏，不高效

#### 用邻接表实现

<div style="display: flex; justify-content: center;">
  <div style="margin-right: 20px;">
    <img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/20230708225903_g.png" width="250" />
  </div>
  <div style="margin-left: 20px;">
    <img src="https://cdn.jsdelivr.net/gh/SSSayon/imgbed@main/img/20230708225928_g2.png" width="300" />
  </div>
</div>

为图对象的所有顶点保存一个主列表，同时为每一个顶点都维护一个列表（图中用了字典）记录与它相连的顶点。

具体实现见 [这里](.\graph.py) （ `Vertex` 类和 `Graph` 类）



## 宽度优先搜索 BFS

### 词梯问题



## 深度优先搜索 DFS

### 骑士周游问题

### 通用深度优先搜索

### 拓扑排序

根据有向无环图生成一个包含所有顶点的线性序列，使得如果图 G 中有一条边为 (v, w)，那么顶点 v 排在顶点 w 之前。在很多应用中，有向无环图被用于表明**事件优先级**。

- 算法
  1. 对图 G 调用 dfs ，计算每一个顶点的结束时间
  2. 基于结束时间，将顶点按照递减顺序存储在列表中
  3. 将有序列表作为拓扑排序的结果返回



## 强连通分量 SCC

在有向图 G 中，如果两点互相可达，则称这两个点*强连通*，如果 G 中任意两点互相可达，则称 G 是强连通图。非强连通有向图的极大强连通子图，称为*强连通分量* (SCC, Strongly Connected Component)。

把强连通分量中的所有顶点组合成单个顶点，**从而将图简化**。

### Tarjan 算法

- 算法：用栈跟踪已访问过的节点，`disc[v]` 记录顶点 v 的发现时间，`low[v]` 记录 v 或 v 的**子树**能够回溯到的最早的栈中节点。

  对图 G 调用 `dfs` ，对于每个未访问的顶点 v ：

  1. 将 `disc[v]` 和 `low[v]` 记录为当前 dfs 时间；增加 dfs 时间的计数

  2. 将 v 推入栈中

  3. 遍历顶点的邻居 neighbor：

     1. 若邻居未访问：

        1. 递归地对其 dfs 遍历
        2. 更新 `low[v]` ：`low[v] = min(low[v], low[neighbor])` 

     2. 若邻居在栈中：

        1. 更新 `low[v]` ：`low[v] = min(low[v], disc[neighbor])` 

        > > 注意为什么是 `disc[neighbor]` 而不是 `low` ！（仅仅求 SCCs 时好像无所谓，但在利用这一算法的其它情况下好像会出问题）

  4. 遍历完所有邻居后，检查当前顶点是否是一个强连通分量的根：

     若 `disc[v] == low[v]` ，则 v 是一个强连通分量的根。从栈中弹出顶点直到当前顶点，形成并存储一个强连通分量

- 实现：详见 [这里](.\SCC.py) 

- 时间复杂度：$O(V + E)$ 

### Kosaraju 算法

- 算法

  1. 对图 G 调用 `dfs` ，计算每一个顶点的结束时间
  2. 计算 G 的转置 G'
  3. 对图 G' 调用 `dfs` ，按照结束时间的递减顺序访问顶点
  4. 第3步得到的深度优先森林中的每一棵树都是一个强连通分量

- 解释 (by ChatGPT)

  - The first DFS traversal gives us the finishing times of vertices, which essentially **provides a reverse topological order** of the graph.
  - In the second DFS traversal, we explore the transpose graph G' **starting from the ‘sink’ vertices** (those with the highest finishing times), which guarantees that we cover all vertices within each strongly connected component before moving to the next sink vertex.
  - The algorithm takes advantage of the fact that in the transpose graph G', the sink vertices of each strongly connected component become the **roots** of the trees in the DFS forest, and each exploration from a sink vertex covers the **entire** component.

- 实现：详见 [这里](.\SCC.py) 

- 时间复杂度：$O(V + E)$ ，但因为完整 dfs 了两次，应该说是 asymptotically optimal 。在实际的测试中，Tarjan 算法的运行效率比 Kosaraju 算法高 30% 左右

  

## 最短路径问题

### Dijkstra 算法

提供从一个顶点到其他所有顶点的最短路径

- 算法：利用*优先级队列*维护循环顺序。将起始顶点的距离初始化为 0 ，其他所有顶点的距离初始化为无穷大。将所有顶点放入一个优先级队列（最小堆）中。
  1. 从队列中 pop 出最小元 v（第一次即为起始顶点）
  2. 更新与 v 相连的顶点的距离信息（取 min），同时维护队列
  3. 重复 1-2 ，直到队列为空
- 实现：详见 [这里](.\shortest_distance.py) 
- 时间复杂度：$O((V+E)\log V)$



## 最小生成树

A **spanning tree** is a sub-graph of an undirected connected graph, which includes all the vertices of the graph with a minimum possible number of edges.

称带权连通无向图 G 的所有生成树中权值和最小的生成树为 G 的*最小生成树* (Minimum Spanning Tree，MST)。

### Prim 算法

从某一个**顶点**开始构建生成树，每次将代价最小的新顶点纳入生成树，直到全部纳入为止。

- 算法：利用*优先级队列*维护待加入顶点的顺序。初始化空的 set `mst` 记录最小生成树，空的 priority queue `pq` 记录可加入的边。
  1. 任意选取起始顶点，将其相连的边加入 pq 中
  2. 从 pq 中 pop 出具有最小权重的边 e
  3. 若 e 连接的顶点 v 不在 mst 中，将其加入，并将 v 相连的边加入 pq 中
  4. 重复 2-3 步，直到 pq 为空
- 实现：详见 [这里](.\mst.py) 
- 时间复杂度：$O(V^2)$ ，适用于稠密图

### Kruskal 算法

每次选择一条权值最小的**边**，将这条边的两头连通(不选已经连通的)，直到所有节点连通。

- 算法：利用*并查集* (Disjointset) 记录连通情况。初始化空的 set `mst` 记录最小生成树，将所有边按权值从小到大排序。将所有顶点视为孤立的连通集。
  1. 从小到大依次取出边 e 
  2. 若加入 e 不会在 mst 中形成环（体现为 e 两端的顶点不位于同一个并查集内），将其加入 mst 中，并将其两端顶点所在的集合合并为一个
  3. 重复 1-2 步，直到所有边都已处理
- 实现：详见 [这里](.\mst.py) 
- 时间复杂度：$O(E \log E)$ ，适用于稀疏图





