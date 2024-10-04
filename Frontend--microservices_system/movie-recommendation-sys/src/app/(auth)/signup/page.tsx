'use client';

import { Button, FormControl, FormLabel, Input } from "@chakra-ui/react";
import Link from "next/link";
import React, { FormEvent, useState } from "react";
import { Interface } from "readline";

interface FormData {
    name: string;
    email: string;
    password: string;
}

const SignupPage = () => {

    const [formData, setFormData] = useState<FormData>({ name: '', email: '', password: '' });

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        try {
            const response = await fetch('/api/signup', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
                
            });
            
            if (response.ok) {
                const data = await response.json();
                console.log("Account created successfully", data);
            } else {
                console.error("Error creating account", response.status);
            }
        }

        catch (error) { 
            console.error("***", error);
        };
     };

    return (
        <>
            <form className='w-[100%] h-[80%] px-[5px]' onSubmit={handleSubmit}>

                <div className='w-[100%] h-[100%] flex flex-col justify-between items-center gap-[15px] p-[10px]'>
                    <p className='font-medium'> Create an account for free </p>
                    <FormControl isInvalid={ false } >
                        <FormLabel fontSize="small"> Name </FormLabel>
                        <Input type='text'
                            value={ formData.name }
                            name="name"
                            onChange={handleInputChange}
                        />

                    </FormControl>

                    <FormControl isInvalid={ false } >
                        <FormLabel fontSize="small"> Email </FormLabel>
                        <Input type='email'
                            // required
                            value={ formData.email }
                            name="email"
                            onChange={ handleInputChange }
                        />

                    </FormControl>

                    <FormControl isInvalid={ false }>
                        <FormLabel fontSize="small"> Password  </FormLabel>
                        <Input
                            type="password"
                            value={ formData.password }
                            name="password"
                            onChange={ handleInputChange }
                        />


                    </FormControl>

                    <Button colorScheme='teal' type='submit'> Sign Up</Button>
                </div>
            </form>
            <Link href="/login" className="underline text-[14px] text-gray-500 "> Already have an account? Sign in here </Link>
        </>
    )
}

export default SignupPage;