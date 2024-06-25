<template>
    <ResourceStats v-if="showResourceStats" :regionId="selectedRegionId" :toggleResourceStats="toggleResourceStats"/>
    <div className="list_title">
        {{  $t('list')  }}
    </div>
    <div className="wrapper-list">
        <div className="list_wrapper_title">
            {{  $t('qolir')  }}
        </div>
        <div className="list_wrapper_items">
            <div className="head_wrapper_items flex">
                <div class="head_item">
                    {{  $t('regionname')  }}
                </div>
                <div class="head_item">
                    {{  $t('amountofdata')  }}
                </div>
                <div class="head_item">
                    {{  $t('bestcategory')  }}
                </div>
                <div class="head_item">
                    {{  $t('worstcategory')  }}
                </div>
                <div class="head_item">
                    QOL
                </div>
            </div>
            <div v-if="loading" class="loading">
                <Loader />
            </div>
            <div v-else>
                <div v-for="region in data" :key="region.id" className="wrapper_items_simple flex">
                    <div class="list_item">
                        {{ region.name }}
                    </div>
                    <div class="list_item">
                        {{ region.count_data }}
                    </div>
                    <div class="list_item">
                        {{ region.bestcategory }}
                    </div>
                    <div class="list_item">
                        {{ region.worstcategory }}
                    </div>
                    <div class="list_item">
                        <span className="list_item_qol">{{ region.qol }}</span>
                        <button className="btn" @click="toggleResourceStats(region.id)">{{  $t('more')  }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Loader from './Loader.vue'

import ResourceStats from './ResourceStats.vue';
export default {
    components: {ResourceStats, Loader},
    data(){
        return {
            showResourceStats: false,
            loading: true,
            data: {},
            selectedRegionId: null,
        }
    },
    created() {
    this.fetchRegionQOLdata()
    },
    methods: {
        toggleResourceStats(regionId) {
            this.selectedRegionId = regionId;
            this.showResourceStats = !this.showResourceStats;
        },
        fetchRegionQOLdata() {
            axios.get(`${import.meta.env.BASE_URL}/api/v1/dashboard/region-qol-data/`)
            .then(response => {
            this.data = response.data
            this.loading = false;
            })
            .catch(error => {
            console.error(error);
            this.loading = false;
            });
        },
    }
}
</script>

<style scoped>
.wrapper-list{
    overflow-x: scroll;
    max-width: 1400px;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
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
    display: flex;
    align-items: center;
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