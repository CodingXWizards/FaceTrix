<script setup lang="ts">
import { useAuthStore } from "./store/authStore";

const authStore = useAuthStore();

async function fetchUser() {
  try {
    const response = await fetch("http://localhost:8000/api/user", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    });
    const body = await response.json();
    authStore.login(body.user);
  } catch (error) {
    console.log(error);
  }
}
fetchUser();
</script>

<template>
  <RouterView />
</template>

<style scoped></style>
