<script setup lang="ts">
import CameraAdd from "@/components/Camera/Add.vue";
import CameraView from "@/components/Camera/View.vue";
import GoogleMaps from "@/components/GoogleMaps.vue";
import Navbar from "@/components/Navbar.vue";
import { useFetch } from "@/composables/useFetch";
import { Camera } from "@/types/camera";
import { Marker } from "@/types/marker";
import { LucideEye, LucidePlus } from "lucide-vue-next";
import { onMounted, ref, watch } from "vue";

const activeSection = ref<'VIEW' | 'ADD' | 'UPDATE'>('VIEW');
const lat = ref(21.170240);
const lng = ref(81.646880);

function handleUpdate({ newLat, newLng }: { newLat: number, newLng: number }) {
    lat.value = newLat;
    lng.value = newLng;
}

const markers = ref<Marker[]>([]);

const { data: cameras, isLoading, fetchData } = useFetch<Camera[]>('/api/camera/', { method: 'GET' });

onMounted(() => {
    fetchData();
});

watch(cameras, (newValue, _) => {
    if (newValue && newValue.length > 0) {
        markers.value = newValue.map((camera: Camera) => ({ id: camera.id, latitude: camera.latitude, longitude: camera.longitude, azimuth: camera.azimuth }));
    }
})

</script>

<template>
    <main>
        <Navbar />
        <section>
            <header class="flex justify-between items-center">
                <h2>Camera</h2>
                <div class="flex gap-x-4">
                    <LucidePlus @click="activeSection = 'ADD'"
                        :class="'p-2 size-9 text-white rounded-md ' + (activeSection === 'ADD' ? 'bg-gray-800 hover:bg-opacity-100' : 'bg-orange-600 hover:bg-opacity-90')" />
                    <LucideEye @click="activeSection = 'VIEW'"
                        :class="'p-2 size-9 text-white rounded-md ' + (activeSection === 'VIEW' ? 'bg-gray-800 hover:bg-opacity-100' : 'bg-orange-600 hover:bg-opacity-90')" />
                </div>
            </header>
            <div class="w-full flex flex-grow gap-x-2">
                <div :class="activeSection === 'VIEW' ? 'basis-1/2' : 'basis-1/3'"
                    class="transition-all duration-500 overflow-auto">
                    <CameraAdd :lng="lng" :lat="lat" v-if="activeSection == 'ADD'" />
                    <CameraView :loading="isLoading" :cameras="cameras" v-if="activeSection == 'VIEW'" />
                </div>
                <div :class="activeSection === 'VIEW' ? 'basis-1/2' : 'basis-2/3'"
                    class="rounded-lg overflow-hidden h-full transition-all duration-500">
                    <GoogleMaps :markers="markers" @update:value="handleUpdate" />
                </div>
            </div>
        </section>
    </main>
</template>

<style scoped>
/* You can add any additional styles for the map container here if needed */
</style>