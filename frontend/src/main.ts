import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './ukit/css/uikit.css'
import './ukit/js/uikit.js'
import './ukit/js/uikit-icons.js'

const app = createApp(App)

app.use(router)

app.mount('#app')
