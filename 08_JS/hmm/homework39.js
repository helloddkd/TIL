const name = '김싸피';
const hobby = '프로그래밍';
const student = {
    name: name,
    hobby: hobby,
    introduce: function () {
        return `이름은 ${this.name}, 취미는 ${this.hobby}`;
    }
};
console.log(student.introduce());


function solveMe(a,...numbers) {
    let result = [];
    for (const number of numbers){
        result.push(a*number)
    }
    return result;
}
const a = solveMe(2, 1, 2, 3, 4); // [2, 4, 6, 8]
const b = solveMe(5, 10, 20); // [50, 100]
console.log([...a, ...b]); // [2, 4, 6, 8, 50, 100]