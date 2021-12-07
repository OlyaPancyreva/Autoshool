<template>
  <div>
    <img src="../assets/dfsfss.jpg" alt="..." style="width: 100%">
    <b-card id="contact-card">
      <h3>
        Сведения об инструкторе автошколы
      </h3>
      <b-row>
        <b-col>
          <b-card>
            <h5 style="text-align: center">
              Личная информация
            </h5>
            <p class="mrgn">
              ФИО: {{ instructor.fio }}
            </p>
            <p class="mrgn">
              Номер телефона: {{ instructor.phone }}
            </p>
            <p class="mrgn">
              Почта: {{ instructor.login }}
            </p>
            <p class="mrgn">
              Машина: {{ instructor.car }}
            </p>
          </b-card>
        </b-col>
        <b-col>
          <b-card>
            <h5 style="text-align: center">
              Расписание
            </h5>
            <div v-for="sch in schedule" :key="sch.id">
              <p v-if="sch.datetime>new Date().toISOString()">
                {{ new Date(sch.datetime).toLocaleString("ru") }}, {{ sch.student }} <a href="#"
                                                                                        v-if="sch.student==null"
                                                                                        @click="cancelSchedule(sch.id)">Отменить</a>
              </p>
            </div>
            <b-button style="float: right" @click="showModal">Добавить расписание</b-button>
          </b-card>

          <b-modal ref="modal"
                   title="Добавить расписание"
                   @ok="newScheduleClick">
            <div style="width: 350px; margin-left: auto; margin-right: auto">
              <label for="date">Дата</label>
              <b-form-input type="date" v-model="date"></b-form-input>
              <label for="time">Время</label>
              <b-form-input type="time" v-model="time"></b-form-input>
            </div>

          </b-modal>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "InstructorPage",
  data() {
    return {
      instructor: '',
      schedule: '',
      newSchedule: [],
      date: '',
      time: '',
      now: '',
      id: sessionStorage.getItem("userId"),
    }
  },
  created() {
    this.getInstructorDetail();
    this.getInstructorSchedule();
  },
  methods: {
    // показ модального окна
    showModal() {
      this.$refs['modal'].show()
    },
    // загрузка детальной информации инструктора
    getInstructorDetail() {
      $.ajax({
        url: `http://127.0.0.1:8000/instructors/${this.id}/`,
        method: 'GET',
        success: (response) => {
          this.instructor = response;
        },
        error: (response) => {
          alert("Не удалось загрузить данные инструктора");
          console.log(response)
        }
      });
    },
    // получение расписания инструктора
    getInstructorSchedule() {
      $.ajax({
        url: `http://127.0.0.1:8000/instructor/schedule/?instructor=${this.id}`,
        method: 'GET',
        success: (response) => {
          this.schedule = response;
          for (let i = 0; i < this.schedule.length; i++) {
            let date = new Date(this.schedule[i].datetime);
            this.schedule[i].datetime = date.toISOString()
            if (this.schedule[i].student != null) {
              this.schedule[i].student = this.schedule[i].student.fio
            }
          }
        },
        error: (response) => {
          alert("Не удалось загрузить расписание инструктора");
          console.log(response)
        }
      });
    },
    // добавление нового расписания
    newScheduleClick() {
      var temp = this.date + 'T' + this.time + ":00+03:00";
      $.ajax({
        url: `http://127.0.0.1:8000/schedule/create/`,
        method: 'POST',
        data: {
          instructor: this.id,
          datetime: temp
        },
        success: () => {
          this.getInstructorSchedule()
          this.date = ""
          this.time = ""
        },
        error: (response) => {
          alert("Не удалось добавить расписание инструктора");
          console.log(response)
        }
      });
    },
    // удаление расписания
    cancelSchedule(id) {
      $.ajax({
        url: `http://127.0.0.1:8000/schedule/${id}/`,
        type: 'DELETE',
        data: {
          id: id,
        },
        success: () => {
          this.getInstructorSchedule()
        },
        error: (response) => {
          alert("Не удалось удалить расписание инструктора");
          console.log(response)
        }
      });
    }
  }
}
</script>

<style scoped>

</style>