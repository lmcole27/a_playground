/* function showPopup() {
    document.getElementById('popup').style.display = 'flex';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
} 

const showPopup = { show_popup | tojson };

const showPopup = document.body.dataset.showPopup === "true";
*/
/*
localStorage.setItem('token', jwt_token);

const token = localStorage.getItem('token');
fetch('/protected', {
  headers: { 'Authorization': `Bearer ${token}` }
});
*/
// Check if JWT token exists and is valid
function isJwtValid(token) {
    try {
        const decoded = jwt_decode(token); // from jwt-decode
        const currentTime = Math.floor(Date.now() / 1000); // in seconds
        return decoded.exp && decoded.exp > currentTime;
    } catch (e) {
        return false;
    }
}

function handleAuthFlow() {
    const token = localStorage.getItem('token'); // or sessionStorage.getItem()

    if (token && isJwtValid(token)) {
        console.log("✅ Token exists and is valid");
        // Do something: redirect to dashboard, hide login popup, etc.
        document.getElementById('popup').style.display = 'none';
        document.body.classList.remove('modal-open');
        document.getElementById('main-content').classList.add('active');
    } else {
        console.log("❌ No token or token is invalid/expired");
        // Show login popup or redirect
        document.getElementById('popup').style.display = 'flex';
        document.body.classList.add('modal-open');
        document.getElementById('main-content').classList.remove('active');
    }
}

window.onload = handleAuthFlow;


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : null;
}
/*
const token = getCookie('token');
const token = localStorage.getItem('token');
const decoded = jwt_decode(token); 
/*
window.onload = function () {
    if (showPopup) {
        document.getElementById('popup').style.display = 'flex';
        document.body.classList.add('modal-open');
        document.getElementById('main-content').classList.remove('active');
    } else {
        document.getElementById('popup').style.display = 'none';
        document.getElementById('main-content').classList.add('active');
    }
};

function closePopup() {
    document.getElementById('popup').style.display = 'none';
    document.body.classList.remove('modal-open');
    document.getElementById('main-content').classList.add('active');
}
*/

let token = ''

function showOutput(data) {
document.getElementById('output').textContent = JSON.stringify(data, null, 2);
}

function getGuestToken() {
fetch('http://localhost:5005/guest')
    .then(res => res.json())
    .then(data => {
    token = data.access_token;
    showOutput({ msg: 'Token received', token });
    localStorage.setItem('token', token);})
    .catch(err => showOutput({ error: err.message }));
    document.getElementById('popup').style.display = 'none';
    document.getElementById('main-content').classList.add('active');
}

function callWhoAmI() {
fetch('http://localhost:5005/whoami', {
    headers: {
    Authorization: `Bearer ${token}`
    }
})
    .then(res => res.json())
    .then(data => showOutput(data))
    .catch(err => showOutput({ error: err.message }));
}

function callGuestZone() {
fetch('http://localhost:5005/guest-zone', {
    headers: {
    Authorization: `Bearer ${token}`
    }
})
    .then(res => res.json())
    .then(data => showOutput(data))
    .catch(err => showOutput({ error: err.message }));
}