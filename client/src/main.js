import { createApp } from 'vue'

import './css/index.css'
import '@unrest/tailwind/dist.css'
import App from './App.vue'
import store from '@/store'


const app = createApp(App)
  .use(store)

app.config.unwrapInjectedRef = true
app.mount('#app')
