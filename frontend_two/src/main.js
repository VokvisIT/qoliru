import './assets/normalize.css'
import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import i18n from './i18n'

const app = createApp(App)
app.use(router)
app.use(i18n)
app.config.globalProperties.$t = i18n.global.t
app.mount('#app')
