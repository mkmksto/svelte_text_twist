<script>
    import { faGear } from '@fortawesome/free-solid-svg-icons'
    import Fa from 'svelte-fa'
    import { showModal } from '../stores/gameSettings'
    import { currentRoundScore } from '../stores/gameStates'

    function openModal() {
        $showModal = true
    }
</script>

<nav class="header">
    <ul>
        <span class="game-info"
            >Score: <li class="score">{$currentRoundScore}</li></span
        >
        <li>Time</li>
        <li>Round</li>
        <li class="icons" on:click={openModal}>
            <Fa icon={faGear} size="1.5rem" />
        </li>
    </ul>
</nav>

<style>
    .header {
        @apply fixed top-0 left-0 w-full h-14 bg-white text-gray-500 mx-24;
        font-family: 'Open Sans';
    }

    .header ul {
        @apply list-none flex justify-around items-center h-full mx-3;
    }

    .game-info {
        display: flex;
    }

    .score {
        @apply ml-4;
        font-family: 'Roboto Mono';
    }

    .icons {
        @apply cursor-pointer;
    }
</style>
