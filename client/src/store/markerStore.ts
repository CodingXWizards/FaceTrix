import { Marker } from "@/types/marker";
import { defineStore } from "pinia";

interface MarkerState {
    markers: Marker[];
};

export const useMarkerStore = defineStore('marker', {
    state: (): MarkerState => ({
        markers: []
    }),
    actions: {
        setMarkers(markers: Marker[]) {
            this.markers = markers;
        }
    }
});