import { createRouter, createWebHistory } from 'vue-router'
import PortfolioView from '@/views/PortfolioView.vue';
import DashBoard from '@/views/DashBoard.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: DashBoard,
    },
  ],
});

export default router
