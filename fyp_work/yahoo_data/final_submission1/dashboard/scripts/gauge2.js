const gaugeElement2 = document.querySelector(".gauge2");

function setGaugeValue2(gauge, value) {
    if (value < 0 || isNaN(value)) {
        value = 0; // Replace NaN with 0
    }

    gauge.querySelector(".gauge__fill2").style.transform = `rotate(${((value)/100) / 2}turn)`;
    gauge.querySelector(".gauge__cover2").textContent = `${value}%`;

    const statsElement2 = document.querySelector(".overall-stats2");
    statsElement2.querySelector(".used_cpu").textContent = `${((value*12)/100).toFixed(2)} cores`;
}


function fetchAndSetGaugeValue2() {
    fetch('integration_Code/Sock-shop_cpu_usage.csv')
        .then(response => response.text())
        .then(csvText => {
            const rows = csvText.trim().split('\n');
            const lastRow = rows[rows.length - 1];
            const columns = lastRow.split(',');
            const value = parseFloat(columns[1]); // Get the value from the second column
            setGaugeValue2(gaugeElement2, value);
        })
        .catch(error => {
            console.error('Error fetching CSV:', error);
        });
}

// Call fetchAndSetGaugeValue initially
fetchAndSetGaugeValue2();

// Call fetchAndSetGaugeValue every minute
setInterval(fetchAndSetGaugeValue, 60000); // 60000 milliseconds = 1 minute