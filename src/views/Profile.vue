<template>
<div class="theme-layout">
	
	<section>
			<div class="feature-photo">
				<figure><img v-bind:src="'/src/assets/images/resources/timeline1.jpg'" alt=""></figure>
				<form>
					<div class="add-btn">
					<span style="color: white; font-size: 27px; margin-right: 520px;"><b><u><a href="/">Home</a></u></b></span>
					<span style="color: white; font-size: 27px;"><b>11 Post</b></span>
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
									<img src="https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png" style="height: 250px; width: 100%;" alt="">
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
									  <h5 style="color: black;white-space: nowrap; width: 110px; font-size: 27px;"><b>@username</b><!--<i class="fa fa-check-circle" style="color: #48dbfb;" aria-hidden="true"></i>--></h5>
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
				Bio goes here...
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
        }
    }, 
    computed: {
        ...mapState(useAuthStore, ['getToken']),
    },
	mounted() {
		this.getProfile()
	},
	methods : {
		async getProfile() {
			const username = this.$route.params.user_name
			console.log("username from route: " + username)

			await axios

				.get('http://127.0.0.1:8000/api/profile/')
				.then(response =>{
					console.log("what is profile: " + JSON.stringify(response.data))
					console.log("what is user profile: " + JSON.stringify(response.data.user_profile))
					console.log("what is user post: " + JSON.stringify(response.data.user_post))
					console.log("what is follower count: " + JSON.stringify(response.data.follower_count))
				
				
				
				})
				.catch(error => {
                    console.log("errors: " + error)
                    //console.error(error.response.data)
                })
		}
	},
}
</script>
