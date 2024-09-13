import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import Settings from '../views/Settings.vue'
import Profile from '../views/Profile.vue'
import Signin from '../views/Signin.vue'
import Signup from '../views/Signup.vue'

import { useAuthStore } from '/src/stores/authStore.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: IndexView
    },
    {
      path: '/settings',
      name: 'settings',
      component: Settings,
      meta: {requireLogin: true}
    },
    {
      path: '/profile/:user_name',
      //path: '/profile',
      name: 'profile',
      component: Profile,
      meta: {requireLogin: true}
    },
    {
      path: '/Signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/Signup',
      name: 'Signup',
      component: Signup
    },
    
    /*{
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }*/
  ]
})

router.beforeEach((to, from, next) => {
  const store = useAuthStore()
  console.log("Whats auth: " + store.isAuthenticated)
  if(to.matched.some(record => record.meta.requireLogin) && !store.isAuthenticated) {
      console.log("whats to path: " + to.path)
      next({
        name: 'Signin', query: { to: to.path}
      });
  }
  else {
    next()
  }
})




export default router
