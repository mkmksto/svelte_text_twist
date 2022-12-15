<script>
    import { currentRandomWord } from '../stores/gameSettings'
</script>

<div class="card">
    <div class="word-columns">
        {#if $currentRandomWord.sub_words.length > 0}
            {#each $currentRandomWord.sub_words as { sub_word, id, has_been_guessed } (id)}
                <div class="word-cells">
                    {#each sub_word as subWordLetter}
                        <div class="cell" class:has-been-guessed={has_been_guessed}>
                            {subWordLetter}
                        </div>
                    {/each}
                </div>
            {/each}
        {:else}
            <div class="fetching">...</div>
        {/if}
    </div>
</div>

<style>
    :root {
        --card-width: 1000px;
        --card-height: 400px;
    }

    .card {
        @apply h-[var(--card-height)] w-[var(--card-width)] max-w-4xl flex flex-col bg-neutral-300 flex-wrap rounded-xl p-3;
    }

    .word-columns {
        @apply flex flex-col flex-wrap content-start gap-x-12 h-[calc(var(--card-height)-0.5rem)] w-[var(--card-width)];
        /* display: flex;
        gap: 0 3rem; */
    }

    .word-cells {
        @apply flex select-none;
    }

    .cell.has-been-guessed {
        @apply bg-pink-600 text-white;
        transition: background-color 0.5s ease;
    }

    .cell {
        @apply flex justify-center items-center uppercase h-8 w-7 my-1 mx-0.5 bg-white text-white rounded-sm;
    }

    .fetching {
        @apply text-gray-300;
    }
</style>
