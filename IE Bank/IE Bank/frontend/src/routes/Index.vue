<script setup>
import Button from '../components/Button.vue'
import Accounts from '../components/Accounts.vue';
import Functions from '../components/Functions.vue';
</script>

<template>
    <section class="bg-gray-900 text-white">
        <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
            <div class="mx-auto max-w-3xl text-center">
                <h1
                    class="text-5xl">
                    Welcome to Fintech.

                    <span class="sm:block">Your secure bank </span>
                </h1>

                <p class="mx-auto mt-4 max-w-xl sm:text-xl/relaxed">
                    Welcome to Fintech, your trusted partner for secure and reliable banking solutions.
                </p>

                <div class="mt-8 flex flex-wrap justify-center gap-4">
                    <Button title="Get started!" to="/register" />
                    <Button title="Login" to="/login" />
                </div>
            </div>
        </div>
    </section>
    
    <section>
        <Accounts />
    </section>
    <section>
        <div class="mt-8 flex flex-wrap justify-center gap-4">
            <Button title="Create Account" />
            <Button title="Edit an Account" />
            <Button title="Delete an Account" />
        </div>
    </section>
    <section>
        <Functions/>
    </section>
</template>
