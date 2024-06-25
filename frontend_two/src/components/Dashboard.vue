<template>
    <main className="main flex">
      <Sidebar :isMenuActive="isMenuActive" :closeMenu="closeMenu"/>
      <div className="right">
        <Header :toggleMenu="toggleMenu"/>
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
    data() {
        return {
            isMenuActive: false,
        };
    },
    methods: {
      toggleMenu() {
        this.isMenuActive = !this.isMenuActive;
      },
      closeMenu() {
        this.isMenuActive = false;
      },
      updateBodyClass() {
            if (this.isMenuActive) {
                document.body.classList.add('stop-scroll');
            } else {
                document.body.classList.remove('stop-scroll');
            }
        },
    },
    watch: {
        isMenuActive(newVal) {
            this.updateBodyClass();
        }
    },
    mounted() {
        this.updateBodyClass();
    }
  };
  </script>

<style scoped>
.right {
  width: 100%;
}
.stop-scroll {
    overflow: hidden;
  }
.router_container{
  padding: 30px;
}
</style>