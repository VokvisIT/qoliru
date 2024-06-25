<template>
  <main className="mainlk">
    <div class="lk_region">
      <div className="lk_close btn" @click="toggleResourceStats()">
        {{  $t('close')  }}
      </div>
      <div>
        <div v-if="loading" class="loading">
          <Loader/>
        </div>
        <div v-else>
          <div class="region_info">
            <div class="region_name">
              {{resources.name}}
            </div>
            <div class="region_qol">
              <div class="region_qolInfo">
                <div class="region_bar">
                  <div class="region_bar_activ" :style="{ width: barWidth, backgroundColor: barColor}"></div>
                </div>
                <div class="region_qolTitle" :style="{ color: barColor }">{{ resources.qol }}</div>
              </div>
              <div>{{  $t('assessment')  }}</div>
              <div>Данных собрано: {{ resources.count_data }}</div>
            </div>
          </div>
        </div>
      <div class="region_chart">
        <canvas id="marksChart" class="chart_canvas"></canvas>
      </div>
    </div>
    </div>
  </main>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios'
import Loader from './Loader.vue'

export default {
  components: {Loader},
  props: {
    toggleResourceStats: {
      type: Function,
      requirements: true,
    },
    regionId: {
      type: String,
      requirements: true,
    }
  },
  data() {
    return {
      loading: true,
      resources: null,
      chart: null,
      marksData: {
        labels: [], // пустой массив для меток
        datasets: [{
          label: 'QoL Categories',
          data: [],
          backgroundColor: 'rgba(66, 182, 246, 0.3)',
          borderColor: '#4379EE',
          borderWidth: 2,
          pointBackgroundColor: '#4379EE',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#4379EE',
          pointHoverBorderColor: '#4379EE',
        }]
      },
    };
  },
  computed: {
    barWidth() {
      // Вычисляем ширину полосы в зависимости от значения resources.qol
      return (this.resources.qol / 10) * 100 + "%";
    },
    barColor() {
      // Вычисляем цвет фона в зависимости от значения resources.qol
      const hue = (this.resources.qol / 10) * 120; // Преобразуем resources.qol в оттенок цвета
      return `hsl(${hue}, 100%, 50%)`; // Используем HSL для создания градиента цвета
    },
  },
  created() {
    this.fetchRegionDetail(this.regionId)
  },
  methods: {
    fetchRegionDetail(regionId) {
      console.log(regionId)
      axios.get(`${import.meta.env.BASE_URL}/api/v1/dashboard/region-detail/${regionId}/`)
        .then(response => {
          this.resources = response.data;
          this.loading = false;
          this.updateChartData();
          this.renderChart();
        })
        .catch(error => {
          console.error(error);
          this.loading = false;
        });
    },
    updateChartData() {
      const labels = [];
      const data = [];
      for (const category in this.resources.qol_category) {
        labels.push(category);
        data.push(this.resources.qol_category[category]);
      }
      this.marksData.labels = labels;
      this.marksData.datasets[0].data = data;
    },
    renderChart() {
      if (this.chart) {
        this.chart.destroy();
      }
      const marksCanvas = document.getElementById("marksChart");
      this.chart = new Chart(marksCanvas, {
        type: 'radar',
        data: this.marksData,
        options: {
          plugins: {
            legend: {
              display: false,
            },
            tooltip: {
              enabled: true,
              callbacks: {
                label: function(context) {
                  const label = context.chart.data.labels[context.dataIndex];
                  const value = context.raw;
                  return `${label}: ${value}`;
                }
              }
            }
          },
          elements: {
            line: {
              borderWidth: 2,
              borderColor: '#4379EE',
              backgroundColor: 'rgba(66, 182, 246, 0.3)',
              fill: true,
              tension: 0.2,
            },
            point: {
              backgroundColor: '#4379EE',
              radius: 4,
              borderWidth: 2,
              borderColor: '#fff',
              hoverRadius: 6,
              hoverBorderWidth: 2,
            },
          },
          scales: {
            r: {
              suggestedMin: 0,
              suggestedMax: 10,
              ticks: {
                stepSize: 2,
                showLabelBackdrop: false,
                font: {
                  size: 20, // установить размер шрифта
                },
              },
              grid: {
                color: '#ccc',
                lineWidth: 1,
              },
            },
          },
          layout: {
            padding: 20,
          },
        },
      });
    },
  },
};
</script>

<style scoped>
.loading {
  position: absolute;
  top: 50%;
  right: 50%;
}
.mainlk {
  position: absolute;
  z-index: 10000000;
  top: 0;
  left: 0;
  display: flex;
  width: 100%;
  height: 100vh;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.34);
}

.lk_region {
  position: relative;
  background: #fff;
  border-radius: 15px;
  padding: 30px;
}
.lk_close {
  font-weight: 500;
  position: absolute;
  right: 30px;
  bottom: 30px;
}

.btn {
    padding: 8px 30px;
    background: #4880FF;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 14px;
    border: 0;
    border-radius: 6px;
    transition: background 300ms ease-in-out;
}

.btn:hover {
    background: #749eff;
    cursor: pointer;
}

.region_name {
  font-weight: 700;
  font-size: 24px;
}
.region_qol {
  font-weight: 700;
  font-size: 14px;
}
.region_qolInfo {
  display: flex;
  justify-content: end;
  align-items: center;
}
.region_qolTitle {
  font-weight: 700;
  font-size: 28px;
  color: #4AD991;
}
.region_bar{
  margin-right: 5px;
  width: 100%;
  height: 15px;
  border-radius: 5px;
  background: #D9D9D9;
}
.region_bar_activ{
  width: 0;
  height: 15px;
  border-radius: 5px;
  background-color: #4AD991;
  transition: width 500ms ease-in-out;
}
.region_filters, .region_data_filter {
  visibility: hidden;
}
.chart_canvas{
  width: 600px !important;
  height: 600px !important;
}
@media (max-width: 768px) {
  .chart_canvas{
  width: 300px !important;
  height: 300px !important;
}
}
</style>
