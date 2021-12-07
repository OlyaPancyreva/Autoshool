<template>
  <div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th scope="col">ФИО</th>
        <th scope="col">Дата рождения</th>
        <th scope="col">Почта</th>
        <th scope="col">Телефон</th>
        <th scope="col">Занятий с инструктором</th>
        <th scope="col">Инструктор</th>
        <th scope="col">Группа</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in items" :key="item.id">
        <td>{{ item.fio }}</td>
        <td>{{ new Date(item.birthday).toLocaleDateString('ru') }}</td>
        <td>{{ item.login }}</td>
        <td>{{ item.phone }}</td>
        <td>{{ item.drive_count }}</td>
        <td>{{ item.instructor.fio }}</td>
        <td>{{ item.group.name }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "StudentBase",
  data() {
    return {
      items: '',
      student: '',
    }
  },
  created() {
    this.uploadList();
  },
  methods: {
    // загрузка данных студентов
    uploadList() {
      $.ajax({
        url: "http://127.0.0.1:8000/students/",
        method: 'GET',
        success: (response) => {
          this.items = response;
        },
        error: (response) => {
          alert("Невозможно получить список учеников");
          console.log(response)
        }
      })
    },
  }
}
</script>

<style scoped>

</style>