function hi () {

}

const bye = () => {

};

{}


const me = {
    name : 'baik jiwon',
    phone : '01012345678',
    email : 'img9672@daum.net',
    intro : function (){
        return `hi my name is ${this.name}.`
    }
};

console.log(me.intro());


const you = {
    name : 'baik jiwon',
    phone : '01012345678',
    email : 'img9672@daum.net',
    intro : ()=>{
        return `hi my name is ${this.name}.`
    },
    wait : function() {
        setTimeout(()=>{
            console.log(this.email)
        }, 1000)
    }
};

console.log(you.intro());
console.log(you.wait())