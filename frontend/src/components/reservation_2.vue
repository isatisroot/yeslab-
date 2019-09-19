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
      <el-button plain v-on:click="get_info(date4)">{{date4|format("yyyy-MM-dd")}}</el-button>
      <el-button plain v-on:click="get_info(date5)">{{date5|format("yyyy-MM-dd")}}</el-button>
      <el-button plain v-on:click="get_info(date6)">{{date6|format("yyyy-MM-dd")}}</el-button>
      <el-button plain v-on:click="get_info(date7)">{{date7|format("yyyy-MM-dd")}}</el-button>
		</el-col>

		<el-col :span="20" class="con">
			<el-row class="con_title">{{info[0].date}}</el-row>
			<el-divider></el-divider>
			<el-row class="con_con">
				<el-col :span=5 v-for="it in info">
					<el-badge :value="it.userid&&it.userid==userid?'预约':''" class="item">
						<el-button type="success" v-on:click="sub_rv(it.date,it.tb_id)" :disabled="it.userid?true:false">
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
				info:[],
        old_info:[],
				date:new Date()
			}
		},
		computed:{
			date2:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+1)},
			date3:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+2)},
      date4:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+3)},
      date5:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+4)},
      date6:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+5)},
      date7:function(){return new Date(this.date.getFullYear(),this.date.getMonth(),this.date.getDate()+6)},
			reserved:function(){var j=0;for(var i of this.info){if(i.userid){j+=1}};return j;},
			remanent:function(){return 16-this.reserved},
		},
		mounted(){
			this.get_info(this.date);
		},
		methods:{
			get_info:function(date){
		    let rock = this.$route.query.rock;
			  var d = this.date2str(date);
			  this.old_info=[
			    {"date":d,"tb_id":1,"time_bucket":"00:00-06:00"},
        {"date":d,"tb_id":2,"time_bucket":"06:30-10:30"},
        {"date":d,"tb_id":3,"time_bucket":"11:00-15:00"},
        {"date":d,"tb_id":4,"time_bucket":"15:30-19:30"},
        {"date":d,"tb_id":5,"time_bucket":"20:00-24:00"}];

				this.axios.get(this.host+'/get_info/?rock='+rock+'&date='+this.date2str(date),
				{responseType:'json',
				headers: {'Authorization': 'JWT ' + this.token},
				withCredentials: true,    //跨域带上cookies
				},
				).then(response=>{
					// console.log(response.data);
					// console.log(this.old_info);
          this.info = this.merge_data(response.data);
            // console.log(this.merge_data(response.data))
				}).catch(error=>{
					console.log(error.response.data);
				})
			},
      merge_data:function(data){
        if(data!=''){
          for(var i=0;i<data.length;i++){
            for(var j=0;j < 5;j++){
              if (data[i].tb_id === this.old_info[j].tb_id){
                this.old_info[j] = data[i]
              }
          }
        }
          return this.old_info
        }else{return this.old_info}


      },
			sub_rv:function(date,tb_id){
				// 提交预约
				// 弹窗确认
				this.$confirm('确定预约, 是否继续?', '提示', {
				  confirmButtonText: '确定',
				  cancelButtonText: '取消',
				  type: 'warning'
				}).then(() => {
					this.axios.post(this.host+'/sub_rv/',
					{date:date,tb_id:tb_id,userid:this.userid},
					{responseType:'json',
					headers: {'Authorization': 'JWT ' + this.token},
					withCredentials: true,    //跨域带上cookies
					},
					).then(response=>{
					  console.log(response.data);
						this.info=this.merge_data(response.data);
            // this.$router.go(0);
						// this.open1();
						this.$message({
							type: 'success',
							message: '已提交预约!'
						});
					}).catch(error=>{
					  // alert('fail');
					  console.log(error);
						this.$message({
							type: 'error',
							message: '预约失败!'+error.response.data.msg
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
