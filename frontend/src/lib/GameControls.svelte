<script>
    import { gameSettings } from '../stores/gameSettings'
</script>

<div class="controls">
    <button class="btn">Twist</button>
    <button class="btn">Give Up</button>
    <button class="btn">Clear</button>
    <button class="btn">Enter</button>
    <button class="btn" on:click={() => ($gameSettings = $gameSettings)}>New Word</button>
</div>

<style>
    .controls {
        @apply mt-4;
        /* margin-top: 1rem; */
    }

    .btn {
        @apply mx-4 py-2 px-4 bg-neutral-400 text-neutral-50;
        /* font-family: 'Pragati Narrow'; */
    }
</style>
