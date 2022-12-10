<script>
    import { faGear } from '@fortawesome/free-solid-svg-icons'
    import Fa from 'svelte-fa'

    function openModal() {
        console.log('open modal')
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
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 50px;
        background-color: white;
        color: var(--g70-grey);
    }

    .header ul {
        list-style: none;
        display: flex;
        justify-content: space-around;
        height: 100%;
        align-items: center;
        margin: 0 10rem;
    }

    .icons {
        cursor: pointer;
    }
</style>
