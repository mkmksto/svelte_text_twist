import { svelte } from '@sveltejs/vite-plugin-svelte'
import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte()],
    // https://stackoverflow.com/questions/71180561/vite-change-ouput-directory-of-assets
    build: {
        // outDir: '../backend/templates',
        // assetsDir: 'static',
        // publicPath: '/static',
        //     rollupOptions: {
        //         output: {
        //             assetFileNames: (assetInfo) => {
        //                 let extType = assetInfo.name.split('.').at(1)
        //                 if (/png|jpe?g/i.test(extType)) {
        //                     extType = 'img'
        //                 }
        //                 return path.resolve(`../static/${extType}/[name]-[hash][extname]`)
        //             },
        //             chunkFileNames: '',
        //         },
        //     },
    },
})
