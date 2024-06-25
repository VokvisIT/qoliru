<template>
    <div :class="['sidebar_container', { 'sidebar_container--active': isMenuActive }]">
        <div className="sidebar">
            <div className="sidebar_logo flex">
                <div className="logo">
                    <router-link to="/component-main" @click="closeMenu"><img src="../assets/img/LightLogo_Light.svg" alt="Доготип"></router-link>
                </div>
            </div>
            <ul class="sidebar_list list-reset">
                <router-link to="/component-main" active-class="active" @click="closeMenu">
                    <li className="sidebar_item">
                        {{  $t('dashboard')  }}
                    </li>
                </router-link>
                <router-link to="/component-map" active-class="active" @click="closeMenu">
                    <li className="sidebar_item">
                        {{  $t('map')  }}
                    </li>
                </router-link>
                <router-link to="/component-list" active-class="active" @click="closeMenu">
                    <li className="sidebar_item">
                        {{  $t('list')  }}
                    </li>
                </router-link>
                <router-link to="/component-about" active-class="active" @click="closeMenu">
                    <li className="sidebar_item">
                        {{  $t('about')  }}
                    </li>
                </router-link>
            </ul>
        </div>
    </div>
</template>

<script>
export default{
    props: {
        isMenuActive: {
            type: Boolean,
            required: true
        },
        closeMenu: {
            type: Function,
            required: true
        }
    },
    methods: {
        changeLanguage() {
            this.$i18n.locale = this.$i18n.locale === 'en' ? 'ru' : 'en'
        },
        
    }
}
</script>

<style scoped>
.sidebar_container{
    padding: 24px;
    width: 240px;
    height: 100vh;
    border-right: 1px solid #E8E8E8;
}
.sidebar_logo {
    justify-content: center;
    margin-bottom: 15px;
    color: #202224;
}
.sidebar_logo .logo {
    width: 132px;
}
.sidebar_list .sidebar_item{
    width: 100%;
    padding: 13px;
    border-radius: 6px;
    font-family: "Nunito Sans";
    font-weight: 700;
    background: none;
    transition: background 200ms ease-in-out;
}
.sidebar_list .sidebar_item:hover{
    background: #4880FF;
    color: #fff;
}
.active{
    display: block;
    border-radius: 6px;
    background: #4880FF;
    color: #fff !important;
}
.stop-scroll {
    overflow: hidden;
  }
@media (max-width: 768px) {
    .sidebar_container{
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100vh;
        z-index: 10008;
        background-color: #FFF;
        overflow-y: auto;
        visibility: hidden;
        transform: translateX(-120%);
        transition: visibility 0.3s ease-in-out, transform 0.3s ease-in-out;
    }
    .sidebar_container--active {
        visibility: visible;
        transform: none;
    }
    .sidebar_container {
        justify-content: start;
    }
}
</style>