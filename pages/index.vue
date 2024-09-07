<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-3">
      <a class="navbar-brand" href="#">My Project</a>
    </nav>

    <div class="card mb-3">
      <div class="card-body">
        <h5 class="card-title">Hello, World!</h5>
        <p class="card-text">Welcome to my Nuxt project with Bootstrap and Leaflet.</p>
        <button class="btn btn-primary mr-2">Primary Button</button>
        <button class="btn btn-success mr-2">Success Button</button>
        <button class="btn btn-danger">Danger Button</button>
      </div>
    </div>

    <div class="row mt-4">
      <div class="col">
        <div id="map" style="height: 500px;"></div>
      </div>
    </div>
  </div>
</template>

<script>
let L;

export default {
  mounted() {
    if (process.client) {
      import('leaflet').then((module) => {
        L = module.default;

        const map = L.map('map').setView([54.6872, 25.2797], 13);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
        }).addTo(map);
      });
    }
  },
};
</script>

<style scoped>
#map {
  height: 500px;
}
</style>
