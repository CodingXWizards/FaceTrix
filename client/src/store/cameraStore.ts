import { Camera } from "@/types/camera";
import { defineStore } from "pinia";

interface CameraState {
    isLoading: boolean;
    error: string | null;
    cameras: Camera[] | null;
};

export const useCameraStore = defineStore('camera', {
    state: (): CameraState => ({
        isLoading: false,
        error: null,
        cameras: null
    }),
    actions: {
        async fetchAllCameras() {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await fetch('http://localhost:8000/api/camera/', { method: 'GET', credentials: 'include' });
                const data = await response.json();
                if (response.status !== 200) {
                    throw Error("Something went wrong");
                }
                this.cameras = data.value;
            } catch (error: any) {
                this.error = error.message;
            } finally {
                this.isLoading = false;
            }
        }
    }
});