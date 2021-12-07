<template>
  <div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th scope="col">ФИО</th>
        <th scope="col">Почта</th>
        <th scope="col">Номер телефона</th>
        <th scope="col">Машина</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in items" :key="item.id">
        <td>{{ item.fio }}</td>
        <td>{{ item.login }}</td>
        <td>{{ item.phone }}</td>
        <td>{{ item.car }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "InstructorBase",
  data() {
    return {
      items: '',
    }
  },
  created() {
    this.uploadList();
  },
  methods: {
    //  загрузка данных из бд
    uploadList() {
      $.ajax({
        url: "http://127.0.0.1:8000/instructors/",
        method: 'GET',
        success: (response) => {
          this.items = response;

        },
        error: (response) => {
          alert("Невозможно получить список инструкторов");
          console.log(response)
        }
      })
    },
  }
}
</script>

<style scoped>

</style>