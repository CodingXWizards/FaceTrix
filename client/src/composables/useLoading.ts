// composables/useLoading.ts
import { ref } from "vue";

export function useLoading() {
    // Reactive loading state
    const loading = ref(false);

    // Function to wrap async operations
    const withLoading = async (asyncFunc: () => Promise<any>) => {
        loading.value = true;
        try {
            await asyncFunc();
        } finally {
            loading.value = false;
        }
    };

    return {
        loading,
        withLoading,
    };
};