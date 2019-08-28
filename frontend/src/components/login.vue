<template>
	<div class="login">
		<h1>登&nbsp;&nbsp;陆</h1>
<el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm">
	
	  <el-form-item label="用 户 名" prop="user">
		<el-input type="text" v-model="ruleForm2.user" auto-complete="off"></el-input>
	  </el-form-item>
	  
	  <el-form-item label="密    码" prop="pass">
		<el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
	  </el-form-item>
	  
	  <el-form-item label="验 证 码" prop="captcha">
		<el-input type="text" v-model.number="ruleForm2.captcha">
			<el-button slot="append"><img :src="captcha_url" @click="generate_captcha" alt=""></el-button>
		</el-input>
	  </el-form-item>
	  
	  <el-form-item label="" prop="remember">
	  		<el-checkbox v-model="ruleForm2.remeber" label="1">记住密码</el-checkbox>
	  </el-form-item>
	  
	  <el-form-item>
		<el-button type="primary" @click="submitForm('ruleForm2')">登&nbsp;&nbsp;陆</el-button>
		<el-button @click="resetForm('ruleForm2')">重置</el-button>
	  </el-form-item>
  
	  <el-form-item style="text-align: right;">
		<router-link :to="'/register'">去注册...</router-link>
		</el-form-item>
  
</el-form>
</div>
</template>

<script>
	import util from '../utils/util.js'
	export default {
	  name:'login',
    data() {
      var validateuser = (rule, value, callback) => {
		  console.log(value,/^\w{6,12}$/.test(value))
		if (value === '') {
			callback(new Error('请输入用户名'));
        }else if(!/^\w{6,12}$/.test(value)) {
			callback(new Error('用户名必须是6-12位数字字母下划线组成'));
		}else{
			callback()
			}
      };
      var validatepass = (rule, value, callback) => {
		  console.log(value,/^.{6,12}$/.test(value))
		if (value === '') {
			callback(new Error('请输入密码'));
        }else if(!/^.{6,12}$/.test(value)) {
			callback(new Error('密码必须是6-12位'));
		}else{
			callback()
			}
 
      };
      var validatecaptcha = (rule, value, callback) => {
		  console.log(value,/^[a-zA-Z0-9]{4}$/.test(value))
		if (value === '') {
			callback(new Error('请输入验证码'));
        }else if(!/^[a-zA-Z0-9]{4}$/.test(value)) {
			callback(new Error('验证码必须是4位数字与字母'));
		}else{
			callback()
			}

      };
      return {
		captcha_url:"",
        ruleForm2: {
          user: '',
          pass: '',
          captcha: '',
		  remember:false,
		  
        },
        rules2: {
          user: [
            { validator: validateuser, trigger: 'blur' }
          ],
          pass: [
            { validator: validatepass, trigger: 'blur' }
          ],
          captcha: [
            { validator: validatecaptcha, trigger: 'blur' }
          ]
        }
      };
    },
	mounted(){
		this.generate_captcha()
	},
    methods: {
	  generate_captcha(){
		  this.captcha_url = this.host+'/captcha/'+util.generate_uuid()+"/";
	  },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
			this.axios.post(this.host+"/login/",
			{username:this.user,password:this.pass,captcha:this.captcha,uuid:this.uuid},
			{responseType:'json',withCredentials: true,}
			).then(response=>{
				 // 使用浏览器本地存储保存token
                        if (this.remember) {
                            // 记住登录
                            sessionStorage.clear();
                            localStorage.token = response.data.token;
                            localStorage.user_id = response.data.user_id;
                            localStorage.username = response.data.username;
                        } else {
                            // 未记住登录
                            localStorage.clear();
                            sessionStorage.token = response.data.token;
                            sessionStorage.user_id = response.data.user_id;
                            sessionStorage.username = response.data.username;
                        }

                        // 跳转页面
                        var return_url = this.get_query_string('next');
                        if (!return_url) {
                            return_url = '/info.html';
                        }
                        // 页面跳转
                        // location.href = return_url;
						this.$router.push({name:'info'})
			}).catch(error=>{
				this.$message({
									type: 'error',
									message: '登陆失败!'
				});
			});
			

          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
    }
  }
</script>

<style>
	.login{
		width:500px;
		height:500px;
		margin:100px 0 0 900px;
		border:1px solid #ccc;
		border-radius: 6px;
		box-shadow: #333 10px 10px 30px 5px;
		background: -webkit-linear-gradient(#bea4fb, #8e9cfa); /* Safari 5.1 - 6.0 */
		background: -o-linear-gradient(#bea4fb, #8e9cfa); /* Opera 11.1 - 12.0 */
		background: -moz-linear-gradient(#bea4fb, #8e9cfa); /* Firefox 3.6 - 15 */
		background: linear-gradient(#bea4fb, #8e9cfa); /* 标准的语法 */
		
	}
	.login h1{
		text-align: center;
		
	}
	.el-form{
		width:400px;
		height:300px;
		margin:50px auto;
		font-size: 16px;
		
		
	}
	
	.el-button img{
		width:80px;
		
	}
</style>
