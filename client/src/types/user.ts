export enum UserType {
    BASIC = "BASIC",
    ADMIN = "ADMIN",
    SUPER = "SUPER"
}

export interface User {
    id: string;
    user_type: UserType;
    name: string;
    email: string;
    phoneNumber: string;
    designation: string;
}