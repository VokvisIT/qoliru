<template>
  <Dashboard/>
</template>

<script>
import ResourceStats from './components/ResourceStats.vue';
import Dashboard from './components/Dashboard.vue';
export default {
  components: {ResourceStats, Dashboard},
  data() {
    return {
      amount: 0,
      cryptoFirst: "",
      cryptoSecond: "",
      error: '',
      result: 0,
      favs: [],
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
