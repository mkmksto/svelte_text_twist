<script>
    import { renewCurrentWord } from '../functions/dataFetching'
    import { validateGuess } from '../functions/guessValidation'
    import { shuffleItems } from '../functions/math'
    import {
        currentGuess,
        currentRandomWord,
        gameSettings,
        validLetters,
    } from '../stores/gameSettings'

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
        let store = $currentGuess.map((letterObj) => letterObj.letter)
        const curGuess = store.join('')
        const [isGuessInArray, idxOfGuess] = validateGuess(curGuess, $currentRandomWord.sub_words)
        console.log('is guess in array? ', isGuessInArray)
        console.log('idx of guess', idxOfGuess)
        console.log('valid letters: ', $validLetters)
    }

    function resetGuessStore() {
        $currentGuess = []
    }

    // have to re-implement these functions from CurrentWord.svelte
    // because they have some slight differences
    // that aren't worth creating a module for
    function moveLetter(key) {
        const clickedLetter = $currentRandomWord.shuffled_word.find(
            (letter) => key === letter.letter
        )
        // as opposed to CurrentWord.svelte, we don't toggle
        // because we'll use the backspace key to remove letters
        // from the guessing area
        clickedLetter.letter_transferred = true

        $currentRandomWord = $currentRandomWord
    }

    function updateGuessStore(key) {
        const clickedLetter = $currentRandomWord.shuffled_word.find(
            (letter) => key === letter.letter
        )
        // console.log('previous guess ' $currentGuess)

        // stop if letter with the same unique ID is already in the guess
        // checks for same ids
        const letterAlreadyInGuess = $currentGuess.some((letter) => letter.id === clickedLetter.id)
        console.log('letter already in guess ', letterAlreadyInGuess)
        if (letterAlreadyInGuess) return
        $currentGuess = [...$currentGuess, { letter: clickedLetter.letter, id: clickedLetter.id }]
        console.log('new current guess: ', $currentGuess)
    }

    function removeLetterFromGuess() {
        try {
            console.log('current guess ', $currentGuess)
            const lastItem = $currentGuess[$currentGuess.length - 1]
            const correspondingLetterFromCurrentWordStore = $currentRandomWord.shuffled_word.find(
                (letter) => lastItem.id === letter.id
            )

            // const newGuessArray = [...$currentGuess]
            // newGuessArray.pop()
            // $currentGuess = newGuessArray
            $currentGuess.pop()
            $currentGuess = $currentGuess

            correspondingLetterFromCurrentWordStore.letter_transferred = false
            $currentRandomWord = $currentRandomWord
        } catch (e) {}
    }
</script>

<svelte:window
    on:keydown={(e) => {
        if (e.repeat) {
            console.log('repeat key press: ', e.key)
        }
        if (e.key === 'Backspace') {
            removeLetterFromGuess()
            return
        }
        if (e.key === ' ') shuffleLetters()
        if (e.key === 'Enter') testGuess()
        if (e.key === 'Escape') returnLettersToOriginalPlace()
        if (!Array.from($validLetters).includes(e.key)) {
            return
        } else {
            moveLetter(e.key)
            updateGuessStore(e.key)
        }
        return
    }}
/>

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
