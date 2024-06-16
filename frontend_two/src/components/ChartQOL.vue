<template>
    <div className="chart_wrapper">
        <div className="chart_title">
          {{  $t('avgregionqol')  }}
        </div>
        <canvas id="myChart" width="1078" height="300"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';
import plugin from "chartjs-plugin-gradient";

Chart.register(plugin);
export default {
  data() {
    return {
      dataChart: {
        labels: ['2022 Jan', '2022 Feb', '2022 Mar', '2022 Apr', '2022 May', '2022 Jun', '2022 Jul', '2022 Aug', '2022 Sep', '2022 Oct', '2022 Nov', '2022 Dec','2023 Jan', '2023 Feb', '2023 Mar', '2023 Apr', '2023 May', '2023 Jun', '2023 Jul', '2023 Aug', '2023 Sep', '2023 Oct', '2023 Nov', '2023 Dec'],
        datasets: [
          {
            label: 'QOL in Russia',
            data: [5.6, 3.8, 7.2, 9.3, 2.9, 4.1, 6.7, 8.4, 1.5, 0.8, 9.6, 3.2, 5.6, 3.8, 7.2, 9.3, 2.9, 4.1, 6.7, 8.4, 1.5, 0.8, 9.6, 3.2],
            borderColor: '#4379EE',
            backgroundColor: 'rgba(67, 121, 238, 0.5)',
            borderWidth: 1.5,
            pointRadius: 4,
            pointBackgroundColor: '#4379EE',
            pointBorderWidth: 0,
            tension: 0.4,
            fill: true,
            borderJoinStyle: 'round',
            pointHitRadius: 10,
            backgroundColor: 'rgba(66, 182, 246, 0.3)',
            hoverBackgroundColor: 'rgba(67, 121, 238, 0.7)',
            hoverBorderColor: '#4379EE',
            spanGaps: false,
          },
        ],
      },
      chart: null,
    };
  },
  mounted() {
    console.log('Component mounted!');
    this.renderChart();
  },
  methods: {
    renderChart() {
      const ctx = document.getElementById('myChart');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: this.dataChart,
        options: {
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            y: {
              ticks: {
                stepSize: 2,
              },
            },
            x: {
              grid: {
                display: false,
              },
            },
          },
          elements: {
            line: {
              borderWidth: 1.5, // Установка толщины линии графика
            },
            point: {
              radius: 4, // Установка размера точек
              borderWidth: 0, // Установка толщины обводки точек
              backgroundColor: '#4379EE',
            },
          },
          interaction: {
            mode: 'index',
            intersect: false,
          },
          tooltips: {
            enabled: true,
            mode: 'index',
            intersect: false,
            callbacks: {
              label: function (tooltipItem, data) {
                return (
                  data.datasets[tooltipItem.datasetIndex].label +
                  ': ' +
                  tooltipItem.yLabel
                );
              },
            },
          },
        },
      });
    },
  },
};
</script>

<style scoped>
.chart_wrapper {
    width: 100%;
    padding: 32px;
    border-radius: 15px;
    background: #fff;
    box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.chart_title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 50px;
}

</style>