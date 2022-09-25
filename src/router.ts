import { createRouter, createWebHashHistory } from 'vue-router'

const Home = () => import('./pages/Home.vue')
const BoxOffice = () => import('./pages/BoxOffice.vue')
const Top250 = () => import('./pages/Top250.vue')
const BoxOfficeAllTime = () => import('./pages/BoxOfficeAllTime.vue')
const Single = () => import('./pages/Single.vue')
const Actor = () => import('./pages/Actor.vue')
const Search = () => import('./pages/Search.vue')

const routes = [
    { path: '/', name:'home', component: Home },
    { path: '/boxoffice', name:'boxoffice', component: BoxOffice },
    { path: '/top250', name:'top250', component: Top250 },
    { path: '/boxofficeall', name:'boxofficeall', component: BoxOfficeAllTime },
    { path: '/title/:id', name: 'single', component: Single },
    { path: '/actor/:id', name: 'actor', component: Actor },
    { path: '/search/:exp', name: 'Search', component: Search },
    // { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHashHistory(),
    routes
})

export default router;