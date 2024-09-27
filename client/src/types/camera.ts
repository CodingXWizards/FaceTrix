export enum Status{
    ACTIVE = 'ACTIVE',
    INACTIVE = 'INACTIVE'
}

export interface Camera {
    id: string;
    username: string;
    ipAddress: string;
    password: string;
    port: number;
    channel: number;
    subType: number;
    latitude: number;
    longitude: number;
    azimuth: number;
    status: Status;
    thana: string;
}