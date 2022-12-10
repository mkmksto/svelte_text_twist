import { derived, writable } from 'svelte/store'

export const gameSettings = writable({
    min_chars: 6,
    max_chars: 12,
    difficulty: 'medium',
    max_subwords: 20,
    timer: 120,
})

export const getRandomWord = derived(gameSettings, async ($gameSettings) => {
    const res = await fetch('http://127.0.0.1:5000/api/random_word', {
        method: 'POST',
        headers: {
            Accept: 'applications/json',
            'Content-type': 'application/json',
        },
        body: JSON.stringify($gameSettings),
    })
    const py_resp = await res
    return py_resp.json()
})

export const showModal = writable(false)
