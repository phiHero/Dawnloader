new fullpage('#fullPage', {
  autoScrolling: true,
  navigation: true,
  navigationPosition: 'left',
});
const expression =
  /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi;
const regexURL = new RegExp(expression);
// Input validation 😅
const forms = document.querySelectorAll('.download_form');
for (const form of forms) {
  const input = form.querySelector('.url_input');
  const btn = form.querySelector('.download_btn');

  btn.addEventListener('click', () => {
    validateInput(input, btn) && form.submit();
  });
  form.addEventListener('input', () => {
    validateInput(input, btn);
  });
}

function validateInput(inputEl, btn) {
  const result = inputEl.value.match(regexURL);
  if (result) {
    btn.removeAttribute('disabled');
  } else {
    btn.setAttribute('disabled', 'disabled');
  }
  return result;
}

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
