import './index.css'
import './assets/assets/css/icons.css'
import './assets/assets/css/uikit.css'
import './assets/assets/css/style.css'
import './assets/assets/css/tailwind.css'
//import './assets/css/main.min.css'
import './assets/css/style.css'
import './assets/css/color.css'
import './assets/css/responsive.css'



import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia )
app.use(router)



app.mount('#app')
