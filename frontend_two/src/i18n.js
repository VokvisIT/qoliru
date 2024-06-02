import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    dashboard: 'Dashboard Test CI/CD',
    map: 'Map',
    list: 'List',
    about: 'About',
    qolir: 'Quality of life in the regions',
    button: 'Change language'
  },
  ru: {
    dashboard: 'Дашборд',
    map: 'Карта',
    list: 'Список',
    about: 'Как всё работает',
    qolir: 'Качество жизни в регионах',
    button: 'Сменить язык'
  }
}

const i18n = createI18n({
  locale: 'en', // default locale
  messages,
})

export default i18n