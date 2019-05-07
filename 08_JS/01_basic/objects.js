const me = {
    name: 'jiwon baik',
    number:'01012341234',
    appleproducts: {
        ipad:'2018pro',
        iphone: '6s+',
        macbook: '2018pro',
    }
};

me.name;
me['name']; //여기는 꼭 따옴표 붙여야

me.app


function myFunc(){
    return n => n+1
}

const num_101 = [];

num_101.push(myFunc()(100));
console.log(num_101);
