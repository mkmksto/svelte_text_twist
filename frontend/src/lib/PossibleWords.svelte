<script>
    import { currentRandomWord } from '../stores/gameSettings'
</script>

<div class="card">
    <div class="word-columns">
        <div class="word-cells">
            {#each $currentRandomWord.word as letterOfWord}
                <div class="cell">{letterOfWord}</div>
            {/each}
        </div>
        {#each $currentRandomWord.sub_words as sub_words}
            <div class="word-cells">
                {#each sub_words as subWordLetter}
                    <div class="cell">{subWordLetter}</div>
                {/each}
            </div>
        {:else}
            <div class="fetching">...</div>
        {/each}
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
        @apply flex;
    }

    .cell {
        @apply flex justify-center items-center uppercase h-8 w-8 my-1 mx-0.5 bg-white text-neutral-500 rounded-sm;
    }

    .fetching {
        @apply text-gray-300;
    }
</style>
