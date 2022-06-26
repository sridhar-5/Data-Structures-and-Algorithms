const canSum = function(sum, arr,mem={}){
    if(sum === 0) return true;
    if(sum < 0) return false;
    
    for(var num of arr){
        var rem = sum - num;
        console.log(rem)
        if(canSum(rem, arr) === true) {
            return true;
        }
    }
    return false;
}

console.log(canSum(7,[5,3,4,7]));
console.log(canSum(8, [5,7]));
console.log(canSum(7,[2,4]));
