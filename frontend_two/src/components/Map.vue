<template>
  <ResourceStats v-if="showResourceStats" :regionId="selectedRegionId" :toggleResourceStats="toggleResourceStats"/>
  <div>
    <div class="map_title">
      {{ $t('map') }}
    </div>
    <div class="wrapper-map">
      <div class="map_wrapper_title">
        {{ $t('qolir') }}
      </div>
      <div v-if="loading" class="loading">
        <Loader />
      </div>
      <div v-else>
        <yandex-map class="yandex-map"
              :settings="{
              location: {
                center: [data[0].latitude, data[0].longitude],
                zoom: 3,
              },
            }"
            width="100%"
            height="500px"
        >
          <yandex-map-default-scheme-layer />
          <yandex-map-default-features-layer />
          <yandex-map-marker
            v-for="region in data"
            :key="region.id"
            :settings="{ coordinates: [region.latitude, region.longitude] }"
            position="top-center left-center"
          >
            <div class="custom-marker" @click="toggleResourceStats(region.id)">
              <div class="custom-marker-qol" >
                {{ region.qol }}
              </div>
            </div>
          </yandex-map-marker>
        </yandex-map>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Loader from './Loader.vue'
import ResourceStats from './ResourceStats.vue';
import { YandexMap, YandexMapDefaultSchemeLayer, YandexMapMarker, YandexMapDefaultFeaturesLayer  } from 'vue-yandex-maps'
import { ref } from 'vue'
export default {
  components: {
    Loader,
    YandexMap,
    YandexMapDefaultSchemeLayer,
    YandexMapMarker,
    YandexMapDefaultFeaturesLayer,
    ResourceStats,
  },
  data() {
    return {
      data: {},
      loading: true,
      showResourceStats: false,
      selectedRegionId: null,
    };
  },
  created() {
    this.fetchRegionQOL()
  },
  methods: {
    toggleResourceStats(regionId) {
        this.selectedRegionId = regionId;
        this.showResourceStats = !this.showResourceStats;
    },
    fetchRegionQOL() {
      axios.get(`${import.meta.env.BASE_URL}/api/v1/dashboard/region-qol/`)
        .then(response => {
          this.data = response.data
          this.loading = false;
        })
        .catch(error => {
          console.error(error);
          this.loading = false;
        });
    },
    produceAnAlert(regionName) {
      alert(`Регион: ${regionName}`);
    },
  },
  computed: {
    mapCenter() {
      if (this.data.length) {
        return [this.data[0].longitude, this.data[0].latitude];
      }
      return [0, 0];
    },
    customIconLayout() {
      return 'default#imageWithContent';
    },
  },
};
</script>

<style scoped>
.wrapper-map {
  max-width: 1400px;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.custom-marker {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #D9F7E7;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 25px;
  border: 3px solid #4AD991;
  scale: 1;
  transition: scale 200ms ease-in-out;
}
.custom-marker:hover {
  cursor: pointer;
  scale: 1.5;
}
.custom-marker-qol {
    font-weight: 700;
    color: #4AD991;
}
.map_title {
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 32px; 
}
.map_wrapper_title{
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 24px; 
}
.loading {
  position: absolute;
  top: 50%;
  right: 50%;
}
</style>