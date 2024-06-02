<template>
    <div className="about_title">
      {{  $t('about')  }}
    </div>
    <div className="about_wrapper flex">
      <div className="about_item">
        <div className="item_title">
          Rating the category F
        </div>
        <div className="item_descr">
          1. Counting the number of opinions (positive, negative and neutral)
        </div>
        <div className="item_descr">
          2. Dividing the number of positive opinions by the number of other opinions
        </div>
        <div className="item_descr">
          3. Multiplying the received score by 100
        </div>
      </div>
      <div className="about_item">
        <div className="item_title">
          Rating the region
        </div>
        <div className="item_descr">
          1. Counting the number of categories
        </div>
        <div className="item_descr">
          2. Adding up the scores of each category
        </div>
        <div className="item_descr">
          3. Dividing the sum of the category ratings by the sum of the number of categories
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