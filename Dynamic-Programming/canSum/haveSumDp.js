const haveSum = function(sum, arr, mem ={}){
    if(sum === 0) return [];
    if(sum < 0) return null;
    if(sum in mem) return mem[sum];

    for(var num of arr){
        var rem = sum - num;
        var newArray = haveSum(rem, arr);
        if(newArray !== null) {
            mem[sum] = [...newArray, num];
            return mem[sum]; 
        }
    } 
    mem[sum] = null;
    return null;
}

console.log(haveSum(7,[5,3,4,7]));
console.log(haveSum(8, [5,4,7]));
console.log(haveSum(7,[2,4]));
console.log(haveSum(8, [3,5,2]));
