<template>
	<div class="reservation">
    <el-row>
		<el-col :span="24" class="title">
			<span>面试已预约时间段：<b>{{num}}</b></span>
		</el-col>
	</el-row>
	<el-row class="myrev">
		<el-collapse v-model="activeNames" >

		  <el-collapse-item :title="it.date" :name="index" v-for="(it,index) in interview">
			<el-row class="con_con">

				<el-col :span=6 v-for="tb in it.tbs">
					<el-badge value="已预约" class="item" >
						<el-button type="success" v-on:click="sub_rv(it.date,tb.tb_id)">
						{{tb.time_bucket}}
						</el-button>
					</el-badge>
				</el-col>
			</el-row>
		  </el-collapse-item>

		</el-collapse>
	</el-row>
    <br>
	<el-row>
		<el-col :span="24" class="title">
			<span>实验已预约时间段：<b>{{num}}</b></span>
		</el-col>
	</el-row>
	<el-row class="myrev">
		<el-collapse v-model="activeNames" >
			
		  <el-collapse-item :title="it.date" :name="index" v-for="(it,index) in info">
			<el-row class="con_con">
				
				<el-col :span=6 v-for="tb in it.tbs">
					<el-badge value="已预约" class="item" >
						<el-button type="success" v-on:click="sub_rv(it.date,tb.tb_id)">
						{{tb.time_bucket}}
						</el-button>
					</el-badge>
				</el-col>
			</el-row>
		  </el-collapse-item>
		  
		</el-collapse>
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
				activeNames:"",  //展开信息序号
				info:[],
        interview:[],

			}
		},
		computed:{
			//已预约时间段数量
			num:function(){
				var j=0
				for (let i of this.info){
					j+=i.tbs.length
				}
				return j
			}

		},
		mounted(){
			this.get_info(this.date);
		},
		methods:{
			get_info:function(date){
				// 获取 预约信息
				this.axios.get(this.host+'/get_reservation/'+ this.userid,
				{responseType:'json',
				headers: {'Authorization': 'JWT ' + this.token},
				withCredentials: true,    //跨域带上cookies
				},
				).then(response=>{
				  console.log(response.data[1].tbs);
					this.info = response.data
				}).catch(error=>{
					console.log(error.response.data);
				})
			},
			sub_rv:function(date,tb_id){
				// 取消预约
				// 弹窗确认
				this.$confirm('取消预约, 是否继续?', '提示', {
				  confirmButtonText: '确定',
				  cancelButtonText: '取消',
				  type: 'warning'
				}).then(() => {
					this.axios.post(this.host+'/cancel_rv/',
					{date:date,tb_id:tb_id,userid:this.userid},
					{responseType:'json',
					headers: {'Authorization': 'JWT ' + this.token},
					withCredentials: true    //跨域带上cookies
					},
					).then(response=>{
						this.info=response.data;
						// this.open1();
						this.$message({
							type: 'success',
							message: '取消预约成功!'
						});
					}).catch(error=>{
						this.$message({
							type: 'error',
							message: '取消预约失败!'
						});
					})
				}).catch(() => {
				  this.$message({
					type: 'info',
					message: '无法取消预约'
				  });
				});

			},
			date2str:function(date){
				// 日期转字符串
				return date.getFullYear()+"-"+date.getMonth()+"-"+date.getDate()
			},
			// open1() {
			// 	const h = this.$createElement;
      //
			// 	this.$notify({
			// 	  title: '标题名称',
			// 	  message: h('i', { style: 'color: teal'}, '操作成功！')
			// 	});
      // },
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
		color:greenyellow;
		text-align: left;
		height: 50px;
		line-height: 50px;
		border: 1px solid #DCDFE6;
		background-color: #bea4fb;
		border-radius: 6px;
		margin-bottom: 10px;
	}
	.title span{
		margin-left: 20px;
	}
	.reservation{
		background-color: #eee;
	}
	
	
	.myrev{
		border: 1px solid #DCDFE6;
		background-color: #fff;
		border-radius:6px;
		overflow: hidden;
	}
	.myrev .el-collapse-item{
		padding:0 20px;
	}
	
	.myrev .el-collapse-item__header{
		font-size:20px;
		padding-left: 20px;
	}
	
	.con_con .el-col{
		margin: 15px 0;
		text-align: center;
	}
	.con_con .el-col .el-button{
		width:150px;
	}
	
	

</style>

