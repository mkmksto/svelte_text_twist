<script>
    import { onDestroy, onMount } from 'svelte'
    import { flip } from 'svelte/animate'
    import { renewCurrentWord } from '../functions/dataFetching'
    import { currentRandomWord, gameSettings } from '../stores/gameSettings'

    let shuffledWord

    onMount(async () => {
        await renewCurrentWord($gameSettings)
        console.log($currentRandomWord.shuffled_word)
    })

    onDestroy(() => {
        console.log('cur word destroyed')
    })
</script>

<div class="letter-spaces letter">
    {#each $currentRandomWord.word as letter}
        <div class="cell empty-cell">{letter}</div>
    {:else}
        <div class="fetching">...</div>
    {/each}
</div>

<div class="letter-options letter" bind:this={shuffledWord}>
    {#each $currentRandomWord.shuffled_word as { letter, id } (id)}
        <div class="cell letter-cell" animate:flip={{ duration: 600 }}>{letter}</div>
    {:else}
        <div class="fetching">...</div>
    {/each}
    <!-- {#if $currentRandomWord.shuffled_word.length > 0}
        {#each $currentRandomWord.shuffled_word as { letter, id } (id)}
            <div class="cell letter-cell" animate:flip={{ duration: 600 }}>{letter}</div>
            <div class="fetching">...</div>
        {/each}
    {:else}
        <div class="fetching">...</div>
    {/if} -->
</div>

<style>
    .letter {
        @apply flex mt-4;
    }

    .letter-options {
        background-color: white;
        border-color: 3px solid var(--pink);
    }

    .letter-spaces {
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
