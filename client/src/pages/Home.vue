<script setup lang="ts">
import Navbar from '@/components/Navbar.vue';
</script>

<template>
  <main class="h-screen flex flex-col">
    <Navbar />
    <section class="flex-grow p-5 flex flex-col gap-y-5">
      <div class="flex-grow flex flex-col justify-between bg-gray-200 rounded-lg">
        <span></span>
        <div>
        </div>
      </div>
      <RouterLink class="p-2 px-4 w-fit bg-orange-500 hover:bg-opacity-90 text-white rounded-lg" to="/camera">
        Camera</RouterLink>
    </section>
  </main>
</template>

<style scoped></style>