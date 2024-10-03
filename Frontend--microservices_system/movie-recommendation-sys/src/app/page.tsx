'use client';

import React from "react";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

const HomePage = () => {
    const router = useRouter();

    useEffect(() => {
        router.push("/login");
    },[router])

    return null;
}

export default HomePage;