<script setup lang="ts">
import './camera.css';

const data: {
    id: number,
    ip: string;
    port: number;
    gr: string;
    azimuth: number,
    thana: string
}[] = [
        { id: 1, ip: '0.0.0.0', port: 545, gr: '21, 81', azimuth: 80, thana: 'Bhilai' },
        { id: 1, ip: '0.0.0.0', port: 545, gr: '21, 81', azimuth: 80, thana: 'Bhilai' },
        { id: 1, ip: '0.0.0.0', port: 545, gr: '21, 81', azimuth: 80, thana: 'Bhilai' },
        { id: 1, ip: '0.0.0.0', port: 545, gr: '21, 81', azimuth: 80, thana: 'Bhilai' },
        { id: 1, ip: '0.0.0.0', port: 545, gr: '21, 81', azimuth: 80, thana: 'Bhilai' },
        { id: 1, ip: '0.0.0.0', port: 545, gr: '21, 81', azimuth: 80, thana: 'Bhilai' },
    ]

</script>

<template>
    <form>
        <h3>All Camera</h3>
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>IP</th>
                    <th>Port</th>
                    <th>GR</th>
                    <th>Azimuth</th>
                    <th>Thana</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ele in data" :key="ele.id">
                    <td>{{ ele.id }}</td>
                    <td>{{ ele.ip }}</td>
                    <td>{{ ele.port }}</td>
                    <td>{{ ele.gr }}</td>
                    <td>{{ ele.azimuth }}</td>
                    <td>{{ ele.thana }}</td>
                </tr>
            </tbody>
        </table>
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
    @apply p-1.5 text-center rounded-md text-gray-700
}

th {
    @apply font-medium text-gray-900
}
</style>