/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
        fontFamily: {
            // 'sans': ['ui-sans-serif', 'system-ui',],
            // 'serif': ['ui-serif', 'Georgia', "NewYork", 'PolySans'],
            // 'mono': ['ui-monospace', 'SFMono-Regular',],
            // 'display': ['Oswald',],
            // 'body': ['"Open Sans"',],
            'josephin': ['"Josefin Sans"']    ,
            'analogist': ['"Analogist"']
        },
        extend: {},
    },
    plugins: [
        require('daisyui'),
    ],
    daisyui: {
        themes: ["light"]
    }
}
