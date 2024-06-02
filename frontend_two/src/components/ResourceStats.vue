<template>
  <main className="mainlk">
    <div class="lk_region">
      <div className="lk_close btn" @click="toggleResourceStats()">
        Close
      </div>
      <div class="flex" style="justify-content: space-between;">
        <div>
          <div class="region_info">
            <div class="region_name">
              Архангельская область
            </div>
            <div class="region_qol">
              <div class="region_qolInfo">
                <div class="region_bar">
                  <div class="region_bar_activ" :style="{ width: barWidth, backgroundColor: barColor }"></div>
                </div>
                <div class="region_qolTitle" :style="{ color: barColor }">{{ overallAverage.toFixed(1) }}</div>
              </div>
              <div>Assessment of the quality of life</div>
              <div>Данных собрано: {{ countData }}</div>
            </div>
          </div>
          <div class="region_filters">
            <div v-for="resource in resources" :key="resource.resource_name">
              <input type="checkbox" v-model="selectedResources" :value="resource.resource_name" @change="updateChartData" di> {{ resource.resource_name }}
            </div>
          </div>
          <div class="region_data_filter">
            <label for="startDate">Start Date:</label>
            <select v-model="paramsFilter.param1" @change="fetchResourceStats">
              <option v-for="date in availableDates" :value="date">{{ date }}</option>
            </select>
            <label for="endDate">End Date:</label>
            <select v-model="paramsFilter.param2" @change="fetchResourceStats">
              <option v-for="date in availableDates" :value="date">{{ date }}</option>
            </select>
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

export default {
  props: {
    toggleResourceStats: {
      type: Function,
      requirements: true,
    }
  },
  data() {
    return {
      resources: [],
      selectedResources: [], // массив для хранения выбранных ресурсов
      chart: null, // переменная для хранения экземпляра графика
      marksData: {
        labels: [], // пустой массив для меток
        datasets: [{
          label: "Архангельск",
          backgroundColor: "rgb(85,225,255, 0.2)",
          data: [] // пустой массив для данных
        }]
      },
      overallAverage: 0, // переменная для хранения общего среднего
      paramsFilter : {
        // Ваши параметры здесь, например:
        param1: '2023-09-01',
        param2: '2023-12-31'
      },
      availableDates: [], // Массив доступных дат
      countData: null,
    };
  },
  computed: {
    barWidth() {
      // Вычисляем ширину полосы в зависимости от значения overallAverage
      return (this.overallAverage / 10) * 100 + "%";
    },
    barColor() {
      // Вычисляем цвет фона в зависимости от значения overallAverage
      const hue = (this.overallAverage / 10) * 120; // Преобразуем overallAverage в оттенок цвета
      return `hsl(${hue}, 100%, 50%)`; // Используем HSL для создания градиента цвета
    },
    titleColor() {
      // Вычисляем цвет текста в зависимости от значения overallAverage
      const hue = (this.overallAverage / 10) * 120; // Преобразуем overallAverage в оттенок цвета
      const lightness = this.overallAverage >= 7 ? 50 : 100; // Устанавливаем яркость в зависимости от значения overallAverage
      return `hsl(${hue}, 100%, ${lightness}%)`; // Используем HSL для создания градиента цвета
    }
  },
  mounted() {
    this.fetchResourceStats();
  },
  methods: {
    updateCountData() {
      this.countData = this.resources.reduce((total, resource) => {
        if (this.selectedResources.includes(resource.resource_name)) {
          return total + resource.data_count;
        }
        return total;
      }, 0);
    },
    renderChart() {
      const marksCanvas = document.getElementById("marksChart");

      this.chart = new Chart(marksCanvas, {
        type: 'radar',
        data: this.marksData,
        options: {
          layout: {
    padding: 0
  },
          plugins: {
            legend: {
              display: false
            }
          }
        }
      });
    },
    async fetchResourceStats() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/v1/dashboard/resource_stats/?param1=${this.paramsFilter.param1}&param2=${this.paramsFilter.param2}`);
        const data = await response.json();
        this.selectedResources = data.map(resource => resource.resource_name);
        // Получаем метки из первого объекта JSON-данных
        this.marksData.labels = Object.keys(data[0].categories);
        console.log(data)
        // Обновляем данные для графика и общую среднюю оценку
        this.resources = data;
        this.updateChartData();
        
        // Рисуем график
        this.renderChart();
        
      } catch (error) {
        console.error('Error fetching resource stats:', error);
      }
    },
    updateChartData() {
      this.updateCountData();
      // Очищаем данные о категориях в датасете
      this.marksData.datasets[0].data = [];
      
      // Считаем среднее значение по каждой категории и общую среднюю оценку
      let totalSum = 0;
      let totalCount = 0;
      for (let category in this.resources[0].categories) {
        let sum = 0;
        for (let resource of this.resources) {
          if (this.selectedResources.includes(resource.resource_name)) {
            sum += resource.categories[category];
          }
        }
        let average = sum / this.selectedResources.length;
        totalSum += average;
        totalCount++;
        this.marksData.datasets[0].data.push(average);
      }
      this.overallAverage = totalSum / totalCount;
      
      // Перерисовываем график
      if (this.chart) {
        this.chart.destroy();
      }
      this.renderChart(); // Заново рисуем график с обновленными данными
    }
  }
}
</script>

<style scoped>
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
  width: 1400px; /*  Тут хз */
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

.region_info{
  /* display: flex; */
  width: 300px;
  justify-content: space-between;
  margin-bottom: 15px;
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
  width: 50%;
  height: 15px;
  border-radius: 5px;
  transition: width 500ms ease-in-out;
}
.region_filters, .region_data_filter {
  visibility: hidden;
}
.chart_canvas{

  width: 900px !important;
  height: 900px !important;
}

</style>
