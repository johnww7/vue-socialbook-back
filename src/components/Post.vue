<template>

<div class="bg-white shadow rounded-md  -mx-2 lg:mx-0">
    
    <!-- post header-->
    <div class="flex justify-between items-center px-4 py-3">
    <div class="flex flex-1 items-center space-x-4">
    
        <span class="block font-semibold "><a v-bind:href="'/profile/' + userFeed.user">@{{userFeed.user}}</a></span>
    </div>
    <div>
    <a href="#"> <i class="icon-feather-more-horizontal text-2xl hover:bg-gray-200 rounded-full p-2 transition -mr-1 "></i> </a>
    <div class="bg-white w-56 shadow-md mx-auto p-2 mt-12 rounded-md text-gray-500 hidden text-base border border-gray-100  " uk-drop="mode: hover;pos: top-right">

        <ul class="space-y-1">
        
            <li> 
                <a href="#" class="flex items-center px-3 py-2 text-red-500 hover:bg-red-100 hover:text-red-500 rounded-md ">
                <i class="uil-trash-alt mr-1"></i>  Delete Post
                </a> 
            </li>
        </ul>

    </div>
    </div>
    </div>

    <div uk-lightbox>
    <!--<a href="#">-->
    <a v-bind:href="'http://127.0.0.1:8000/' + userFeed.image"> 
        <img v-bind:src="'http://127.0.0.1:8000/' + userFeed.image" alt="">
    </a>
    </div>


    <div class="py-3 px-4 space-y-3"> 

    <div class="flex space-x-4 lg:font-bold">
        <a v-bind:href="'http://127.0.0.1:8000/like-post?post_id=' + userFeed.id" class="flex items-center space-x-2">
            <div class="p-2 rounded-full text-black">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" width="25" height="25" class="">
                    <path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z" />
                </svg>
             <!--   {% if post.no_of_likes == 0 %}
                <p>No likes</p>
                {% elif post.no_of_likes == 1 %}
                <p>Liked by {{post.no_of_likes}} person</p>
                {% else %}
                <p>Liked by {{post.no_of_likes}} people</p>
                {% endif %}-->
            </div>
            
        </a>

        <a v-bind:href="'http://127.0.0.1:8000/' + userFeed.image" class="flex items-center space-x-2 flex-1 justify-end" download>
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="25" height="25" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><g fill="currentColor"><path d="M8.5 1.5A1.5 1.5 0 0 1 10 0h4a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h6c-.314.418-.5.937-.5 1.5v6h-2a.5.5 0 0 0-.354.854l2.5 2.5a.5.5 0 0 0 .708 0l2.5-2.5A.5.5 0 0 0 10.5 7.5h-2v-6z"/></g></svg>
            
        </a>
    </div>


    <p>
        <!--<a href="/profile/{{post.user}}"><strong>{{userFeed.user}}</strong></a> {{userFeed.caption}}
        -->
        <router-link :to="{name: 'profile', params: {user_name: userFeed.user}}"><strong>{{userFeed.user}}</strong></router-link> {{userFeed.caption}}

    </p>



    </div>

</div>
                        
</template>

<script>
export default {
    name: 'Post',
    props: {
        userFeed: {
            type:Object
        }
    },
    mounted(){
        this.displayFeed()
    },
    methods: {
        displayFeed(){
            console.log("Whats in my userFeed: " + JSON.stringify(this.userFeed))
        }
    }

}
</script>