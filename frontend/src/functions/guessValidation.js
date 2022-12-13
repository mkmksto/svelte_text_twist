/**
 *
 * @param {String} guess
 * @param {Array} arrayOfWords
 * @returns [bool, int] true if the guess is valid, int is the index of the guess in the array
 */
export function validateGuess(guess, arrayOfWords) {
    const isGuessInArray = arrayOfWords.includes(guess)
    const idxOfGuess = arrayOfWords.indexOf(guess)
    return [isGuessInArray, idxOfGuess]
}
