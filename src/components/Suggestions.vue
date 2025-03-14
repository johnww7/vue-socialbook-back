<template>
<div class="flex items-center justify-between py-3">
    <div class="flex flex-1 items-center space-x-4">
        <router-link :to="{name: 'profile', params: {user_name: suggestionsUserList.user.username}}">
        <!--<a href="#">-->
            <img v-bind:src="'http://127.0.0.1:8000/' + suggestionsUserList.profileimg" class="bg-gray-200 rounded-full w-10 h-10">
        <!--</a>-->
        </router-link>
        <div class="flex flex-col">
            <span  class="block capitalize font-semibold"> {{suggestionsUserList.user.username}} </span>
            <span class="block capitalize text-sm"> {{suggestionsUserList.bio}} </span>
        </div>
    </div>

    <!--<a href="#" class="border border-gray-200 font-semibold px-4 py-1 rounded-full hover:bg-pink-600 hover:text-white hover:border-pink-600 "> Follow </a>-->
    <router-link :to="{name: 'profile', params: {user_name: suggestionsUserList.user.username}}">
        <p class="border border-gray-200 font-semibold px-4 py-1 rounded-full hover:bg-pink-600 hover:text-white hover:border-pink-600 "> Follow </p>

    </router-link> 
</div>
</template>

<script>
export default {
    name: 'Suggestions',
    props: {
        suggestionsUserList: {
            type:Object
        }
    }
}
</script>