<template>
    <div className="chart_wrapper">
      <div className="chart_title">
          {{  $t('avgregionqol')  }}
        </div>
      <div v-if="loading" className="loading">
        <Loader />
      </div>
      <div>
        <canvas id="myChart" width="1078" height="300"></canvas>
      </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';
import plugin from "chartjs-plugin-gradient";
import axios from 'axios';
import Loader from './Loader.vue'
Chart.register(plugin);

export default {
  components: {
        Loader
    },
  data() {
    return {
      loading: true,
      dataChart: {
        labels: null,
        datasets: [
          {
            label: 'QOL in Russia',
            data: null,
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
  created(){
    this.fetchAVGRegionQOL()
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
              // beginAtZero: true,
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
    fetchAVGRegionQOL(){
      axios.get(`${import.meta.env.BASE_URL}/api/v1/dashboard/avg-qoliru/`)
        .then(response => {
          this.dataChart.labels = response.data.labels
          this.dataChart.datasets[0].data = response.data.data
          this.loading = false;
          this.renderChart();
        })
        .catch(error => {
        console.error(error)
        this.loading = false;
        this.renderChart();
        })
    }
  },
};
</script>

<style scoped>
.chart_wrapper {
  position: relative;
    width: 100%;
    padding: 32px;
    border-radius: 15px;
    background: #fff;
    box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.loading {
  position: absolute;
  top: 50%;
  right: 50%;
}
.chart_title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 50px;
}

</style>