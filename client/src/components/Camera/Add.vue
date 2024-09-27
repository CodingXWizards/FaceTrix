<script setup lang="ts">
import { reactive } from 'vue';
import Input from '../Input.vue';
import { Camera } from '@/types/camera';
import { watch } from 'vue';

const props = defineProps<{ lng: number, lat: number }>();

const data = reactive<Camera>({
    id: "",
    username: "",
    ipAddress: "",
    password: "",
    port: null,
    channel: "",
    subType: "",
    latitude: props.lat,
    longitude: props.lng,
    azimuth: null,
    status: "",
    thana: "",
});

watch(
    () => props.lat,
    (newLat) => {
        data.latitude = newLat;
    }
);

watch(
    () => props.lng,
    (newLng) => {
        data.longitude = newLng;
    }
);

</script>

<template>
    <form>
        <header class="flex justify-between items-center gap-x-5">
            <h3>Add Camera</h3>
            <div class="w-[160px] flex items-center">
                <v-select :items="['RTSP', 'IP Address']" class="h-[40px]" density="compact" variant="outlined"
                    label="Select Format" model-value="RTSP"></v-select>
            </div>
        </header>
        <div class="flex flex-col gap-y-3">
            <div class="flex gap-x-2">
                <Input id="username" label="Username" :value="data.username" placeholder="username" />
                <Input id="password" label="Password" :value="data.password" placeholder="password" />
            </div>
            <div class="flex gap-x-2">
                <Input id="ip" label="IP Address" :value="data.ipAddress" placeholder="0.0.0.0" />
                <Input id="port" label="Port" :value="data.port" placeholder="554" />
                <Input id="channel" label="Channel" :value="data.channel" placeholder="1" />
            </div>
            <div class="flex gap-x-2">
                <Input id="subtype" label="Subtype" :value="data.subType" placeholder="0" />
                <Input id="latitude" label="Latitude" :value="data.latitude" placeholder="0" />
                <Input id="longitude" label="Longitude" :value="data.longitude" placeholder="0" />
                <Input id="azimuth" label="Azimuth" :value="data.azimuth" placeholder="0" />
            </div>
            <div class="flex gap-x-2">
                <Input id="thana" label="Thana" :value="data.thana" placeholder="thana" />
                <Input id="status" label="Status" :value="data.status" placeholder="active" />
            </div>
        </div>
        <div class="w-full flex gap-x-4">
            <button type="button"
                class="py-2 px-5 text-sm bg-orange-500 hover:bg-orange-600 transition text-white rounded-md">Save</button>
            <button type="button"
                class="py-2 px-5 text-sm bg-red-500 hover:bg-red-600 transition text-white rounded-md">Cancel</button>
        </div>
    </form>
</template>

<style scoped></style>