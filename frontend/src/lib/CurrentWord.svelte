<script>
    import { afterUpdate, onDestroy, onMount } from 'svelte'
    import { flip } from 'svelte/animate'
    import { quintOut } from 'svelte/easing'
    import { crossfade } from 'svelte/transition'
    import { renewCurrentWord } from '../functions/dataFetching'
    import {
        currentGuess,
        currentRandomWord,
        gameSettings,
        validLetters,
    } from '../stores/gameSettings'

    const [send, receive] = crossfade({
        duration: (d) => Math.sqrt(d * 500),

        fallback(node, params) {
            const style = getComputedStyle(node)
            const transform = style.transform === 'none' ? '' : style.transform

            return {
                duration: 600,
                easing: quintOut,
                css: (t) => `
					transform: ${transform} scale(${t});
					opacity: ${t}
				`,
            }
        },
    })

    onMount(async () => {
        await renewCurrentWord($gameSettings)
        currentGuess.set([])
        validLetters.set(new Set($currentRandomWord.word))
        console.log('valid keyboard letters ', $validLetters)
    })

    afterUpdate(() => {
        validLetters.set(new Set())
        validLetters.set(new Set($currentRandomWord.word))
        console.log('current word after update')
    })

    onDestroy(() => {
        currentGuess.set([])
        validLetters.set(new Set())
        console.log('destroy??')
    })

    /**
     * Move the clicked letter to/from the options / guessing area
     * @param letterId unique ID of the letter
     */
    function moveLetter(letterId) {
        const clickedLetter = $currentRandomWord.shuffled_word.find(
            (letter) => letterId === letter.id
        )
        clickedLetter.letter_transferred = !clickedLetter.letter_transferred
        $currentRandomWord = $currentRandomWord
    }

    function updateGuessStore(letter, letterId) {
        const clickedLetter = $currentRandomWord.shuffled_word.find(
            (letter) => letterId === letter.id
        )

        if (clickedLetter.letter_transferred) {
            $currentGuess = [...$currentGuess, { letter: letter, id: letterId }]
        } else {
            const idx = $currentGuess.findIndex((letter) => letter.id === letterId)

            if (idx > -1) $currentGuess.splice(idx, 1)
            $currentGuess = $currentGuess
        }
        console.log('new current guess', $currentGuess)
    }
</script>

<div class="letter-guesses letter">
    {#if $currentGuess.length > 0}
        {#each $currentGuess as { letter, id } (id)}
            <div
                class="cell letter-cell "
                in:receive={{ key: id }}
                out:send={{ key: id }}
                animate:flip={{ duration: 600 }}
                on:click={() => {
                    moveLetter(id)
                    updateGuessStore(letter, id)
                }}
            >
                {letter}
            </div>
        {/each}
    {:else}
        <div class="fetching" />
    {/if}
</div>

<div class="letter-options letter">
    {#each $currentRandomWord.shuffled_word.filter((letter) => !letter.letter_transferred) as { letter, id } (id)}
        <div
            class="cell letter-cell"
            in:receive={{ key: id }}
            out:send={{ key: id }}
            animate:flip={{ duration: 600 }}
            on:click={() => {
                moveLetter(id)
                updateGuessStore(letter, id)
            }}
        >
            {letter}
        </div>
    {:else}
        <div class="fetching">...</div>
    {/each}
</div>

<style>
    .letter {
        @apply flex mt-4 h-14;
    }

    .letter-options {
        background-color: white;
        border-color: 3px solid var(--pink);
    }

    .letter-guesses {
    }

    .cell {
        @apply flex justify-center items-center mx-2 text-4xl w-14 h-14 bg-white rounded text-neutral-500 font-bold;
    }

    .letter-cell {
        @apply rounded-full uppercase cursor-pointer text-neutral-600 hover:text-neutral-400 bg-white border border-solid border-neutral-400;
    }

    .empty-cell {
        @apply relative bg-neutral-200 text-opacity-0;
    }

    .empty-cell::after {
        @apply content-none absolute w-full h-full border border-solid border-white rounded-full;
    }

    .fetching {
        @apply text-gray-300 w-14 h-14;
    }
</style>
