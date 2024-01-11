let option = localStorage.getItem('setOption');
    (() => {
        Array.from(document.querySelectorAll('option')).forEach((item) => {
            if (item.innerText === '') {
                item.setAttribute('hidden', '');
            }
            if (item.text === option) {
                item.setAttribute('selected', '');
            }
        });
    })();