import { currentRandomWord } from '../stores/gameSettings'
/**
 * Fetch data from the backend contaiing the word, its subwords, and a shuffled representation
 * @param {Object} gameSettings
 * @returns Promise, when resolved is a json representation of the python response
 */
export async function fetchBackendWord(gameSettings) {
    const res = await fetch('http://127.0.0.1:5000/api/random_word', {
        method: 'POST',
        headers: {
            Accept: 'applications/json',
            'Access-Control-Allow-Origin': '*',
            'Content-type': 'application/json',
        },
        body: JSON.stringify(gameSettings),
    })
    const py_resp = await res
    return py_resp.json()
}

export async function renewCurrentWord(gameSettings) {
    const backEndData = await fetchBackendWord(gameSettings)
    currentRandomWord.set({ shuffled_word: [], sub_words: [], word: '' })
    currentRandomWord.set(backEndData)
}
