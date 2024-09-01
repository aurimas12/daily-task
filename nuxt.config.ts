// nuxt.config.ts
export default {
  app: {
    head: {
      title: 'My Nuxt 3 App',
      meta: [
        { name: 'description', content: 'A Nuxt 3 application' },
      ],
    },
  },

  modules: [
    ],

  css: [
      'leaflet/dist/leaflet.css',
      '~/assets/css/tailwind.css',
    ],
    plugins: [
        '~/plugins/leaflet.client.js'
    ],

    analyze:true,
  compatibilityDate: '2024-09-01'
};