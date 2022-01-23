function hasPath(graph, src, dest) {
  // Bfs approach - Breadth first search
  var queue = [src];

  while (queue.length > 0) {
    var current = queue.shift();

    if (current == dest) {
      return true;
    }
    graph[current].forEach((neighbor) => {
      queue.push(neighbor);
    });
  }
  return false;
}

function hasPathDfs(graph, src, dst) {
  //base case
  if (src == dst) return true;

  for (var neighbour of graph[src]) {
    if (hasPathDfs(graph, neighbour, dst)) {
      return true;
    }
  }
  return false;
}

const graph = {
  f: ["g", "i"],
  g: ["h"],
  h: [],
  i: ["g", "k"],
  j: ["i"],
  k: [],
};

console.log(hasPath(graph, "f", "k"));
console.log(hasPathDfs(graph, "f", "k"));
