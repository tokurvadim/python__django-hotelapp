(() => {
        currentDate = new Date();
        let year = currentDate.getFullYear();
        let month = currentDate.getMonth() + 1;
        let day = currentDate.getUTCDate();
        if (month < 10) month = '0' + month;
        if (day < 10) day = '0' + day;
        minFormDateValue = year + '-' + month + '-' + day;
        dateInOption = document.getElementById('input_datein');
        dateOutOption = document.getElementById('input_dateout');
        dateInOption.setAttribute('min', minFormDateValue);
        dateOutOption.setAttribute('min', minFormDateValue);
    })();