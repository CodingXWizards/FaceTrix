<script setup lang="ts">
import { onMounted, watch } from "vue";
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

// Sync localStorage with authStore on page load
onMounted(() => {
  const storedAuth = localStorage.getItem("isAuthenticated");
  if (storedAuth === "true" && !authStore.isAuthenticated) {
    authStore.isAuthenticated = true;
  }
});

// Watch isAuthenticated in the authStore and localStorage
watch(
  () => authStore.isAuthenticated,
  (newValue, _) => {
    // Fetch user if authenticated
    if (newValue) {
      fetchUser();
    }
  }
);
</script>

<template>
  <RouterView />
</template>

<style scoped></style>
