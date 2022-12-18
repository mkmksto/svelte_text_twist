import { svelte } from '@sveltejs/vite-plugin-svelte'
import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte()],
    // https://stackoverflow.com/questions/66863200/changing-the-input-and-output-directory-in-vite
    // https://stackblitz.com/edit/vitejs-output-file-paths?file=package.json,vite.config.js
    build: {
        outDir: '../../backend/templates',
        rollupOptions: {
            output: {
                assetFileNames: (assetInfo) => {
                    let extType = assetInfo.name.split('.').at(1)
                    if (/png|jpe?g|svg|gif|tiff|bm|ico/i.test(extType)) {
                        extType = 'img'
                    }
                    return `../../${extType}/[name]-[hash][extname]`
                },
                chunkFileNames: '../../static/js/[name]-[hash].js',
                entryFileNames: '../../static/js/[name]-[hash].js',
            },
        },
    },
})
