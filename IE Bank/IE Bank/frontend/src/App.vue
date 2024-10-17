<script setup>
import Index from './routes/index.vue'
import Navbar from './components/navbar.vue'
</script>

<template>
  <main class="bg-gray-900">
    <Navbar />
    <RouterView />
  </main>
</template>
