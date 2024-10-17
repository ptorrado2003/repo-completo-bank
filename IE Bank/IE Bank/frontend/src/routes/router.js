import { createMemoryHistory, createRouter } from 'vue-router'

import Index from './Index.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import Hello from './Hello.vue'

const routes = [
    { path: '/', component: Index },
    { path: '/hello', component: Hello },
    { path: '/register', component: Register },
    { path: '/login', component: Login }

]

export const router = createRouter({
    history: createMemoryHistory(),
    routes,
})