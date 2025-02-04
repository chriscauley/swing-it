import { createApp } from 'vue'
import unrest from '@unrest/vue'
import Form from '@unrest/vue-form'

import components from './components'
import App from './App.vue'
import store from '@/store'
import router from '@/router'

import './css/index.css'
import '@unrest/tailwind/dist.css'

const app = createApp(App).use(Form).use(unrest.plugin).use(unrest.ui).use(router).use(store)

Object.entries(components).forEach(([name, component]) => app.component(name, component))

app.config.unwrapInjectedRef = true
app.mount('#app')
