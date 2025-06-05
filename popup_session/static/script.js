/*
function showPopup() {
    document.getElementById('popup').style.display = 'flex';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
} 
*/

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

function handleAuthFlow() {
    const id = getCookie("session"); // or sessionStorage.getItem()

    if (id) {
        // Do something: redirect to dashboard, hide login popup, etc.
        document.getElementById('popup').style.display = 'none';
        document.body.classList.remove('modal-open');
        document.getElementById('main-content').classList.add('active');
        showOutput(id)
    } else {
        // Show login popup or redirect
        document.getElementById('popup').style.display = 'flex';
        document.body.classList.add('modal-open');
        document.getElementById('main-content').classList.remove('active');
    }
}


window.onload = handleAuthFlow;

function closePopup() {
    document.getElementById('popup').style.display = 'none';
    document.body.classList.remove('modal-open');
    document.getElementById('main-content').classList.add('active');
}

let token = ''

function showOutput(data) {
document.getElementById('output').textContent = JSON.stringify(data, null, 2);
}

function getGuestToken() {
    fetch('http://localhost:5003/set_session', {
        method: 'GET',
        credentials: 'include',  // This is needed to include cookies in the request
        mode: 'no-cors'  // Add no-cors mode
    })
        .then(res => res.json())
        .then(data => {
            showOutput({ msg: 'Guest Session Started', data });
            document.getElementById('popup').style.display = 'none';
            document.getElementById('main-content').classList.add('active');
        })
        .catch(err => {
            showOutput({ error: err.message });
            console.error('Error:', err);
        });
}

function getStoredToken() {
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
        const parsedToken = JSON.parse(storedToken);
        showOutput({ msg: 'Retrieved stored token', token: parsedToken });
        return parsedToken;
    } else {
        showOutput({ msg: 'No token found in storage' });
        return null;
    }
}

function verifyTokenWithServer() {
    const storedToken = getStoredToken();
    if (!storedToken) {
        showOutput({ error: 'No token to verify' });
        return;
    }

    fetch('http://localhost:5005/verify_token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token: storedToken })
    })
    .then(res => res.json())
    .then(data => {
        showOutput({ msg: 'Server verification result', ...data });
    })
    .catch(err => {
        showOutput({ error: err.message });
        console.error('Error:', err);
    });
}
