<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Šoninis skydelis -->
    <!-- <Sidebar /> -->
    
    <!-- Turinio zona -->
    <main class="flex-1 flex flex-col p-6">
      <!-- Žemėlapio vieta -->
      <div class="bg-black flex-1 mb-6 rounded-lg shadow-lg">
        <Map />
      </div>

      <!-- Veiksmų mygtukai -->
      <div class="mb-6 flex space-x-4">
        <button @click="addPoint" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Pridėti Tašką</button>
        <button @click="highlightArea" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Pažymėti Plotą</button>
        <button @click="markTrajectory" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">Pažymėti Trajektoriją</button>
      </div>

      <!-- Aktualių taškų sąrašas -->
      <div class="bg-white p-6 rounded-lg shadow-lg border border-gray-200">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Aktyvūs Taškai</h2>
        <ul>
          <li v-for="(point, index) in points" :key="index" class="text-gray-600 mb-2">
            {{ point.name }} ({{ point.coordinates.join(', ') }})
          </li>
        </ul>
      </div>
    </main>
  </div>

</template>

<script setup>
import { ref } from 'vue'

import Map from '~/components/Map.vue'


// Taškai sąraše
const points = ref([])

// Veiksmų funkcijos
const addPoint = () => {
  console.log('Pridėti tašką')
}

const highlightArea = () => {
  console.log('Pažymėti plotą')
}

const markTrajectory = () => {
  console.log('Pažymėti trajektoriją')
}
</script>

<style scoped>
/* Papildomi stiliai, jei reikia */
</style>
