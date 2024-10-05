import { ReactNode } from "react";
import {
    FormControl,
    FormLabel,
    FormErrorMessage,
    FormHelperText,
    Input,
} from '@chakra-ui/react';
import Image from "next/image";
import banner from '@/public/images/pic1.png'

export default function AuthLayout({ children }: { children: ReactNode }) {
    return (
        <div className="auth-layout flex flex-col justify-center items-center h-[100%] w-[100%] bg-teal-500">
            <div className="h-[600px] w-[1000px] flex justify-center items-center bg-white rounded-lg">
                <div className='w-[60%] flex flex-col items-center gap-[15px]'>
                    {children}
                </div>

                <div className='w-[40%] h-[100%] flex'>
                    <Image className='bg-cover bg-no-repeat bg-center rounded-r-lg' src={ banner } alt="logo" priority={ true } />

                </div>

            </div>          
        </div>
    );
}
