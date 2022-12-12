<script>
    import { getRandomWord } from '../stores/gameSettings'
</script>

<div class="card">
    <div class="word-columns">
        {#await $getRandomWord}
            <div class="fetching">...</div>
        {:then $getRandomWord}
            {#each $getRandomWord.sub_words as sub_words}
                <div class="word-cells">
                    {#each sub_words as sub_word}
                        <div class="cell">{sub_word}</div>
                    {/each}
                </div>
            {/each}
        {/await}
    </div>
</div>

<style>
    :root {
        --card-width: 1000px;
        --card-height: 400px;
    }

    .card {
        @apply h-[var(--card-height)] w-[var(--card-width)] max-w-4xl flex flex-col bg-gray-300 flex-wrap rounded-xl p-3;
    }

    .word-columns {
        @apply flex flex-col flex-wrap content-start gap-x-12 h-[calc(var(--card-height)-0.5rem)] w-[var(--card-width)];
        /* display: flex;
        gap: 0 3rem; */
    }

    .word-cells {
        @apply flex;
    }

    .cell {
        @apply flex justify-center items-center uppercase h-8 w-8 my-1 mx-0.5 bg-white text-gray-700 rounded-sm;
    }

    .fetching {
        @apply text-gray-300;
    }
</style>
