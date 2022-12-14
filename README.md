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

- ensure that the letter order click is preserved when showing the user's guess
- maybe i can store the UUID inside the guess store as well
- and then from lines 72 onward `CurrentWord.svelte`, iterate over the elements
- how to:
- { letter, id}, idx
- use the above idx, maybe use some js on line 83 to get the item from the currentGuess store by idx
- iirc, anything inside {} can be valid js

# To Do List

- timer of 2 minutes
- skip button disabled when longest word has not been guessed
- skippable if longest=Ok
- SCORE tracker
- ROUND tracker
- Intersection observer that limits the num of words if the subwords intersect with the border of the card
- check the tempSettings store thing, might not be nec. anymore
- ^ or simply resize the card to accomodate the num of words
