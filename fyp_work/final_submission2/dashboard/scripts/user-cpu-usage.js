let lastLine3 = 0;
let chart3;

function requestNewData3() {
  fetch('intergation_Code/user_cpu_result.csv')
   .then(response => response.text())
   .then(csv => {
      const lines = csv.split('\n');
      const newData = lines.slice(-60); // get last 60 lines
      updateGraph3(newData);
    });
  setTimeout(requestNewData3, 60000); // call this function every 3 minute
}

function updateGraph3(data) {
  const seriesData3 = [];
  const  formattedSeriesData = [];
 data.forEach(line => {
  const [x, y, isAnomaly] = line.split(',');

  const point = [x, parseFloat(y)];
  const date = new Date(x);
  date.setHours(date.getHours() + 5);


  if (isAnomaly === '3') {
    seriesData3.push({
      x: date.getTime(), // Convert x to timestamp
      y: parseFloat(y),
      marker: {
        symbol: 'circle',
        fillColor: 'red'
      }
    });
  } else {
    seriesData3.push([date.getTime(), parseFloat(y)]);
  }
});


  if (!chart3) {
    chart3 = Highcharts.chart('container3', {
      chart3: {
        type: 'line'
      },
      title: {
        text: 'User Pod CPU Usage'
      },
      xAxis: {
        type: 'datetime'
      },
      series: [{
        data: seriesData3,
        color: "gray"
      }]
    });
  } else {
    
    chart3.series[0].setData(seriesData3);
  }
}

requestNewData3(); // initial call to fetch data and create graph