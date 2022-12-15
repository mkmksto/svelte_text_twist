import { writable } from 'svelte/store'

export const validatedGuessesStore = writable([])

export const currentRoundScore = writable(0)

export const countdownLength = writable()

export const currentRound = writable(1)

export const isGameWon = writable(false)

export const isGameLost = writable(false)
