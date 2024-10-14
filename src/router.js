import { createRouter, createWebHistory } from 'vue-router'
import Viewer from './components/Viewer.vue'

const routes = [
  { path: '/decolace_web_viewer/:dataset/:area', component: Viewer, name:"area"},
  { path: '/decolace_web_viewer/:dataset', component: Viewer},
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router