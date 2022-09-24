import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './pages/Home.vue'
import BoxOffice from './pages/BoxOffice.vue'
import Top250 from './pages/Top250.vue'
import BoxOfficeAllTime from './pages/BoxOfficeAllTime.vue'
import Single from './pages/Single.vue'
import Actor from './pages/Actor.vue'
import Awards from './pages/Awards.vue'
import Search from './pages/Search.vue'

const routes = [
    { path: '/', name:'home', component: Home },
    { path: '/boxoffice', name:'boxoffice', component: BoxOffice },
    { path: '/top250', name:'top250', component: Top250 },
    { path: '/boxofficeall', name:'boxofficeall', component: BoxOfficeAllTime },
    { path: '/title/:id', name: 'single', component: Single },
    { path: '/actor/:id', name: 'actor', component: Actor },
    { path: '/awards/:id', name: 'awards', component: Awards },
    { path: '/search/:exp', name: 'Search', component: Search },
    // { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHashHistory(),
    routes
})

export default router;