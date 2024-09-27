<script setup lang="ts">
import { Marker as MarkerType } from "@/types/marker";
import { reactive, ref } from "vue";
import { GoogleMap, InfoWindow, Marker, Polygon } from "vue3-google-map"; // Import Polygon

const center = reactive({ lat: 21.22562, lng: 81.30462 });
const lat = ref(21.22562)
const lng = ref(81.30462)

const YOUR_GOOGLE_MAPS_API_KEY = "AIzaSyAQ5uRhnxw1ayb0EeVimce6svQRuYiE-q0";

defineProps<{
    markers: MarkerType[];
}>();

const emit = defineEmits(["update:value"]);

function onClick(e: any) {
    const newLat = parseFloat(e.latLng.lat().toFixed(5));
    const newLng = parseFloat(e.latLng.lng().toFixed(5));
    emit("update:value", { newLat, newLng });
    lat.value = newLat;
    lng.value = newLng;
};

// Function to calculate a new point
function calculatePoint(lat: number, lon: number, azimuth: number, distance: number): { newLat: number, newLng: number } {
    const earthRadius = 6371; // Earth's radius in kilometers

    // Convert degrees to radians
    const latRad = degreesToRadians(lat);
    const lonRad = degreesToRadians(lon);
    const azimuthRad = degreesToRadians(90 - azimuth);  // Adjust for north as up

    // Calculate new latitude and longitude
    const newLatRad = Math.asin(
        Math.sin(latRad) * Math.cos(distance / earthRadius) +
        Math.cos(latRad) * Math.sin(distance / earthRadius) * Math.cos(azimuthRad)
    );

    const newLonRad = lonRad + Math.atan2(
        Math.sin(azimuthRad) * Math.sin(distance / earthRadius) * Math.cos(latRad),
        Math.cos(distance / earthRadius) - Math.sin(latRad) * Math.sin(newLatRad)
    );

    // Convert radians back to degrees
    const newLat = radiansToDegrees(newLatRad);
    const newLng = radiansToDegrees(newLonRad);

    return { newLat, newLng };
}

// Helper functions for conversion
function degreesToRadians(deg: number): number {
    return deg * (Math.PI / 180);
}

function radiansToDegrees(rad: number): number {
    return rad * (180 / Math.PI);
}

// Create azimuth range
function createAzimuthRange(lat: number, lng: number, azimuth: number) {
    const azimuthRange = [];
    const startAngle = azimuth - 60;
    const endAngle = azimuth + 60;

    for (let angle = startAngle; angle <= endAngle; angle += 5) {
        const { newLat, newLng } = calculatePoint(lat, lng, angle, 0.05);
        azimuthRange.push({ lat: newLat, lng: newLng });
    }

    // Radial points
    const { newLat: startRadialLat, newLng: startRadialLng } = calculatePoint(lat, lng, startAngle, 0.05);
    const { newLat: endRadialLat, newLng: endRadialLng } = calculatePoint(lat, lng, endAngle, 0.05);

    azimuthRange.push({ lat: startRadialLat, lng: startRadialLng });
    azimuthRange.push({ lat: endRadialLat, lng: endRadialLng });

    // Include the center point
    azimuthRange.push({ lat, lng });

    return azimuthRange;
}

</script>

<template>
    <GoogleMap :api-key="YOUR_GOOGLE_MAPS_API_KEY" style="width: 100%; height: 100%" :center="center" :zoom="15"
        @click='onClick'>
        <Marker :options="{ position: { lat, lng } }" :pin-options="{ background: '#FBBC04' }" />
        <Marker v-for="(marker, index) in markers" :key="index" :content="`Camera No. ${index}`"
            :options="{ position: { lat: marker.latitude, lng: marker.longitude } }">
            <InfoWindow class="flex items-center justify-center">
                <h5>Camera No: {{ index + 1 }}</h5>
            </InfoWindow>
        </Marker>

        <!-- Add the semi-circle Polygon -->
        <Polygon v-for="marker in markers" :key="marker.id"
            :options="{ paths: createAzimuthRange(marker.latitude, marker.longitude, marker.azimuth), fillColor: '#f97316', fillOpacity: 0.35, strokeColor: '#f97316', strokeOpacity: 0.8, strokeWeight: 2 }" />
    </GoogleMap>
</template>

<style scoped></style>