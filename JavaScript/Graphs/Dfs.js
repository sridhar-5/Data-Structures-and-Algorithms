function DepthFirstSearch(graph, start) {
  var stack = [start];

  while (stack.length > 0) {
    var current = stack.pop();
    console.log(current);
    for (let neighbour of graph[current]) {
      stack.push(neighbour);
    }
  }
}

function DepthFirstSearchRecursive(graph, start) {
  console.log(start);
  for (var neighbour of graph[start]) {
    DepthFirstSearchRecursive(graph, neighbour);
  }
}

const graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

DepthFirstSearch(graph, "a");
console.log("\n");
DepthFirstSearchRecursive(graph, "a");
