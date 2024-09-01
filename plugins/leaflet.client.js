import { defineNuxtPlugin } from '#app'
import L from 'leaflet'

export default defineNuxtPlugin(nuxtApp => {
  nuxtApp.provide('leaflet', L)
})