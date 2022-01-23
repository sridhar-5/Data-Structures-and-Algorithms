function BreadthFirstSearch(graph, start) {
  // [1, 2 , 3 ,4 ,5]
  //operations used - push, shift
  var queue = [start];

  while (queue.length > 0) {
    var current = queue.shift();
    console.log(current);
    for (var neighbour of graph[current]) {
      queue.push(neighbour);
    }
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

BreadthFirstSearch(graph, "a");
