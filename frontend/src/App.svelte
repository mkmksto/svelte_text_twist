<script>
    import CurrentWord from './lib/CurrentWord.svelte'
    import GameControls from './lib/GameControls.svelte'
    import GameLostModal from './lib/GameLostModal.svelte'
    import Header from './lib/Header.svelte'
    import PossibleWords from './lib/PossibleWords.svelte'
    import SettingsModal from './lib/SettingsModal.svelte'
    import { showModal } from './stores/gameSettings'
    import { isGameLost } from './stores/gameStates'
</script>

{#if $showModal}
    <SettingsModal />
{/if}

{#if $isGameLost}
    <GameLostModal />
{/if}

<Header />
<main>
    <PossibleWords />
    <CurrentWord />
    <GameControls />
</main>

<style>
    :root {
        --orange: rgb(245, 72, 0);
        --yellow: rgb(244, 205, 0);
        --blue: rgb(0, 139, 200);
        --light-blue: rgb(127, 187, 210);
        --pink: rgb(223, 35, 136);
        --light-pink: rgba(223, 35, 136, 0.4);
    }

    main {
        @apply flex flex-col items-center;
    }
</style>
