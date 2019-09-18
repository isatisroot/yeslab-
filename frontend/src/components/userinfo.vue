<template>
<el-form ref="form" :model="form" label-width="110px">
		
	  <el-form-item label="真实姓名">
		<el-input v-model="form.name" placeholder="请填写真实姓名"></el-input>
	  </el-form-item>
	  
	  <el-form-item label="手机号码">
	  	<el-input v-model="form.phone" placeholder="请填写手机号码"></el-input>
	  </el-form-item>

    <el-form-item label="QQ">
	  	<el-input v-model="form.phone" placeholder="请填写QQ号码"></el-input>
	  </el-form-item>

    <el-form-item label="学校/企业名称">
	  	<el-input v-model="form.phone" placeholder="请填写学校或企业名称"></el-input>
	  </el-form-item>

	  <el-form-item>
		<el-button type="primary" @click="onSubmit">提&nbsp;&nbsp;&nbsp;&nbsp;交</el-button>
	  </el-form-item>
</el-form>
</template>

<script>
	 export default {
    data() {
      return {
        msg:'',
        form: {
          name: '',
          phone: '',
          qq:'',
          adress:''
        }
      };
    },
     mounted() {
      this.get_info();
    },
    methods: {
      onSubmit() {
        this.axios.post(this.host + "/userinfo/", {
              form:this.form
            }, {
              responseType: 'json',
              withCredentials: true,
            }).then(response => {
            }).catch(error => {
              console.log(error, "error");
              this.$message({
                type: 'error',
                message: '提交失败!'
              });
            });
      },
      get_info:function(){
				// 获取用户个人信息
				this.axios.get(this.host+'/userinfo/'+ this.userid,
				{responseType:'json',
				headers: {'Authorization': 'JWT ' + this.token},
				withCredentials: true,    //跨域带上cookies
				},
				).then(response=>{
        this.msg = response.data
				}).catch(error=>{
					console.log(error.response.data);
				})
			},
    }
  }
</script>

<style scoped>
.el-form{
	margin:20px auto;
	width: 600px;
}
</style>
