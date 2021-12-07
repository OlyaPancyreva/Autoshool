<template>
  <div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th scope="col">Имя</th>
        <th scope="col">Почта</th>
        <th scope="col">Номер телефона</th>
        <th scope="col">Статус</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in items" :key="item.id">
        <td id="name">{{ item.name }}</td>
        <td id="mail">{{ item.mail }}</td>
        <td id="phone">{{ item.phone }}</td>
        <b-form-select :id="item.id" :options="options" :value="item.status" @change="changeStatus(item)"
                       style="margin-top: 7px"></b-form-select>
      </tr>

      </tbody>
    </table>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "RequestList",
  data() {
    return {
      items: '',
      options: [
        {value: 1, text: 'На рассмотрении'},
        {value: 2, text: 'Заявка обработана'},
        {value: 3, text: 'Клиент отказался'},
      ]
    }
  },
  created() {
    this.uploadList();
  },
  methods: {
    // список заявок на обучение
    uploadList() {
      $.ajax({
        url: "http://127.0.0.1:8000/request/",
        method: 'GET',
        success: (response) => {
          this.items = response;

        },
        error: (response) => {
          alert("Невозможно получить список заявок ");
          console.log(response)
        }
      })
    },
    changeStatus(item) {
      $.ajax({
        url: `http://127.0.0.1:8000/request/${item.id}/`,
        type: 'PUT',
        data: {
          name: item.name,
          mail: item.mail,
          phone: item.phone,
          status: document.getElementById(item.id).value
        },
        success: (response) => {
          console.log(response);
        },
        error: (response) => {
          console.log(response)
          alert("Ошибка в редактировании");
        }
      })
    }
  }
}
</script>

<style scoped>

</style>