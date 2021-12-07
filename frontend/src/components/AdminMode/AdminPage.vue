<template>
  <div>
    <img src="../../assets/dfsfss.jpg" alt="..." style="width: 100%">
    <b-aspect :aspect="3">
      <b-card class="buts">
<!--        навигация для админа  -->
        <div>
          <b-navbar type="light" variant="light" id="nav">
            <b-navbar-nav>
              <b-nav-item-dropdown text="Добавить" right style="margin-left: 20px">
                <b-dropdown-item href="#" v-on:click="onNewGroup">Добавить группу</b-dropdown-item>
                <b-dropdown-item href="#" v-on:click="onNewStudent">Добавить студента</b-dropdown-item>
                <b-dropdown-item href="#" v-on:click="onNewInstructor">Добавить инструктора</b-dropdown-item>
              </b-nav-item-dropdown>

              <b-nav-item-dropdown text="База данных" right style="margin-left: 20px">
                <b-dropdown-item href="#" v-on:click="onStudentBase">Студенты</b-dropdown-item>
                <b-dropdown-item href="#" v-on:click="onInstructorBase">Инструкторы</b-dropdown-item>
                <b-dropdown-item href="#" v-on:click="onGroupBase">Группы</b-dropdown-item>
              </b-nav-item-dropdown>

              <b-nav-item-dropdown text="Заявки" right style="margin-left: 20px">
                <b-dropdown-item href="#" v-on:click="onRequestList">Заявки на обучение</b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-navbar>
        </div>

        <StudentBase v-show="studentBase"></StudentBase>
        <InstructorBase v-show="instructorBase"></InstructorBase>
        <NewGroup v-show="newGroup"></NewGroup>
        <RequestList v-show="requestList"></RequestList>
        <NewStudent v-show="newStudent"></NewStudent>
        <NewInstructor v-show="newInstructor"></NewInstructor>
        <GroupBase v-show="groupBase"></GroupBase>
      </b-card>
    </b-aspect>
  </div>
</template>

<script>
import StudentBase from "@/components/AdminMode/StudentBase";
import InstructorBase from "@/components/AdminMode/InstructorBase";
import NewGroup from "@/components/AdminMode/NewGroup";
import RequestList from "@/components/AdminMode/RequestList";
import NewStudent from "@/components/AdminMode/NewStudent";
import NewInstructor from "@/components/AdminMode/NewInstructor";
import GroupBase from "@/components/AdminMode/GroupBase";

export default {
  name: "AdminPage",
  components: {GroupBase, NewInstructor, NewStudent, RequestList, NewGroup, InstructorBase, StudentBase},
  data() {
    return {
      studentBase: false,
      instructorBase: false,
      newGroup: false,
      requestList: false,
      newStudent: false,
      newInstructor: false,
      groupBase: false,
    }
  },
  methods: {
    clear() {
      this.studentBase = false;
      this.instructorBase = false;
      this.newGroup = false;
      this.requestList = false;
      this.newStudent = false;
      this.newInstructor = false;
      this.groupBase = false;
    },
    onStudentBase() {
      this.clear();
      this.studentBase = true;
    },
    onInstructorBase() {
      this.clear();
      this.instructorBase = true;
    },
    onGroupBase() {
      this.clear();
      this.groupBase = true;
    },
    onNewGroup() {
      this.clear();
      this.newGroup = true;
    },
    onRequestList() {
      this.clear();
      this.requestList = true;
    },
    onNewStudent() {
      this.clear();
      this.newStudent = true;
    },
    onNewInstructor() {
      this.clear();
      this.newInstructor = true;
    }
  }
}
</script>

<style scoped>
.buts {
  width: 1300px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 20px;
}

</style>