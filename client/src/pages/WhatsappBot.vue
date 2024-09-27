<template>
  <main class="min-h-screen flex flex-col bg-gray-100">
    <Navbar />
    <section class="">
      <h2>WhatsApp Bot for Criminal Recognition</h2>
      <div class="flex flex-col md:flex-row justify-around gap-8">
        <div class="w-full md:w-1/2 bg-white rounded-lg shadow-md p-6">
          <h2 class="text-2xl font-semibold mb-4 text-gray-700">Normal User</h2>
          <img src="\wa.link_wrnl4q.png" alt="QR Code" class="w-48 h-48 mx-auto mb-6" />
          <a href="https://wa.link/wrnl4q" target="_blank" class="block w-full text-center bg-green-500 text-white py-3 px-4 rounded-lg hover:bg-green-600 transition duration-300 text-lg font-semibold">
            Thana Access
          </a>
          <p class="mt-6 text-sm text-gray-600 leading-relaxed">
            The user needs to login by scanning the above QR code or by clicking the button. After logging in, they can simply send an image of a suspect and get the result instantly.
          </p>
          
        </div>
        <div class="w-full md:w-1/2 bg-white rounded-lg shadow-md p-6">
          <h2 class="text-2xl font-semibold mb-4 text-gray-700">Admin User</h2>
          <img src="\wa.link_admin.png" alt="Admin QR Code" class="w-48 h-48 mx-auto mb-6" />
          <a href="https://wa.link/y82rxu" target="_blank" class="block w-full text-center bg-blue-500 text-white py-3 px-4 rounded-lg hover:bg-blue-600 transition duration-300 text-lg font-semibold">
            Admin Access
          </a>
          <p class="mt-6 text-sm text-gray-600 leading-relaxed">
            The admin can access the bot by scanning the above QR code or by clicking the button. After logging in, they can send an image of a suspect, which can then be added to the database if it doesn't already exist.
          </p>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import Navbar from '@/components/Navbar.vue';
</script>

<style scoped>
/* Add any additional styles here */
</style>