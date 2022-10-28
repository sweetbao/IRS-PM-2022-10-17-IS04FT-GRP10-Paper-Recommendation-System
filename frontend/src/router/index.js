import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import Domain from '../views/DomainView.vue'
import Keyword from '../views/KeywordView.vue'
import Myprefer from '../views/Myprefer.vue'
import Paper from '../views/PaperView.vue'

const routes = [
  {
    path: "/",
    name: "Home",
    component: Domain,
  },
  {
    path: "/keyword/:topic",
    name: "Keyword",
    component: Keyword, props:true
  },
  {
    path: "/myprefer",
    name: "Myprefer",
    component: Myprefer,
  },
  {
    path: "/Paper/:keywords",
    name: "Paper",
    component: Paper,
    props:true
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;