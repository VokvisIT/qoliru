import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { createProxyMiddleware } from 'vite-plugin-proxy'

export default defineConfig({
  plugins: [
    vue(),
    createProxyMiddleware('/api', {
      target: process.env.VUE_APP_API_URL,
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, '')
    })
  ],
  server: {
    port: 8080,
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
