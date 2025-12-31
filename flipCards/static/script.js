const card = document.getElementById('card');
const phrase = document.getElementById("cardFront")
const tranlation = document.getElementById("cardBack")
const flipBTN = document.getElementById("flipBtn")
const nextBTN = document.getElementById("nextBtn")
flipBTN.addEventListener('click', flipCard)
nextBTN.addEventListener('click', getPhrase)

//generateJoke()


//USING ASYNC/AWAIT
async function generateJoke() {
    const config = { 
        headers:{
            'Accept': 'application/json'
            } }
    
    const response = await fetch('https://icanhazdadjoke.com', config)
    const data = await response.json()
    jokeEl.innerHTML = data.joke
}

// getPhrase()
async function getPhrase() {
    const config = { 
        headers:{
            'Accept': 'application/json'
            } }
    
    const response = await fetch('http://127.0.0.1:5001/api', config)
    const data = await response.json()
    phrase.innerHTML = data.Phrase
    tranlation.innerHTML = data.Translation
    //console.log(data.Phrase)
    //console.log(data.Translation)
}

// flipCard()
function flipCard() {
  cardFront.classList.toggle('hidden');
  cardBack.classList.toggle('hidden');
}


