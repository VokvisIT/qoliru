<template>
    <div class="header_container flex">
        <div @click="toggleMenu" class="menu">
            <img src="../assets/img/Arrow_right_stop.svg" alt="Доготип">
        </div>
        <!-- <div class="header_container__input">
            <input type="text" :placeholder="$t('searchregion')">
        </div> -->
        <div class="header_language">
            <div className="lang_wrap flex" @click="toggleLanguageMenu()" v-if="this.$i18n.locale=='ru'">
                <img src="../assets/img/ru-04.svg" alt="" className="lang_img"/>
                <div class="lang_title">Русский</div>
            </div>
            <div className="lang_wrap flex" @click="toggleLanguageMenu()" v-if="this.$i18n.locale=='en'">
                <img src="../assets/img/en-04.svg" alt="" className="lang_img"/>
                <div class="lang_title">English</div>
            </div>
            <div className="select_lang" v-if="isLanguageMenuVisible">
                <div className="select_title">
                    {{ $t('button') }}
                </div>
                <ul class="list_lang list-reset">
                <li @click="changeLanguage('en')" className="lang_item flex">
                    <div style="align-items: center; display: flex;">
                        <img src="../assets/img/en-04.svg" alt="" className="lang_img"/>
                        <div className="lang_item_title">English</div>
                    </div>
                    <img src="../assets/check.svg" alt="" className="lang_img_chech" v-if="this.$i18n.locale=='en'"/>
                </li>
                <li @click="changeLanguage('ru')" className="lang_item flex">
                    <div style="align-items: center; display: flex;">
                        <img src="../assets/img/ru-04.svg" alt="" className="lang_img"/>
                        <div className="lang_item_title">Русский</div>
                    </div>
                    <img src="../assets/check.svg" alt="" className="lang_img_chech" v-if="this.$i18n.locale=='ru'"/>
                </li>
                </ul>
            </div>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
        toggleMenu: {
        type: Function,
        required: true
        }
    },
    data() {
      return {
        isLanguageMenuVisible: false,
      }
    },
    methods: {
        changeLanguage(locale) {
        this.$i18n.locale = locale;
        this.isLanguageMenuVisible = false;
        },
      toggleLanguageMenu() {
        this.isLanguageMenuVisible = !this.isLanguageMenuVisible;
      }
    }
  }
  </script>

<style scoped>
.menu {
    display: none;
}

.header_container {
    position: relative;
    z-index: 10000;
    padding: 0 30px;
    height: 70px;
    align-items: center;
    justify-content: end;
    border-bottom: 1px solid #E8E8E8;
}
.header_container input {
    all: unset;
}
.header_container input {
    color: #202224;
    max-width: 400px;
    padding: 9px 15px;
    border-radius: 19px;
    border: 0.6px solid #D5D5D5;
}
.header_language {
    position: relative;
    width: 250px;
}
.lang_wrap {
    align-items: center;
}
.lang_wrap:hover {
    cursor: pointer;
}
.select_lang {
    width: 250px;
    position: absolute;
    background: #FFFFFF;
    border-radius: 15px;
    box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.select_title{
    width: 100%;
    padding: 15px;
    font-size: 15px;
    font-weight: 400;
    border-bottom: 1px solid #979797;
}
.lang_img{
    width: 50px;
    margin-right: 20px;
}
.lang_img_chech{
    right: 0;
    width:18px
}
.lang_item {
    align-items: center;
    justify-content: space-between;
    padding: 15px;
}

.lang_item:hover {
    cursor: pointer;
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
@media (max-width: 768px) {
    .menu {
        display: flex;
        margin-right: 15px;
    }
    .menu img {
        width: 30px;
        height: 30px;
    }
    .header_container {
        justify-content: start;
    }
    .header_container input {
        width: 100px;
        margin-right: 15px;
    }
    .header_container__input{
        margin-right: 15px;
    }
    .lang_title {
        display: none;
    }
    
}
</style>