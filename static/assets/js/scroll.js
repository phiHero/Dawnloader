new fullpage("#fullPage", {
  autoScrolling: true,
  navigation: true,
  navigationPosition: "left",
});

const inputBox = document.getElementById("input1");
const Dbutton = document.getElementById("button1");
const inputBox2 = document.getElementById("input2");
const Dbutton2 = document.getElementById("button2");
Dbutton.disabled = true;
Dbutton.onclick = () => {
  setTimeout(function () {
    inputBox.value = "";
  }, 1300);
};
inputBox.onkeydown = () => {
  let userData = inputBox.value;
  if (userData.trim() != 0) {
    Dbutton.disabled = false;
  }
};
inputBox.onkeyup = () => {
  let userData = inputBox.value;
  if (userData.trim() != 0) {
    Dbutton.disabled = false;
  }
};
Dbutton2.disabled = true;
Dbutton2.onclick = () => {
  setTimeout(function () {
    inputBox2.value = "";
  }, 1300);
};
inputBox2.onkeydown = () => {
  let userData2 = inputBox2.value;
  if (userData2.trim() != 0) {
    Dbutton2.disabled = false;
  }
};
inputBox2.onkeyup = () => {
  let userData2 = inputBox.value;
  if (userData2.trim() != 0) {
    Dbutton2.disabled = false;
  }
};
