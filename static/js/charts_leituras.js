const rowTable = document.querySelectorAll(
  "table#tabelaUltimasLeituras tbody tr"
);
const dados = [["Mes", "Consumo"]];

for (const row of rowTable) {
  const totalTDs = row.querySelectorAll("td").length;
  if (totalTDs == 4) {
    const mes = row.querySelectorAll("td:nth-child(1)")[0].innerText;
    const consumo = row.querySelectorAll("td:nth-child(4)")[0].innerText;
    const consumoTratado = parseInt(
      consumo.replace("m3", "").replace(/\D/, "")
    );
    const mesTratado = mes.replace(/^\d+\//, "");
    dado = [mesTratado, consumoTratado];
    dados.push(dado);
  }
}
google.charts.load("current", {
  packages: ["corechart"],
});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var dataChart = google.visualization.arrayToDataTable(dados);

  const optionsChart = {
    lineWidth: 3,
    pointsVisible: true,
    backgroundColor: "transparent",
    legend: {
      position: "bottom",
      alignment: "start",
    },
    hAxis: {
      slantedText: true,
      textStyle: {
        color: "black",
        fontSize: 12,
      },
    },
    vAxis: {
      gridlines: {
        color: "#777",
      },
    },
  };

  var chart = new google.visualization.AreaChart(
    document.getElementById("chart1")
  );
  chart.draw(dataChart, optionsChart);
}
