const gaugeElement1 = document.querySelector(".gauge");

function setGaugeValue(gauge, value) {
    if (value < 0 || isNaN(value)) {
        value = 0; // Replace NaN with 0
    }

    gauge.querySelector(".gauge__fill").style.transform = `rotate(${((value)/100) / 2}turn)`;
    gauge.querySelector(".gauge__cover").textContent = `${value}%`;

    const statsElement1 = document.querySelector(".overall-stats");
    statsElement1.querySelector(".used_memory").textContent = `${((value*16)/100).toFixed(2)} GiB`;
}


function fetchAndSetGaugeValue() {
    fetch('integration_Code/Sock-shop_memory_usage.csv')
        .then(response => response.text())
        .then(csvText => {
            const rows = csvText.trim().split('\n');
            const lastRow = rows[rows.length - 1];
            const columns = lastRow.split(',');
            const value = parseFloat(columns[1]); // Get the value from the second column
            setGaugeValue(gaugeElement1, value);
        })
        .catch(error => {
            console.error('Error fetching CSV:', error);
        });
}

// Call fetchAndSetGaugeValue initially
fetchAndSetGaugeValue();

// Call fetchAndSetGaugeValue every minute
setInterval(fetchAndSetGaugeValue, 60000); // 60000 milliseconds = 1 minute



