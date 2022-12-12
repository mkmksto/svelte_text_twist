<script>
    import { faGear } from '@fortawesome/free-solid-svg-icons'
    import Fa from 'svelte-fa'
    import { showModal } from '../stores/gameSettings'

    function openModal() {
        $showModal = true
    }
</script>

<nav class="header">
    <ul>
        <li>Score</li>
        <li>Time</li>
        <li>Round</li>
        <li class="icons" on:click={openModal}>
            <Fa icon={faGear} size="1.5rem" />
        </li>
    </ul>
</nav>

<style>
    .header {
        @apply fixed top-0 left-0 w-full h-14 bg-white text-gray-500;
        font-family: 'Open Sans';
    }

    .header ul {
        @apply list-none flex justify-around items-center h-full mx-3;
    }

    .icons {
        @apply cursor-pointer;
    }
</style>
