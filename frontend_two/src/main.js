import './assets/normalize.css'
import './assets/main.css'

import { createApp } from 'vue'
import { createYmaps } from "vue-yandex-maps"
import App from './App.vue'
import router from './router';
import i18n from './i18n'

const app = createApp(App)
const ymaps = createYmaps({
    apikey: "5c6bf1ab-5061-42b9-886f-1b895474b796",
  });
app.use(router)
app.use(i18n)
app.use(ymaps)
app.config.globalProperties.$t = i18n.global.t
app.mount('#app')
