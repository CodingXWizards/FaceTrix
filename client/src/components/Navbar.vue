<script setup lang="ts">
import { useAuthStore } from "@/store/authStore";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const router = useRouter();

async function handleLogout() {
  try {
    const response = await fetch("http://localhost:8000/api/auth/logout", {
      method: "GET",
      credentials: "include",
    });
    console.log(await response.json());
    localStorage.removeItem("isAuthenticated");
    router.push("/login");
  } catch (error) {
    console.log(error);
  }
}
</script>

<template>
  <nav class="w-full h-14 shadow-md shadow-gray-300 flex items-center justify-between px-10">
    <div class="flex items-center gap-x-3">
      <img src="/police.png" alt="police" width="40" height="40">
      <div>
        <h5>{{ authStore.user?.name }}</h5>
        <p class="text-xs">{{ authStore.user?.designation }}</p>
      </div>
    </div>
    <div class="flex items-center gap-x-6">
      <RouterLink to="/" class="nav-link">Home</RouterLink>
      <RouterLink to="/camera" class="nav-link">Camera</RouterLink>
      <RouterLink to="/whatsapp-bot" class="nav-link">Whatsapp Bot</RouterLink>
      <button class="p-2 px-4 bg-red-600 rounded-lg text-white text-sm" @click="handleLogout">
        Logout
      </button>
    </div>
  </nav>
</template>

<style scoped>
.nav-link {
  @apply text-gray-700 hover:text-orange-500 transition-colors;
}

.router-link-active {
  @apply text-orange-500 font-semibold;
}
</style>