export interface Camera {
    id: string;
    username: string;
    ipAddress: string;
    password: string;
    port: number | null;
    channel: string;
    subType: string;
    latitude: number | null;
    longitude: number | null;
    azimuth: number | null;
    status: string;
    thana: string;
}