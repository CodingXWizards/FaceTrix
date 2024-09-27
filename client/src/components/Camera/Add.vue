<script setup lang="ts">
import { reactive, ref } from 'vue';
import Input from '../Input.vue';
import { Camera, Status } from '@/types/camera';
import { watch } from 'vue';
import { useLoading } from '@/composables/useLoading';
import { LucideLoader2 } from 'lucide-vue-next';

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
    status: Status.ACTIVE,
    thana: "",
});

const snackMesg = ref<string>("");
const snackbar = ref<boolean>(false);
const type = ref<'RTSP' | 'IP'>('RTSP');

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
            console.log(data.status)
            const response = await fetch("http://localhost:8000/api/camera", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    ip_address: data.ipAddress,
                    cam_type: type.value,
                    username: (type.value === 'RTSP' ? data.username : null),
                    password: (type.value === 'RTSP' ? data.password : null),
                    port: data.port,
                    channel: (type.value === 'RTSP' ? data.channel : null),
                    subtype: (type.value === 'RTSP' ? data.subType : null),
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
            data.status = Status.ACTIVE;
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
    data.status = Status.ACTIVE;
    data.thana = "";
}

</script>

<template>
    <form @submit="handleSubmit" @reset="handleReset">
        <header class="flex justify-between items-center gap-x-5">
            <h3>Add Camera</h3>
            <div class="w-[160px] flex items-center">
                <v-select :items="['RTSP', 'IP']" class="h-[40px]" density="compact" variant="outlined"
                    label="Select Format" v-model:model-value="type"></v-select>
            </div>
        </header>
        <div class="flex flex-col gap-y-3">
            <div class="flex gap-x-2" v-if="type === 'RTSP'">
                <Input id="username" label="Username" v-model:value="data.username" placeholder="username" />
                <Input id="password" label="Password" v-model:value="data.password" placeholder="password" />
            </div>
            <div class="flex gap-x-2">
                <Input id="ip" label="IP Address" v-model:value="data.ipAddress" placeholder="0.0.0.0" />
                <Input id="port" label="Port" v-model:value="data.port" placeholder="554" />
                <Input v-if="type === 'RTSP'" id="channel" label="Channel" v-model:value="data.channel"
                    placeholder="1" />
            </div>
            <div class="flex gap-x-2">
                <Input v-if="type === 'RTSP'" id="subtype" label="Subtype" v-model:value="data.subType"
                    placeholder="0" />
                <Input id="latitude" label="Latitude" v-model:value="data.latitude" placeholder="0" />
                <Input id="longitude" label="Longitude" v-model:value="data.longitude" placeholder="0" />
                <Input id="azimuth" label="Azimuth" v-model:value="data.azimuth" placeholder="0" />
            </div>
            <div class="flex gap-x-2">
                <Input id="thana" label="Thana" v-model:value="data.thana" placeholder="thana" />
                <div class="w-full flex flex-col">
                    <label for="status">Status</label>
                    <select name="status" id="status"
                        @change="(e: Event) => data.status = (e.target as HTMLSelectElement).value as Status"
                        style="border-color: #9ca3af !important;"
                        class="w-full mt-1 p-2 border rounded-lg focus:outline-none focus:border-orange-500">
                        <option value="ACTIVE">ACTIVE</option>
                        <option value="INACTIVE">INACTIVE</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="w-full flex gap-x-4">
            <button type="submit"
                class="py-2 px-5 text-sm bg-orange-500 hover:bg-orange-600 transition text-white rounded-md">
                <LucideLoader2 v-if="loading" class="size-5 animate-spin mx-auto" />
                <span v-else>Save</span>
            </button>
            <button type="reset"
                class="py-2 px-5 text-sm bg-red-500 hover:bg-red-600 transition text-white rounded-md">Reset</button>
        </div>
        <v-snackbar v-model="snackbar" color="deep-purple-accent-4" elevation="24">
            {{ snackMesg }}
        </v-snackbar>
    </form>
</template>

<style scoped></style>