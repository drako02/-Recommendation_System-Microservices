import { NextResponse } from "next/server";

export async function POST(request:Request) {
    try {
        // const { name_or_email, password } = await request.json();

        const res = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify(await request.json())
            
        });

        if (!res.ok) {
            throw new Error('Failed to send data')
        }

        const data = await res.json();
        console.log('Response fromBackend:', data)

        return NextResponse.json({ status: 'success' }, { status: 200 });

        // console.log("Received form data: ", { name_or_email, password });

        // return NextResponse.json
    } catch (error) {
        console.error('Error processinf submission:', error);
        return NextResponse.json({ status: 'error', message: 'Form submission failed' }, { status: 500 });

    }
}