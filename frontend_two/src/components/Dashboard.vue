<template>
    <main className="main flex">
      <Sidebar/>
      <div className="right">
        <Header/>
        <div className="router_container">
          <router-view />
        </div>
      </div>
    </main>
  </template>
  
  <script>
  import Sidebar from './Sidebar.vue';
  import Header from './Header.vue';
  import { RouterView } from 'vue-router';
  
  export default {
    components: {
      Sidebar,
      Header,
      RouterView,
    },
  };
  </script>

<style scoped>
.right {
  width: 100%;
}
.router_container{
  padding: 30px;
}
</style>