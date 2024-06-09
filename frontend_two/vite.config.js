import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8080,
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  configureServer(server) {
    const proxy = require('http-proxy-middleware')
    const { VUE_APP_API_URL } = process.env

    server.middlewares.use(
      '/api',
      proxy({
        target: VUE_APP_API_URL,
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      })
    )
  }
})
