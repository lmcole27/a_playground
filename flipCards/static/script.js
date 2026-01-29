const card = document.getElementById('card');
const phrase = document.getElementById("cardFront")
const tranlation = document.getElementById("cardBack")
const flipBTN = document.getElementById("flipBtn")
const nextBTN = document.getElementById("nextBtn")
const hideBTN = document.getElementById("hideBtn")
let currentCardID = null;
flipBTN.addEventListener('click', flipCard)
nextBTN.addEventListener('click', getPhrase)
hideBTN.addEventListener('click', hideCard)

//USING ASYNC/AWAIT
async function getPhrase() {
    const config = { 
        headers:{
            'Accept': 'application/json'
            } }
    const response = await fetch('http://127.0.0.1:5001/api/nextCard', config)
    const data = await response.json()
    phrase.innerHTML = data.Phrase
    tranlation.innerHTML = data.Translation
    currentCardID = data.cardID
    cardFront.classList.remove('hidden');
    cardBack.classList.add('hidden');
    console.log(data.Phrase)
    console.log(data.Translation)
    console.log(data.cardID)
}

// flipCard()
function flipCard() {
  cardFront.classList.toggle('hidden');
  cardBack.classList.toggle('hidden');
}

// hideCard()
// async function hideCard() {
//   console.log("Hiding card");
//     const response = await fetch('http://127.0.0.1:5001/api/userCard', config)
//     const data = await response.json()
//     console.log(data.message);
// }

async function hideCard() {
  console.log("Hiding card", currentCardID);

  const response = await fetch("http://127.0.0.1:5001/api/hideCard",
    {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        currentCardID: currentCardID,
        status: "hide"
      })
    }
  );

  const data = await response.json();
  console.log(data.message);
  getPhrase(); // Fetch a new phrase after hiding the current one
}

// window.onload = () => {
//     fetch('/api/get_session', {
//         method: 'GET', // HTTP method
//         headers: {
//             'Content-Type': 'application/json' // Tells the server you're sending JSON
//         },
//         credentials: 'include',
//         //body: JSON.stringify('xyz')
//       })
//       .then(res => res.json())
//       .then(data => {
//         if (data.success) {
//           const token = data.token
//           showOutput(`Welcome Guest ${token}`);
//           closePopup();
//         } else {
//             showPopup();
//         }
// })
// };

