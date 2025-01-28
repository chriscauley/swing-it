import { fileURLToPath, URL } from "url"
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const options = {
  plugins: [vue()],
  resolve: {
    alias: [
      { find: '@', replacement: fileURLToPath(new URL('./src', import.meta.url)) },
    ]
  }
}


if (process.env.NODE_ENV === 'development') {
  options.server = {
    host: 'as.localhost',
    port: '9909',
    proxy: {
      '/api': {
        target: 'http://localhost:8273',
        changeOrigin: true,
        secure: false,
      }
    }
  }
}

if (process.env.NODE_ENV === 'production') {
  console.log(1)
  options.base = '/static/'
  options.publicPath = '/static/'
}
export default defineConfig(options)
