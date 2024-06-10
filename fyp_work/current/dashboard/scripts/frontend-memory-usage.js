let lastLine = 0;
let chart;

function requestNewData() {
  fetch('integration_Code/frontend_memory_result.csv')
   .then(response => response.text())
   .then(csv => {
      const lines = csv.split('\n');
      const newData = lines.slice(-60); // get last 60 lines
      updateGraph(newData);
    });
  setTimeout(requestNewData, 60000); // call this function every 1 minute
}

function updateGraph(data) {
  const seriesData = [];
  const  formattedSeriesData = [];
 data.forEach(line => {
  const [x, y, isAnomaly] = line.split(',');

  const point = [x, parseFloat(y)];
  const date = new Date(x);
  date.setHours(date.getHours() + 5);


  if (isAnomaly === '1') {
    seriesData.push({
      x: date.getTime(), // Convert x to timestamp
      y: parseFloat(y),
      marker: {
        symbol: 'circle',
        fillColor: 'red'
      }
    });
  } else {
    seriesData.push([date.getTime(), parseFloat(y)]);
  }
});


  if (!chart) {
    chart = Highcharts.chart('container', {
      chart: {
        type: 'line'
      },
      title: {
        text: 'Frontend Pod Memory Usage'
      },
      xAxis: {
        type: 'datetime'
      },
      series: [{
        data: seriesData,
        color: "gray"
      }]
    });
  } else {
    
    chart.series[0].setData(seriesData);
  }
}

requestNewData(); // initial call to fetch data and create graph