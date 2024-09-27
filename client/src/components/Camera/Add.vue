<script setup lang="ts">
import { reactive, ref } from 'vue';
import Input from '../Input.vue';
import { Camera } from '@/types/camera';
import { watch } from 'vue';
import { useLoading } from '@/composables/useLoading';

const props = defineProps<{ lng: number, lat: number }>();
const { loading, withLoading } = useLoading();

const data = reactive<Camera>({
    id: "",
    username: "",
    ipAddress: "",
    password: "",
    port: 554,
    channel: 0,
    subType: 0,
    latitude: props.lat,
    longitude: props.lng,
    azimuth: 30,
    status: "",
    thana: "",
});

const snackMesg = ref<string>("");
const snackbar = ref<boolean>(false);

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

function handleSubmit(e: Event) {
    e.preventDefault();
    withLoading(async () => {
        try {

            const response = await fetch("http://localhost:8000/api/camera", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    ip_address: data.ipAddress,
                    username: data.username,
                    password: data.password,
                    port: data.port,
                    channel: data.channel,
                    subtype: data.subType,
                    latitude: data.latitude,
                    longitude: data.longitude,
                    azimuth: data.azimuth,
                    status: data.status,
                    thana: data.thana
                })
            });
            if (response.status !== 200) {
                snackMesg.value = "Something went wrong";
                snackbar.value = true;
                return;
            }
            snackMesg.value = "Camera Added Successfully";
            snackbar.value = true;
            // handleReset();
            data.id = "";
            data.username = "";
            data.ipAddress = "";
            data.password = "";
            data.port = 554;
            data.channel = 0;
            data.subType = 0;
            data.latitude = props.lat;
            data.longitude = props.lng;
            data.azimuth = 30;
            data.status = "";
            data.thana = "";
        } catch (error) {
            console.log(error)
            snackMesg.value = "Something went wrong";
            snackbar.value = true;
        }
    })
};

function handleReset(e: Event) {
    e!.preventDefault();
    data.id = "";
    data.username = "";
    data.ipAddress = "";
    data.password = "";
    data.port = 554;
    data.channel = 0;
    data.subType = 0;
    data.latitude = props.lat;
    data.longitude = props.lng;
    data.azimuth = 30;
    data.status = "";
    data.thana = "";
}

</script>

<template>
    <form @submit="handleSubmit" @reset="handleReset">
        <header class="flex justify-between items-center gap-x-5">
            <h3>Add Camera</h3>
            <div class="w-[160px] flex items-center">
                <v-select :items="['RTSP', 'IP Address']" class="h-[40px]" density="compact" variant="outlined"
                    label="Select Format" model-value="RTSP"></v-select>
            </div>
        </header>
        <div class="flex flex-col gap-y-3">
            <div class="flex gap-x-2">
                <Input id="username" label="Username" v-model:value="data.username" placeholder="username" />
                <Input id="password" label="Password" v-model:value="data.password" placeholder="password" />
            </div>
            <div class="flex gap-x-2">
                <Input id="ip" label="IP Address" v-model:value="data.ipAddress" placeholder="0.0.0.0" />
                <Input id="port" label="Port" v-model:value="data.port" placeholder="554" />
                <Input id="channel" label="Channel" v-model:value="data.channel" placeholder="1" />
            </div>
            <div class="flex gap-x-2">
                <Input id="subtype" label="Subtype" v-model:value="data.subType" placeholder="0" />
                <Input id="latitude" label="Latitude" v-model:value="data.latitude" placeholder="0" />
                <Input id="longitude" label="Longitude" v-model:value="data.longitude" placeholder="0" />
                <Input id="azimuth" label="Azimuth" v-model:value="data.azimuth" placeholder="0" />
            </div>
            <div class="flex gap-x-2">
                <Input id="thana" label="Thana" v-model:value="data.thana" placeholder="thana" />
                <Input id="status" label="Status" v-model:value="data.status" placeholder="active" />
            </div>
        </div>
        <div class="w-full flex gap-x-4">
            <button type="submit"
                class="py-2 px-5 text-sm bg-orange-500 hover:bg-orange-600 transition text-white rounded-md">Save</button>
            <button type="reset"
                class="py-2 px-5 text-sm bg-red-500 hover:bg-red-600 transition text-white rounded-md">Reset</button>
        </div>
        <v-snackbar v-model="snackbar" color="deep-purple-accent-4" elevation="24">
            {{ snackMesg }}
        </v-snackbar>
    </form>
</template>

<style scoped></style>