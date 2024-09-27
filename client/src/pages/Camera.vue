<script setup lang="ts">
import CameraAdd from "@/components/Camera/Add.vue";
import CameraView from "@/components/Camera/View.vue";
import GoogleMaps from "@/components/GoogleMaps.vue";
import Navbar from "@/components/Navbar.vue";
import { LucideEye, LucidePlus } from "lucide-vue-next";
import { ref } from "vue";

const activeSection = ref<'VIEW' | 'ADD' | 'UPDATE'>('ADD');
const lat = ref(21.170240);
const lng = ref(81.646880);

function handleUpdate({ newLat, newLng }: { newLat: number, newLng: number }) {
    lat.value = newLat;
    lng.value = newLng;
}

</script>

<template>
    <main class="h-screen">
        <Navbar />
        <div class="h-[calc(100vh-3.5rem)] flex-grow px-10 py-5 flex flex-col gap-y-4">
            <header class="flex justify-between items-center">
                <h2>Camera</h2>
                <div class="flex gap-x-4">
                    <LucidePlus @click="activeSection = 'ADD'"
                        :class="activeSection === 'ADD' && 'bg-gray-800 hover:bg-opacity-100'"
                        class="bg-orange-600 hover:bg-opacity-90 p-2 size-9 text-white rounded-md" />
                    <LucideEye @click="activeSection = 'VIEW'"
                        :class="activeSection === 'VIEW' && 'bg-gray-800 hover:bg-opacity-100'"
                        class="bg-orange-600 hover:bg-opacity-90 p-2 size-9 text-white rounded-md" />
                </div>
            </header>
            <section class="w-full flex flex-grow gap-x-2">
                <div :class="activeSection === 'VIEW' ? 'basis-1/2' : 'basis-1/3'" class="transition-all duration-500">
                    <CameraAdd :lng="lng" :lat="lat" v-if="activeSection == 'ADD'" />
                    <CameraView v-if="activeSection == 'VIEW'" />
                </div>
                <div :class="activeSection === 'VIEW' ? 'basis-1/2' : 'basis-2/3'"
                    class="rounded-lg overflow-hidden h-full transition-all duration-500">
                    <GoogleMaps :lat="lat" :lng="lng" @update:value="handleUpdate" />
                </div>
            </section>
        </div>
    </main>
</template>

<style scoped>
/* You can add any additional styles for the map container here if needed */
</style>