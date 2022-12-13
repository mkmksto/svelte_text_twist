My implementation of text twist with Svelte on the frontend and Flask on the backend

# Organization

- frontend: svelte iniviated using Vite
- backend: Python Flask app
- has a virtual environment called text_twist_venv (backend/text_twist_venv) containing all python dependencies

# Animation

- use `animate:flip` on every element you want animated
- those elements should have an accompanying unique ID
- these enables animations like shuffle
- (word transfer animation)
- place an additional word_transfer property for each letter
- we then filter the letters to go up or down depending on wether the value is true or false

# Tomorrow To Do

- guessing adds guess to particular box

# To Do List

- timer of 2 minutes
- skip button disabled when longest word has not been guessed
- skippable if longest=Ok
- SCORE tracker
- ROUND tracker
- Intersection observer that limits the num of words if the subwords intersect with the border of the card
- check the tempSettings store thing, might not be nec. anymore
- ^ or simply resize the card to accomodate the num of words
