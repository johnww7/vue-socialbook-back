<template>
<div class="container m-auto"> 

    <h1 class="text-2xl leading-none text-gray-900 tracking-tight mt-3"> / Account Setting for</h1>
    <!--<ul class="mt-5 -mr-3 flex-nowrap lg:overflow-hidden overflow-x-scroll uk-tab">
        <li class="uk-active"><a href="#">General</a></li>
        <li><a href="#">Profile</a></li>
        <li><a href="#">Privacy</a></li>
        <li><a href="#">Notification</a></li>
        <li><a href="#">Social links</a></li>
        <li><a href="#">Billing</a></li>
        <li><a href="#">Security</a></li>
    </ul>-->

    <div class="grid lg:grid-cols-3 mt-12 gap-8">
        <div>
            <h3 class="text-xl mb-2"> Basic</h3>
            <p></p>
        </div>
        <div class="bg-white rounded-md lg:shadow-lg shadow col-span-2">
          <!-- Form here -->  
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <div class="grid grid-cols-2 gap-3 lg:p-6 p-4">
                
                <div class="col-span-2">
                    <label for=""> Profile Image</label>
                    <img width="100" height="100" v-bind:src="profile.image" />
                    <!--<input type="file" name="image" value="" class="shadow-none bg-gray-100">-->
                    <input v-on:change="getUploadImage" type="file" id="image_upload">
                </div>

                <div class="col-span-2">
                    <label for="about">Bio</label>  
                    <textarea id="about" v-model="bio" name="bio" rows="3"  class="shadow-none bg-gray-100"></textarea>
                </div> 
                <div class="col-span-2">
                    <label for="location"> Location</label>
                    <input type="text" v-model="location" name="location"  class="shadow-none bg-gray-100">
                </div>
                
                
            </div> 

            <div class="bg-gray-10 p-6 pt-0 flex justify-end space-x-3">
                <button class="p-2 px-4 rounded bg-gray-50 text-red-500"> Cancel </button>
                <button type="submit" class="button bg-blue-700"> Save </button>
            </div>
        </form>    
        </div>

 <!--       <div>
            <h3 class="text-xl mb-2"> Privacy</h3>
            <p> </p>
        </div>
        <div class="bg-white rounded-md lg:shadow-lg shadow lg:p-6 p-4 col-span-2">

        <div class="space-y-3">
            <div class="flex justify-between items-center">
                <div>
                    <h4> Who can follow me ?</h4>
                    <div>  </div>
                </div>
                <div class="switches-list -mt-8 is-large">
                    <div class="switch-container">
                        <label class="switch"><input type="checkbox"><span class="switch-button"></span> </label>
                    </div>
                </div>
            </div>
            <hr>
            <div class="flex justify-between items-center">
                <div>
                    <h4> Show my activities ?</h4>
                    <div>  </div>
                </div>
                <div class="switches-list -mt-8 is-large">
                    <div class="switch-container">
                        <label class="switch"><input type="checkbox" checked><span class="switch-button"></span> </label>
                    </div>
                </div>
            </div>
            <hr>
            <div class="flex justify-between items-center">
                <div>
                    <h4> Search engines?</h4>
                    <div>  </div>
                </div>
                <div class="switches-list -mt-8 is-large">
                    <div class="switch-container">
                        <label class="switch"><input type="checkbox"><span class="switch-button"></span> </label>
                    </div>
                </div>
            </div>
            <hr>
            <div class="flex justify-between items-center">
                <div>
                    <h4> Allow Commenting?</h4>
                    <div>  </div>
                </div>
                <div class="switches-list -mt-8 is-large">
                    <div class="switch-container">
                        <label class="switch"><input type="checkbox"><span class="switch-button"></span> </label>
                    </div>
                </div>
            </div>
        </div>-->

        </div>
        <br>

    

</div>
        
  
</template>

<script>
import axios from 'axios'
import {useAuthStore} from '/src/stores/authStore.js'
import {mapState} from 'pinia'

export default {
    name: 'Settings', 
    data() {
        return {
            image: '',
            bio: '',
            location: '',
            profile:[]
        }
    }, 
    computed: {
        ...mapState(useAuthStore, ['getToken']),
    },
    mounted() {
        this.getSettings()
    },
    methods: {
         getUploadImage(event) {
            //const myImageInput = ref(null)
            const file = event.target.files[0]
            //myImageInput.value = file[0]
            this.image = file
        },
        /*submitForm() {
            const formData = {
                image: this.image,
                bio: this.bio,
                location: this.location
            } 
        },*/
        async getSettings() {
            await axios
                .get('http://127.0.0.1:8000/api/settings')
                .then(response => {
                    this.profile = response
                    console.log("whats profile: " + JSON.stringify(this.profile))

                })
                .catch(error => {
                    console.log("errors: " + error)
                    //console.error(error.response.data)
                })

        }
    }
}
</script>