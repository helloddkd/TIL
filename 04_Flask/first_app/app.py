import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/') #고급문법. 메소드를 실행할 거 같지만 조건부 실행이다. 
#요때 슬래시는 최상단의 디렉토리란 뜻으로 루트라고 불린다. 요것은 루트라우트~
def index():
    return 'HI!'

@app.route('/ssafy')
def ssafy():
    return 'sssssssafy'

@app.route('/hi/<string:name>')
def hi(name): #함수는 함수만의 세계가 있어서 name변수를 꼭 인자로 받아줘야한다.
    return (f'hi {name}!')

@app.route('/pick_lotto')
def pick_lotto():
    pick = random.sample(range(1,41), 6)
    return jsonify(pick)


@app.route('/dictionary/<string:word>')
def dic(word):
    en = []
    kr = []
    result_f = open("voca.txt") 
    for line in result_f: 
        (e, k) = line.split('\t') 
        en.append(e)
        kr.append(k[:-1])
    result_f.close()
    wdict = dict(zip(en, kr))
    if wdict.get(word):
        return (f'{word}은(는) {wdict[word]}!')
    else:
        return (f'{word}은(는) 나만의 단어장에 없는 단어입니다!')

if __name__ == '__main__':  #__name__은 태세변환을 잘 하는 변수. 일단 지금 이 이프문은 항상 True
    app.run(debug=True)

# class Flask:
#     def run(self, **kwargs):

# @app.route('/keyword/<string:word>')
# def keyword(word):
#     search_results = DB.find(word)
