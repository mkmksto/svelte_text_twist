<script>
    import { currentRound, isGameLost } from '../stores/gameStates'
    import { newWordBtn } from './GameControls.svelte'
</script>

<div class="modal">
    <div class="modal-card">
        <span class="you-lose">You Have Lost</span><button
            on:click={() => {
                newWordBtn.click()
                $isGameLost = false
                $currentRound = 1
                console.log('restart btn clicked')
            }}>Restart</button
        >
    </div>
</div>

<style>
    .modal {
        @apply fixed top-0 left-0 h-screen w-screen z-10 flex items-center justify-center;
        background-color: rgba(50, 50, 50, 0.8);
    }

    .modal-card {
        @apply w-96 h-80 bg-red-500 text-white flex flex-col items-center justify-between rounded-lg text-4xl;
    }

    .you-lose {
        @apply mt-20;
    }

    button {
        @apply bg-white bottom-1 text-neutral-700 text-xl mb-6;
    }
</style>
