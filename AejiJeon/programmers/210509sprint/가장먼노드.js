const solution = (n, edge) => {
  const graph = new Array(n);

  for (let i = 0; i < n; i++) {
    // initialization to the empty array
    graph[i] = [];
  }

  for (let i = 0; i < edge.length; i++) {
    graph[edge[i][0] - 1].push(edge[i][1] - 1);
    graph[edge[i][1] - 1].push(edge[i][0] - 1);
  }
  const distance = new Array(n);

  // 1e9?
  const INF = 1e9;
  distance.fill(INF);

  // bfs 구현
  queue = [];
  queue.push(0);
  distance[0] = 0;
  while (queue.length !== 0) {
    const now = queue.shift();
    for (let i = 0; i < graph[now].length; i++) {
      if (distance[graph[now][i]] === INF) {
        distance[graph[now][i]] = distance[now] + 1;
        queue.push(graph[now][i]);
      }
    }
  }
  let count = 0;
  const max_value = Math.max(...distance);
  for (let i = 0; i < n; i++) {
    if (max_value === distance[i]) {
      count++;
    }
  }
  return count;
};

// test
console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);
