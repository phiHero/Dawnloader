new fullpage('#fullPage', {
  autoScrolling: true,
  navigation: true,
  navigationPosition: 'left',
});

// Getting things
const inputBox = document.getElementById('input1');
const Dbutton = document.getElementById('button1');
const inputForm1 = document.getElementById('inputForm1');

const inputBox2 = document.getElementById('input2');
const Dbutton2 = document.getElementById('button2');
const inputForm2 = document.getElementById('inputForm2');

inputForm1.addEventListener('input', () => {
  if (inputBox.value.trim().length > 20) {
    Dbutton.removeAttribute('disabled');
  } else {
    Dbutton.setAttribute('disabled', 'disabled');
  }
});

Dbutton2.onclick = () => {
  setTimeout(function () {
    inputBox2.value = '';
  }, 1500);
};

inputForm2.addEventListener('input', () => {
  if (inputBox2.value.trim().length > 20) {
    Dbutton2.removeAttribute('disabled');
  } else {
    Dbutton2.setAttribute('disabled', 'disabled');
  }
});

// Slideshow

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName('mySlides');
  var dots = document.getElementsByClassName('dot');
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(' active', '');
  }
  slides[slideIndex - 1].style.display = 'block';
  dots[slideIndex - 1].className += ' active';
}
