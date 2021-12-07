<template>
  <div>
    <img src="../assets/dfsfss.jpg" alt="..." style="width: 100%">
    <!--    карточка с контактами автошколы   -->
    <b-card id="contact-card">
      <p>
        <b-icon icon="geo-alt-fill" class="my-icon"></b-icon>
        г. Казань, ул. Сафиуллина, 50а
      </p>
      <p>
        <b-icon icon="clock-history" class="my-icon"></b-icon>
        Пн.- пт. с 12.00. до 19.00., сб. с 12.00 до 15.00
      </p>
      <p>
        <b-icon icon="telephone" class="my-icon"></b-icon>
        т. 511-99-04
      </p>
      <p>
        <b-icon icon="telephone-fill" class="my-icon"></b-icon>
        Прием граждан: запись по телефону (843) 511-13-31; 511-99-04
      </p>
      <p>
        <b-icon icon="envelope" class="my-icon"></b-icon>
        drive-autoschool@mail.ru
      </p>
    </b-card>

    <!--    яндекс карта  -->
    <yandex-map
        zoom="13"
        id="map"
        :coords="coords"
    >
      <ymap-marker
          marker-type="placemark"
          :coords="coords"
          :marker-id="index"
          :key="index"
          hint-content="ул. Сафиуллина, 50а"
      ></ymap-marker>
    </yandex-map>
  </div>
</template>

<script>


import {yandexMap, ymapMarker} from 'vue-yandex-maps'

export default {
  name: "ContactPage",
  components: {yandexMap, ymapMarker},
  data() {
    return {
      coords: [55.747252, 49.227687] //  координаты для карты
    }
  }
}
</script>

<style scoped>

.my-icon {
  width: 30px;
  height: 30px;
}

#map {
  width: 80%;
  height: 98vh;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px
}
</style>