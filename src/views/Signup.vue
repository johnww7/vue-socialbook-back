<template>
    <div id="body" class="bg-gray-100">
        <div id="wrapper" class="flex flex-col justify-between h-screen">

        <!-- header-->
        <div class="bg-white py-4 shadow dark:bg-gray-800">
            <div class="max-w-6xl mx-auto">


                <div class="flex items-center lg:justify-between justify-around">

                    <a href="trending.html">
                        <b><h1 style="font-size: 1.5rem;">Social Book</h1></b>
                    </a>

                    <div class="capitalize flex font-semibold hidden lg:block my-2 space-x-3 text-center text-sm">
                        
                        <a href="/" class="bg-pink-500 pink-500 px-6 py-3 rounded-md shadow text-white">Login</a>
                    </div>

                </div>
            </div>
        </div>

        <!-- Content-->

        <div>
            <div class="lg:p-12 max-w-md max-w-xl lg:my-0 my-12 mx-auto p-6 space-y-">
                <h1 class="lg:text-3xl text-xl font-semibold mb-6"> Sign up</h1>
                <!--<p class="mb-2 text-black text-lg"> Register to manage your account </p>-->
                <!-- 

                    Loop for messages
                -->
                
                <form @submit.prevent="submitForm">
                    <!--<div class="flex lg:flex-row flex-col lg:space-x-2">
                        <input type="text" placeholder="First Name"  class="bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                        <input type="text" placeholder="Last Name" class="bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    </div>-->
                    <input type="text" name="username" v-model="username" placeholder="Username" class="bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <input type="email" name="email" v-model="email" placeholder="Email" class="bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <input type="password" name="password" v-model="password1" placeholder="Password" class="bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <input type="password" name="password2" v-model="password2" placeholder="Confirm Password" class="bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <!--<div class="flex justify-start my-4 space-x-1">
                        <div class="checkbox">
                            <input type="checkbox" id="chekcbox1" checked>
                            <label for="chekcbox1"><span class="checkbox-icon"></span> I Agree</label>
                        </div>
                        <a href="#"> Terms and Conditions</a>
                    </div> -->
                    <button type="submit" class="bg-gradient-to-br from-pink-500 py-3 rounded-md text-white text-xl to-red-400 w-full">Register</button>
                    <div class="text-center mt-5 space-x-2">
                        <p class="text-base"> Do you have an account? <router-link to="/Signin"> Login</router-link></p>
                    </div>
                </form>
            </div>
        </div>
        
        <!-- Footer -->

        <div class="lg:mb-5 py-3 uk-link-reset">
            <div class="flex flex-col items-center justify-between lg:flex-row max-w-6xl mx-auto lg:space-y-0 space-y-3">
                <div class="flex space-x-2 text-gray-700 uppercase">
                    <a href="#"> About</a>
                    <a href="#"> Help</a>
                    <a href="#"> Terms</a>
                    <a href="#"> Privacy</a>
                </div>
                <p class="capitalize"> © copyright 2020 by socol</p>
            </div>
        </div>

    </div> 

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Signup",
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            email:'',
            errors: [],
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email === '') {
                this.errors.push('This field is required')
            }
            if(this.password1 === '') {
                this.errors.push('This field is required')
            }
            if(this.password2 === '') {
                this.errors.push('This field is required')
            }
            let passwordLength = this.password1.length
            if(passwordLength < 8) {
                this.errors.push('Password must be greater than 8 characters')
            }
            if(this.password1 !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }

            console.log("whats errors: " + this.errors)

            if(!this.errors.length) {
                const formData = {
                    username: this.username,
                    email: this.email,
                    password1: this.password1,
                    password2: this.password2
                }

                console.log("whats form data: " + JSON.stringify(formData))

                axios
                    .post("http://127.0.0.1:8000/api/register/", formData)
                    .then(response => {
                        console.log("Whats resposne: " + JSON.stringify(response))
                        this.$router.push('/settings')
                    })
                    .catch(error => {
                        if(error.response) {
                            for (const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        }
                        else if(error.message){
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })

            }


        }
    }
}
</script>