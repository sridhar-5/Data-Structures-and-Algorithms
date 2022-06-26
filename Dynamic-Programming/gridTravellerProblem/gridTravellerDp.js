const gridTraveller = function(m,n, memory ={}){

    //check if this sub problem exists in the memeory
    const key = m+ ","+ n;
    if(key in memory) return memory[key];
    //base case is having a (1,1) grid
    if(m === 1 && n === 1) return 1;
    if(m === 0 || n === 0) return 0;
    memory[key] = gridTraveller(m-1, n, memory) + gridTraveller(m, n-1, memory);
    return memory[key];
}

console.log(gridTraveller(1,1));
console.log(gridTraveller(2,3));
console.log (gridTraveller(3,3));
console.log (gridTraveller(13,13));


//time complexity - O(m*n)
//space complexity - O(n+m)

// example of 4,3
// m = {0,1,2,3,4}
// n = {0,1,2,3}

// we have only m*n unique pairs after that we'll memorize so its m*n