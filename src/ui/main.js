const app = Vue.createApp({
    data() {
        return {
            name: 'Battle of Alesia',
            date: 'September 52 BC',
            location: 'Alise-Sainte-Reine, France',
            belligerentA: 'Roman Republic',
            belligerentB: 'Gaulic Confederation',
            leaderAName: 'Julius Caesar',
            leaderAImageLink: 'https://upload.wikimedia.org/wikipedia/commons/6/62/Retrato_de_Julio_C%C3%A9sar_%2826724093101%29_%28cropped%29.jpg',
            leaderBName: 'Vercingetorix',
            leaderBImageLink: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Vercingetorix_stat%C3%A8re_MAN.jpg/800px-Vercingetorix_stat%C3%A8re_MAN.jpg',
            result: 'A',
            showDate: false,
            showLocation: false,
            showBelligerents: false,
            guessed: null,  // init as NULL, when a user guesses, it will become their guess, either A or B
        }
    },
    methods: {
        revealDate() {
            this.showDate = true
        },
        revealLocation() {
            this.showLocation = true
        },
        revealBelligerents() {
            this.showBelligerents = true
        },
        guessLeft() {
            this.guessed = 'A'
        },
        guessRight() {
            this.guessed = 'B'
        }
    }
})
