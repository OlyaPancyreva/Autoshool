<template>
  <div>
    <img src="../assets/dfsfss.jpg" alt="..." style="width: 100%">
    <b-card id="my-card">
      <h3>
        Сведения об ученике автошколы
      </h3>
      <b-row>
        <b-col>
          <b-card>
            <h5 style="text-align: center">
              Личная информация
            </h5>
            <p class="mrgn">
              ФИО: {{ student.fio }}
            </p>
            <p class="mrgn">
              Дата рождения: {{ new Date(student.birthday).toLocaleDateString("ru") }}
            </p>
            <p class="mrgn">
              e-mail: {{ student.login }}
            </p>
            <p class="mrgn">
              Телефон: {{ student.phone }}
            </p>
            <p class="mrgn">
              Оставшееся количество занятий с инструктором: {{ student.drive_count }}
            </p>
            <p class="mrgn">
              Дата следующего занятия: {{ drive }}
              <br>
              <a v-show="get_drive" href="#" @click="cancelSchedule">Отменить занятие</a>
              <a v-show="!get_drive" href="#" @click="showModal">Записаться на занятие</a>
              <br>
            </p>
          </b-card>
        </b-col>
        <b-col>
          <b-card>
            <h5 style="text-align: center">
              Информация о занятиях
            </h5>
            <p class="mrgn">
              Группа: {{ student.group.name }}
            </p>
            <p class="mrgn">
              Дата начала занятий: {{ new Date(student.group.date_start).toLocaleDateString("ru") }}
            </p>
            <p class="mrgn">
              Дата окончания занятий: {{ new Date(student.group.date_end).toLocaleDateString("ru") }}
            </p>
            <p class="mrgn">
              Дата экзаменов: {{ new Date(student.group.date_exam).toLocaleDateString("ru") }}
            </p>
            <p class="mrgn">
              Расписание занятий в группе: {{ student.group.time }}
            </p>
            <p class="mrgn">
              Преподаватель: {{ student.group.teacher }}
            </p>
          </b-card>
        </b-col>
        <b-col>
          <b-card>
            <h5 style="text-align: center">
              Информация об инструкторе
            </h5>
            <p class="mrgn">
              ФИО: {{ student.instructor.fio }}
            </p>
            <p class="mrgn">
              Машина: {{ student.instructor.car }}
            </p>
            <p class="mrgn">
              Номер телефона: {{ student.instructor.phone }}
            </p>
          </b-card>
        </b-col>
      </b-row>

      <b-modal ref="modal"
               title="Запись на следующее занятие"
               @ok="newSchedule">
        <table class="table table-hover border">
          <tbody>
          <tr v-for="schedule in instructorSchedule" :key="schedule.id" @click="selectScheduleClick(schedule.id,
      schedule.datetime)">
            <td v-if="schedule.student==null && schedule.datetime>new Date().toISOString()">
              {{ new Date(schedule.datetime).toLocaleString('ru') }}
            </td>
          </tr>
          </tbody>
        </table>
        <p> Выбранное время: {{ new Date(selectedSchedule).toLocaleString('ru') }}</p>
      </b-modal>
    </b-card>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "StudentPage",
  data() {
    return {
      student: '',
      get_drive: '',
      drive: '',
      datetime: '',
      schedule: '',
      schedule_id: '',
      instructor_id: '',
      instructorSchedule: '',
      selectedSchedule: '',
      selectedSchedule_id: '',
      id: sessionStorage.getItem("userId")
    }
  },
  mounted() {
    this.getStudentDetail()
    this.getStudentSchedule()
  },
  methods: {
    // запрос детальной информации студента
    getStudentDetail() {
      $.ajax({
        url: `http://127.0.0.1:8000/students/${this.id}/`,
        method: 'GET',
        success: (response) => {
          this.student = response;
          this.instructor_id = response.instructor.id
        },
        error: (response) => {
          alert("Не удалось загрузить данные студента");
          console.log(response)
        }
      });
    },
    // записи на занятия студента
    getStudentSchedule() {
      $.ajax({
        url: `http://127.0.0.1:8000/student/schedule/?student=${this.id}`,
        method: 'GET',
        success: (response) => {
          this.schedule = response;
          for (let i = 0; i < this.schedule.length; i++) {
            if (this.schedule[i] == '' || this.schedule[i] == null || this.schedule[i].datetime < new Date().toISOString()) {
              this.get_drive = false
              this.drive = "-"
            } else {
              this.schedule_id = this.schedule[i].id;
              this.drive = new Date(this.schedule[i].datetime).toLocaleString("ru")
              this.get_drive = true
              break
            }
          }
        },
        error: (response) => {
          alert("Не удалось загрузить данные студента");
          console.log(response)
        }
      });
    },
    // расписание инструктора для записи студента
    getInstructorSchedule() {
      $.ajax({
        url: `http://127.0.0.1:8000/instructor/schedule/?instructor=${this.student.instructor.id}`,
        method: 'GET',
        success: (response) => {
          this.instructorSchedule = response;
        },
        error: (response) => {
          alert("Не удалось загрузить расписание инструктора");
          console.log(response)
        }
      });
    },
    // загрузка модального окна
    showModal() {
      this.getInstructorSchedule()
      this.$refs['modal'].show()
    },
    selectScheduleClick(id, time) {
      this.selectedSchedule_id = id
      this.selectedSchedule = time
    },
    // новая запись на занятие
    newSchedule() {
      if (this.selectedSchedule_id == '') {
        alert("Выберите время!")
      } else {
        $.ajax({
          url: `http://127.0.0.1:8000/schedule/${this.selectedSchedule_id}/`,
          method: 'PUT',
          data: {
            datetime: new Date(this.selectedSchedule).toISOString(),
            student: this.student.id,
            instructor: this.instructor_id,
          },
          success: () => {
            this.decrementCount()
            this.getStudentSchedule()
          },
          error: (response) => {
            alert("Не удалось записаться на занятие");
            console.log(response)
          }
        });
      }
    },
    // отмена записи
    cancelSchedule() {
      $.ajax({
        url: `http://127.0.0.1:8000/schedule/${this.schedule_id}/`,
        method: 'PUT',
        data: {
          student: null,
          datetime: this.schedule[this.schedule.length-1].datetime,
          instructor: this.schedule[this.schedule.length-1].instructor.id
        },
        success: () => {
          this.drive = null
          this.get_drive = false
          this.incrementCount()
          this.getStudentSchedule()
        },
        error: (response) => {
          alert("Не удалось отменить запись");
          console.log(response)
        }
      });
    },
    // прибавляем количество занятий с инструктором
    incrementCount() {
      $.ajax({
        url: `http://127.0.0.1:8000/students/${this.id}/`,
        method: 'PUT',
        data: {
          drive_count: this.student.drive_count + 1,
          fio: this.student.fio,
          login: this.student.login,
          password: this.student.password,
          birthday: this.student.birthday,
          phone: this.student.phone,
        },
        success: () => {
          this.getStudentDetail();
        },
        error: (response) => {
          alert("Не удалось изменить количество занятий с инструктором");
          console.log(response)
        }
      });
    },
    // уменьшаем количество занятий с инструктором
    decrementCount() {
      $.ajax({
        url: `http://127.0.0.1:8000/students/${this.id}/`,
        method: 'PUT',
        data: {
          drive_count: this.student.drive_count - 1,
          fio: this.student.fio,
          login: this.student.login,
          password: this.student.password,
          birthday: this.student.birthday,
          phone: this.student.phone,
        },
        success: () => {
          this.getStudentDetail();
        },
        error: (response) => {
          alert("Не удалось изменить количество занятий с инструктором");
          console.log(response)
        }
      });
    }
  }
}
</script>

<style scoped>
#my-card {
  width: 1300px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
}

.mrgn {
  margin-top: 20px;
}
</style>