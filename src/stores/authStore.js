import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/*export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})*/

export const useAuthStore = defineStore('authStore', {
  state:() => ({
    
      isAuthenticated: false,
      token: '',
      user: '',
    }),
  
  getters: {
    getToken(state) {
        console.log("Whats this: " + state.token)
        return state.token
    },
    getAuthentication(state) {
        return state.isAuthenticated
    },
    getUser(state){
      console.log("Current user: " + state.user)
      return state.user
    }
  },
  actions: {
    setToken(value) {
        this.token = value
        this.isAuthenticated = true
        console.log('Token: ' + this.token)
    },
    removeToken() {
        this.token = ''
        this.isAuthenticated = false
    },
    initializeStore() {
        if(localStorage.getItem('token')) {
            this.token = localStorage.getItem('token')
            this.isAuthenticated = true
        }
        else {
            this.token = ''
            this.isAuthenticated = false
        }
    },
    setUser(value){
      console.log("whats set user: " + value)
      this.user = value
      console.log("user now: " +this.user)
    },
    removeUser(){
      this.user = ''
    }
}
})