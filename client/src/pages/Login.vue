<script setup lang="ts">
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { LucideLoader2 } from "lucide-vue-next";
import { useLoading } from "@/composables/useLoading";
import { useAuthStore } from "@/store/authStore";

const credentials = reactive<{ email: string; password: string }>({
  email: "",
  password: "",
});

const router = useRouter();
const authStore = useAuthStore();

const { loading, withLoading } = useLoading();
const error = ref<string | null>(null);

function handleSubmit(event: Event) {
  error.value = null;
  event.preventDefault();
  withLoading(async () => {
    const response = await fetch("http://localhost:8000/api/auth/signin", {
      method: "POST",
      credentials: 'include',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: credentials.email,
        password: credentials.password,
      }),
    });
    const body = await response.json();
    console.log(body)
    if (response.status !== 200) {
      error.value = body.detail;
      const errorElement = document.getElementById("error");
      errorElement!.style.height = "20px";
      setTimeout(() => {
        errorElement!.style.height = "0px";
      }, 5000);
      return;
    }
    router.push("/");
  });
}
</script>

<template>
  <main class="w-full h-screen flex justify-center items-center bg-gray-100">
    <form
      @submit="handleSubmit"
      class="w-[400px] text-gray-700 bg-white shadow-[0_0_10px] shadow-gray-300 rounded-xl p-5 flex flex-col gap-y-4"
    >
      <h2 class="text-2xl text-center font-semibold">Police 5 Star</h2>
      <div>
        <label class="block" for="email">Email</label>
        <input
          class="w-full mt-1 p-2 border border-gray-300 rounded-lg"
          type="text"
          v-model="credentials.email"
          placeholder="janedoe@gmail.com"
        />
      </div>
      <div>
        <label class="block" for="email">Password</label>
        <input
          class="w-full mt-1 p-2 px-3 border border-gray-300 rounded-lg"
          type="password"
          v-model="credentials.password"
          placeholder="Password"
        />
      </div>
      <p
        id="error"
        class="text-red-600 h-0 overflow-hidden transition-all text-sm"
      >
        {{ error }}
      </p>
      <button
        class="w-full p-2 px-3 bg-blue-600 hover:bg-opacity-90 transition-colors text-white rounded-lg text-center"
        type="submit"
      >
        <LucideLoader2 v-if="loading" class="size-6 animate-spin mx-auto" />
        <span v-else>Login</span>
      </button>
      <p class="text-sm text-center">Don't have an accont? Contact the Admin</p>
    </form>
  </main>
</template>

<style scoped></style>
