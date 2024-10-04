'use client';

import React, { ButtonHTMLAttributes, ChangeEvent, FormEvent } from 'react';
import {
    FormControl,
    FormLabel,
    FormErrorMessage,
    FormHelperText,
    Input,
    Button,
} from '@chakra-ui/react'
import { useState } from 'react';

interface FormData {
    name_or_email: string;
    password: string;
}

const LoginPage = () => {

    const [formData, setFormData] = useState<FormData>({ name_or_email: '', password: '' });

    const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value })
    };

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        console.log(formData)

        if (response.ok) {
            const data = await response.json();
            console.log('Login successful', data);
            setFormData({ name_or_email: '', password: '' });
        } else {
            console.error('Login failed');
        }
    };

    return (
        // <div>
        <form className='w-[100%] h-[80%] px-[5px]' onSubmit={handleSubmit} >
            
            <div className='w-[100%] h-[100%] flex flex-col justify-between items-center gap-[15px] p-[10px]'>
                <p className='font-medium'> Login Here </p>
                    <FormControl isInvalid={ false } >
                    <FormLabel fontSize="small"> Username / Email </FormLabel>
                    <Input type='text'
                        name='name_or_email'
                        value={formData.name_or_email}
                        onChange={ handleInputChange} />
                        
                    </FormControl>

                    <FormControl isInvalid={ false }>
                    <FormLabel fontSize="small"> Password  </FormLabel>
                    <Input type='password'
                        name='password'
                        value={ formData.password }
                        onChange={ handleInputChange} />
                    
                       
                </FormControl>
                
                <Button colorScheme='teal' type='submit'> Sign In</Button>
                </div>
            </form>
        // </div>
    );
};

export default LoginPage;