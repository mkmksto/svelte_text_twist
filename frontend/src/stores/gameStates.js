import { writable } from 'svelte/store'

export const validatedGuessesStore = writable([])

export const currentRoundScore = writable(0)
