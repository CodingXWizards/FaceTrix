import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/pages/Home.vue';
import Login from '@/pages/Login.vue';
import { Component } from 'vue';

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
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;