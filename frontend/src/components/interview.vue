<template>
	<div class="reservation">
<!--	<el-row>-->
<!--		<el-col :span="24" class="title">-->
<!--			<span>注意：<b>{{reserved}}</b></span>-->

<!--		</el-col>-->
<!--	</el-row>-->
<div v-for="i in info">
	<el-row>
		<el-col :span="4"  class="date">
			  <el-button plain v-on:click="get_info(date)" >{{i.date}}</el-button>
		</el-col>
		<el-col :span="20" class="con">
<!--			<el-row class="con_title" >{{i.date}}</el-row>-->
<!--			<el-divider></el-divider>-->
			<el-row class="con_con">
				<el-col :span=6 v-for="it in i.tbs">
					<el-badge :value="it.remaining?'剩余：'+it.remaining:''" class="item">
						<el-button type="success" v-on:click="sub_rv(i.date,it.tb_id)" :disabled="it.remaining==0?true:false">
						{{it.time_bucket}}
						</el-button>
					</el-badge>
				</el-col>

			</el-row>

		</el-col>

	</el-row>
  </div>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				userid:sessionStorage.user_id || localStorage.user_id,
				username:sessionStorage.username || localStorage.username,
				token:sessionStorage.token || localStorage.token,
				info:[],
				date:new Date()
			}
		},
		computed:{
			date2:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+1)},
			// date3:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+2)},
      // date4:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+3)},
      // date5:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+4)},
      // date6:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+5)},
      // date7:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+6)},
			reserved:function(){var j=0;for(var i of this.info){if(i.userid){j+=1}};return j;},
			remanent:function(){return 16-this.reserved},
		},
		mounted(){
			this.get_info(this.date);
		},
		methods:{
			get_info:function(date){
			  // console.log(date.getMonth()+1)
				// console.log(this.date2str(date));

				this.axios.get(this.host+'/interview_msg/?date='+this.date2str(date),
				{responseType:'json',
				headers: {'Authorization': 'JWT ' + this.token},
				withCredentials: true,    //跨域带上cookies
				},
				).then(response=>{
					console.log(this.userid);
					this.info = response.data
				}).catch(error=>{
					console.log(error.response.data);
				})
			},
			sub_rv:function(date,tb_id){
				// 提交预约
				// 弹窗确认
				this.$confirm('确定预约, 是否继续?', '提示', {
				  confirmButtonText: '确定',
				  cancelButtonText: '取消',
				  type: 'warning'
				}).then(() => {

					this.axios.post(this.host+'/interview/',
					{date:date,tb_id:tb_id,userid:this.userid},
					{responseType:'json',
					headers: {'Authorization': 'JWT ' + this.token},
					withCredentials: true,    //跨域带上cookies
					},
					).then(response=>{
					  console.log(response.data);
						this.info=response.data;
            this.$router.go(0);
						// this.open1();
						this.$message({
							type: 'success',
							message: '已提交预约!'
						});
					}).catch(error=>{
					  alert('fail');
					  console.log(error);
						this.$message({
							type: 'error',
							message: '预约失败!'
						});
					})

				}).catch(() => {
				  this.$message({
					type: 'info',
					message: '已取消预约'
				  });

				});


			},
			date2str:function(date){
				// 日期转字符串
        var month = date.getMonth()+1
				return date.getFullYear()+"-"+month+"-"+date.getDate()
			},
			open1() {
				const h = this.$createElement;

				this.$notify({
				  title: '标题名称',
				  message: h('i', { style: 'color: teal'}, '预约成功！')
				});
      },
		},
		filters:{
			format2:function(date,fmt){
				console.log(date,fmt)
				var o = {
					"M+" : date.getMonth()+1,                 //月份
					"d+" : date.getDate(),                    //日
					"h+" : date.getHours(),                   //小时
					"m+" : date.getMinutes(),                 //分
					"s+" : date.getSeconds(),                 //秒
					"q+" : Math.floor((date.getMonth()+3)/3), //季度
					"S"  : date.getMilliseconds()             //毫秒
				  };
				if(/(y+)/.test(fmt))
					fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length));
				for(var k in o)
					if(new RegExp("("+ k +")").test(fmt))
				fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
				return fmt;
			}
		}
	}
</script>

<style>
	.title{
		color:#999;
		text-align: right;
		height: 50px;
		line-height: 50px;
		border: 1px solid #DCDFE6;
		background-color: #fff;
		border-radius: 6px;
		margin-bottom: 10px;
	}
	.title span{
		margin-right: 20px;
	}
	.reservation{
		background-color: #eee;
	}
	.date .el-button{
		width:80%;
		height:50px;
		margin:10px auto;
		display: block;

	}
	.con{
		background-color: #fff;
		border-radius: 6px;
	}
	.con_title{
		text-align: center;
		height: 50px;
		line-height: 50px;
	}
	.con .el-divider{
		margin:0 0 20px 0;
	}
	.con_con .el-col{
		margin: 15px 0;
		text-align: center;
	}
	.con_con .el-col .el-button{
		width:150px;


	}
</style>
