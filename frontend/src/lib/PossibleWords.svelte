<script>
    import { randomWord } from '../stores/randomWord'
</script>

<div class="card">
    <div class="word-columns">
        {#await $randomWord}
            ...
        {:then $randomWord}
            {#each $randomWord.sub_words as sub_words}
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
        width: var(--card-width);
        max-width: 900px;
        height: var(--card-height);
        max-height: 900px;
        display: flex;
        flex-direction: column;
        background-color: var(--light-grey);
        /* border: 1px dotted var(--g150-grey); */
        flex-wrap: wrap;
        /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); */
        border-radius: 0.7rem;
        padding: 0.7rem;
    }

    .word-columns {
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        align-content: flex-start;
        gap: 0 3rem;
        width: var(--card-width);
        height: var(--card-height);
    }

    .word-cells {
        display: flex;
    }

    .cell {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 2rem;
        width: 2rem;
        margin: 0.2rem;
        background-color: white;
        color: var(--g40-grey);
        border-radius: 0.15rem;
    }
</style>
