import { NextResponse } from "next/server";

interface FormData {
    name: string;
    email: string;
    password: string;
}
export async function POST(request: Request) {
    const { name, email, password } = await request.json();
    const formData: FormData = { name, email, password };
    
    try {
        const res = await fetch('http://127.0.0.1:8000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),

        });
        
        if (!res.ok) {
            throw new Error("Failed to send formData to backend");
        }

        const data = await res.json();
        console.log("Response from backend", data);

        return NextResponse.json({ status: "Success" }, { status: 200 });

    } catch (error) {
        console.error("Error sending formData to backend", error);
        return NextResponse.json({ status: 'error', message: 'Form submission failed' }, { status: 500 });
    }

}