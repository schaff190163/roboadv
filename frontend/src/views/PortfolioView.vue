<template>
  <main>
    <h1>Portfolio</h1>
    <Portfolio_Worth></Portfolio_Worth>
  </main>
</template>

<script setup lang="ts">
import Portfolio_Worth from '@/components/Portfolio_Worth.vue';
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: calc(15px + 5vw);
}
</style>