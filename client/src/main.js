import { createApp } from 'vue'
import unrest from '@unrest/vue'
import Form from '@unrest/vue-form'

import App from './App.vue'
import store from '@/store'
import router from '@/router'

import './css/index.css'
import '@unrest/tailwind/dist.css'

const app = createApp(App)
  .use(Form)
  .use(unrest.plugin)
  .use(unrest.ui)
  .use(router)
  .use(store)

app.config.unwrapInjectedRef = true
app.mount('#app')
