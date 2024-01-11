(() => {
        BirthOption = document.getElementById('input_birth');
        currentDate = new Date();
        let year = currentDate.getFullYear();
        let month = currentDate.getMonth() + 1;
        let day = currentDate.getUTCDate();
        if (month < 10) month = '0' + month;
        if (day < 10) day = '0' + day;
        year = year - 18;
        maxBirth = year + '-' + month + '-' + day;
        BirthOption.setAttribute('max', maxBirth);
    })();