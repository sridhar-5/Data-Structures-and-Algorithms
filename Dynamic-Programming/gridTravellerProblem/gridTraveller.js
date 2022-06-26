const gridTraveller = function(m,n){

    //base case is having a (1,1) grid
    if(m === 1 && n === 1) return 1;
    if(m === 0 || n === 0) return 0;
    return gridTraveller(m-1, n) + gridTraveller(m, n-1);
}

console.log(gridTraveller(1,1));
console.log(gridTraveller(2,3));
console.log (gridTraveller(3,3));

