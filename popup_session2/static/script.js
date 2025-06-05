window.onload = () => {
    fetch('/api/profile', { credentials: 'include' })
      .then(res => res.json())
      .then(data => {
        if (data.username) {
          document.getElementById('welcome').innerText = `Welcome, ${data.username}!`;
        } else {
          showPopup();
        }
      });
  };
  
  function showPopup() {
    document.getElementById('popup').style.display = 'block';
  }
  
  function submitLogin() {
    const username = document.getElementById('usernameInput').value;
  
    fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({ username })
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        location.reload(); // reload to show welcome
      } else {
        alert('Login failed');
      }
    });
  }