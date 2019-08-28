<template>
	<div class="reservation">
	<el-row>
		<el-col :span="24" class="title">
			<span>已预约时间段<b>{{reserved}}</b></span>
			<span>剩余约时间段<b>{{remanent}}</b></span>
		</el-col>
	</el-row>
	
	<el-row>
		<el-col :span="4"  class="date">
			  <el-button plain v-on:click="get_info(date)">{{date|format("yyyy-MM-dd")}}</el-button>
			  <el-button plain v-on:click="get_info(date2)">{{date2|format("yyyy-MM-dd")}}</el-button>
			  <el-button plain v-on:click="get_info(date3)">{{date3|format("yyyy-MM-dd")}}</el-button> 
		</el-col>
		
		<el-col :span="20" class="con">
			<el-row class="con_title">{{info[0].date}}</el-row>
			<el-divider></el-divider>
			<el-row class="con_con">
				<el-col :span=6 v-for="it in info">
					<el-badge :value="it.userid&&it.userid==userid?'预约':''" class="item">
						<el-button type="success" v-on:click="sub_rv(it.tb_id)" :disabled="it.userid?true:false">
						{{it.time_bucket}}
						</el-button>
					</el-badge>
				</el-col>

			</el-row>
		</el-col>
		
	</el-row>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				userid:sessionStorage.user_id || localStorage.user_id,
				username:sessionStorage.username || localStorage.username,
				token:sessionStorage.token || localStorage.token,

				info:[
					{"id":10,"date":"2019-9-10","userid":"10","tb_id":1,"time_bucket":"0:00-1:00"},
					{"id":10,"date":"2019-9-10","userid":"12","tb_id":2,"time_bucket":"1:30-2:30"},
					{"tb_id":3,"time_bucket":"3:00-4:00"},
					{"tb_id":4,"time_bucket":"4:30-5:30"},
					{"tb_id":5,"time_bucket":"6:00-7:00"},
					{"tb_id":6,"time_bucket":"7:30-8:30"},
					{"id":10,"date":"2019-9-10","userid":"10","tb_id":7,"time_bucket":"9:00-10:00"},
					{"id":10,"date":"2019-9-10","userid":"14","tb_id":8,"time_bucket":"10:30-11:30"},
					{"tb_id":9,"time_bucket":"12:00-13:00"},
					{"tb_id":10,"time_bucket":"13:30-14:00"},
					{"tb_id":11,"time_bucket":"14:30-15:00"},
					{"id":10,"date":"2019-9-10","userid":"10","tb_id":12,"time_bucket":"15:30-16:30"},
					{"tb_id":13,"time_bucket":"17:00-18:00"},
					{"tb_id":14,"time_bucket":"18:30-19:30"},
					{"tb_id":15,"time_bucket":"20:00-21:00"},
					{"id":10,"date":"2019-9-10","userid":"16","tb_id":16,"time_bucket":"21:30-22:30"},
				],
				date:new Date()
			}
		},
		computed:{
			date2:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+1)},
			date3:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+2)},
			reserved:function(){var j=0;for(var i of this.info){if(i.id){j+=1}};return j;},
			remanent:function(){return 16-this.reserved},
		},
		mounted(){
			this.get_info(this.date);
		},
		methods:{
			get_info:function(date){
				console.log(date)
				this.axios.get(this.host+'/get_info/?date='+this.date2str(date),
				{responseType:'json',
				headers: {'Authorization': 'JWT ' + this.token},
				withCredentials: true,    //跨域带上cookies
				},
				).then(response=>{
					console.log(response)
					this.info = response.data
				}).catch(error=>{
					console.log(error.response.data);
				})
			},
			sub_rv:function(tb_id){
				// 提交预约
				// 弹窗确认
				this.$confirm('确定预约, 是否继续?', '提示', {
				  confirmButtonText: '确定',
				  cancelButtonText: '取消',
				  type: 'warning'
				}).then(() => {
					this.axios.get(this.host+'/sub_rv/',
					{date:this.info[0].date,tb_id:tb_id},
					{responseType:'json',
					headers: {'Authorization': 'JWT ' + this.token},
					withCredentials: true,    //跨域带上cookies
					},
					).then(response=>{
						this.info=response.data
						this.open1()
						this.$message({
							type: 'success',
							message: '已提交预约!'
						});
					}).catch(error=>{
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
				return date.getFullYear()+"-"+date.getMonth()+"-"+date.getDate()
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
