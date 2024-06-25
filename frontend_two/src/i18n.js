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
    regionname: "Region Name",
    amountofdata: "Amount of Data",
    more:"More",
    ratingcategory:"Rating the category",
    one_rc:"Counting the number of opinions (positive, negative and neutral)",
    two_rc:"Dividing the number of positive and neutral opinions by the total number of opinions by category",
    three_rc:"Multiplying the score by 10",
    rr: "Rating the region",
    one_rr: "Calculating the rating for each category of the region",
    two_rr: "The average value of all categories will be the rating of the region",
    assessment: "Assessment of the quality of life",
    close: "Close",

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
    regionname: "Название региона",
    amountofdata: "Кол-во собранных данных",
    more:"Подробнее",
    ratingcategory: "Рейтинг категорий",
    one_rc:"Подсчитываем количество мнений (положительных, отрицательных и нейтральных)",
    two_rc:"Делим количество положительных и нейтральных мнений на общее количество мнений по категории",
    three_rc:"Умножаем полученную оценку на 10",
    rr: "Рейтинг региона",
    one_rr: "Подсчитываем рейтинг по каждой категории региона",
    two_rr: "Среднее значение всех категорий будет являться рейтингом региона",
    assessment: "Оценка качества жизни",
    close: "Закрыть",
  }
}

const i18n = createI18n({
  locale: 'ru', // default locale
  messages,
})

export default i18n