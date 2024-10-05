import { NextResponse } from "next/server";

interface Params {
    userId: string;
}
export async function GET(request: Request, { params }: { params: Params }) {
    const { userId } = params;

    const token = request.headers.get('Authorization');
    if (!token) {
        return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    try {
        const res = await fetch(`http://127.0.0.1:8000/profile${userId}`, {
            method: 'GET',
            headers: {
                'Authorization': token,
                'Content-Type': 'application/json',
            }

        });

        if (!res.ok) {
            throw new Error(res.statusText);
        }

        const data = await res.json();

        return NextResponse.json(data);
    } catch (error) {
        console.error('Error fetching user profile', error);
        return NextResponse.json({error:'Internal Server Error'}, {status:500})
    }

}