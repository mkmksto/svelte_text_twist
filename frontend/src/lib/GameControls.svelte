<script>
    import { renewCurrentWord } from '../functions/dataFetching'
    import { shuffleItems } from '../functions/math'
    import { currentRandomWord, gameSettings } from '../stores/gameSettings'

    function shuffleLetters() {
        const curShuffledWord = $currentRandomWord.shuffled_word
        const shuffledWordArray = Array.from(curShuffledWord)
        const newArr = shuffleItems(shuffledWordArray)
        $currentRandomWord.shuffled_word = newArr
    }
</script>

<div class="controls">
    <button class="btn" on:click={shuffleLetters}>Twist</button>
    <button class="btn">Give Up</button>
    <button class="btn">Clear</button>
    <button class="btn">Enter</button>
    <button class="btn" on:click={() => renewCurrentWord($gameSettings)}>New Word</button>
</div>

<style>
    .controls {
        @apply mt-4;
    }

    .btn {
        @apply mx-4 py-2 px-4 bg-neutral-400 hover:bg-neutral-500 text-neutral-50;
    }
</style>
