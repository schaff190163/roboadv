import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Registration from '../views/Registration.vue'
import EditPortfolio from '../views/EditPortfolio.vue'
import Dashboard from '../views/Dashboard.vue'

Vue.use(VueRouter)

const routes = [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Registration },
    { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
    { path: '/edit-portfolio', component: EditPortfolio, meta: { requiresAuth: true } },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
