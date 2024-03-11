<template>
  <ResourceStats/>
</template>

<script>
import ResourceStats from './components/ResourceStats.vue';

export default {
  components: {ResourceStats},
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
