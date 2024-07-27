const form = document.querySelector('#all-platforms');
const button = form.querySelector('button');
const select = form.querySelector('select');
const errMsg = document.getElementById('error-message');

const title = form.querySelector('h3').innerText;

button.addEventListener('click', (e) => {
  e.preventDefault();
  button.innerText = 'Downloading file...';
  const URL = select.value;
  fetch(URL)
    .then((res) => {
      if (!res.ok) {
        throw new Error('Network Problem');
      }
      return res.blob();
    })
    .then((file) => {
      let tUrl = URL.createObjectURL(file);
      const tmp1 = document.createElement('a');
      tmp1.href = tUrl;

      const selectedOption = select.options[select.selectedIndex];
      const quality = selectedOption.getAttribute('data-label');
      const ext = selectedOption.getAttribute('data-ext');

      tmp1.download = `${title} - ${quality}.${ext}`;
      document.body.appendChild(tmp1);
      tmp1.click();
      button.innerText = 'Download File';
      URL.revokeObjectURL(tUrl);
      tmp1.remove();
    })
    .catch(() => {
      errMsg.textContent = 'Cannot Download Restricted Content!';
      button.innerText = 'Download File';
      window.open(URL, '_blank').focus();
    });
});
