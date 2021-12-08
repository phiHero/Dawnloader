new fullpage("#fullPage", {
  autoScrolling: true,
  navigation: true,
  navigationPosition: "left",
});

// Getting things
const inputBox = document.getElementById("input1");
const Dbutton = document.getElementById("button1");
const inputForm1 = document.getElementById("inputForm1");

const inputBox2 = document.getElementById("input2");
const Dbutton2 = document.getElementById("button2");
const inputForm2 = document.getElementById("inputForm2");

Dbutton.onclick = () => {
  setTimeout(function () {
    inputBox.value = "";
  }, 1250);
};

inputForm1.addEventListener("input", () => {
  if (inputBox.value.trim().length > 20) {
    Dbutton.removeAttribute("disabled");
  } else {
    Dbutton.setAttribute("disabled", "disabled");
  }
});

Dbutton2.onclick = () => {
  setTimeout(function () {
    inputBox2.value = "";
  }, 1250);
};

inputForm2.addEventListener("input", () => {
  if (inputBox2.value.trim().length > 20) {
    Dbutton2.removeAttribute("disabled");
  } else {
    Dbutton2.setAttribute("disabled", "disabled");
  }
});
