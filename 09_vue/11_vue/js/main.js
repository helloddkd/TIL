// json-server 의 기본 접속 URI 는 아래와 같습니다. 필요에 따라 수정 가능합니다.
const HOST = "http://localhost:3000";
Vue.component('modal', {
    template: '#modal-template',
    
})
const app = new Vue({
        el: "#app",
        data: {
            logo: 'MO<i class="fab fa-vuejs"></i>IE',
            isMain: true,
            genres: [],
            movies: [],
            search: '', // 검색 기능을 구현할 때, 사용자의 입력 값을 이곳에 쌍방향 바인딩 합니다.
            isdetail: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
            movieDetail: {},  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
            inputScore: {
                content: '',
                score: 10,
                movieId: '',
                created: '',
            },
            showModal: false,
            scores: []
        },
        methods: {
            async toggleDetail(id = null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
                if (id) {
                    this.movieDetail = this.movies.find(movie => movie.id === id)
                    const res = await axios.get(`${HOST}/movies/${id}/scores`)
                    this.scores = res.data.reverse()
                }
                this.isdetail = !this.isdetail
            },
            getmovies: async function (genreId = null) {
                const URL = genreId ? `${HOST}/genres/${genreId}/movies` : `${HOST}/movies`
                const res = await axios.get(URL);
                this.movies = res.data
            },
            postScore: async function (id) {
                function getAverageScore(scores){
                    const result = scores.reduce((acc, score) => {
                        acc.total += score.score
                        acc.count ++
                        return acc
                    }, {total:0, count:0})
                    return (result.total/result.count).toFixed(2)
                }
                if (this.inputScore.content && this.inputScore.score) {
                    this.inputScore.movieId = id
                    this.inputScore.created = this.getTimeStamp()
                    const response = await axios.post(`${HOST}/scores`, this.inputScore)
                    const newScore = response.data
                    this.scores.unshift(newScore)
                    this.inputScore = {content:'', score:10}
                    res = await axios.patch(`${HOST}/movies/${id}/`, {averageScore:getAverageScore(this.scores)})
                    this.movieDetail = res.data

                } else {
                    alert('내용과 평점을 모두 입력해주세요')
                }
            },
            orderMovies: async function(standard=''){
                const res = await axios.get(`${HOST}/movies?_sort=${standard}&_order=desc`)
                this.movies = res.data
            },
            getTimeStamp() {
                var d = new Date();
                var s =
                    this.leadingZeros(d.getFullYear(), 4) + '-' +
                    this.leadingZeros(d.getMonth() + 1, 2) + '-' +
                    this.leadingZeros(d.getDate(), 2) + ' ' +
                    this.leadingZeros(d.getHours(), 2) + ':' +
                    this.leadingZeros(d.getMinutes(), 2) + ':' +
                    this.leadingZeros(d.getSeconds(), 2);
                return s;
            },
            leadingZeros(n, digits) {
                var zero = '';
                n = n.toString();

                if (n.length < digits) {
                    for (i = 0; i < digits - n.length; i++)
                        zero += '0';
                }
                return zero + n;
            }
        },
        computed: {
        },

        watch: {
            async search(keyword) {
                if (keyword) {
                    const URL = `${HOST}/movies?title_like=${keyword}|description_like=${keyword}`
                    const res = await axios.get(URL)
                    this.movies = res.data
                } else {
                }
            }
            ,
            movies() {
                this.isdetail = false;
            }
        }
        ,

        created: async function () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, json-server 에서 장르목록만 받아옵니다.
            const res = await axios.get(`${HOST}/genres`)
            this.genres = res.data;

        }
    })
;


document.addEventListener('keyup', e => {
    if (e.key === 'Escape') {
        app.$data.isdetail = false
    }
})