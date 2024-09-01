<template>
    <div id="map" ref="map" style="height: 100%; width: 100%;"></div>
  </template>
  
  <script>
  import { onMounted, ref } from 'vue';
  import L from 'leaflet'; // Įsitikinkite, kad šis importas yra teisingas
  
  export default {
    setup() {
      const mapElement = ref(null);
  
      onMounted(() => {
        const map = L.map('map').setView([51.505, -0.09], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);
    L.marker([51.505, -0.09]).addTo(map)
      .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
      .openPopup();
          
      });
  
      return {
        mapElement,
      };
    },
  };
  </script>
  
  <style scoped>
  #map {
    height: 100vh;
      width: 100vw;
  }
  </style>
  