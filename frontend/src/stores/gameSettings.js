import { writable } from 'svelte/store'

export const gameSettings = writable({
    min_chars: 6,
    max_chars: 12,
    difficulty: 'medium',
    max_subwords: 20,
    timer: 120,
})

// temporary Game settings used only for display
// so that the page doesn't refresh when i update the settings
// TODO: check this, this might not even be necessary now that
// the random word isn't a derived store
export const tempGameSettings = writable({
    min_chars: 6,
    max_chars: 12,
    difficulty: 'medium',
    max_subwords: 20,
    timer: 120,
})

export const currentRandomWord = writable({ shuffled_word: [], sub_words: [], word: '' })

export const currentGuess = writable([])

export const showModal = writable(false)

export const validLetters = writable(new Set())
