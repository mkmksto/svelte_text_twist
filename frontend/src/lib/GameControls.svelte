<script>
    import { renewCurrentWord } from '../functions/dataFetching'
    import { validateGuess } from '../functions/guessValidation'
    import { shuffleItems } from '../functions/math'
    import { currentGuess, currentRandomWord, gameSettings } from '../stores/gameSettings'

    function shuffleLetters() {
        const curShuffledWord = $currentRandomWord.shuffled_word
        const shuffledWordArray = Array.from(curShuffledWord)
        const newArr = shuffleItems(shuffledWordArray)
        $currentRandomWord.shuffled_word = newArr
    }

    function returnLettersToOriginalPlace() {
        $currentRandomWord.shuffled_word.forEach((letter) => (letter.letter_transferred = false))
        $currentRandomWord = $currentRandomWord
        $currentGuess = []
    }

    function testGuess() {
        let store = $currentGuess
        const curGuess = store.join('')
        const [isGuessInArray, idxOfGuess] = validateGuess(curGuess, $currentRandomWord.sub_words)
        console.log('is guess in array? ', isGuessInArray)
        console.log('idx of guess', idxOfGuess)
    }

    function resetGuessStore() {
        $currentGuess = []
    }
</script>

<div class="controls">
    <button class="btn" on:click={shuffleLetters}>Twist</button>
    <button class="btn">Give Up</button>
    <button class="btn" on:click={returnLettersToOriginalPlace}>Clear</button>
    <button class="btn" on:click={testGuess}>Enter</button>
    <button
        class="btn"
        on:click={() => {
            renewCurrentWord($gameSettings)
            resetGuessStore()
        }}>New Word</button
    >
</div>

<style>
    .controls {
        @apply mt-4;
    }

    .btn {
        @apply mx-4 py-2 px-4 bg-neutral-400 hover:bg-neutral-500 text-neutral-50;
    }
</style>
