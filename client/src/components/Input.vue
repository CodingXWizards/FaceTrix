<script setup lang="ts">

interface Props {
  id: string;
  label: string;
  value: string | number | null;
  placeholder: string;
}
defineProps<Props>();

const emit = defineEmits(["update:value"]);

function handleChange(e: Event) {
  const target = e.target as HTMLInputElement;
  emit("update:value", target.value);
}

</script>

<template>
  <div class="w-full">
    <label class="block" for="password">{{ label }}</label>
    <input :id="id" type="text" :value="value" @change="handleChange" :placeholder="placeholder" required/>
  </div>
</template>

<style scoped>
@tailwind base;
@tailwind components;
@tailwind utilities;

input {
  @apply w-full mt-1 p-2 border border-gray-400 rounded-lg focus:outline-none focus:border-orange-500
}
</style>
