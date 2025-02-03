import { fileURLToPath, URL } from "url"
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const _url = (s) => fileURLToPath(new URL('./' + s, import.meta.url))

const options = {
  plugins: [vue()],
  resolve: {
    alias: [
      { find: '@', replacement: _url('./src', import.meta.url) },
      { find: "jsonschema", replacement: _url("./node_modules/jsonschema") },
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
