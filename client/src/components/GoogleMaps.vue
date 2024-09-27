<script setup lang="ts">
import { reactive, ref, watchEffect } from "vue";
import { GoogleMap, AdvancedMarker, Marker } from "vue3-google-map";
const center = reactive({ lat: 21.170240, lng: 81.646880 });
const lat = ref(21.170240)
const lng = ref(81.646880)

const YOUR_GOOGLE_MAPS_API_KEY = "AIzaSyAQ5uRhnxw1ayb0EeVimce6svQRuYiE-q0";

const emit = defineEmits(["update:value"]);

function onClick(e: any) {
    const newLat = parseFloat(e.latLng.lat().toFixed(5));
    const newLng = parseFloat(e.latLng.lng().toFixed(5));
    emit("update:value", { newLat, newLng });
    lat.value = newLat;
    lng.value = newLng;
}

</script>

<template>
    <GoogleMap :api-key="YOUR_GOOGLE_MAPS_API_KEY" style="width: 100%; height: 100%" :center="center" :zoom="15"
        @click='onClick'>
        <Marker :options="{ position: { lat, lng } }" :pin-options="{ background: '#FBBC04' }" />
    </GoogleMap>
</template>

<style scoped></style>