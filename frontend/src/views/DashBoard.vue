<template>
    <main>
      <h1>Dashboard</h1>
      <div>
        <Portfolio_Separation></Portfolio_Separation>
        <router-link to="/portfolio">View Portfolio</router-link>
      </div>
    </main>
  </template>
  
<script setup lang="ts">
import Portfolio_Separation from '@/components/Portfolio_Separation.vue';

</script>
  
<style scoped>
.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: calc(15px + 5vw);
  }
</style>