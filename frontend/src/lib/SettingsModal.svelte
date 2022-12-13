<script>
    import { onMount } from 'svelte'
    import { renewCurrentWord } from '../functions/dataFetching'
    import { gameSettings, showModal, tempGameSettings } from '../stores/gameSettings'

    onMount(() => {
        $tempGameSettings = $gameSettings
    })

    function hideModal() {
        $showModal = false
        console.log($tempGameSettings)
    }

    function handleKeyDown(e) {
        if (e.key === 'Escape') {
            $showModal = false
        }
    }

    function saveSettingsAndRestart() {
        renewCurrentWord($gameSettings)
        hideModal()
    }
</script>

<svelte:window on:keydown={(e) => handleKeyDown(e)} />

<div class="modal" on:click|self={hideModal}>
    <div class="modal-card">
        <div class="setting">
            <label for="min-chars">Min Number of Characters</label>
            <input
                type="range"
                min="6"
                max="10"
                bind:value={$tempGameSettings.min_chars}
                class="range"
                id="min-chars"
            />
            <span class="label-val">{$tempGameSettings.min_chars}</span>
        </div>
        <div class="setting">
            <label for="max-chars">Max Number of Characters</label>
            <input
                type="range"
                min="9"
                max="13"
                bind:value={$tempGameSettings.max_chars}
                class="range"
                id="max-chars"
            />
            <span class="label-val">{$tempGameSettings.max_chars}</span>
        </div>
        <div class="setting">
            <label for="difficulty">Difficulty</label>
            <select
                id="difficulty"
                class="bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg block w-40 p-1.5 ml-auto"
                bind:value={$tempGameSettings.difficulty}
            >
                <option selected>Medium</option>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
                <option value="very_hard">Very Hard</option>
            </select>
        </div>
        <div class="setting">
            <label for="max-subwords">Max Number of Subwords</label>
            <input
                type="range"
                min="10"
                max="30"
                bind:value={$tempGameSettings.max_subwords}
                class="range"
                id="max-subwords"
            />
            <span class="label-val">{$tempGameSettings.max_subwords}</span>
        </div>
        <div class="setting">
            <label for="timer">Alloted Time</label>
            <input
                type="range"
                min="30"
                max="300"
                bind:value={$tempGameSettings.timer}
                class="range"
                id="timer"
            />
            <span class="label-val">{$tempGameSettings.timer}</span>
        </div>

        <button class="save" on:click={hideModal}>Save but don't Restart</button>
        <button class="restart" on:click={saveSettingsAndRestart}>Save and Restart</button>
    </div>
</div>

<style>
    button {
        @apply cursor-pointer mt-auto;
    }

    .save {
        @apply bg-neutral-200 text-neutral-600 hover:bg-neutral-300;
    }

    .restart {
        @apply bg-red-700 text-white mt-2 hover:bg-red-800;
    }

    .setting {
        @apply flex items-center mb-4;
    }

    .setting input {
        @apply ml-auto;
    }

    .setting label {
        color: grey;
    }

    .label-val {
        @apply w-4 text-center ml-2;
    }

    .modal {
        font-family: 'Open Sans';
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        width: 100vw;
        background-color: rgba(50, 50, 50, 0.4);
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .modal-card {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 20%;
        width: 400px;
        height: 450px;
        border-radius: 1rem;
        background-color: white;
        padding: 1.5rem;
    }

    .range {
        @apply bg-gray-200 rounded-lg appearance-none h-2 mt-auto mb-auto;
    }
</style>
