<script>
    import { afterUpdate, onDestroy, onMount } from 'svelte'
    import { shuffleItems } from '../functions/math'
    import { getRandomWord } from '../stores/gameSettings'

    let shuffledWord
    $: wardo = shuffledWord

    onMount(async () => {
        console.log('current word mounted')
        // await tick()
    })

    afterUpdate(async () => {
        await $getRandomWord
        let children = shuffledWord.children
        children = Array.from(children)

        children.forEach((letter) => letter.remove())
        children = shuffleItems(children)
        children.forEach((letter) => {
            shuffledWord.appendChild(letter)
        })
    })

    // async function after() {
    //     await afterUpdate
    //     shuffledWord = newOrder
    // }
    // after()

    // async function shuffleWordRendered(node) {
    //     await $getRandomWord
    //     console.log(node)
    //     const newOrder = shuffleItems(Array.from(node.children))
    //     // node.forEach((oldDiv) => oldDiv.delete())
    //     newOrder.forEach((newDiv) => {
    //         node.appendChild(newDiv)
    //     })
    // }

    onDestroy(() => {
        console.log('cur word destroyed')
    })
</script>

<div class="letter-spaces letter">
    {#await $getRandomWord}
        <div class="fetching">...fetching</div>
    {:then $getRandomWord}
        <!-- loop through each letter -->
        {#each $getRandomWord.word as word}
            <div class="cell empty-cell">{word}</div>
        {/each}
    {/await}
</div>

<!-- <div class="letter-options letter" bind:this={shuffledWord} use:shuffleWordRendered> -->
<div class="letter-options letter" bind:this={shuffledWord}>
    {#await $getRandomWord then $getRandomWord}
        {#each $getRandomWord.word as word}
            <div class="cell letter-cell">{word}</div>
        {/each}
    {/await}
</div>

<style>
    .letter {
        @apply flex mt-4;
    }

    .letter-options {
        background-color: white;
        border-color: 3px solid var(--pink);
    }

    .letter-spaces {
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
        @apply text-gray-300;
    }
</style>
