<template>
  <div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th scope="col">Номер группы</th>
        <th scope="col">Категория</th>
        <th scope="col">Преподаватель</th>
        <th scope="col">Расписание</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in items" :key="item.id">
        <td>{{ item.name }}</td>
        <td>{{ item.category }}</td>
        <td>{{ item.teacher }}</td>
        <td>{{ item.time }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "GroupBase",
  data() {
    return {
      items: '',
    }
  },
  created() {
    this.uploadList()
  },
  methods: {
    //  загрузка данных из бд
    uploadList() {
      $.ajax({
        url: "http://127.0.0.1:8000/group/",
        method: 'GET',
        success: (response) => {
          this.items = response;

        },
        error: (response) => {
          alert("Невозможно получить список групп");
          console.log(response)
        }
      })
    },
  }
}
</script>

<style scoped>

</style>