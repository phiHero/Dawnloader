// Getting things
const inputBox = document.getElementById("input1");
const Dbutton = document.getElementById("button1");

Dbutton.disabled = true;
Dbutton.onclick = () => {
  setTimeout(function () {
    inputBox.value = "";
  }, 1000);
};

inputBox.onkeydown = () => {
  let userData = inputBox.value;
  if (userData.trim() != 0) {
    Dbutton.classList.add("active_1");
    Dbutton.disabled = false;
  } else {
    Dbutton.classList.remove("active_1");
  }
};
inputBox.onkeyup = () => {
  let userData = inputBox.value;
  if (userData.trim() != 0) {
    Dbutton.classList.add("active_1");
    Dbutton.disabled = false;
  } else {
    Dbutton.classList.remove("active_1");
  }
};
