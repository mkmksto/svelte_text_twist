<script>
    import { getRandomWord } from '../stores/gameSettings'
</script>

<div class="letter-spaces letter">
    {#await $getRandomWord}
        <div class="fetching">...fetching</div>
    {:then $getRandomWord}
        <!-- loop through each letter -->
        {#each $getRandomWord.word as word}
            <div class="cell empty-cell">{word}</div>
        {/each}
    {/await}
</div>

<div class="letter-options letter">
    {#await $getRandomWord then $getRandomWord}
        {#each $getRandomWord.word as word}
            <div class="cell letter-cell">{word}</div>
        {/each}
    {/await}
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
        @apply rounded-full uppercase cursor-pointer text-neutral-600 bg-white border border-solid border-neutral-400 hover:text-neutral-400;
    }

    .empty-cell {
        @apply relative bg-neutral-200 text-opacity-0;
    }

    .empty-cell::after {
        @apply content-none absolute w-full h-full border border-solid border-white rounded-full;
    }

    .fetching {
        @apply text-gray-300;
    }
</style>
