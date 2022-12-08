<script>
    const sampleWord = 'Rainbow'
    // const colors = ['var(--orange)', 'var(--yellow)', 'var(--blue)', 'var(--light-blue)']
</script>

<div class="letter-spaces letter">
    {#each sampleWord as word}
        <!-- <div style:background-color={getRandomItem(colors)} class="cell empty-cell"> -->
        <div class="cell empty-cell">
            {word}
        </div>
    {/each}
</div>

<div class="letter-options letter">
    <div class="cell letter-cell">A</div>
    <div class="cell letter-cell">B</div>
    <div class="cell letter-cell">C</div>
    <div class="cell letter-cell">D</div>
    <div class="cell letter-cell">D</div>
    <div class="cell letter-cell">D</div>
</div>

<style>
    .letter {
        display: flex;
        margin-top: 1rem;
    }

    .letter-options {
        background-color: white;
        border-color: 3px solid var(--pink);
    }

    .letter-spaces {
    }

    .cell {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 0.3rem;
        font-size: 1.8rem;
        font-weight: 400;
        width: 3.5rem;
        height: 3.5rem;
        background-color: white;
        border-radius: 0.2rem;
        color: var(--g100-grey);
    }

    .letter-cell {
        border-radius: 50%;
        text-transform: uppercase;
        cursor: pointer;
        color: var(--g70-grey);
        background-color: white;
        border: 1px solid var(--g150-grey);
    }

    .empty-cell {
        position: relative;
        color: rgba(0, 0, 0, 0);
        background-color: var(--g150-grey);
    }

    .empty-cell::after {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        border: 1px solid white;
        border-radius: 50%;
    }
</style>
