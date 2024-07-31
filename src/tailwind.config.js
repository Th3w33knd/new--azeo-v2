/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "../templates/**/*.html",
        "../webapp/templates/**/*.html",
    ],
    theme: {
        extend: {},
    },
    plugins: [require('daisyui')],
    daisyui: {
        themes: ["light", "synthwave"]
    }
}

