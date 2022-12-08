<script>
    import CurrentWord from './lib/CurrentWord.svelte'
    import GameControls from './lib/GameControls.svelte'
    import Header from './lib/Header.svelte'
    import PossibleWords from './lib/PossibleWords.svelte'
</script>

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
        --grey1: rgba(200, 200, 200, 0.3);
        --light-pink: rgba(223, 35, 136, 0.4);
        --light-grey: rgba(200, 200, 200, 0.6);
        --g150-grey: rgba(150, 150, 150, 0.6);
        --g100-grey: rgba(100, 100, 100, 0.6);
        --g70-grey: rgba(70, 70, 70, 0.6);
        --g40-grey: rgba(40, 40, 40, 0.6);
    }

    main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
