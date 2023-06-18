import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/News.vue')
    },
    {
      path: '/detail/:id',
      name: 'detail',
      props: true,
      component: () => import('../views/Detail.vue')
    }
  ]
})

export default router
