<template>
  <div class="map-container">
    <div class="map" id="map" ref="mapRef"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css'; 

const mapRef = ref<HTMLElement | null>(null);
const map = ref<L.Map | null>(null);

const initMap = () => {
  if (mapRef.value) {
    const parisCoords: L.LatLngExpression = [48.8566, 2.3522];
  map.value = L.map(mapRef.value).setView(parisCoords, 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  }).addTo(map.value as L.Map);
  }


};

onMounted(() => {
  initMap();
});
</script>

<style scoped>

.map-container {
  width: 1200px; 
  height: 600px;
  margin: 0 auto; 
  max-width: 100%; 
}

.map {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}
</style>