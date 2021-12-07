<template>
  <div id="my-form">
    <h3>
      Добавить нового ученика
    </h3>
    <b-container>
      <b-row>
        <b-col>
          <label for="fio" class="mrgn">ФИО ученика</label>
          <b-form-input v-model="fio" id="fio"></b-form-input>
          <label for="mail" class="mrgn">e-mail</label>
          <b-form-input v-model="login" id="mail"></b-form-input>
          <label for="instructor" class="mrgn">Инструктор</label>
          <b-form-select v-model="instructor" id="instructor" style="margin-top: 7px">
            <b-form-select-option v-for="instr in instructors" :key="instr.id" :value="instr.id">
              {{ instr.fio }}
            </b-form-select-option>
          </b-form-select>
          <label for="password" class="mrgn">Пароль</label>
          <b-form-input v-model="password" id="password"></b-form-input>
          <a href="#" style="float: right" @click="generatePassword">сгенерировать пароль</a>
        </b-col>
        <b-col>
          <label for="birthday" class="mrgn">Дата рождения</label>
          <b-form-input v-model="birthday" id="birthday" type="date"></b-form-input>
          <label for="phone" class="mrgn">Номер телефона</label>
          <b-form-input v-model="phone" id="phone" type="phone"></b-form-input>
          <label for="group" class="mrgn">Группа</label>
          <b-form-select v-model="group" id="group" style="margin-top: 7px">
            <b-form-select-option v-for="gr in groups" :key="gr.id" :value="gr.id">
              {{ gr.name }}
            </b-form-select-option>
          </b-form-select>
        </b-col>
      </b-row>
    </b-container>
    <b-button style="float: right; margin:20px" @click="newStudent">Сохранить</b-button>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "NewStudent",
  data() {
    return {
      fio: '',
      birthday: '',
      login: '',
      password: '',
      instructor: '',
      group: '',
      instructors: '',
      groups: '',
      phone: '',
    }
  },
  created() {
    this.getInstructors();
    this.getGroups();
  },
  methods: {
    //  генерация пароля
    generatePassword() {
      this.password = Math.random().toString(36).slice(-8);
    },
    // получение всех интрукторов
    getInstructors() {
      $.ajax({
        url: "http://127.0.0.1:8000/instructors/",
        method: 'GET',
        success: (response) => {
          this.instructors = response;
        },
        error: (response) => {
          alert("Не удалось загрузить список инструкторов");
          console.log(response)
        }
      });
    },
    //  получение всех групп
    getGroups() {
      $.ajax({
        url: "http://127.0.0.1:8000/group/",
        method: 'GET',
        success: (response) => {
          this.groups = response;
        },
        error: (response) => {
          alert("Невозможно получить список групп");
          console.log(response)
        }
      })
    },
    // запрос к бд для создания нового студента
    newStudent() {
      $.ajax({
        url: "http://127.0.0.1:8000/students/create/",
        type: "POST",
        data: {
          fio: this.fio,
          login: this.login,
          password: this.password,
          phone: this.phone,
          birthday: this.birthday,
          instructor: this.instructor,
          group: this.group
        },
        success: () => {
          alert("Студент добавлен!")
          this.fio = ''
          this.login = ''
          this.password = ''
          this.phone = ''
          this.birthday = ''
          this.instructor = ''
          this.group = ''
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