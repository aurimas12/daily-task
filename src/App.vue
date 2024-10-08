<template>
  <div class="flex flex-col min-h-screen font-Roboto bg-weather-primary bg-pri">
    <SiteNavigation />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router';
import SiteNavigation from './components/SiteNavigation.vue';
// import '@fortawesome/fontawesome-free/css/all.min.css';


</script>

<style scoped>

</style>