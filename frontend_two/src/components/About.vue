<template>
    <div className="about_title">
      {{  $t('about')  }}
    </div>
    <div className="about_wrapper flex">
      <div className="about_item">
        <div className="item_title">
          {{  $t('ratingcategory')  }}
        </div>
        <div className="item_descr">
          1. {{  $t('one_rc')  }}
        </div>
        <div className="item_descr">
          2. {{  $t('two_rc')  }}
        </div>
        <div className="item_descr">
          3. {{  $t('three_rc')  }}
        </div>
      </div>
      <div className="about_item">
        <div className="item_title">
          {{  $t('rr')  }}
        </div>
        <div className="item_descr">
          1. {{  $t('one_rr')  }}
        </div>
        <div className="item_descr">
          2. {{  $t('two_rr')  }}
        </div>
      </div>
    </div>
</template>

<script>

</script>

<style scoped>
.about_title{
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 32px;
}

.about_wrapper{
  width: 1100px;
  justify-content: space-around;
}
.about_item {
  width: 400px;
  padding: 16px;
  border-radius: 15px;
  background: #fff;
  box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.item_title {
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 24px;
}
.item_descr {
  margin-bottom: 16px;
  font-size: 16px;
  font-weight: 500;
}
</style>