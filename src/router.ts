import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './pages/Home.vue'
import BoxOffice from './pages/BoxOffice.vue'

const routes = [
    { path: '/', name:'home', component: Home },
    { path: '/boxoffice', name:'boxoffice', component: BoxOffice },
    // { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHashHistory(),
    routes
})

export default router;