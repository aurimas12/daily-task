<template>
  <div id="app">
    <h1>Vue with Leaflet Map</h1>
    <MapComponent />
  </div>
</template>

<script>
import MapComponent from './components/MapComponent.vue'; // Importuojame MapComponent

export default {
  components: {
    MapComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
