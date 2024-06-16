import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    dashboard: 'Dashboard',
    map: 'Map',
    list: 'List',
    about: 'About',
    qolir: 'Quality of life in the regions',
    button: 'Change language',
    bestregion: 'The best region',
    bestcategory: 'The best category',
    worstcategory: 'The worst category',
    datacollected: 'Data collected',
    comparison: 'Compared to the previous day',
    avgregionqol: 'Assessment of the quality of life in Russia',
    searchregion: 'Search region',
  },
  ru: {
    dashboard: 'Дашборд',
    map: 'Карта',
    list: 'Список',
    about: 'Как всё работает',
    qolir: 'Качество жизни в регионах',
    button: 'Сменить язык',
    bestregion: 'Лучший регион',
    bestcategory: 'Лучшая категория',
    worstcategory: 'Худшая категория',
    datacollected: 'Собрано данных',
    comparison: 'По сравнению с прошлым днём',
    avgregionqol: 'Оценка качества жизни по России',
    searchregion: 'Введите название или код региона',
  }
}

const i18n = createI18n({
  locale: 'ru', // default locale
  messages,
})

export default i18n