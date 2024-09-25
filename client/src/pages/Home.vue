<script setup lang="ts">
import { useAuthStore } from "@/store/authStore";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const router = useRouter();

async function handleLogout() {
  try {
    const response = await fetch("http://localhost:8000/api/auth/logout");
    console.log(await response.json());
    router.push("/login");
  } catch (error) {
    console.log(error);
  }
}
</script>

<template>
  <main>
    <nav
      class="w-full h-14 shadow-md shadow-gray-300 flex items-center justify-between px-10"
    >
      <div>
        <h4>{{ authStore.user?.name }}</h4>
        <p class="text-xs">{{ authStore.user?.designation }} (IPS)</p>
      </div>
      <button
        class="p-2 px-4 bg-red-500 rounded-lg text-white text-sm"
        @click="handleLogout"
      >
        Logout
      </button>
    </nav>
  </main>
</template>

<style scoped></style>
