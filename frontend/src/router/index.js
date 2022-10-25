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
    path: "/keyword",
    name: "Keyword",
    component: Keyword,
  },
  {
    path: "/myprefer",
    name: "Myprefer",
    component: Myprefer,
  },
  {
    path: "/Paper",
    name: "Paper",
    component: Paper,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;