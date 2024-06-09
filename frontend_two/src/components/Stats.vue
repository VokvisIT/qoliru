<template>
    <div className="stats_wrapper flex">
        <div className="stats_item">
            <div v-if="loading" className="loading">
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
                <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    {{ bestRegion.qol_change }} Compared to last quarter Compared to last quarter
                </div>
            </div>
            </div>
            
        </div>
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    7.4
                </div>
            </div>
            <div className="stats_descr">
                The best category
            </div>
            <div className="stats_title">
                Safety
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    1.2 Compared to last quarter
                </div>
            </div>
        </div>
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    1.5
                </div>
            </div>
            <div className="stats_descr">
                The worst category
            </div>
            <div className="stats_title">
                Tourism
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/downarrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    0.3 Compared to last quarter
                </div>
            </div>
        </div>
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    <img src="../assets/img/Subtract.svg" alt="">
                </div>
            </div>
            <div className="stats_descr">
                Data collected
            </div>
            <div className="stats_title">
                2040
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    1058 Compared to last quarter
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
      loading: false
    }
  },
  created() {
    this.fetchBestRegionQOL()
  },
  methods: {
    fetchBestRegionQOL() {
        this.loading = true
        axios.get('${process.env.VUE_APP_API_URL}/api/v1/dashboard/best-region-qol/')
        .then(response => {
        this.bestRegion = response.data
        this.loading = false
        })
        .catch(error => {
        console.error(error)
        this.loading = false
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