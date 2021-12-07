import Vue from 'vue'
import VueRouter from 'vue-router'
import StartPage from "@/components/StartPage";
import ContactPage from "@/components/ContactPage";
import AdminPage from "@/components/AdminMode/AdminPage";
import StudentPage from "@/components/StudentPage";
import InstructorPage from "@/components/InstructorPage";
import Links from "@/components/Links";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'StartPage',
    component: StartPage
  },
  {
    path: '/contact',
    name: 'ContactPage',
    component: ContactPage
  },
  {
    path: '/admin',
    name: 'AdminPage',
    component: AdminPage
  },
  {
    path: '/student',
    name: 'StudentPage',
    component: StudentPage
  },
  {
    path: '/instructor',
    name: 'InstructorPage',
    component: InstructorPage
  },
  {
    path: '/link',
    name: 'Links',
    component: Links
  },
]

const router = new VueRouter({
  routes
})

export default router
