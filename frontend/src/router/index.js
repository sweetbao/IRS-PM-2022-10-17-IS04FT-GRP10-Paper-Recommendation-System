import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import TextEmotion from '../views/HomeView.vue'
import twoclass from '../views/twoclass.vue'

const routes = [
  // history: createWebHistory(import.meta.env.BASE_URL),
  {path:"/",redirect:"/home"},
  
    {
      path: '/home',
      name: 'home',
      component: TextEmotion
    },
    {
      path: '/twoclass',
      name: 'twoclass',
      component: twoclass
    }
  ]


export const router=createRouter({
  history:createWebHashHistory(),
  routes:routes
})
