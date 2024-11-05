<template>
<div class="theme-layout">
	
	<section>
			<div class="feature-photo">
				<figure><img v-bind:src="'/src/assets/images/resources/timeline1.jpg'" alt=""></figure>
				<!--<form @submit.prevent="submitForm">
                    <input type="text" v-model="username" placeholder="Username" class="bg-gray-200 mb-2 shadow-none dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <input type="password" v-model="password" placeholder="password" class="bg-gray-200 mb-2 shadow-none dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;">
                    <div class="flex justify-between my-4">
                        <div class="checkbox">
                            <input type="checkbox" id="chekcbox1" checked>
                            <label for="chekcbox1"><span class="checkbox-icon"></span>Remember Me</label>
                        </div>
                        <a href="#"> Forgot Your Password? </a>
                    </div>
                    <button type="submit" class="bg-gradient-to-br from-pink-500 py-3 rounded-md text-white text-xl to-red-400 w-full">Logout</button>
                    <div class="text-center mt-5 space-x-2">
                        <p class="text-base"> Not registered? <a href="/" class=""> Create a account </a></p>
                    </div>
                </form>-->
				
				<form @submit.prevent="updateFollowing">
					<div class="add-btn">
					<span style="color: white; font-size: 27px; margin-right: 520px;"><b><u><a href="/">Home</a></u></b></span>
					
					<span v-if="lengthOfUserPost = 0" style="color: white; font-size: 27px;"><b>No Post</b></span>
					<span v-else-if="lengthOfUserPost = 1" style="color: white; font-size: 27px;"><b>{{lengthOfUserPost}} Post</b></span>
					<span v-else style="color: white; font-size: 27px;"><b>{{lengthOfUserPost}} Posts</b></span>

					
					<span style="color: white; font-size: 27px;"><b>1.7m followers</b></span>
					
					<span style="color: white; font-size: 27px;"><b>3.5k following</b></span>
					

					<a href="" title="" data-ripple=""><button style="background-color: #ffc0cb; border: #ffc0cb;">Follow</button></a>
					
					</div>
				</form>

				<!-- <form class="edit-phto">
					<i class="fa fa-camera-retro"></i>
					<label class="fileContainer">
						Upload Cover Photo
					<input type="file"/>
					</label>
				</form> -->
				<div class="container-fluid">
					<div class="row merged">
						<div class="col-lg-2 col-sm-3">
							<div class="user-avatar">
								<figure>
									        

									<img v-bind:src="'http://127.0.0.1:8000/' + userProfile.profileimage" v-bind:style="'height:250px; width: 100px;'" alt="">
								<!--	<form class="edit-phto">
										<i class="fa fa-camera-retro"></i>
										<label class="fileContainer">
											<a href="#account-settings">Upload Profile Photo</a>
										</label>
									</form>-->
								</figure>
							</div>
						</div>
						<div class="col-lg-10 col-sm-9">
							<div class="timeline-info">
								<ul>
									<li class="admin-name">
									  <h5 style="color: black;white-space: nowrap; width: 110px; font-size: 27px;"><b>@{{username}}</b><!--<i class="fa fa-check-circle" style="color: #48dbfb;" aria-hidden="true"></i>--></h5>
									  <!--<span>Group Admin</span>-->
									</li>
									<!--<li>
										<a class="" href="javascript:void(0)" title="" data-ripple="">Go live!</a>
										<a class="" href="javascript:void(0)" title="" data-ripple="">Music</a>
										<a class="" href="emporium/index-3.html" title="" data-ripple="">Emporium</a>
										<a class="" href="fitness/index.html" title="" data-ripple="">Health Inspection</a>
										<a class="" href="settings/account-setting.html" title="" data-ripple="">Settings</a>
										<a class="" href="javascript:void(0)" title="" data-ripple="">Upload</a>
										<a class="" href="time-line.html" title="" data-ripple="">time line</a>
										<a class="" href="timeline-photos.html" title="" data-ripple="">Photos</a>
										<a class="" href="timeline-videos.html" title="" data-ripple="">Videos</a>
										<a class="" href="timeline-friends.html" title="" data-ripple="">Friends</a>
										<a class="" href="timeline-groups.html" title="" data-ripple="">Groups</a>
										<a class="" href="about.html" title="" data-ripple="">about</a>
										<a class="" href="#" title="" data-ripple="">more</a>

									</li>-->
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section><!-- top area -->
		<section>
			<div class="bio">
				{{userProfile.bio}}
			</div>
		</section>
		
	<section>
		<div class="gap gray-bg">
			<div class="container-fluid">
				<div class="row">
					<div class="col-lg-12">
						<div class="row" id="page-contents">
							<div class="col-lg-3">
								<aside class="sidebar static">
									
									
									
								</aside>
							</div><!-- sidebar -->
							









							<div class="col-lg-6">
								<div class="central-meta">
									<ul class="photos">
					
										<li>
											<a class="strip" href="https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png" title="" data-strip-group="mygroup" data-strip-group-options="loop: false">
												<img src="https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png" style="height: 250px; width: 300px;" alt=""></a>
										</li>

		
										
									</ul>
									<!--<div class="lodmore"><button class="btn-view btn-load-more"></button></div>-->
								</div><!-- photos -->
							</div><!-- centerl meta -->
							<div class="col-lg-3">
								<aside class="sidebar static">
									
								</aside>
							</div><!-- sidebar -->
						</div>	
					</div>
				</div>
			</div>
		</div>	
	</section>  
