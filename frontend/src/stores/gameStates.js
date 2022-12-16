import { writable } from 'svelte/store'
import { currentRandomWord, validLetters } from './gameSettings'

export const validatedGuessesStore = writable([])

export const currentRoundScore = writable(0)

export const countdownLength = writable()

export const currentRound = writable(1)

export const isGameWon = writable(false)

export const isGameLost = writable(false)

export function revealYourSecrets() {
    let curWord
    const unsub = currentRandomWord.subscribe((word) => {
        curWord = word
    })

    curWord.sub_words.forEach((subword) => {
        subword.has_been_guessed = true
    })

    currentRandomWord.set(curWord)
    unsub()
}

export function setGameToLost() {
    isGameLost.set(true)
}

export function incrementCurrentRound() {
    let prevRound
    currentRound.subscribe((round) => (prevRound = round))
    currentRound.set(prevRound++)
}

export function resetCurrentRound() {
    currentRound.set(1)
}

export function resetValidLetters() {
    validLetters.set(new Set())
}

export function resetScore() {
    currentRoundScore.set(0)
}

export function setGameWonStatus(bool) {
    isGameWon.set(bool)
}

export function setGameLostStatus(bool) {
    isGameLost.set(bool)
}
