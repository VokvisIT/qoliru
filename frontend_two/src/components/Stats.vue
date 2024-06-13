<template>
    <div className="stats_wrapper flex">
        <div className="stats_item">
            <div v-if="loading_best_region" className="loading">
                <Loader />
            </div>
            <div v-else>
                <div className="stats_item_qol flex">
                    <div className="item_qol">
                        {{ bestRegion.qol }}
                    </div>
                </div>
                <div className="stats_descr">
                    The best region
                </div>
                <div className="stats_title">
                    {{ bestRegion.name }}
                </div>
                <div className="stats_hist flex">
                    <div v-if="bestRegion.qol_change > 0">
                        <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                    </div>
                    <div v-else>
                        <div className="stats_hist_img"><img src="../assets/img/downarrow.svg" alt=""></div>
                    </div>
                    <div className="stats_hist_text">
                        {{ bestRegion.qol_change }} По сравнению с прошлым днём
                    </div>
                </div>
            </div>
        </div>
        <div className="stats_item">
            <div v-if="loading_best_category" className="loading">
                <Loader />
            </div>
            <div v-else>
                <div className="stats_item_qol flex">
                    <div className="item_qol">
                        {{ bestCategory.qol }}
                    </div>
                </div>
                <div className="stats_descr">
                    The best category
                    <p>
                        {{ bestCategory.name }}
                    </p>
                </div>
                <div className="stats_title">
                    {{ bestCategory.category_name }}
                </div>
                <div className="stats_hist flex">
                    <div v-if="bestCategory.qol_change > 0">
                        <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                    </div>
                    <div v-else>
                        <div className="stats_hist_img"><img src="../assets/img/downarrow.svg" alt=""></div>
                    </div>
                    <div className="stats_hist_text">
                        {{ bestCategory.qol_change }} По сравнению с прошлым днём
                    </div>
                </div>
            </div>
        </div>

        <div className="stats_item">
            <div v-if="loading_worst_category" className="loading">
                <Loader />
            </div>
            <div v-else>
                <div className="stats_item_qol flex">
                <div className="item_qol">
                    {{ worstCategory.qol }}
                </div>
                </div>
                <div className="stats_descr">
                    The worst category
                    <p>
                        {{ worstCategory.name }}
                    </p>
                </div>
                <div className="stats_title">
                    {{ worstCategory.category_name }}
                </div>
                <div className="stats_hist flex">
                    <div v-if="worstCategory.qol_change > 0">
                        <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                    </div>
                    <div v-else>
                        <div className="stats_hist_img"><img src="../assets/img/downarrow.svg" alt=""></div>
                    </div>
                    <div className="stats_hist_text">
                        {{ worstCategory.qol_change }} По сравнению с прошлым днём
                    </div>
                </div>
            </div>
        </div>

        <div className="stats_item">
            <div v-if="loading_count_data" className="loading">
                <Loader />
            </div>
            <div v-else>
                <div className="stats_item_qol flex">
                    <div className="item_qol">
                        <img src="../assets/img/Subtract.svg" alt="">
                    </div>
                </div>
                <div className="stats_descr">
                    Data collected
                </div>
                <div className="stats_title">
                    {{ dataCount.count_yesterday }}
                </div>
                <div className="stats_hist flex">
                    <div v-if="dataCount.count_difference > 0">
                        <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                    </div>
                    <div v-else>
                        <div className="stats_hist_img"><img src="../assets/img/downarrow.svg" alt=""></div>
                    </div>
                    <div className="stats_hist_text">
                        {{ dataCount.count_difference }} По сравнению с прошлым днём
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Loader from './Loader.vue'
export default {
    components: {
        Loader
    },
  data() {
    return {
      bestRegion: {},
      bestCategory: {},
      worstCategory: {},
      dataCount: {},
      loading_best_region: true,
      loading_best_category: true,
      loading_worst_category: true,
      loading_count_data: true,
    }
  },
  created() {
    this.fetchBestRegionQOL()
    this.fetchBestCategoryQOL()
    this.fetchWorstCategoryQOL()
    this.fetchDataCount()
  },
  methods: {
    fetchBestRegionQOL() {
        //axios.get(`http://127.0.0.1:8000/api/v1/dashboard/best-region-qol/`)
        axios.get(`http://87.242.86.194:8000/api/v1/dashboard/best-region-qol/`)
        .then(response => {
        this.bestRegion = response.data
        this.loading_best_region = false
        })
        .catch(error => {
        console.error(error)
        this.loading_best_region = false
        })
    },
    fetchBestCategoryQOL(){
        //axios.get(`http://127.0.0.1:8000/api/v1/dashboard/best-category-qol/`)
        axios.get(`http://87.242.86.194:8000/api/v1/dashboard/best-category-qol/`)
        .then(response => {
        this.bestCategory = response.data
        this.loading_best_category = false
        })
        .catch(error => {
        console.error(error)
        this.loading_best_category = false
        })
    },
    fetchWorstCategoryQOL() {
        //axios.get(`http://127.0.0.1:8000/api/v1/dashboard/worst-category-qol/`)
        axios.get(`http://87.242.86.194:8000/api/v1/dashboard/worst-category-qol/`)
        .then(response => {
        this.worstCategory = response.data
        this.loading_worst_category = false
        })
        .catch(error => {
        console.error(error)
        this.loading_worst_category = false
        })
    },
    fetchDataCount() {
        //axios.get(`http://127.0.0.1:8000/api/v1/dashboard/data-count-yesterday/`)
        axios.get(`http://87.242.86.194:8000/api/v1/dashboard/data-count-yesterday/`)
        .then(response => {
        this.dataCount = response.data
        this.loading_count_data = false
        })
        .catch(error => {
        console.error(error)
        this.loading_count_data = false
        })
    }
  }
}
</script>


<style scoped>
.stats_wrapper {
    position: relative;
    z-index: 1;
    width: 100%;
    justify-content: space-between;
    margin-bottom: 30px;
}
.stats_item {
    position: relative;
    padding: 16px;
    width: 300px;
    border-radius: 15px;
    background: #fff;
    box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.loading {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
.stats_item_qol {
    width: 60px;
    height: 60px;
    position: absolute;
    border-radius: 23px;
    background-color: #D9F7E7;
    right: 16px;
    align-items: center;
    justify-content: center;
}
.item_qol {
    font-weight: 700;
    font-size: 28px;
    color: #4AD991;
}
.stats_descr {
    margin-bottom: 16px;
    font-size: 16px;
    font-weight: 500;
}
.stats_title {
    width: 190px;
    margin-bottom: 12px;
    font-size: 28px;
    font-weight: 700;
}
.stats_hist {
    align-items: center;
}
.stats_hist_img {
    margin-right: 5px;
}
.stats_hist_text{
    font-weight: 500;
    font-size: 16px;
}
</style>