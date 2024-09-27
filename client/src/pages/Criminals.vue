<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { LucideEye, LucidePlus, LucideLoader2 } from 'lucide-vue-next';
import Navbar from '@/components/Navbar.vue';
import { useLoading } from '@/composables/useLoading';

interface Criminal {
  id: string;
  criminalname: string;
  crimes: number;
  date: string;
  time: string;
  location: string;
  cameraid: number;
  thana: string;
  images: string;
}

const activeSection = ref<'VIEW' | 'ADD'>('VIEW');
const criminals = ref<Criminal[]>([]);
const newCriminal = ref<Omit<Criminal, 'id'>>({
  criminalname: '',
  crimes: 0,
  date: '',
  time: '',
  location: '',
  cameraid: 0,
  thana: '',
  images: '',
});

const { loading: loadingCriminals, withLoading: withLoadingCriminals } = useLoading();
const { loading: loadingAdd, withLoading: withLoadingAdd } = useLoading();

onMounted(() => {
  fetchCriminals();
});

async function fetchCriminals() {
  await withLoadingCriminals(async () => {
    try {
      const response = await fetch('http://localhost:8000/api/criminals', {
        method: 'GET',
        credentials: 'include',
      });
      if (!response.ok) throw new Error('Failed to fetch criminals');
      criminals.value = await response.json();
    } catch (error) {
      console.error('Error fetching criminals:', error);
    }
  });
}

async function addCriminal() {
  await withLoadingAdd(async () => {
    try {
      const response = await fetch('http://localhost:8000/api/criminals', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newCriminal.value),
      });
      if (!response.ok) throw new Error('Failed to add criminal');
      await fetchCriminals();
      activeSection.value = 'VIEW';
      // Reset form
      newCriminal.value = {
        criminalname: '',
        crimes: 0,
        date: '',
        time: '',
        location: '',
        cameraid: 0,
        thana: '',
        images: '',
      };
    } catch (error) {
      console.error('Error adding criminal:', error);
    }
  });
}
</script>

<template>
  <main class="h-screen flex flex-col">
    <Navbar />
    <div class="flex-grow px-10 py-5 flex flex-col gap-y-4 bg-gray-100">
      <header class="flex justify-between items-center">
        <h2 class="text-2xl font-bold">Criminals</h2>
        <div class="flex gap-x-4">
          <LucidePlus @click="activeSection = 'ADD'"
            :class="'p-2 size-9 text-white rounded-md cursor-pointer ' + (activeSection === 'ADD' ? 'bg-gray-800 hover:bg-opacity-100' : 'bg-orange-600 hover:bg-opacity-90')" />
          <LucideEye @click="activeSection = 'VIEW'"
            :class="'p-2 size-9 text-white rounded-md cursor-pointer ' + (activeSection === 'VIEW' ? 'bg-gray-800 hover:bg-opacity-100' : 'bg-orange-600 hover:bg-opacity-90')" />
        </div>
      </header>

      <section v-if="activeSection === 'ADD'" class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-xl font-semibold mb-4">Add New Criminal</h3>
        <form @submit.prevent="addCriminal" class="grid grid-cols-2 gap-4">
          <div>
            <label class="block mb-1">Name</label>
            <input v-model="newCriminal.criminalname" type="text" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Crimes</label>
            <input v-model="newCriminal.crimes" type="number" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Date</label>
            <input v-model="newCriminal.date" type="date" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Time</label>
            <input v-model="newCriminal.time" type="time" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Location</label>
            <input v-model="newCriminal.location" type="text" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Camera ID</label>
            <input v-model="newCriminal.cameraid" type="number" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Thana</label>
            <input v-model="newCriminal.thana" type="text" required class="w-full p-2 border rounded">
          </div>
          <div>
            <label class="block mb-1">Images</label>
            <input v-model="newCriminal.images" type="text" required class="w-full p-2 border rounded">
          </div>
          <button type="submit" class="col-span-2 bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition-colors">
            <LucideLoader2 v-if="loadingAdd" class="size-5 animate-spin mx-auto" />
            <span v-else>Add Criminal</span>
          </button>
        </form>
      </section>

      <section v-else class="bg-white p-6 rounded-lg shadow-md overflow-x-auto">
        <h3 class="text-xl font-semibold mb-4">View Criminals</h3>
        <div v-if="loadingCriminals" class="flex justify-center items-center h-32">
          <LucideLoader2 class="size-8 animate-spin text-blue-600" />
        </div>
        <table v-else class="w-full">
          <thead>
            <tr class="bg-gray-100">
              <th class="p-2 text-left">Name</th>
              <th class="p-2 text-left">Crimes</th>
              <th class="p-2 text-left">Date</th>
              <th class="p-2 text-left">Time</th>
              <th class="p-2 text-left">Location</th>
              <th class="p-2 text-left">Camera ID</th>
              <th class="p-2 text-left">Thana</th>
              <th class="p-2 text-left">Images</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="criminal in criminals" :key="criminal.id" class="border-b">
              <td class="p-2">{{ criminal.criminalname }}</td>
              <td class="p-2">{{ criminal.crimes }}</td>
              <td class="p-2">{{ criminal.date }}</td>
              <td class="p-2">{{ criminal.time }}</td>
              <td class="p-2">{{ criminal.location }}</td>
              <td class="p-2">{{ criminal.cameraid }}</td>
              <td class="p-2">{{ criminal.thana }}</td>
              <td class="p-2">{{ criminal.images }}</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  </main>
</template>

<style scoped>
/* Add any additional styles here if needed */
</style>