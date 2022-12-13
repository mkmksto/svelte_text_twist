/**
 * Fetch data from the backend contaiing the word, its subwords, and a shuffled representation
 * @param {Object} gameSettings 
 * @returns Promise, when resolved is a json representation of the python response 
 */
export async function(gameSettings) {
    const res = await fetch('http://127.0.0.1:5000/api/random_word', {
        method: 'POST',
        headers: {
            'Accept': 'applications/json',
            'Content-type': 'application/json'
        },
        body:JSON.stringify(gameSettings) 
    })
    const py_resp = await res
    return py_resp.json()
}