<template>
<div id="body" class="bg-gray-100">
    <div id="wrapper" class="flex flex-col justify-between h-screen">

        <!-- header-->
        <div class="bg-white py-4 shadow dark:bg-gray-800">
            <div class="max-w-6xl mx-auto">


                <div class="flex items-center lg:justify-between justify-around">

                    <a href="trending.html">
                       <b><h1 style="font-size: 1.5rem;">Social book</h1></b>
                    </a>

                    <div class="capitalize flex font-semibold hidden lg:block my-2 space-x-3 text-center text-sm">

                        <router-link to="/Signup" class="bg-pink-500 pink-500 px-6 py-3 rounded-md shadow text-white">Register</router-link>
                    </div>

                </div>
            </div>
        </div>

        <!-- Content-->
        <div>
            <div class="lg:p-12 max-w-md max-w-xl lg:my-0 my-12 mx-auto p-6 space-y-">
                <h1 class="lg:text-3xl text-xl font-semibold  mb-6"> Log in</h1>
                <!-- 
                    loop for messages

                -->
                
                <form @submit.prevent="submitForm">
                    <input type="text" v-model="username" placeholder="Username" class="bg-gray-200 mb-2 shadow-none dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <input type="password" v-model="password" placeholder="password" class="bg-gray-200 mb-2 shadow-none dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <!--<div class="flex justify-between my-4">
                        <div class="checkbox">
                            <input type="checkbox" id="chekcbox1" checked>
                            <label for="chekcbox1"><span class="checkbox-icon"></span>Remember Me</label>
                        </div>
                        <a href="#"> Forgot Your Password? </a>
                    </div>-->
                    <button type="submit" class="bg-gradient-to-br from-pink-500 py-3 rounded-md text-white text-xl to-red-400 w-full">Logout</button>
                    <div class="text-center mt-5 space-x-2">
                        <p class="text-base"> Not registered? <a href="/" class=""> Create a account </a></p>
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
import {useAuthStore} from '@/stores/authStore.js'
//const store = useAuthStore()

export default {
    name: "Signin",
    data() {
        return {
            username: '',
            password: '',
            errors: [],
        }
    },
    setup(){
        const store = useAuthStore()
        return {store}
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password,
               // email: 'what@what.com',
            }
            console.log("whats form data: " + JSON.stringify(formData))
            await axios
                .post("http://127.0.0.1:8000/api/login/", formData)
                .then(response => {
                    const token = response.data.key
                    console.log('token: ' + JSON.stringify(token))
                    //this.store.setToken(token)
                    /*this.store.setToken(token)
                    console.log("whats store token: " + store.token)
                    */
                    console.log("component name: " + this.username)
                    this.store.setUser(this.username)
                    console.log(" whats user name: " + this.store.getUser)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    console.log("Token: " + localStorage.getItem("token"))
                    const toRedirect = this.$route.query.to || '/'
                    console.log("where am I going: " + toRedirect)
                    this.$router.push(toRedirect)
                })
                .catch(error => {
                    console.log("Whats main error: " + error)
                    if(error.response) {
                            for (const property in error.response.data){
                                this.errors.push(`${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response))
                        }
                        else if(error.message){
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }       
                })

        }

    }

}
/*
curl -XGET -H 'Authorization: Token 7237fd664685cea7149696041eaf8074e5335568' \
    -H "Content-type: application/json" 'http://localhost:8000/api/user/'

curl -XPOST -H "Content-type: application/json" -d '{
      "username": "william",
      "password": "complexpassword123"
  }' 'http://localhost:8000/api/login/'
*/
</script>

