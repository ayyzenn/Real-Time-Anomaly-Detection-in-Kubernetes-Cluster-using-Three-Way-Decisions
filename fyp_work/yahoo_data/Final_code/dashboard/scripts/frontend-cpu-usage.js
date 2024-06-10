let lastLine1 = 0;
let chart1;

function requestNewData1() {
  fetch('integration_Code/frontend_cpu_result.csv')
   .then(response => response.text())
   .then(csv => {
      const lines = csv.split('\n');
      const newData = lines.slice(-60); // get last 60 lines
      updateGraph1(newData);
    });
  setInterval(requestNewData1, 60000); // call this function every 1 minute
}

function updateGraph1(data) {
  const seriesData1 = [];
  const  formattedSeriesData1 = [];
 data.forEach(line => {
  const [x, y, isAnomaly] = line.split(',');

  const point = [x, parseFloat(y)];
  const date = new Date(x);
  date.setHours(date.getHours() + 5);


  if (isAnomaly === '1') {
    seriesData1.push({
      x: date.getTime(), // Convert x to timestamp
      y: parseFloat(y),
      marker: {
        symbol: 'circle',
        fillColor: 'red'
      }
    });
  } else {
    seriesData1.push([date.getTime(), parseFloat(y)]);
  }
});


  if (!chart1) {
    chart1 = Highcharts.chart('container1', {
      chart1: {
        type: 'line'
      },
      title: {
        text: 'Frontend Pod CPU Usage'
      },
      xAxis: {
        type: 'datetime'
      },
      series: [{
        data: seriesData1,
        color: "gray"
      }]
    });
  } else {
    
    chart1.series[0].setData(seriesData1);
  }
}

requestNewData1(); // initial call to fetch data and create graph