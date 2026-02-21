const card = document.getElementById('card');
const phrase = document.getElementById("cardFront")
const tranlation = document.getElementById("cardBack")
const flipBTN = document.getElementById("flipBtn")
const nextBTN = document.getElementById("nextBtn")
const hideBTN = document.getElementById("hideBtn")
const showAllBTN = document.getElementById("showAllBtn")
const shuffleBTN = document.getElementById("shuffleBtn")
let currentCardID = null;
flipBTN.addEventListener('click', flipCard)
nextBTN.addEventListener('click', getPhrase)
hideBTN.addEventListener('click', hideCard)
showAllBTN.addEventListener('click', showAll)
// shuffleBTN.addEventListener('click', shuffleCards)

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



function showToast(message, options = {}) {
  const { duration = 4000, undoText, onUndo } = options;

  const container = document.getElementById("toast-container");

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;

  // Close (X) button
  const closeBtn = document.createElement("button");
  closeBtn.className = "toast-close";
  closeBtn.innerHTML = "&times;";
  closeBtn.onclick = () => toast.remove();
  toast.appendChild(closeBtn);

  if (undoText && onUndo) {
    const undoBtn = document.createElement("button");
    undoBtn.textContent = undoText;
    undoBtn.onclick = () => {
      onUndo();
      toast.remove();
    };
    toast.appendChild(undoBtn);
  }

  container.appendChild(toast);

  setTimeout(() => {
    toast.remove();
  }, duration);
}

// Show All Cards
async function showAll() {
  console.log("Showing all cards");

  const response = await fetch("http://127.0.0.1:5001/api/showAll",
    {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        status: "show"
      })
    }
  );
  showToast("All cards are now visible.");
}