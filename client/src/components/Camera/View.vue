<script setup lang="ts">
import './camera.css';
import { Camera } from '@/types/camera';
import { LucideLoader2 } from 'lucide-vue-next';

defineProps<{
    loading: boolean;
    cameras: Camera[] | null;
}>();

</script>

<template>
    <form class="h-full">
        <h3>All Camera</h3>
        <table v-if="!loading" border="1">
            <thead>
                <tr>
                    <th>S.no</th>
                    <th>IP</th>
                    <th>Port</th>
                    <th>GR</th>
                    <th>Azimuth</th>
                    <th>Thana</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="camera, index in cameras" :key="camera.id">
                    <td>{{ index+1 }}</td>
                    <td>{{ camera.ipAddress }}</td>
                    <td>{{ camera.port }}</td>
                    <td>{{ camera.latitude + ", " + camera.longitude }}</td>
                    <td>{{ camera.azimuth }}</td>
                    <td>{{ camera.thana }}</td>
                    <td>
                        <p :style='camera.status === "ACTIVE" ? "background-color: #86efac; color: #16a34a; border-color: #16a34a" : "background-color: #fca5a5; color: #dc2626; border-color: #dc2626"'
                            class='p-2 px-2 h-7 flex border red-300 items-center justify-center font- rounded'>
                            {{ camera.status }}</p>
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-else class="h-full flex items-center justify-center">
            <LucideLoader2 class="mx-auto size-7 animate-spin" />
        </div>
    </form>
</template>

<style scoped>
@tailwind base;
@tailwind components;
@tailwind utilities;

h3 {
    @apply text-2xl
}

table,
th,
td {
    @apply border border-gray-400
}

th, td {
    @apply p-1.5 text-center rounded-md text-gray-700 min-w-[100px]
}

th {
    @apply font-medium text-gray-900 text-sm
}

td {
    @apply text-xs
}
</style>