<script context="module">
    let interval
    export let renewInterval
    export function clearHeaderInterval() {
        clearInterval(interval)
        console.log('clearing interval')
    }
</script>

<script>
    import { faGear } from '@fortawesome/free-solid-svg-icons'
    import Fa from 'svelte-fa'
    import { showModal } from '../stores/gameSettings'
    import {
        countdownLength,
        currentRound,
        currentRoundScore,
        isGameWon,
        revealYourSecrets,
        setGameLostStatus,
        setGameWonStatus,
    } from '../stores/gameStates'

    let gameInfoTimer
    // onMount(async () => {
    //     await tick()
    //     setNewCountdownLength()
    //     renewHeaderInterval()
    // })

    renewInterval = renewHeaderInterval
    function renewHeaderInterval() {
        interval = setInterval(() => {
            const remaining = getRemainingSeconds()
            gameInfoTimer.innerHTML = getDisplayTimer(remaining)
            checkIfGameLost()

            if (remaining <= 0) {
                clearInterval(interval)
            }
        }, 1000)
    }

    // function setNewCountdownLength() {
    //     $countdownLength = Date.now() + 120000
    // }

    function getRemainingSeconds() {
        const now = Date.now()
        const remaining = Math.floor(($countdownLength - now) / 1000)
        return remaining
    }

    function getDisplayTimer(remainingSeconds) {
        const minutes = Math.floor(remainingSeconds / 60)
        let seconds = (remainingSeconds - minutes * 60).toString()
        seconds = seconds.length > 1 ? seconds : `0${seconds}`
        return `0${minutes}: ${seconds}`
    }

    function checkIfGameLost() {
        if (!$isGameWon && getRemainingSeconds() <= 0) {
            revealYourSecrets()
            setGameLostStatus(true)
            setGameWonStatus(false)
        } else if (isGameWon && getRemainingSeconds() <= 0) {
            revealYourSecrets()
            setGameLostStatus(false)
            setGameWonStatus(false)
        }
    }

    function openModal() {
        $showModal = true
    }
</script>

<nav class="header">
    <ul>
        <span class="game-info"
            >Score: <li class="current-info">{$currentRoundScore}</li></span
        >
        <span class="game-info"
            >Time: <li class="current-info" bind:this={gameInfoTimer} /></span
        >
        <span class="game-info"
            >Round: <li class="current-info">{$currentRound}</li></span
        >
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

    .current-info {
        @apply ml-4;
        font-family: 'Roboto Mono';
    }

    .icons {
        @apply cursor-pointer;
    }
</style>
