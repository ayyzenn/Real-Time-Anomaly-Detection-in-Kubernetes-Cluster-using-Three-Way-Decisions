let lastLine2 = 0;
let chart2;

function requestNewData2() {
  fetch('intergation_Code/user_memory_result.csv')
   .then(response => response.text())
   .then(csv => {
      const lines = csv.split('\n');
      const newData = lines.slice(-60); // get last 60 lines
      updateGraph2(newData);
    });
  setInterval(requestNewData2, 60000); // call this function every 1 minute
}

function updateGraph2(data) {
  const seriesData2 = [];
  const  formattedSeriesData2 = [];
 data.forEach(line => {
  const [x, y, isAnomaly] = line.split(',');

  const point = [x, parseFloat(y)];
  const date = new Date(x);
  date.setHours(date.getHours() + 5);


  if (isAnomaly === '1') {
    seriesData2.push({
      x: date.getTime(), // Convert x to timestamp
      y: parseFloat(y),
      marker: {
        symbol: 'circle',
        fillColor: 'red'
      }
    });
  } else {
    seriesData2.push([date.getTime(), parseFloat(y)]);
  }
});


  if (!chart2) {
    chart2 = Highcharts.chart('container2', {
      chart1: {
        type: 'line'
      },
      title: {
        text: 'User Pod Memory Usage'
      },
      xAxis: {
        type: 'datetime'
      },
      series: [{
        data: seriesData2,
        color: "gray"
      }]
    });
  } else {
    
    chart2.series[0].setData(seriesData2);
  }
}

requestNewData2(); // initial call to fetch data and create graph