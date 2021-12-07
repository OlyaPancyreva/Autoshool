<template>
  <div>
    <img src="../assets/carousel.jpg" alt="..." style="width: 100%">
    <b-card id="my-card">
      <h3 style="margin: 30px">Новости</h3>
      <b-card-group deck
                    style="color: #0f6890; margin:10px;font-family: 'Open Sans', Helvetica, Arial, sans-serif;">
        <b-card>
          <b-card-text>ОБНОВЛЕНИЕ САЙТА</b-card-text>
          <b-card-text style="color: black; font-size: 14px">Мы постоянно развиваемся и рады представить Вам наш
            новый сайт. Просто нажмите на кнопку "Подать заявку" и наш менеджер Вам перезвонит.
          </b-card-text>
        </b-card>
        <b-card>
          <b-card-text>АДАПТИВНЫЙ САЙТ</b-card-text>
          <b-card-text style="color: black; font-size: 14px">Наш сайт адаптирован для мобильных устройств, а это
            значит, что Вы можете использовать его прямо со своего телефона или планшета.
          </b-card-text>
        </b-card>
        <b-card>
          <b-card-text>ОНЛАЙН ДОСТУП 24/7</b-card-text>
          <b-card-text style="color: black; font-size: 14px">Мы используем передовые технологии, а это
            значит, что на нашем сайте Вы можете просматривать расписание, записываться на занятие или в группы в любое
            время суток.
          </b-card-text>
        </b-card>
      </b-card-group>
      <img src="../assets/Artboard.png" alt="..."
           style="width: 1200px; height: auto; margin-left: 30px; margin-bottom: 40px">
      <div class="container" style="margin: 30px; ">
        <div class="row">
          <div class="col-1-2">
            <h4>Хотите узнать подробности?</h4>
            <p class="text-muted">Оставьте заявку, и мы перезвоним Вам. Мы отвечаем быстро, не рассылаем
              спам и не навязываем дополнительных услуг. Просто попробуйте и убедитесь сами!</p>
          </div>
          <div class="col-1-3">
            <b-button v-b-modal.modal-sm class="btn-req">Подать заявку на обучение</b-button>

            <!--            модальное окно для заявки   -->
            <b-modal id="modal-sm" size="sm" title="Оставьте заявку на обучение" ref="modal" @ok="handleOk">
              <b-form-group>
                <b-form-input id="name" v-model="name" placeholder="Введите свое имя" class="mrgn"></b-form-input>
                <b-form-input id="mail" v-model="mail" placeholder="Введите почту" class="mrgn"></b-form-input>
                <b-form-input id="phone" type="tel" v-model="phone" placeholder="Номер телефона"
                              class="mrgn"></b-form-input>
              </b-form-group>
            </b-modal>
          </div>
        </div>
      </div>
    </b-card>
  </div>
</template>
<script>
import $ from 'jquery'

export default {
  name: "StartPage",
  data() {
    return {
      name: '',
      mail: '',
      phone: '',
    }
  },
  methods: {
    // отправка заявки на обучение в бд
    handleOk() {
      $.ajax({
        url: "http://127.0.0.1:8000/request/",
        type: "POST",
        data: {
          name: this.name,
          mail: this.mail,
          phone: this.phone,
        },
        success: () => {
          alert("Заявка зарегистрирована")
        },
        error: (response) => {
          alert("Были введены некорректные данные");
          console.log(response)
        }
      })
    },
  }
}

</script>

<style scoped>
#my-card {
  width: 1300px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
}

.col-1-2 {
  width: 70%;
  float: left;
  font-size: 18px;
}

.col-1-3 {
  width: 25%;
  margin-left: 5%;
  float: left;
  font-size: 18px;
}

.btn-req {
  margin-top: 8%;
  min-height: 50px;
  width: auto;
  font-size: 20px;
  background-color: #0f6890 !important;
  display: flex;
  animation: radial-pulse 1s infinite;
}

@keyframes radial-pulse {
  0% {
    box-shadow: 0 0 0 0px rgba(0, 0, 0, 0.5);
  }

  100% {
    box-shadow: 0 0 0 40px rgba(0, 0, 0, 0);
  }
}

.mrgn {
  margin: 10px;
  width: 250px;
  margin-top: 20px;
}
</style>