</div>  
</template>

<script>
import axios from 'axios'
import {useAuthStore} from '/src/stores/authStore.js'
import {mapState} from 'pinia'

export default {
    name: 'Profile', 
	data() {
        return {
            userProfile:[],
			userPost:[],
            followerCount:[],
			username: this.$route.params.user_name,
			lengthOfUserPost: '', 
        }
    }, 
    computed: {
        ...mapState(useAuthStore, ['getToken', 'getUser']),
    },
	mounted() {
		this.getProfile()
		//this.userPostLength()
	},
	methods : {
		async getProfile() {
			const username = this.$route.params.user_name
			console.log("username from route: " + username)

			await axios

				.get(`http://127.0.0.1:8000/api/profile/${username}`)
				.then(response =>{
					console.log("what is profile: " + JSON.stringify(response.data))
					this.userProfile = response.data.user_profile
					console.log("what is user profile: " + JSON.stringify(this.userProfile))
					this.userPost = response.data.user_post
					console.log("what is user post: " + JSON.stringify(this.userPost))
					this.followerCount = response.data.follower_count
					console.log("what is follower count: " + JSON.stringify(this.followerCount))
				
				
				
				})
				.catch(error => {
                    console.log("errors: " + error)
                    //console.error(error.response.data)
                })
				this.userPostLength()
				this.userFollowerCount()
		},
		updateFollowing() {
			this.userPostLength()	
		},
		userPostLength() {
			console.log("whats user posts data: " + JSON.stringify(this.userPost))
			let postOfUser = []
			for(let elem in this.userPost) {
				console.log("whats each post: " + this.userPost[elem]["user"])
				if(this.userPost[elem]["user"] === this.username) {
					postOfUser.push(this.userPost[elem])
				}
			}

			console.log("What's in post of User: " + JSON.stringify(postOfUser))

			this.lengthOfUserPost = postOfUser.length

		},
		userFollowerCount(){
			console.log("Whats followers count: " + JSON.stringify(this.followerCount))

			let user = this.username
			let follower = this.getUser

			console.log("Who is user: " + user + " Who is follower: " + follower)
			
			let buttonText = ''
			let countOfFollowers = (this.followerCount).filter(value => value.follower.includes(follower) && value.user.includes(user))
			console.log("filter count of followers: " + JSON.stringify(countOfFollowers))
		
			if(countOfFollowers) {
				buttonText = 'Unfollow'
			}
			else {
				buttonText = 'Follow'
			}

			console.log("whats button text: " + buttonText)

			let userFollowers = (this.followerCount).filter(value => value.user.includes(this.username))
			let userFollowing = (this.followerCount).filter(value => value.follower.includes(this.username))

			console.log("whats user followers: " + userFollowers.length + " whats user following: " + userFollowing.length)
		}
	},
}
</script>
