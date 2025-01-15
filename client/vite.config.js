import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const options = {
  plugins: [vue()],
}
if (process.env.NODE_ENV === 'development') {
  options.server = {
    host: 'swing.localhost',
    port: '9909'
  }
}
export default defineConfig(options)
