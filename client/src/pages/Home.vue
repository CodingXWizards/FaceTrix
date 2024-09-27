<template>
  <div class="bg-gray-100 min-h-screen font-sans">
    <!-- Header is now handled by your Navbar component -->
    <Navbar />

    <!-- Hero Section -->
    <section class="text-center py-20 px-4 bg-white mb-8">
      <h2 class="text-6xl font-bold mb-4">FaceTrix</h2>
      <h3 class="text-4xl mb-6">Police 5Star do nothing</h3>
      <p class="max-w-2xl mx-auto mb-10 text-gray-600">
        Empowering police and communities through advanced technology. Access live camera feeds, facial
        recognition, and comprehensive logs for enhanced security, ensuring safety and transparency in every
        neighborhood we serve
      </p>
      <button class="bg-blue-600 text-white px-8 py-3 rounded-full flex items-center mx-auto hover:bg-blue-700 transition-colors">
        See Feeds <ArrowRight class="ml-2" />
      </button>
    </section>

    <!-- Main Content -->
    <div class="flex justify-between px-8 space-x-8">
      <!-- Left Column -->
      <div class="w-1/4 space-y-6">
        <div class="bg-white p-6 rounded-2xl shadow-md">
          <h4 class="font-bold mb-4 text-lg">Channels</h4>
          <div class="space-y-4">
            <button class="bg-blue-600 text-white w-full py-3 rounded-full flex items-center justify-between px-6 hover:bg-blue-700 transition-colors">
              <span class="flex items-center"> Whatsapp</span>
              <ArrowRight :size="18" />
            </button>
            <button class="bg-blue-600 text-white w-full py-3 rounded-full flex items-center justify-between px-6 hover:bg-blue-700 transition-colors">
              <span class="flex items-center"><MessageSquare :size="18" class="mr-3" /> Message</span>
              <ArrowRight :size="18" />
            </button>
            <button class="bg-blue-600 text-white w-full py-3 rounded-full flex items-center justify-between px-6 hover:bg-blue-700 transition-colors">
              <span class="flex items-center"><Mail :size="18" class="mr-3" /> Email</span>
              <ArrowRight :size="18" />
            </button>
          </div>
        </div>
        <div class="bg-blue-600 text-white p-6 rounded-2xl">
          <h5 class="font-bold mb-3 text-lg">View</h5>
          <p>Facial recognition Section</p>
          <div class="flex justify-center mt-4">
            <span class="bg-white w-2 h-2 rounded-full mx-1"></span>
            <span class="bg-white w-2 h-2 rounded-full mx-1"></span>
            <span class="bg-white w-2 h-2 rounded-full mx-1"></span>
          </div>
        </div>
      </div>

      <!-- Center Column (Map) -->
      <div class="w-1/2">
  <div class="w-full max-w-[714px] mx-auto overflow-hidden rounded-3xl shadow-lg">
    <img 
      src="/map.png" 
      alt="Map showing various camera locations and alerts" 
      class="w-full h-[690px] object-contain"
    />
  </div>
  <div class="mt-4 bg-blue-50 p-4 rounded-2xl">
    <p class="font-semibold">Camera 4 not responding</p>
    <p class="text-red-500 mt-2">Potential miss ratio!</p>
  </div>
</div>

      <!-- Right Column -->
      <div class="w-1/4 space-y-6">
        <div class="bg-white p-6 rounded-2xl shadow-md">
          <h4 class="font-bold mb-4 text-lg flex items-center justify-between text-blue-600">
            Logs & Reports <ArrowRight :size="18" />
          </h4>
          <p class="mb-4 text-gray-600"><Eye :size="18" class="inline mr-3 text-blue-600" /> Criminal 1 - 23/SEP/2024</p>
          <button class="bg-blue-600 text-white px-6 py-2 rounded-full w-full hover:bg-blue-700 transition-colors">Download report</button>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-md">
          <h4 class="font-bold mb-4 text-lg text-blue-600">Quick Metrics</h4>
          <div class="grid grid-cols-2 gap-4">
            <div class="bg-blue-600 p-4 rounded-xl text-white">
              <p class="text-sm mb-1 opacity-80">Criminals in Database</p>
              <p class="font-bold text-xl">5000</p>
            </div>
            <div class="bg-blue-600 p-4 rounded-xl text-white">
              <p class="text-sm mb-1 opacity-80">Detected criminals</p>
              <p class="font-bold text-xl">24</p>
            </div>
            <div class="bg-blue-600 p-4 rounded-xl text-white">
              <p class="text-sm mb-1 opacity-80">Active cameras</p>
              <p class="font-bold text-xl">6</p>
            </div>
            <div class="bg-blue-600 p-4 rounded-xl text-white">
              <p class="text-sm mb-1 opacity-80">Alerts</p>
              <p class="font-bold text-xl">18</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ArrowRight, MessageSquare, Mail, Eye } from 'lucide-vue-next';
import Navbar from '@/components/Navbar.vue';
</script>

<style scoped>
</style>