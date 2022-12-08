function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min
}

/**
 *
 * @param {Array} arr
 * @returns
 */
export function getRandomItem(arr) {
    return arr[getRandomInt(0, arr.length - 1)]
}
