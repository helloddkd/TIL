// rest operator가 없다면..

function addAll(a,b,c,d,e) {
    const numbers = [a,b,c,d,e];
    let sum = 0
    for (const number of numbers){
        sum += number;
    }
    return sum;
}

//rest operator가 있다면

function addAll(...numbers) {
    let sum = 0
    for (const number of numbers){
        sum += number;
    }
    return sum;
}


const a1 = [1,2,3,4];
const a2 = [5,6,7,8];
const a3 = [...a1, ...a2];  //[1,2,3,4,5,6,7,8]
