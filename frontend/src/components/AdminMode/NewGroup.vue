<template>
  <div id="my-form">
    <h3>
      Добавить новую группу обучения
    </h3>
    <b-container>
      <b-row>
        <b-col>
          <label for="name" class="mrgn">Номер группы</label>
          <b-form-input v-model="name" id="name"></b-form-input>
          <label for="date_start" class="mrgn">Дата начала занятий</label>
          <b-form-input v-model="date_start" type="date" id="date_start"></b-form-input>
          <label for="teacher" class="mrgn">Преподаватель группы</label>
          <b-form-input v-model="teacher" id="teacher"></b-form-input>
          <label for="time" class="mrgn">Время занятий</label>
          <b-form-input v-model="time" id="teacher"></b-form-input>
        </b-col>
        <b-col>
          <label for="category" class="mrgn">Категория обучения</label>
          <b-form-select v-model="category" :options="options" id="category"></b-form-select>
          <label for="date_end" class="mrgn">Дата окончания занятий</label>
          <b-form-input v-model="date_end" type="date" id="date_end"></b-form-input>
          <label for="date_exam" class="mrgn">Дата сдачи экзаменов</label>
          <b-form-input v-model="date_exam" type="date" id="date_exam"></b-form-input>
        </b-col>
      </b-row>
    </b-container>
    <b-button style="float: right; margin:20px" @click="newGroup">Сохранить</b-button>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "NewGroup",
  data() {
    return {
      name: '',
      date_start: '',
      date_end: '',
      date_exam: '',
      time: '',
      category: '',
      teacher: '',
      options: [
        {value: 'А', text: 'А-мотоциклы'},
        {value: 'B', text: 'B-легковые автомобили'},
        {value: 'С', text: 'С-грузовики'},
        {value: 'D', text: 'D-автобусы'},
        {value: 'М', text: 'М-мопеды'},
      ]
    }
  },
  methods: {
    // запрос к бд для создания группы
    newGroup() {
      $.ajax({
        url: "http://127.0.0.1:8000/group/create/",
        type: "POST",
        data: {
          name: this.name,
          date_start: this.date_start,
          date_end: this.date_end,
          time: this.time,
          date_exam: this.date_exam,
          category: this.category,
          teacher: this.teacher
        },
        success: () => {
          alert("Группа добавлена!")
          this.name = ''
          this.date_start = ''
          this.date_end = ''
          this.date_exam = ''
          this.category = ''
          this.teacher = ''
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