import { ref } from "vue";

interface FetchOptions {
    method?: string;
    headers?: HeadersInit;
    body?: BodyInit | null;
}

export function useFetch<T>(url: string, options?: FetchOptions) {
    const data = ref<T | null>(null);
    const error = ref<string | null>(null);
    const isLoading = ref<boolean>(false);

    const fetchData = async () => {
        isLoading.value = true;
        error.value = null;

        try {
            const response = await fetch(`http://localhost:8000${url}`, {
                method: options?.method || 'GET',
                credentials: 'include',
                headers: options?.headers || { 'Content-Type': 'application/json' },
                body: options?.body || null
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status} ${response.statusText}`);
            }

            const result = await response.json();
            data.value = result;
        } catch (err) {
            error.value = err instanceof Error ? err.message : 'Unknown error';
        } finally {
            isLoading.value = false;
        }
    };

    return { data, error, isLoading, fetchData };
};