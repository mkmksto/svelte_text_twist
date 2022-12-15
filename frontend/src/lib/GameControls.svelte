<script>
    import { tick } from 'svelte'
    import { renewCurrentWord } from '../functions/dataFetching'
    import { validateGuess } from '../functions/guessValidation'
    import { shuffleItems } from '../functions/math'
    import {
        currentGuess,
        currentRandomWord,
        gameSettings,
        validLetters,
    } from '../stores/gameSettings'
    import {
        countdownLength,
        currentRoundScore,
        isGameWon,
        validatedGuessesStore,
    } from '../stores/gameStates'
    import { clearHeaderInterval, renewInterval } from './Header.svelte'

    let newWordBtn

    function shuffleLetters() {
        const curShuffledWord = $currentRandomWord.shuffled_word
        const shuffledWordArray = Array.from(curShuffledWord)
        const newArr = shuffleItems(shuffledWordArray)
        $currentRandomWord.shuffled_word = newArr
    }

    async function returnLettersToOriginalPlace() {
        await tick()
        $currentRandomWord.shuffled_word.forEach((letter) => (letter.letter_transferred = false))
        $currentRandomWord = $currentRandomWord
        $currentGuess = []
    }

    function testGuess() {
        let store = $currentGuess.map((letterObj) => letterObj.letter)
        const curGuess = store.join('')
        const [isGuessInArray, idxOfGuess] = validateGuess(curGuess, $currentRandomWord.sub_words)
        if (!isGuessInArray) return

        $validatedGuessesStore = [...$validatedGuessesStore, curGuess]
        if (!$currentRandomWord.sub_words[idxOfGuess].has_been_guessed) {
            $currentRoundScore += curGuess.length * 1000
        }
        $currentRandomWord.sub_words[idxOfGuess].has_been_guessed = true

        console.log('is guess in array? ', isGuessInArray)
        console.log('idx of guess', idxOfGuess)
        // console.log('valid keyboard letters: ', $validLetters)
        // console.log('list of valid guesses: ', $validatedGuessesStore)
    }

    function resetGuessStore() {
        $currentGuess = []
    }

    function updateCurRandomWord(key) {
        const clickedLetter = $currentRandomWord.shuffled_word
            .filter((letter) => !letter.letter_transferred)
            .find((letter) => key === letter.letter)
        if (!clickedLetter) return
        clickedLetter.letter_transferred = true

        $currentRandomWord = $currentRandomWord
    }

    function updateGuessStore(key) {
        // only search from the letters that haven't been transferred yet
        let clickedLetter = $currentRandomWord.shuffled_word
            .filter((letter) => !letter.letter_transferred)
            .find((letter) => key === letter.letter)
        if (!clickedLetter) return
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
        if ($currentGuess.length === 0) return

        try {
            console.log('current guess ', $currentGuess)
            const lastItem = $currentGuess[$currentGuess.length - 1]
            const correspondingLetterFromCurrentWordStore = $currentRandomWord.shuffled_word
                .filter((letter) => letter.letter_transferred)
                .find((letter) => lastItem.id === letter.id)
            if (!correspondingLetterFromCurrentWordStore) return

            $currentGuess.pop()
            $currentGuess = $currentGuess

            correspondingLetterFromCurrentWordStore.letter_transferred = false
            $currentRandomWord = $currentRandomWord
        } catch (e) {}
    }

    function resetValidLetters() {
        validLetters.set(new Set())
    }

    let nextRoundBtn
    function updateWinState() {
        if ($currentRandomWord.sub_words[0].has_been_guessed === true) {
            $isGameWon = true
            nextRoundBtn.disabled = false
            console.log('game won')
        }
    }

    function sleep(ms) {
        return new Promise((res) => setTimeout(res, ms))
    }
</script>

<svelte:window
    on:keydown={async (e) => {
        if (e.repeat) return
        if (e.key === 'Backspace') {
            removeLetterFromGuess()
            await sleep(200)
            return
        }
        if (e.key === ' ') shuffleLetters()
        if (e.key === 'Enter') {
            testGuess()
            updateWinState()
        }
        if (e.key === 'Escape') returnLettersToOriginalPlace()
        if (Array.from($validLetters).includes(e.key)) {
            updateGuessStore(e.key)
            updateCurRandomWord(e.key)
        }
    }}
/>

<div class="controls">
    <button class="btn" on:click={shuffleLetters}>Twist</button>
    <button class="btn" on:click={() => ($currentRoundScore = 0)}>Give Up</button>
    <button class="btn" on:click={returnLettersToOriginalPlace}>Clear</button>
    <button
        class="btn"
        on:click={() => {
            testGuess()
            updateWinState()
        }}>Enter</button
    >
    <button
        class="btn"
        bind:this={newWordBtn}
        on:click={async () => {
            // await tick()
            renewCurrentWord($gameSettings)
            resetGuessStore()
            resetValidLetters()
            $currentRoundScore = 0
            newWordBtn.blur()
            // await tick()
            $countdownLength = Date.now() + 120000
            clearHeaderInterval()
            renewInterval()
        }}>New Word</button
    >
    <button
        bind:this={nextRoundBtn}
        class="btn"
        disabled
        on:click={() => {
            $countdownLength = Date.now() + 120000
        }}>Next Round</button
    >
</div>

<style>
    .controls {
        @apply mt-4;
    }

    .btn {
        @apply mx-4 py-2 px-4 bg-neutral-400 hover:bg-neutral-500 text-neutral-50;
    }

    .btn:disabled {
        @apply bg-neutral-200;
    }
</style>
