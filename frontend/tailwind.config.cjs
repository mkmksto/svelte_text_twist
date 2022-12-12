const config = {
    content: ['./src/**/*.{html,js,svelte,ts}'],
    purge: ['./index.html', './src/**/*.{svelte, js, ts}'],
    theme: {
        extend: {},
    },

    plugins: [],
}

module.exports = config
