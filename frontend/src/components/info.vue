<template>
	<el-container class="container">
	  <el-header>
		  <div class="logo">
				<img src="" alt="">
				<span>Yeslab</span>
		  </div>
		  <div class="userinfo">
			  {{username}}
		  </div>

	  </el-header>
	  <el-container style="min-height: 600px;">
		<el-aside>
			<ul>
				<li>
					<i class="el-icon-user-solid"></i>
					<router-link :to="'/info/userinfo'">用户中心</router-link>
				</li>
				<el-divider></el-divider>
				<li>
					<i class="el-icon-phone"></i>
					<router-link :to="'/info/reservation'">预约实验</router-link>
				</li>
				<el-divider></el-divider>
        <li><i class="el-icon-phone"></i>
					<router-link :to="'/info/interview'">预约面试</router-link>
        </li>
        <el-divider></el-divider>

				<li>
					<i class="el-icon-phone"></i>
					<router-link :to="'/info/myreservation'">我的预约</router-link>
				</li>
				<el-divider></el-divider>
			</ul>
		</el-aside>
		<el-main>
			 <router-view></router-view>
		</el-main>
	  </el-container>
	</el-container>
</template>

<script>
	export default {
	  data() {
	    return {
			userid:sessionStorage.user_id || localStorage.user_id,
			username:sessionStorage.username || localStorage.username,
			token:sessionStorage.token || localStorage.token,
	  };
	  },
	  methods: {
	    onSubmit() {
	      console.log('submit!');
	    }
	  },
	}
</script>

<style scoped>
.container{

	width:1440px;
	margin:50px auto;
	box-shadow: #333 10px 10px 30px 5px ;

}
.logo{
	width: 300px;
	height: 60px;
	background-color: #8a82db;
	float: left;
}
.userinfo{
	text-align: right;
	height: 60px;
	line-height: 60px;
	padding-right: 100px;
	float: right;
}
.el-header{

	background-color: #fff;
	padding:0;

}
.el-aside{
	width:300px;
	color:#f9f9f9;
	background: -webkit-linear-gradient(#bea4fb, #8e9cfa); /* Safari 5.1 - 6.0 */
	background: -o-linear-gradient(#bea4fb, #8e9cfa); /* Opera 11.1 - 12.0 */
	background: -moz-linear-gradient(#bea4fb, #8e9cfa); /* Firefox 3.6 - 15 */
	background: linear-gradient(#bea4fb, #8e9cfa); /* 标准的语法 */
}
.el-aside li{
	width: 100%;
	margin: 0;
	text-align: center;
	height:30px;
	line-height: 30px;
	font-size: 20px;
}
.el-aside li i{
	margin-right: 10px;
}
.el-main{
	background-color: #eee;
}
</style>
