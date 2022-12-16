My implementation of text twist with Svelte on the frontend and Flask on the backend

# Organization

- frontend: svelte iniviated using Vite
- backend: Python Flask app
- has a virtual environment called text_twist_venv (backend/text_twist_venv) containing all python dependencies
- !IMPORTANT: the currentRandomWord is do be set from inside `CurrentWord.svelte`, it uses a function from `dataFetching.js` that populates it with the nec data after the backend fetch is successful

# Animation

- use `animate:flip` on every element you want animated
- those elements should have an accompanying unique ID
- these enables animations like shuffle
- (word transfer animation)
- place an additional word_transfer property for each letter
- we then filter the letters to go up or down depending on wether the value is true or false

# Tomorrow To Do

- if timer == 0, and game won, move on to next round, and show the remaining unguessed words
- if next round is clicked, show the remaining words
- implement give up btn, show what words they were
- show answers if (game lost, next round, new word, give up)
- improve animation, check docs

## Possible Game States

- time expired(t.e.), word guessed/game won
- te, no word guessed (game won = false)
- game settings reset ()
- game paused

# To Do List

- skippable if longest=Ok
- clicking settings pauses the game
- game won if ANY of the longest words has been guessed
- Intersection observer that limits the num of words if the subwords intersect with the border of the card
- check the tempSettings store thing, might not be nec. anymore
- ^ or simply resize the card to accomodate the num of words
