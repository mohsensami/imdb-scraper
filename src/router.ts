import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './pages/Home.vue'
import BoxOffice from './pages/BoxOffice.vue'
import Top250 from './pages/Top250.vue'
import BoxOfficeAllTime from './pages/BoxOfficeAllTime.vue'

const routes = [
    { path: '/', name:'home', component: Home },
    { path: '/boxoffice', name:'boxoffice', component: BoxOffice },
    { path: '/top250', name:'top250', component: Top250 },
    { path: '/boxofficeall', name:'boxofficeall', component: BoxOfficeAllTime },
    // { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHashHistory(),
    routes
})

export default router;