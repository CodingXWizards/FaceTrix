<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Navbar from '@/components/Navbar.vue';
import { useFetch } from '@/composables/useFetch';

interface Criminal {
  id: string;
  criminalname: string;
  crimes: string;
  date: string;
  time: string;
  location: string;
  cameraid: number;
  thana: string;
  images: string;
}

const { data: criminals, isLoading, fetchData } = useFetch<Criminal[]>('/api/criminal/', { method: 'GET' });

const newCriminal = ref({
  criminalname: '',
  crimes: '',
  date: '',
  time: '',
  location: '',
  cameraid: 0,
  thana: '',
  image: null as File | null,
});

const errorMessage = ref('');
const successMessage = ref('');

onMounted(() => {
  fetchData();
});

async function handleSubmit() {
  errorMessage.value = '';
  successMessage.value = '';

  const formData = new FormData();
  for (const [key, value] of Object.entries(newCriminal.value)) {
    if (key === 'image' && value instanceof File) {
      formData.append(key, value);
    } else if (value !== null) {
      formData.append(key, value.toString());
    }
  }

  try {
    const response = await fetch('http://localhost:8000/api/criminal/', {
      method: 'POST',
      body: formData,
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Failed to add criminal');
    }

    successMessage.value = 'Criminal added successfully';
    fetchData(); // Refresh the list of criminals
    // Reset form
    newCriminal.value = {
      criminalname: '',
      crimes: '',
      date: '',
      time: '',
      location: '',
      cameraid: 0,
      thana: '',
      image: null,
    };
  } catch (error) {
    errorMessage.value = 'Failed to add criminal';
    console.error(error);
  }
}

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement;
  if (target.files) {
    newCriminal.value.image = target.files[0];
  }
}
</script>

<template>
  <main class="min-h-screen flex flex-col bg-gray-100">
    <Navbar />
    <section class="p-6">
      <h2 class="text-2xl font-bold mb-6">Criminal Management</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Add Criminal Form -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-xl font-semibold mb-4">Add New Criminal</h3>
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div>
              <label for="criminalname" class="block mb-1">Name</label>
              <input v-model="newCriminal.criminalname" id="criminalname" type="text" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="crimes" class="block mb-1">Crimes</label>
              <input v-model="newCriminal.crimes" id="crimes" type="text" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="date" class="block mb-1">Date</label>
              <input v-model="newCriminal.date" id="date" type="date" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="time" class="block mb-1">Time</label>
              <input v-model="newCriminal.time" id="time" type="time" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="location" class="block mb-1">Location</label>
              <input v-model="newCriminal.location" id="location" type="text" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="cameraid" class="block mb-1">Camera ID</label>
              <input v-model.number="newCriminal.cameraid" id="cameraid" type="number" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="thana" class="block mb-1">Thana</label>
              <input v-model="newCriminal.thana" id="thana" type="text" required class="w-full p-2 border rounded">
            </div>
            <div>
              <label for="image" class="block mb-1">Image</label>
              <input @change="handleFileChange" id="image" type="file" accept="image/*" required class="w-full p-2 border rounded">
            </div>
            <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">Add Criminal</button>
          </form>
          <p v-if="errorMessage" class="text-red-500 mt-2">{{ errorMessage }}</p>
          <p v-if="successMessage" class="text-green-500 mt-2">{{ successMessage }}</p>
        </div>
        
        <!-- View Criminals -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-xl font-semibold mb-4">View Criminals</h3>
          <div v-if="isLoading">Loading...</div>
          <div v-else-if="criminals && criminals.length > 0" class="space-y-4">
            <div v-for="criminal in criminals" :key="criminal.id" class="border p-4 rounded">
              <img :src="'http://localhost:8000/' + criminal.images" :alt="criminal.criminalname" class="w-full h-40 object-cover mb-2 rounded">
              <h4 class="font-semibold">{{ criminal.criminalname }}</h4>
              <p><strong>Crimes:</strong> {{ criminal.crimes }}</p>
              <p><strong>Date:</strong> {{ criminal.date }}</p>
              <p><strong>Time:</strong> {{ criminal.time }}</p>
              <p><strong>Location:</strong> {{ criminal.location }}</p>
              <p><strong>Camera ID:</strong> {{ criminal.cameraid }}</p>
              <p><strong>Thana:</strong> {{ criminal.thana }}</p>
            </div>
          </div>
          <div v-else>No criminals found.</div>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
/* Add any additional styles here */
</style>