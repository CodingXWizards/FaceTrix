import { User } from '@/types/user';
import { defineStore } from 'pinia';

interface AuthState {
    isAuthenticated: boolean;
    user: User | null;
};

export const useAuthStore = defineStore('auth', {
    state: (): AuthState => ({
        isAuthenticated: false,
        user: null
    }),
    actions: {
        login(user: User) {
            this.isAuthenticated = true;
            this.user = user;
        },
        logout() {
            this.isAuthenticated = false;
            this.user = null;
        }
    },
    getters: {
        isLoggedIn: (state) => state.isAuthenticated,
    },
})