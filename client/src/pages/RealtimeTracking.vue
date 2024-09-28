<script setup lang="ts">
import Navbar from '@/components/Navbar.vue';
import GoogleMaps from '@/components/GoogleMaps.vue';
import { onMounted, ref } from 'vue';
import { useFetch } from '@/composables/useFetch';
import { LucideLoader2 } from 'lucide-vue-next';
import { Camera } from '@/types/camera';

const { data: cameras, isLoading, error, fetchData } = useFetch<Camera[]>('/api/camera/', { method: 'GET' });
const selectedCamera = ref<Camera | null>(null);

onMounted(() => {
    fetchData();
});

</script>

<template>
    <main>
        <Navbar />
        <section class="flex flex-row gap-x-4">
            <aside class="basis-1/2 w-full h-full flex flex-col gap-y-4">
                <h3 class="text-2xl">Realtime CCTV Feed Tracking</h3>
                <div>
                    <label for="image"
                        class="p-5 border border-dashed border-blue-400 rounded-lg flex flex-col items-center">
                        <img src="/upload.png" class="size-20" />
                        <p class="text-lg mt-4">Drag and drop image files to upload</p>
                    </label>
                </div>
                <input id="image" type="file" class="hidden" accept=".jpeg, .jpg, .png">
                <div>
                    <h4 class="mb-3">Select Camera</h4>
                    <p v-if="isLoading">
                        <LucideLoader2 class="size-6 animate-spin" />
                    </p>
                    <p v-else-if="error">{{ error }}</p>
                    <div class="flex overflow-x-auto gap-x-3 pb-4">
                        <span @click="selectedCamera = camera" v-for="camera, index in cameras" :key="camera.id"
                            :class="(selectedCamera && selectedCamera.id === camera.id) && 'bg-orange-300 border-orange-600 text-orange-700'" class="py-3 px-5 flex-shrink-0 border bg-gray-100 rounded-md flex flex-col gap-y-4">
                            <img src="/cctv.png" alt="cctv" class="size-8">
                            <span class="text-sm text-inherit">Cam {{ index + 1 }}</span>
                        </span>
                    </div>
                </div>
            </aside>
            <div class="basis-1/2 rounded-lg overflow-hidden h-full transition-all duration-500">
                <GoogleMaps />
            </div>
        </section>
    </main>
</template>

<style scoped>
label {
    border-color: #9ca3af !important;
}

label:hover {
    border-color: #fb923c !important;
}
</style>