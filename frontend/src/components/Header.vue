<template>
  <div>
    <!--   Навигация сайта -->
    <div id="sq-masthead" class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-1 shadow-sm">
      <p class="my-0 mr-md-auto main-text" @click="mainPage">АВТОШКОЛА "ДРАЙВ"</p>
      <nav class="my-2 my-md-0 mr-md-3" style="text-align: right">
        <a class="p-3 button-text" @click="mainPage" href="#">Главная</a>
        <a class="p-3 button-text" @click="contactPage" href="#">Контакты</a>
        <a class="p-3 button-text" @click="linkPage" href="#">Полезные ссылки</a>
      </nav>
      <a v-b-modal.modal-1 class="p-3 button-text" v-show="!get_auth" href="#">Авторизация</a>
      <a class="p-3 button-text" @click="studentPage" v-if="type == 'Ученик'" href="#">Личный
        кабинет ученика</a>
      <a class="p-3 button-text" @click="instructorPage" v-if="type == 'Инструктор'" href="#">Личный
        кабинет инструктора</a>
      <a class="p-3 button-text" v-if="isAdmin == 'true'" @click="adminPage" href="#">Страница администратора</a>
      <a class="p-3 button-text" v-show="get_auth" @click="logout" href="#">Выход</a>
    </div>
    <!--    Конец навигации -->

    <!--    модальное окно для авторизации    -->
    <b-modal id="modal-1" title="Авторизация" @ok="auth">
      <b-form-group
          id="login"
          label="Логин"
          label-for="login"
      >
        <b-form-input
            v-model="login"
            id="login"
            type="e-mail"
            required
            placeholder="Введите логин"
        ></b-form-input>
      </b-form-group>
      <b-form-group
          id="password"
          label="Пароль"
          label-for="password"
      >
        <b-form-input
            v-model="password"
            id="password"
            type="password"
            required
            placeholder="Введите пароль"
        ></b-form-input>
        <b-form-select v-model="selected" class="mb-3" style="margin-top: 25px">
          <template #first>
            <b-form-select-option :value="null" disabled>Выберите тип пользователя</b-form-select-option>
          </template>
          <b-form-select-option value="Администратор">Администратор</b-form-select-option>
          <b-form-select-option value="Ученик">Ученик</b-form-select-option>
          <b-form-select-option value="Инструктор">Инструктор по вождению</b-form-select-option>
        </b-form-select>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "Header",
  data() {
    return {
      login: '',
      password: '',
      get_auth: '',
      isAdmin: '',
      users: '',
      students: '',
      instructors: '',
      correctLogin: '',
      type: '',
      selected: null,
    }
  },
  methods: {
    // авторизация на сайте
    auth() {
      if (this.selected != null) {
        if (this.selected === 'Ученик') {
          this.searchUser(this.students)
        } else if (this.selected === 'Инструктор') {
          this.searchUser(this.instructors)
        } else {
          var str = "[{\"login\":\"admin\",\"password\": \"admin\"}]"
          this.searchUser(JSON.parse(str))
        }
      } else {
        alert("Введите тип пользователя")
      }
    },
    // поиск в баз данных пользователя
    searchUser(users) {
      for (let i = 0; i < users.length; i++) {
        //  ищем пользователя в базе данных
        if (users[i].login === this.login && users[i].password === this.password) {
          this.correctLogin = true;
          this.userId = users[i].id;
          sessionStorage.setItem("userId", this.userId);
          sessionStorage.setItem("type", this.selected);
          break
        }
      }
      if (this.correctLogin) {
        this.isAdmin = this.login === 'admin';
        sessionStorage.setItem("admin", this.isAdmin);
        this.get_auth = true;
        location.reload();
      } else {
        alert("Неверный логин или пароль!") // если логин и пароль не совпали, выводим сообщение об ошибке
      }
    },
    // получение всех пользователей
    getStudents() {
      $.ajax({
        url: "http://127.0.0.1:8000/students/",
        methods: 'GET',
        success: (response) => {
          this.students = response;
        },
        error: (response) => {
          alert("Не удалось загрузить список учеников");
          console.log(response)
        }
      });
    },
    // получение всех инструкторов
    getInstructors() {
      $.ajax({
        url: "http://127.0.0.1:8000/instructors/",
        methods: 'GET',
        success: (response) => {
          this.instructors = response;
        },
        error: (response) => {
          alert("Не удалось загрузить список инструкторов");
          console.log(response)
        }
      });
    },
    // проверка авторизации при загрузке страницы
    check_auth() {
      this.userId = sessionStorage.getItem("userId")
      this.get_auth = sessionStorage.getItem("userId") !== null;
      this.isAdmin = sessionStorage.getItem("admin");
      this.type = sessionStorage.getItem("type");
    },
    // выход из аккаунта
    logout() {
      this.get_auth = false;
      this.isAdmin = false;
      this.type = '';
      sessionStorage.removeItem("admin");
      sessionStorage.removeItem("userId");
      sessionStorage.removeItem("type");
      location.reload();
    },
    studentPage() {
      this.$router.push({name: "StudentPage"})
    },
    instructorPage() {
      this.$router.push({name: "InstructorPage"})
    },
    mainPage() {
      this.$router.push({name: "StartPage"})
    },
    adminPage() {
      this.$router.push({name: "AdminPage"})
    },
    contactPage() {
      this.$router.push({name: "ContactPage"})
    },
    linkPage() {
      this.$router.push({name: 'Links'})
    }
  },
  created() {
    this.check_auth()
    this.getInstructors()
    this.getStudents()
  }
}
//  затемнение цвета навигации при скроллинге
$(document).ready(function () {
  $(window).scroll(function () {
    if (document.documentElement.scrollTop > 200) {
      $('#sq-masthead').css({background: 'rgba(30, 36, 42, 0.8)'})
    } else $('#sq-masthead').css({background: 'rgba(30, 36, 42, 0.4)'})
  });
});

</script>


<style scoped>
#sq-masthead {
  background: rgba(30, 36, 42, 0.4);
  font-family: 'Roboto Condensed', sans-serif;
  position: fixed;
  left: 0;
  right: 0;
  z-index: 999;
  height: 82px;
  transition: all 0.6s ease-in-out;
  -moz-transition: all 0.6s ease;
  -webkit-transition: all 0.6s ease;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
}

.main-text {
  font-weight: bold;
  margin-left: 100px;
  letter-spacing: 1px;
  font-size: 28px;
  color: #ffffff;
}

.button-text {
  font-weight: bold;
  letter-spacing: 1px;
  font-size: 20px;
  color: #ffffff;
}
</style>
