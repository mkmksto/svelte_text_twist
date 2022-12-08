<script></script>

<div class="card">
    <div class="word-cells">
        <div class="cell">G</div>
        <div class="cell">O</div>
        <div class="cell">T</div>
    </div>
    <div class="word-cells">
        <div class="cell">X</div>
        <div class="cell">Y</div>
        <div class="cell">Z</div>
    </div>
</div>

<style>
    .card {
        width: 1000px;
        max-width: 900px;
        height: 400px;
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
