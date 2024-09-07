<template>
  <div class="container mt-4">
    <div class="row">
      <!-- Paieškos stulpelis, kuris užima visą pločio eilutę -->
      <div class="col-12">
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Search</h5>
            <input type="text" class="form-control" placeholder="Search...">
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <!-- Meniu stulpelis su 3/12 pločio -->
      <div class="col-md-3">
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Menu</h5>
            <ul class="list-group">
              <li class="list-group-item">Home</li>
              <li class="list-group-item">About</li>
              <li class="list-group-item">Services</li>
              <li class="list-group-item">Contact</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Žemėlapio stulpelis su likusiu pločiu -->
      <div class="col-md-9">
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Map</h5>
            <div id="map" style="height: 400px;"></div>
          </div>
        </div>
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

        // Sukuriame žemėlapį
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
  height: 400px;
}
</style>
