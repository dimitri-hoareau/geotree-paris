<script setup lang="ts">
import TreeMap from './components/TreeMap.vue'
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
import FilterSidebar from './components/FilterSidebar.vue';
</script>

<template>
  <AppHeader />
  <div class="main-content">
      <FilterSidebar />
      <TreeMap />
    </div>
  <AppFooter />
</template>

<style scoped>
.main-content {
  display: flex;
}

</style>
