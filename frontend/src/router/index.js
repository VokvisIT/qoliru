import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../components/Dashboard.vue';
import ComponentMain from '../components/Main.vue';
import ComponentMap from '../components/Map.vue';
import ComponentList from '../components/List.vue';
import ComponentAbout from '../components/About.vue';

const routes = [
  {
    path: '/',
    redirect: '/component-main',
  },
  {
    path: '/component-main',
    component: ComponentMain,
  },
  {
    path: '/component-map',
    component: ComponentMap,
  },
  {
    path: '/component-list',
    component: ComponentList,
  },
  {
    path: '/component-about',
    component: ComponentAbout,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;