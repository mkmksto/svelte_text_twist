/**
 *
 * @param {String} guess
 * @param {Array} arrayOfWordObjects
 * @returns [bool, int] true if the guess is valid, int is the index of the guess in the array
 */
export function validateGuess(guess, arrayOfWordObjects) {
    // const isGuessInArray = arrayOfWords.includes(guess)
    // const idxOfGuess = arrayOfWords.indexOf(guess)
    const isGuessInArray = arrayOfWordObjects.some((wordObj) => wordObj.sub_word === guess)
    const idxOfGuess = arrayOfWordObjects.findIndex((wordObj) => wordObj.sub_word === guess)
    return [isGuessInArray, idxOfGuess]
}
