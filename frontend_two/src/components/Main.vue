<template>
    <div className="main_title">
    Dashboard
    </div>
    <div className="main_wrapper">
      <Stats/>
      <ChartQOL/>
    </div>
    
</template>

<script>
import Stats from './Stats.vue';
import ChartQOL from './ChartQOL.vue'
export default {
    components: {Stats, ChartQOL},
};

</script>

<style scoped>

.main_title {
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 32px;
}
.main_wrapper {
  width: 1400px;
}
</style>