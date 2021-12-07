<template>
  <div id="my-form">
    <h3>
      Добавить нового инструктора
    </h3>
    <b-container>
      <b-row>
        <b-col>
          <label for="fio" class="mrgn">ФИО инструктора</label>
          <b-form-input v-model="fio" id="fio"></b-form-input>
          <label for="mail" class="mrgn">e-mail</label>
          <b-form-input v-model="login" id="mail" type="email"></b-form-input>
          <label for="phone" class="mrgn">Номер телефона</label>
          <b-form-input v-model="phone" id="phone" type="phone"></b-form-input>
        </b-col>
        <b-col>
          <label for="car" class="mrgn">Машина</label>
          <b-form-input v-model="car" id="car"></b-form-input>
          <label for="password" class="mrgn">Пароль</label>
          <b-form-input v-model="password" id="password"></b-form-input>
          <a href="#" style="float: right" @click="generatePassword">сгенерировать пароль</a>
        </b-col>
      </b-row>
    </b-container>
    <b-button style="float: right; margin:20px" @click="newInstructor">Сохранить</b-button>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "NewInstructor",
  data() {
    return {
      fio: '',
      car: '',
      phone: '',
      login: '',
      password: ''
    }
  },
  methods: {
    // генерация пароля
    generatePassword() {
      this.password = Math.random().toString(36).slice(-8);
    },
    newInstructor() {
      //  запрос к бд для создания инструктора
      $.ajax({
        url: "http://127.0.0.1:8000/instructors/create/",
        type: "POST",
        data: {
          fio: this.fio,
          car: this.car,
          phone: this.phone,
          login: this.login,
          password: this.password
        },
        success: () => {
          alert("Инструктор добавлен!")
          this.fio = ''
          this.car = ''
          this.phone = ''
          this.login = ''
          this.password = ''
        },
        error: (response) => {
          alert("Были введены некорректные данные");
          console.log(response)
        }
      })
    }
  }
}
</script>

<style scoped>
.mrgn {
  margin-top: 20px;
}
</style>