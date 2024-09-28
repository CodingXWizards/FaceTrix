import { createRouter, createWebHistory } from 'vue-router';
import { Component } from 'vue';

import Home from '@/pages/Home.vue';
import Login from '@/pages/Login.vue';
import Camera from '@/pages/Camera.vue';
import WhatsappBot from '@/pages/WhatsappBot.vue';
import Criminal from '@/pages/Criminal.vue';
import RealtimeTracking from './pages/RealtimeTracking.vue';

interface Routes {
    path: string;
    component: Component;
}

const routes: Routes[] = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/camera',
        component: Camera
    },
    {
        path: '/whatsapp-bot',
        component: WhatsappBot
      },
      {
        path: '/criminal',
      component: Criminal,
    },
    {
        path: '/realtime-tracking',
        component: RealtimeTracking
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;