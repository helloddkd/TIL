function makearticle (id, title, content) {
    return {
        id: id,
        title: title,
        content: content,
        makeOne: function () {
            return `${this.id}번 글: ${this.title} => ${this.content}`
        }
    };
}
const myobj = {

};


function makearticle (id, title, content) {
    return {
        id,
        title,
        content,
        makeOne: function () {
            return `${this.id}번 글: ${this.title} => ${this.content}`
        }
    };
}