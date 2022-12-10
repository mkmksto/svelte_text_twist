import { readable } from 'svelte/store'

export const randomWord = readable(new Promise((res) => {}), async function start(set) {
    set(getRandomWord())

    return function stop() {}
})

async function getRandomWord() {
    const res = await fetch('http://127.0.0.1:5000/api/random_word')
    const data = await res.json()
    return data
}
