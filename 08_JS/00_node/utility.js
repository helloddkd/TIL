module.exports = {
    addAll(numbers=[]){
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },

    subAll(numbers=[]){
        let acc = 0;
        numbers.forEach(number => acc -= number);
        return acc;
    },

    mulAll(numbers=[]){
        let acc = 1;
        numbers.forEach(number => acc*=number);
        return acc;
    }
};


phoneNumber = '01021212121';
module.exports.phoneNumber = phoneNumber; //keyvalue 추가

