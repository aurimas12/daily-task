// nuxt.config.ts
export default {
  app: {
    head: {
      script: [
        {
          src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js', // Prideda Bootstrap JS
          integrity: 'sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+ftx8aOWhh7y0cH6DYG8N0y3B4ZjYJ', // Patikrinkite versiją
          crossorigin: 'anonymous',
        },
      ],
    },
  },

  modules: [

  ],
   
  css: [
    'bootstrap/dist/css/bootstrap.css',

      'leaflet/dist/leaflet.css',
      '~/assets/css/tailwind.css',

    ],
  
    bootstrapVue: {
      icons: true // Jei norite naudoti „BootstrapVue“ piktogramas
    },

    plugins: [
        '~/plugins/leaflet.client.js',
        '~/plugins/bootstrap-vue.js'

    ],

    analyze:true,
  compatibilityDate: '2024-09-01'
};


