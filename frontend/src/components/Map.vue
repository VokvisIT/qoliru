<template>
    <div className="map_title">
      {{  $t('map')  }}
    </div>
    <div className="wrapper">
      <div className="map_wrapper_title">
        {{  $t('qolir')  }}
      </div>
      <iframe
        src="https://yandex.ru/map-widget/v1/-/CCU5lhT~3D?z=4.5"
        width="100%"
        height="500"
        frameborder="0"
        allowfullscreen="true">
        </iframe>
    </div>
</template>

<script>

</script>

<style scoped>
.map_title {
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 32px; 
}
.map_wrapper_title{
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 24px; 
}
</style>