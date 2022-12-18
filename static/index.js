function classifyText(){
  
let msgerInput = document.getElementById("msger-input");

msgText = msgerInput.value;

if (!msgText) return;

  try {
    fetch('http://127.0.0.1:5000/classify', {
      method: 'POST',
      mode: "cors",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: msgText,
      }),
    })
    .then(res => res.json())
    .then(res => {
      window.alert(res.message)
    })
  } catch (err) {
    console.log(err);
  }

}