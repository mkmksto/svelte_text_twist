<script>
    import { onDestroy, onMount } from 'svelte'
    import { flip } from 'svelte/animate'
    import { crossfade } from 'svelte/transition'
    import { renewCurrentWord } from '../functions/dataFetching'
    import { currentRandomWord, gameSettings } from '../stores/gameSettings'

    let shuffledWord

    const [send, receive] = crossfade({
        duration: 600,
    })

    onMount(async () => {
        await renewCurrentWord($gameSettings)
    })

    onDestroy(() => {
        console.log('cur word destroyed')
    })

    function moveLetter(letterId) {
        const clickedLetter = $currentRandomWord.shuffled_word.find(
            (letter) => letterId === letter.id
        )
        clickedLetter.letter_transferred = !clickedLetter.letter_transferred
        $currentRandomWord = $currentRandomWord
    }
</script>

<div class="letter-guesses letter">
    {#each $currentRandomWord.shuffled_word.filter((letter) => letter.letter_transferred) as { letter, id } (id)}
        <div
            class="cell letter-cell"
            in:receive={{ key: id }}
            out:send={{ key: id }}
            animate:flip={{ duration: 600 }}
            on:click={() => moveLetter(id)}
        >
            {letter}
        </div>
    {/each}
</div>

<div class="letter-options letter" bind:this={shuffledWord}>
    {#each $currentRandomWord.shuffled_word.filter((letter) => !letter.letter_transferred) as { letter, id } (id)}
        <div
            class="cell letter-cell"
            in:receive={{ key: id }}
            out:send={{ key: id }}
            animate:flip={{ duration: 600 }}
            on:click={() => moveLetter(id)}
        >
            {letter}
        </div>
    {:else}
        <div class="fetching">...</div>
    {/each}
</div>

<style>
    .letter {
        @apply flex mt-4 h-14;
    }

    .letter-options {
        background-color: white;
        border-color: 3px solid var(--pink);
    }

    .letter-guesses {
    }

    .cell {
        @apply flex justify-center items-center mx-2 text-4xl w-14 h-14 bg-white rounded text-neutral-500 font-bold;
    }

    .letter-cell {
        @apply rounded-full uppercase cursor-pointer text-neutral-600 hover:text-neutral-400 bg-white border border-solid border-neutral-400;
    }

    .empty-cell {
        @apply relative bg-neutral-200 text-opacity-0;
    }

    .empty-cell::after {
        @apply content-none absolute w-full h-full border border-solid border-white rounded-full;
    }

    .fetching {
        @apply text-gray-300 w-14 h-14;
    }
</style>
