'use client';

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useParams } from "next/navigation";

interface User {
    id: number;
    name: string;
    email: string;
}
const UserProfile = () => {
    const [user, setUser] = useState<User | null>(null);
    const router = useRouter();
    // const params = useParams();
    const { userId } = useParams();

    useEffect(() => {
        const fetchUserProfile = async () => {
            if (!userId) return;

            const token = localStorage.getItem('token');
            if (!token) {
                console.error('No token found, redirect to login');
                router.push('/login');
                return;
            }

            const response = await fetch(`/api/${userId}`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                console.error("Failed to fetch user profile");
                router.push('/login');
            } else {
                const data = await response.json();
                setUser(data);
            }
        };

        fetchUserProfile();
    }, [userId]);

    if (!user) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Your Name: { user.name }</h1>
            <h1>Your Email: { user.email }</h1>
            <h1>Your ID: { user.id }</h1>
        </div>
    );
};

export default UserProfile;