<template>
  <div v-if="isClient">
    <div id="map" style="height: 80vh;"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isClient: process.client
    }
  },
  async mounted() {
    if (this.isClient) {
      const L = await import('leaflet')
      this.initializeMap(L)
    }
  },
  methods: {
    initializeMap(L) {
      // Inicijuokite Leaflet čia
      const map = L.map('map').setView([51.505, -0.09], 13)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map)
    }
  }
}
</script>
