<template>
    <ResourceStats v-if="showResourceStats" :toggleResourceStats="toggleResourceStats"/>
    <div className="list_title">
    List
    </div>
    <div className="wrapper">
        <div className="list_wrapper_title">
            Quality of life in the regions
        </div>
        <div className="list_wrapper_items">
            <div className="head_wrapper_items flex">
                <div class="head_item">
                    Region Name
                </div>
                <div class="head_item">
                    Amount of Data
                </div>
                <div class="head_item">
                    Best
                </div>
                <div class="head_item">
                    Worst
                </div>
                <div class="head_item">
                    QOL
                </div>
            </div>
            <div className="wrapper_items_simple flex">
                <div class="list_item">
                    Arkhangelsk region
                </div>
                <div class="list_item">
                    4587 texts
                </div>
                <div class="list_item">
                    Tourrism 9.6
                </div>
                <div class="list_item">
                    GKH 2.3
                </div>
                <div class="list_item">
                    <span className="list_item_qol">7.9</span>
                    <button className="btn" @click="toggleResourceStats">More</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ResourceStats from './ResourceStats.vue';
export default {
    components: {ResourceStats},
    data(){
        return {
            showResourceStats: false,
        }
    },
    methods: {
    toggleResourceStats() {
      this.showResourceStats = !this.showResourceStats;
    }
  }
}
</script>

<style scoped>


.list_title {
    margin-bottom: 30px;
    font-weight: 700;
    font-size: 32px;
}

.list_wrapper_title {
    margin-bottom: 30px;
    font-weight: 700;
    font-size: 24px;
}

.list_wrapper_items {
    display: inline-block;
}

.list_wrapper_items .head_wrapper_items {
    padding: 15px 30px;
    align-items: center;
    border-radius: 12px;
    background: #cecece;
}
.wrapper_items_simple {
    padding: 15px 30px;
    align-items: center;
}
.head_item {
    margin-right: 20px;
    width: 170px;
    font-weight: 700;
    font-size: 14px;
}
.list_item {
    margin-right: 20px;
    width: 170px;
    font-weight: 500;
    font-size: 14px;
}
.head_item:last-child {
    width: 50px;
    margin-right: 0px;
}
.list_item_qol{
    margin-right: 50px;
    font-weight: 700;
}
.btn {
    padding: 8px 30px;
    background: #4880FF;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 14px;
    border: 0;
    border-radius: 6px;
    transition: background 300ms ease-in-out;
}
.btn:hover {
    background: #749eff;
    cursor: pointer;
}
</style>